CREATE DATABASE students_course_analysis;

USE students_course_analysis;

CREATE TABLE students (
student_id VARCHAR(100) PRIMARY KEY,
student_name VARCHAR(100),
gender VARCHAR(20),
age INT,
city VARCHAR(100),
employment_status VARCHAR(100)
);


CREATE TABLE courses (
course_id VARCHAR(50) PRIMARY KEY,
course_name VARCHAR(100),
category VARCHAR(50),
course_level VARCHAR(50),
course_duration_days INT,
instructor_rating FLOAT
);

SELECT * FROM students_course_analysis.courses;

CREATE TABLE enrollments (
enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
student_id VARCHAR(50),
course_id VARCHAR(20),
enrollment_date DATE,
payment_mode VARCHAR(50),
fee_paid VARCHAR(10),
discount_used VARCHAR(10),
completion_status VARCHAR(50)
); 

SELECT * FROM students_course_analysis.enrollments;

CREATE TABLE progress_matrix (
progress_id INT AUTO_INCREMENT PRIMARY KEY,
student_id VARCHAR(50),
education_level VARCHAR(100),
progress_percentage FLOAT,
project_grade FLOAT,
time_spent_hours FLOAT,
quiz_attempts INT,
avg_quiz_score INT,
assignments_submitted INT,
assignments_missed INT,
peer_interaction_score FLOAT,
rewatch_count INT
);

SELECT * FROM students_course_analysis.progress_matrix;


CREATE TABLE app_ussage (
id INT AUTO_INCREMENT PRIMARY KEY,
student_id VARCHAR(50),
app_usage_percentage INT,
divice_type VARCHAR(50),
internet_quality VARCHAR(20),
video_completion_rate FLOAT
);

SELECT * FROM students_course_analysis.app_ussage;



CREATE TABLE payments (

payment_id INT AUTO_INCREMENT PRIMARY KEY,
payment_mode VARCHAR(100),
student_id VARCHAR(50),
payment_amount INT,
discount_used VARCHAR(10),
completion_status VARCHAR(100)
);

SELECT * FROM students_course_analysis.payments;


CREATE TABLE support_tickets (
ticket_id INT AUTO_INCREMENT PRIMARY KEY,
student_id VARCHAR(20),
satisfaction_rating FLOAT,
support_ticket_raised INT
);

SELECT * FROM students_course_analysis.support_ticket;

CREATE TABLE login (
login_id INT AUTO_INCREMENT PRIMARY KEY,
student_name VARCHAR(100),
login_frequency INT,
days_last_login INT
);

SELECT * FROM students_course_analysis.login;


USE students_course_analysis;
ALTER TABLE enrollments
ADD CONSTRAINT fk_enrollments_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);

ALTER TABLE enrollments
ADD CONSTRAINT fk_enrollments_course
FOREIGN KEY (course_id)
REFERENCES courses(course_id);

ALTER TABLE progress_matrix
ADD CONSTRAINT fk_progress_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);

ALTER TABLE support_tickets
ADD CONSTRAINT fk_support_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);


ALTER TABLE app_ussage
ADD CONSTRAINT fk_app_usage_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);

ALTER TABLE payments
ADD CONSTRAINT fk_payment_student
FOREIGN KEY (student_id)
REFERENCES students(student_id);










