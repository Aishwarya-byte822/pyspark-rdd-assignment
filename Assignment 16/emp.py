from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("EmpRDD").getOrCreate()
sc = spark.sparkContext

# Read CSV
rdd = sc.textFile("emp.csv")

# Remove header
header = rdd.first()
rdd = rdd.filter(lambda x: x != header)

# Convert to list
employees = rdd.map(lambda x: x.split(","))

# Sort by salary
sorted_emp = employees.sortBy(lambda x: int(x[3]), ascending=False)

print("Employees Sorted by Salary:")
for emp in sorted_emp.collect():
    print(emp)

# Department-wise salary
dept_salary = employees.map(lambda x: (x[2], int(x[3]))).reduceByKey(lambda a, b: a + b)

print("\nDepartment Salary Totals:")
for item in dept_salary.collect():
    print(item)

# Top 3
top3 = sorted_emp.take(3)

print("\nTop 3 Highest Paid Employees:")
for emp in top3:
    print(emp)

sc.parallelize(top3).saveAsTextFile("output/top3_employees")

spark.stop()
