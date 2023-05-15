 create table salesperson(
  pksno varchar(50),
  sname varchar(50),
city varchar(50),
  comm varchar(50)
  );
  
   insert into salesperson(pksno,sname,city,comm)
     values("1001","peel","london",".12");
     insert into salesperson(pksno,sname,city,comm)
     values("1002","serres","san jose",".13");
       insert into salesperson(pksno,sname,city,comm)
     values("1004","motika","london",".11");
       insert into salesperson(pksno,sname,city,comm)
     values("1007","rafkin","barcelona",".15");
     insert into salesperson(pksno,sname,city,comm)
     values("1003","axelrod","new york",".1");
     
     
     
      create table customer(
  pkcnm varchar(50),
  cname varchar(50),
city varchar(50),
  rating varchar(50),
  fksno varchar(50)
  );
  
   insert into customer(pkcnm,cname,city,rating, fksno)
     values("201","hoffman","london","101","1001");
      insert into customer(pkcnm,cname,city,rating, fksno)
     values("202","givanne","roe","200","1003");
     insert into customer(pkcnm,cname,city,rating, fksno)
     values("203","liu","san jose","300","1002");
      insert into customer(pkcnm,cname,city,rating, fksno)
     values("204","grass","barcelona","300","1002");
     insert into customer(pkcnm,cname,city,rating, fksno)
     values("206","clemens","london","300","1007");
     insert into customer(pkcnm,cname,city,rating, fksno)
     values("20","pereira","roe","100","1004");
  
  
  