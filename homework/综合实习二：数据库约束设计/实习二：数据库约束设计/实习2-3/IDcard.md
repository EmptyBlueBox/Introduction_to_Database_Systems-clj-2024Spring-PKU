
# 实习二 ： 身份证号码

##### 祝天然 1900012962
##### 郑子豪 1900012935
##### 杨帆 1900012907
---



```python
%load_ext sql
```


```python
import pymysql 
pymysql.install_as_MySQLdb()
%sql mysql://stu1900012935:stu1900012935@162.105.146.37:43306
```


```python
%sql show databases
```

     * mysql://stu1900012935:***@162.105.146.37:43306
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
        <td>stu1900012935</td>
    </tr>
</table>




```python
%sql use stu1900012935
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.





    []




```python
%sql show tables
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    4 rows affected.





<table>
    <tr>
        <th>Tables_in_stu1900012935</th>
    </tr>
    <tr>
        <td>IDnumber</td>
    </tr>
    <tr>
        <td>ref</td>
    </tr>
    <tr>
        <td>weight</td>
    </tr>
    <tr>
        <td>xzqh</td>
    </tr>
</table>




```python
%sql CREATE TABLE if not exists xzqh (code varchar(30), name varchar(30)) SELECT * from dataset.xzqh
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.





    []




```python
%sql select * from xzqh limit 10
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    10 rows affected.





<table>
    <tr>
        <th>code</th>
        <th>name</th>
    </tr>
    <tr>
        <td>110000</td>
        <td>北京市</td>
    </tr>
    <tr>
        <td>110101</td>
        <td>东城区</td>
    </tr>
    <tr>
        <td>110102</td>
        <td>西城区</td>
    </tr>
    <tr>
        <td>110105</td>
        <td>朝阳区</td>
    </tr>
    <tr>
        <td>110106</td>
        <td>丰台区</td>
    </tr>
    <tr>
        <td>110107</td>
        <td>石景山区</td>
    </tr>
    <tr>
        <td>110108</td>
        <td>海淀区</td>
    </tr>
    <tr>
        <td>110109</td>
        <td>门头沟区</td>
    </tr>
    <tr>
        <td>110111</td>
        <td>房山区</td>
    </tr>
    <tr>
        <td>110112</td>
        <td>通州区</td>
    </tr>
</table>




```sql
%%sql

# 把权重保存在表weight中

drop table if exists weight;

create table if not exists weight(
    idx tinyint not null primary key,
    w tinyint not null
);

delete from weight;

insert into weight values (1, 7);
insert into weight values (2, 9);
insert into weight values (3, 10);
insert into weight values (4, 5);
insert into weight values (5, 8);
insert into weight values (6, 4);
insert into weight values (7, 2);
insert into weight values (8, 1);
insert into weight values (9, 6);
insert into weight values (10, 3);
insert into weight values (11, 7);
insert into weight values (12, 9);
insert into weight values (13, 10);
insert into weight values (14, 5);
insert into weight values (15, 8);
insert into weight values (16, 4);
insert into weight values (17, 2);
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.
    17 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []




```python
%sql select * from weight
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    17 rows affected.





<table>
    <tr>
        <th>idx</th>
        <th>w</th>
    </tr>
    <tr>
        <td>1</td>
        <td>7</td>
    </tr>
    <tr>
        <td>2</td>
        <td>9</td>
    </tr>
    <tr>
        <td>3</td>
        <td>10</td>
    </tr>
    <tr>
        <td>4</td>
        <td>5</td>
    </tr>
    <tr>
        <td>5</td>
        <td>8</td>
    </tr>
    <tr>
        <td>6</td>
        <td>4</td>
    </tr>
    <tr>
        <td>7</td>
        <td>2</td>
    </tr>
    <tr>
        <td>8</td>
        <td>1</td>
    </tr>
    <tr>
        <td>9</td>
        <td>6</td>
    </tr>
    <tr>
        <td>10</td>
        <td>3</td>
    </tr>
    <tr>
        <td>11</td>
        <td>7</td>
    </tr>
    <tr>
        <td>12</td>
        <td>9</td>
    </tr>
    <tr>
        <td>13</td>
        <td>10</td>
    </tr>
    <tr>
        <td>14</td>
        <td>5</td>
    </tr>
    <tr>
        <td>15</td>
        <td>8</td>
    </tr>
    <tr>
        <td>16</td>
        <td>4</td>
    </tr>
    <tr>
        <td>17</td>
        <td>2</td>
    </tr>
</table>




```sql
%%sql

# 把对应关系保存在表ref中

drop table if exists ref;

create table if not exists ref(
    idx tinyint not null primary key,
    r char(1) not null
);

delete from ref;

insert into ref values (0, '1');
insert into ref values (1, '0');
insert into ref values (2, 'X');
insert into ref values (3, '9');
insert into ref values (4, '8');
insert into ref values (5, '7');
insert into ref values (6, '6');
insert into ref values (7, '5');
insert into ref values (8, '4');
insert into ref values (9, '3');
insert into ref values (10, '2');
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.
    11 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []




```python
%sql select * from ref
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    11 rows affected.





<table>
    <tr>
        <th>idx</th>
        <th>r</th>
    </tr>
    <tr>
        <td>0</td>
        <td>1</td>
    </tr>
    <tr>
        <td>1</td>
        <td>0</td>
    </tr>
    <tr>
        <td>2</td>
        <td>X</td>
    </tr>
    <tr>
        <td>3</td>
        <td>9</td>
    </tr>
    <tr>
        <td>4</td>
        <td>8</td>
    </tr>
    <tr>
        <td>5</td>
        <td>7</td>
    </tr>
    <tr>
        <td>6</td>
        <td>6</td>
    </tr>
    <tr>
        <td>7</td>
        <td>5</td>
    </tr>
    <tr>
        <td>8</td>
        <td>4</td>
    </tr>
    <tr>
        <td>9</td>
        <td>3</td>
    </tr>
    <tr>
        <td>10</td>
        <td>2</td>
    </tr>
</table>




```sql
%%sql

/*创建表IDnumber，保存存储过程测试时产生的身份证号*/

drop table if exists IDnumber;
create table IDnumber
(
    id varchar(30),
    province varchar(30),
    city varchar(30),
    district varchar(30),
    xzqh_code varchar(6),
    birthday date,
    birth_code varchar(8),
    police_code varchar(2),
    sex varchar(1),
    sex_code varchar(1),
    check_code varchar(1)
);
delete from IDnumber;
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql 

# 校验码生成函数
# 输入身份证号的前17位，根据权值运算，求出和模11的余数，根据对应关系查到校验码
# 返回一个字符，为校验码

drop function if exists gen_idcheck;
create function gen_idcheck (id char(17))
returns char
begin
    declare i integer default 1;
    declare s integer default 0;
    while i <= 17 do
        set s = s + SUBSTRING(id, i, 1) * (select w from weight where idx = i);
        set i = i + 1;
    end while;
    return (select r from ref where idx = s % 11);
end;
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql

# 生成身份证号的存储过程
# 根据省-市-区在xzqh表中查到行政区划码
# 根据生日得到生日码
# 派出所编码和性别编码则简单处理
# 将这四种码拼接得到17位数字，调用函数生成校验码
# 将相应信息和数据插入到表IDnumber中

drop procedure if exists createId;

create 
    procedure createId(province varchar(30), city varchar(30), district varchar(30), birthday varchar(30), sex varchar(1))
begin
    declare xzqh_code varchar(30);
    declare birth_code varchar(30);
    declare police_code varchar(2);
    declare sex_code varchar(1);
    declare check_code varchar(1);
    declare tmp varchar(30);
    declare tmp1 varchar(30);
    
    # 省份code
    set @tmp = (select code from xzqh where (name = province));
    # 城市code
    set @tmp1 = (select code from xzqh where (name = city and code >= @tmp) limit 1);
    # 区县code
    set xzqh_code = (select code from xzqh where (name = district and code >= @tmp1) limit 1);
    
    # 生日code
    set birth_code = birthday;
    
    # 派出所code
    set police_code = "46";
    
    # 性别code
    set sex_code = sex;
    
    set @t = concat(xzqh_code, birth_code, police_code, sex_code);
    # check_code
    set check_code = gen_idcheck(@t);
    
    set @t1 = concat(@t, check_code);
    
    insert into IDnumber values(@t1, province, city, district, xzqh_code, birthday, birth_code, police_code, sex, sex_code, check_code);
    
end;
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    0 rows affected.
    0 rows affected.





    []




```sql
%%sql

call createId('广东省','深圳市','福田区', '20010722', '6');
call createId('广东省','汕头市','潮阳区', '20010721', '7');
call createId('广东省','广州市','白云区', '20010720', '8');
call createId('广东省','揭阳市','惠来县', '20010719', '9');
call createId('广东省','潮州市','潮安区', '20000520', '5');
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.
    1 rows affected.





    []




```sql
%%sql

select * from IDnumber
```

     * mysql://stu1900012935:***@162.105.146.37:43306
    5 rows affected.





<table>
    <tr>
        <th>id</th>
        <th>province</th>
        <th>city</th>
        <th>district</th>
        <th>xzqh_code</th>
        <th>birthday</th>
        <th>birth_code</th>
        <th>police_code</th>
        <th>sex</th>
        <th>sex_code</th>
        <th>check_code</th>
    </tr>
    <tr>
        <td>440304200107224662</td>
        <td>广东省</td>
        <td>深圳市</td>
        <td>福田区</td>
        <td>440304</td>
        <td>2001-07-22</td>
        <td>20010722</td>
        <td>46</td>
        <td>6</td>
        <td>6</td>
        <td>2</td>
    </tr>
    <tr>
        <td>440513200107214672</td>
        <td>广东省</td>
        <td>汕头市</td>
        <td>潮阳区</td>
        <td>440513</td>
        <td>2001-07-21</td>
        <td>20010721</td>
        <td>46</td>
        <td>7</td>
        <td>7</td>
        <td>2</td>
    </tr>
    <tr>
        <td>440111200107204680</td>
        <td>广东省</td>
        <td>广州市</td>
        <td>白云区</td>
        <td>440111</td>
        <td>2001-07-20</td>
        <td>20010720</td>
        <td>46</td>
        <td>8</td>
        <td>8</td>
        <td>0</td>
    </tr>
    <tr>
        <td>445224200107194699</td>
        <td>广东省</td>
        <td>揭阳市</td>
        <td>惠来县</td>
        <td>445224</td>
        <td>2001-07-19</td>
        <td>20010719</td>
        <td>46</td>
        <td>9</td>
        <td>9</td>
        <td>9</td>
    </tr>
    <tr>
        <td>44510320000520465X</td>
        <td>广东省</td>
        <td>潮州市</td>
        <td>潮安区</td>
        <td>445103</td>
        <td>2000-05-20</td>
        <td>20000520</td>
        <td>46</td>
        <td>5</td>
        <td>5</td>
        <td>X</td>
    </tr>
</table>




```python
# 校验码检查

str = '440513200107224678'
w = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 0] 
v = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
i = 0
sum = 0
for c in str:
    x = int(c)
    sum = sum + x * w[i]
    i = i + 1
print(v[sum%11])
```

    8



```python

```
