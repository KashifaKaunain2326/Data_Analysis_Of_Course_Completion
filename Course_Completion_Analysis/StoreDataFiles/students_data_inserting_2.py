import mysql.connector
import numpy as np
import pandas as pd


connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database="students_course_analysis"
)
cursor = connection.cursor()

# support_tickets------------------------------------------------------------------------------------------
# support_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\support_tickets_data.csv")
#
# for _, row in support_df.iterrows():
#     cursor.execute(
#         """
#         INSERT INTO support_tickets
#         (student_id, satisfaction_rating, support_ticket_raised)
#         VALUES (%s, %s, %s)
#         """,
#         (
#             row["student_id"],
#             row["satisfaction_rating"],
#             row["support_ticket_raised"]
#         )
#     )
#
# connection.commit()

# APP_USSAGE---------------------------------------------------------------------------------------
# app_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\app_ussage_data.csv")
#
# for _, row in app_df.iterrows():
#     cursor.execute(
#         """
#         INSERT INTO app_ussage
#         (student_id, app_usage_percentage, divice_type,
#          internet_quality, video_completion_rate)
#         VALUES (%s, %s, %s, %s, %s)
#         """,
#         (
#             row["student_id"],
#             row["app_usage_percentage"],
#             row["divice_type"],
#             row["internet_quality"],
#             row["video_completion_rate"]
#         )
#     )

# connection.commit()

# PAYMENTS-----------------------------------------------------------------------------------------
# payments_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\payments_data.csv")
#
# for _, row in payments_df.iterrows():
#     cursor.execute(
#         """
#         INSERT INTO payments
#         (payment_mode, student_id,
#          payment_amount, discount_used, completion_status)
#         VALUES (%s, %s, %s, %s, %s)
#         """,
#         (
#             row["payment_mode"],
#             row["student_id"],
#             row["payment_amount"],
#             row["discount_used"],
#             row["completion_status"]
#         )
#     )
#
# connection.commit()


# LOGIN------------------------------------------------------------------------------------------


login_df = pd.read_csv("C:\\DANLC labs\\Course_Completion_Analysis\\login.csv")

for _, row in login_df.iterrows():
    cursor.execute(
        """
        INSERT INTO login
        (student_name,
         login_frequency, days_last_login)
        VALUES (%s, %s, %s)
        """,
        (
            row["student_name"],
            row["login_frequency"],
            row["days_last_login"]
        )
    )

connection.commit()

