use databasename
     use universcity
                                 drop database universcity;
delete from student;
delete from studet


create table student(
      rollno int auto_increment,
      name varchar(10),
      branch varchar(100),                         
      
      primary key (rollno)
      );
      
      
      insert into student(name,branch) value("jay","computerscicnce");
         insert into student(name,branch) value("suhani","electonic and corn");
            insert into student(name,branch) value("kriti","electonic and corn");
            
            
            
           create table exam (
           rollno int,
           s_code varchar(100),
           marks int,
           p_code varchar(100),
           
           foreign key(rollno)references student(rollno)
           );
           
            insert into exam(rollno,s_code,marks,p_code ) value(2,"cs11",50,"cs");
            insert into exam(rollno,s_code,marks,p_code ) value(2,"cs12",60,"cs");
            insert into exam(rollno,s_code,marks,p_code ) value(3,"ec101",66,"ec");
            insert into exam(rollno,s_code,marks,p_code ) value(3,"ec102",70,"ec");
            insert into exam(rollno,s_code,marks,p_code ) value(4,"ec101",45,"ec");
            insert into exam(rollno,s_code,marks,p_code ) value(4,"es102",50,"ec");
            
           
           
           