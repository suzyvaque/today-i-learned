select student_info.name from



(select students.name, students.id, packages.salary from students, packages
where students.id = packages.id) as student_info

join

(select friends.id, friends.friend_id, packages.salary as friend_salary from friends, packages
where friends.friend_id = packages.id) as friend_info

on student_info.id = friend_info.id



where student_info.salary < friend_info.friend_salary
order by friend_info.friend_salary;
