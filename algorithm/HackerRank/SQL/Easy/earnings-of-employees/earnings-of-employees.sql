select max(totalsalary), count(*)
from (select (salary * months) as totalsalary from employee) as salary_table
where totalsalary = (select max(salary * months) from employee);
