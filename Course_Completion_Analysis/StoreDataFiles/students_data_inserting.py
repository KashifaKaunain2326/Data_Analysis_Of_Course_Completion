import mysql.connector
import pandas as pd
import numpy as np

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="students_course_analysis"
)
cursor = connection.cursor()

# STUDENTS--------------------------------------------------------------------------------
# students_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\students_data.csv")
#
# students_sql = """
# INSERT IGNORE INTO students
# (student_id, student_name, gender, age, city, employment_status)
# VALUES (%s, %s, %s, %s, %s, %s)
# """
#
# students_data = list(students_df.itertuples(index=False, name=None))
#
# cursor.executemany(students_sql, students_data)
# connection.commit()

#COURSE-----------------------------------------------------------------------------------------------
# courses_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\courses_data.csv")
#
# for _, row in courses_df.iterrows():
#     cursor.execute(
#         """
#         INSERT INTO courses
#         (course_id, course_name, category, course_level,
#          course_duration_days, instructor_rating)
#         VALUES (%s, %s, %s, %s, %s, %s)
#         """,
#         (
#             row["course_id"],
#             row["course_name"],
#             row["category"],
#             row["course_level"],
#             row["course_duration_days"],
#             row["instructor_rating"]
#         )
#     )
#
# connection.commit()


# ENROLLMENT---------------------------------------------------------------------------------------------

enroll_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\enrollment_data.csv")
enroll_df['enrollment_date'] = pd.to_datetime(enroll_df['enrollment_date'], dayfirst=True).dt.strftime('%Y-%m-%d')
for _, row in enroll_df.iterrows():
    cursor.execute(
        """INSERT INTO enrollments 
           (student_id, course_id, enrollment_date, payment_mode, fee_paid, discount_used, completion_status) 
           VALUES (%s, %s, %s, %s, %s, %s, %s)""",
        (
            row["student_id"],
            row["course_id"],
            row["enrollment_date"],
            row["payment_mode"],
            row["fee_paid"],
            row["discount_used"],
            row["completion_status"]
        )
    )
connection.commit()



# PROGRESS------------------------------------------------------------------------------------------

progress_df = pd.read_csv(
    "C:\\DANLC labs\\Course_Completion_Analysis\\progress_data.csv"
)

for _, row in progress_df.iterrows():
    cursor.execute(
        """
        INSERT INTO progress_matrix
        (student_id, education_level, progress_percentage,
         project_grade, time_spent_hours, quiz_attempts, avg_quiz_score,
         assignments_submitted, assignments_missed,
         peer_interaction_score, rewatch_count)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["student_id"],
            row["education_level"],
            row["progress_percentage"],
            row["project_grade"],
            row["time_spent_hours"],
            row["quiz_attempts"],
            row["avg_quiz_score"],
            row["assignments_submitted"],
            row["assignments_missed"],
            row["peer_interaction_score"],
            row["rewatch_count"]
        )
    )

connection.commit()
#
