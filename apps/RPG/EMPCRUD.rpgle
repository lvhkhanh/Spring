**FREE
ctl-opt dftactgrp(*no) actgrp(*new) option(*srcstmt:*nodebugio);

exec sql include sqlca;

dcl-s choice char(1) inz('0');
dcl-s response varchar(256) inz('');
dcl-s empId int(10) inz(0);
dcl-s firstName varchar(30) inz('');
dcl-s lastName varchar(30) inz('');
dcl-s age int(5) inz(0);

dcl-proc main;
  exec sql whenEVER SQLERROR continue;

  dow choice <> '9';
    dsply 'DB2 CRUD Demo -- 1=Create 2=Read 3=Update 4=Delete 5=List 9=Exit' response;
    choice = %trim(response);

    select;
      when choice = '1';
        perform createRecord;
      when choice = '2';
        perform readRecord;
      when choice = '3';
        perform updateRecord;
      when choice = '4';
        perform deleteRecord;
      when choice = '5';
        perform listRecords;
      when choice = '9';
        dsply 'Exiting CRUD application...' response;
      other;
        dsply 'Invalid option. Enter 1-5 or 9.' response;
    endsl;
  enddo;

  *inlr = *on;
  return;
end-proc;

dcl-proc createRecord;
  dsply 'Enter first name:' response;
  firstName = %trim(response);
  dsply 'Enter last name:' response;
  lastName = %trim(response);
  dsply 'Enter age:' response;
  age = %int(%trim(response));

  exec sql
    insert into EMPLOYEE (FIRSTNAME, LASTNAME, AGE)
    values (:firstName, :lastName, :age);

  if sqlcode = 0;
    dsply 'Created employee record.' response;
  else;
    dsply ('SQL error ' + %char(sqlcode)) response;
  endif;
  return;
end-proc;

dcl-proc readRecord;
  dsply 'Enter employee id:' response;
  empId = %int(%trim(response));

  exec sql
    select FIRSTNAME, LASTNAME, AGE
      into :firstName, :lastName, :age
      from EMPLOYEE
      where EMPID = :empId;

  if sqlcode = 0;
    dsply ('ID=' + %char(empId) + ' Name=' + %trim(firstName) + ' ' + %trim(lastName) + ' Age=' + %char(age)) response;
  elseif sqlcode = 100;
    dsply 'Employee not found.' response;
  else;
    dsply ('SQL error ' + %char(sqlcode)) response;
  endif;
  return;
end-proc;

dcl-proc updateRecord;
  dsply 'Enter employee id to update:' response;
  empId = %int(%trim(response));

  dsply 'Enter new first name:' response;
  firstName = %trim(response);
  dsply 'Enter new last name:' response;
  lastName = %trim(response);
  dsply 'Enter new age:' response;
  age = %int(%trim(response));

  exec sql
    update EMPLOYEE
      set FIRSTNAME = :firstName,
          LASTNAME  = :lastName,
          AGE       = :age
      where EMPID = :empId;

  if sqlcode = 0;
    dsply 'Employee updated.' response;
  elseif sqlcode = 100;
    dsply 'Employee not found.' response;
  else;
    dsply ('SQL error ' + %char(sqlcode)) response;
  endif;
  return;
end-proc;

dcl-proc deleteRecord;
  dsply 'Enter employee id to delete:' response;
  empId = %int(%trim(response));

  exec sql
    delete from EMPLOYEE
      where EMPID = :empId;

  if sqlcode = 0;
    dsply 'Employee deleted.' response;
  elseif sqlcode = 100;
    dsply 'Employee not found.' response;
  else;
    dsply ('SQL error ' + %char(sqlcode)) response;
  endif;
  return;
end-proc;

dcl-proc listRecords;
  exec sql
    declare c1 cursor for
      select EMPID, FIRSTNAME, LASTNAME, AGE from EMPLOYEE order by EMPID;

  exec sql open c1;
  dow sqlcode = 0;
    exec sql fetch c1 into :empId, :firstName, :lastName, :age;
    if sqlcode = 0;
      dsply ('ID=' + %char(empId) + ' Name=' + %trim(firstName) + ' ' + %trim(lastName) + ' Age=' + %char(age)) response;
    endif;
  enddo;
  exec sql close c1;
  return;
end-proc;
