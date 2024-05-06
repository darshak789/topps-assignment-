create database  salesperson_and_customer;
use salesperson_and_customer;
create table salesperson(Sno int primary key,SNAME VARCHAR(50),CITY VARCHAR(50),COMM decimal(5,2));
select * from salesperson;
insert into salesperson
values
(1002,'serres','san jose',0.13),
(1004,'motika','london',0.11),
(1007,'rafkin','barcelona',0.15),
(1003,'axelrod','new york',0.1);

select * from  customer;
create table customer(CNM INT PRIMARY KEY,CNAME VARCHAR(50),CITY VARCHAR(10),RATING INT,SNo int);

ALTER TABLE customer
add constraint fk_Sno
FOREIGN KEY (SNo) REFERENCES salesperson(Sno);

insert into  customer
values
(201,'hoffman','london',100,1001),
(202,'giovanne','roe',200,1003),
(203,'liu','san jose',300,1002),
(204,'grass','barcelona',100,1002),
(206,'clemens','london',300,1007),
(207,'pereira','roe',100,1004);

select s.SNo,s.sname,s.city,s.comm
from salesperson as s
inner join customer as c
on s.SNo=c.Sno
where rating>100;

select sname,city from salesperson where city='london' and comm>0.11;

select sname from salesperson where city='barcelona' or city='london';
select  sname from salesperson where comm  between 0.11 and 0.11;
select sname from salesperson where comm>0.10 and comm<0.12;

select cname,cnm from customer where (city='roe' or rating>100);

