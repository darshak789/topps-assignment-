select first_name from employee
where first_name="Tom";

select First_name, Joining_date,Salary from employee;

select * from employee  order by First_name ASC;
select * from  employee order by Salary DESC;

select * from employee where first_name LIKE '%j%';

SELECT Department, MAX(Salary) AS Max_Salary
FROM employee
GROUP BY Department
ORDER BY Max_Salary ASC;

use college;



