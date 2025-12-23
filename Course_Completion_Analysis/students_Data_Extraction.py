import pandas as pd

# students_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
#
# students = pd.DataFrame(
#     {
#         "student_id" : students_df["student_id"],
#         "student_name" : students_df["student_name"],
#         "gender" : students_df["gender"],
#         "age" : students_df["age"],
#         "city" : students_df["city"],
#         "employment_status" : students_df["employment_status"],
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
#
# students.to_csv("students_data.csv", index=False)

# courses_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
# courses = pd.DataFrame(
#     {
#         "course_id" : courses_df["course_id"],
#         "course_name" : courses_df["course_name"],
#         "category" : courses_df["category"],
#         "course_level" : courses_df["course_level"],
#         "course_duration_days" :courses_df["course_duration_days"],
#         "instructor_rating" : courses_df["instructor_rating"]
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
# courses.to_csv("courses_data.csv", index=False)

# enrollments_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
# enrollments = pd.DataFrame(
#     {
#         "student_id" : enrollments_df["student_id"],
#         "course_id" : enrollments_df["course_id"],
#         "enrollment_date" : enrollments_df["enrollment_date"],
#         "payment_mode" : enrollments_df["payment_mode"],
#         "fee_paid" : enrollments_df["fee_paid"],
#         "discount_used" : enrollments_df["discount_used"],
#         "completion_status" : enrollments_df["completion_status"]
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
# enrollments.to_csv("enrollment_data.csv", index=False)

#
progress_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
progress = pd.DataFrame(
    {
        "student_id" : progress_df["student_id"],
        "education_level" :progress_df["education_level"],
        "progress_percentage" :progress_df["progress_percentage"],
        "project_grade" :progress_df["project_grade"],
        "time_spent_hours" :progress_df["time_spent_hours"],
        "quiz_attempts" :progress_df["quiz_attempts"],
        "avg_quiz_score" :progress_df["avg_quiz_score"],
        "assignments_submitted" :progress_df["assignments_submitted"],
        "assignments_missed" :progress_df["assignments_missed"],
        "peer_interaction_score" :progress_df["peer_interaction_score"],
        "rewatch_count" :progress_df["rewatch_count"]
    }
).dropna().drop_duplicates().reset_index(drop=True)
progress.to_csv("progress_data.csv", index=False)


# app_ussage_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
# app_ussage = pd.DataFrame(
#     {
#         "student_id" : app_ussage_df["student_id"],
#         "app_usage_percentage" : app_ussage_df["app_usage_percentage"],
#         "divice_type" : app_ussage_df["divice_type"],
#         "internet_quality" : app_ussage_df["internet_quality"],
#         "video_completion_rate" : app_ussage_df["video_completion_rate"]
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
# app_ussage.to_csv("app_ussage_data.csv", index=False)


# payments_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
# payments= pd.DataFrame(
#     {
#         "payment_mode" : payments_df["payment_mode"],
#         "student_id" : payments_df["student_id"],
#         "payment_amount" : payments_df["payment_amount"],
#         "discount_used" : payments_df["discount_used"],
#         "completion_status" : payments_df["completion_status"]
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
# payments.to_csv("payments_data.csv", index=False)


# support_tickets_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
# support_tickets = pd.DataFrame(
#     {
#         "student_id" : support_tickets_df["student_id"],
#         "satisfaction_rating" : support_tickets_df["satisfaction_rating"],
#         "support_ticket_raised" : support_tickets_df["support_ticket_raised"]
#     }
# ).dropna().drop_duplicates().reset_index(drop=True)
# support_tickets.to_csv("support_tickets_data.csv", index=False)



login_df= pd.read_csv("C:\\DANLC labs\\Course_Completion_Prediction.csv", low_memory=False)
login = pd.DataFrame(
    {
        "student_name" : login_df["student_name"],
        "login_frequency" : login_df["login_frequency"],
        "days_last_login" : login_df["days_last_login"]
    }
).dropna().drop_duplicates().reset_index(drop=True)
login.to_csv("login.csv", index=False)






















