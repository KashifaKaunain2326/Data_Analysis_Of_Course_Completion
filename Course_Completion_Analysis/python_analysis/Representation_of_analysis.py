import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="students_course_analysis"
)
#GENDER-------------------------------------------------------------------------------------------------
# query = """
# SELECT gender, COUNT(*) AS total_students
# FROM students
# GROUP BY gender
# """
# plt.figure()
# df = pd.read_sql(query, connection)
# plt.bar(df["gender"], df["total_students"],
# color=['red' if g=='Male' else 'green' if g=='Female' else 'black' for g in df["gender"]])
#
# plt.xlabel("Gender")
# plt.ylabel("Number of Students")
# plt.title("Students by Gender")
# plt.show()



# CITY------------------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT city, COUNT(*) AS total_students
# FROM students
# GROUP BY city
# ORDER BY total_students DESC
# """, connection)
#
# plt.figure()
# plt.barh(df["city"], df["total_students"])
# plt.title("Students by City")
# plt.show()



# Employment Status------------------------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT employment_status, COUNT(*) AS total_students
# FROM students
# GROUP BY employment_status
# """, connection)
#
# colors = ['red', 'blue', 'green', 'yellow']
# plt.figure(figsize=(8,8))
# plt.pie(df["total_students"], labels=df["employment_status"], colors=colors, autopct="%1.1f%%", pctdistance=0.85, wedgeprops=dict(width=0.3))
# plt.title("Employment Status")
# plt.show()



#Enrollments per Course-------------------------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT c.course_name, COUNT(e.enrollment_id) AS total_enrollments
# FROM enrollments e
# JOIN courses c ON e.course_id = c.course_id
# GROUP BY c.course_name
# ORDER BY total_enrollments DESC
# """, connection)
#
# plt.figure()
# plt.plot(df["course_name"], df["total_enrollments"], marker='o')
# plt.title("Enrollments per Course")
# plt.xticks(rotation=45)
# plt.show()


#Course Completion Status--------------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT completion_status, COUNT(*) AS total_students
# FROM enrollments
# GROUP BY completion_status
# """, connection)
#
# plt.figure()
# plt.pie(df["total_students"], labels=df["completion_status"], autopct="%1.1f%%")
# plt.title("Completion Status")
# plt.show()



#Payment Mode Usage----------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT payment_mode, COUNT(*) AS total_payments
# FROM payments
# GROUP BY payment_mode
# """, connection)
#
# plt.figure()
# plt.plot(df["payment_mode"], df["total_payments"], marker='o')
# plt.title("Payment Mode Usage")
# plt.show()



# #TOP 5 COURSES-------------------------------------------------------------------------------
# df = pd.read_sql("""
# SELECT c.course_name, COUNT(*) AS enrollments
# FROM enrollments e
# JOIN courses c ON e.course_id = c.course_id
# GROUP BY c.course_name
# ORDER BY enrollments DESC
# LIMIT 5
# """, connection)
#
# colors = ['blue', 'black', 'pink', 'green', 'orange']
# plt.figure()
# plt.bar(df["course_name"], df["enrollments"], color=colors)
# plt.title("Top 5 Popular Courses")
# plt.xlabel("Course Name")
# plt.ylabel("Enrollments")
# plt.show()


#DISCOUNT------------------------------------------------------------------------------------------------------
df = pd.read_sql("""
SELECT discount_used, COUNT(*) AS total_students
FROM enrollments
GROUP BY discount_used
""", connection)

plt.figure()
plt.hist(df["total_students"])
plt.title("Discount Usage Distribution")
plt.show()


