create database TOPS;
use tops;
select * from exam;
create table student
(Rollno int primary key,name varchar(50),Branch varchar(50));
insert into student
values
(1,'jay','computer science'),
(2,'suhani','electronic and comm'),
(3,'kriti','electronic and comm');

create table
 exam(Rollno int,S_code varchar(50),Marks int,P_code varchar(50));
 insert into exam
 values
 (1,'CS11',50,'CS'),
 (2,'CS12',60,'CS'),
 (3,'EC101',66,'EC'),
 (3,'EC102',70,'EC');
 
 ALTER TABLE EXAM
 ADD FOREIGN KEY (Rollno) references Student(Rollno);
