-- ANALYSIS
USE students_course_analysis;
-- 1. TOTAL STUDENTS
SELECT COUNT(*) AS total_students FROM students;

-- 2. TOTAL COURSES
SELECT COUNT(*) AS total_courses
FROM courses;

-- 3. Total Enrollments

SELECT COUNT(*) AS total_enrollments
FROM enrollments;

-- 4. Total Payments Done
SELECT COUNT(*) AS total_payments
FROM payments;

-- 5. Students by Gender
SELECT gender, COUNT(*) AS total_students
FROM students
GROUP BY gender;

-- 6. Students by City
SELECT city, COUNT(*) AS total_students
FROM students
GROUP BY city
ORDER BY total_students DESC;

-- 7. Employment Status of Students
SELECT employment_status, COUNT(*) AS total_students
FROM students
GROUP BY employment_status;

-- 8. Enrollments per Course
SELECT c.course_name, COUNT(e.enrollment_id) AS total_enrollments
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_name
ORDER BY total_enrollments DESC;

-- 9.Course Completion Status
SELECT completion_status, COUNT(*) AS total_students
FROM enrollments
GROUP BY completion_status;

-- 10. Payment Mode Usage
SELECT payment_mode, COUNT(*) AS total_payments
FROM payments
GROUP BY payment_mode;

-- 11. Discount Usage Analysis
SELECT discount_used, COUNT(*) AS total_students
FROM enrollments
GROUP BY discount_used;

-- 12. Most Popular Course
SELECT c.course_name, COUNT(*) AS enrollments
FROM enrollments e
JOIN courses c ON e.course_id = c.course_id
GROUP BY c.course_name
ORDER BY enrollments DESC
LIMIT 3;

-- 13. EDUCATIONAL LEVELS
SELECT education_level, COUNT(*) AS total_students
FROM progress_matrix GROUP BY education_level;

-- 14 Most popular tickets
SELECT satisfaction_rating, COUNT(*) AS Best_ticket
FROM support_tickets GROUP BY satisfaction_rating;


-- 15. Highest Payment 
SELECT payment_amount, COUNT(*) AS Highest_Payment
FROM payments GROUP BY payment_amount


