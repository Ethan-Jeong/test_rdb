create table information(

    id text,
    name text

);

create table information(id text,name text);

insert into information(id,name)
values('1','홍길동');

insert into information(name,id)
values('장길산',2);

insert into information(name)
values('정몽길');

select id , name from information ;

select id , name from information
where id = '2';

select id, name from information
where id is null;

delete  from information
where id is null;

select id, name from information
where id is null;

select * from information ;

insert into information
values('4','비망록');

select * from information ;

drop table information;