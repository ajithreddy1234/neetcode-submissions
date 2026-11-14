# Write your MySQL query statement belows
select s.student_id,s.student_name,su.subject_name,sum(case when su.subject_name=e.subject_name then 1 else 0 end) as attended_exams
from Students s 
cross join Subjects su
left join Examinations e
on su.subject_name=e.subject_name and s.student_id=e.student_id
group by s.student_id,su.subject_name
order by s.student_id,su.subject_name