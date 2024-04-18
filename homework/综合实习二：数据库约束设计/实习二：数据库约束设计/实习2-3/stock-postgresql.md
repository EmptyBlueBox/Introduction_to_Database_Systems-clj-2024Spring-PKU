```python
%load_ext sql
```

    The sql extension is already loaded. To reload it, use:
      %reload_ext sql



```python
import pymysql 
pymysql.install_as_MySQLdb()
%sql mysql://stu1900012907:stu1900012907@162.105.146.37:43306
```


```python
%sql show databases;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    3 rows affected.





<table>
    <tr>
        <th>Database</th>
    </tr>
    <tr>
        <td>dataset</td>
    </tr>
    <tr>
        <td>information_schema</td>
    </tr>
    <tr>
        <td>stu1900012907</td>
    </tr>
</table>




```python
%sql use stu1900012907;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.





    []




```sql
%%sql
set @@foreign_key_checks=0;
drop table if exists my_stock;
create table my_stock
(stock_id     integer,
 volume       integer,
 avg_price    numeric(8,2),
 profit       integer,
 primary key(stock_id));
set @@foreign_key_checks=1;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql
set @@foreign_key_checks=0;
drop table if exists trans;
create table trans
(trans_id     integer,
 stock_id     integer,
 date         integer,
 price        integer,
 amount       integer,
 sell_or_buy  varchar(1),
 primary key(trans_id));
set @@foreign_key_checks=1;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql
set @@foreign_key_checks=0;
drop table if exists newset;
create table newset
(trans_id     integer,
 stock_id     integer,
 price        integer,
 amount       integer,
 primary key(trans_id));
set @@foreign_key_checks=1;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql
drop function if exists calc;
create function calc(sid integer,val integer,num integer)
    returns integer
    begin
        declare ans integer default 0;
        declare i integer default 1;
        declare rem integer;
        declare tmp integer;
        declare p integer;
        declare mn integer;
        set rem=num;
        while i<=(select max(trans_id)from newset) and (select count(*)from newset where newset.trans_id=i and newset.stock_id=sid)=0 do
            set i=i+1;
        end while;
        while i<=(select max(trans_id)from newset) and rem>0 do
            select sum(amount) into tmp
            from newset
            where newset.trans_id=i and newset.stock_id=sid;
            select sum(price) into p
            from newset
            where newset.trans_id=i and newset.stock_id=sid;
            set mn=LEAST(rem,tmp);
            set ans=ans+mn*(val-p);
            set rem=rem-mn;
            update newset
            set amount=amount-mn
            where newset.trans_id=i and newset.stock_id=sid;
            set i=i+1;
            while i<=(select max(trans_id)from newset) and (select count(*)from newset where newset.trans_id=i and newset.stock_id=sid)=0 do
                set i=i+1;
            end while;
        end while;
        return ans;
    end;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql
drop trigger if exists newtrans;
create trigger newtrans before insert on trans
for each row
begin
    if new.stock_id not in(
        select stock_id
        from my_stock)then
            insert into my_stock
                values(new.stock_id,0,0,0);
    end if;
    if new.sell_or_buy='B' then
        update my_stock
        set avg_price=(volume*avg_price+new.amount*new.price)/(volume+new.amount)
        where my_stock.stock_id=new.stock_id;
        update my_stock
        set volume=volume+new.amount
        where my_stock.stock_id=new.stock_id;
        insert into newset
            values(new.trans_id,new.stock_id,new.price,new.amount);
    end if;
    if new.sell_or_buy='S'
    and new.amount<=(
    select volume
    from my_stock
    where my_stock.stock_id=new.stock_id)then
        update my_stock
        set volume=volume-new.amount
        where my_stock.stock_id=new.stock_id;
        update my_stock
        set profit=profit+calc(new.stock_id,new.price,new.amount)
        where my_stock.stock_id=new.stock_id;
    end if;
end;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql
insert into trans
    values(1,1,1,10,1000,'B');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1000</td>
        <td>10.00</td>
        <td>0</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(2,1,2,11,500,'B');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1500</td>
        <td>10.33</td>
        <td>0</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(3,1,3,12,800,'S');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>700</td>
        <td>10.33</td>
        <td>1600</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(4,1,4,12,1000,'S');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>700</td>
        <td>10.33</td>
        <td>1600</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(5,1,5,9,1000,'B');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>1700</td>
        <td>9.55</td>
        <td>1600</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(6,1,6,12,800,'S');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>900</td>
        <td>9.55</td>
        <td>2800</td>
    </tr>
</table>




```sql
%%sql
insert into trans
    values(7,1,7,7,800,'S');
select * from my_stock;
```

     * mysql://stu1900012907:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.





<table>
    <tr>
        <th>stock_id</th>
        <th>volume</th>
        <th>avg_price</th>
        <th>profit</th>
    </tr>
    <tr>
        <td>1</td>
        <td>100</td>
        <td>9.55</td>
        <td>1200</td>
    </tr>
</table>




```python

```
