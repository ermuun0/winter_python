1. create database with template lesson_day_15_wrong;
create database lesson_day_15_wrong_template with template lesson_day_15_wrong;
alter database lesson_day_15_wrong rename to lesson_day_15;
\c lesson_day_15
create schema lesson_day_15_schema;
2. 1.reate table country(                                                   country_id integer primary key,                                                         country_name varchar(255));
2.alter table country rename to country_new;
ALTER TABLE
3.alter table country_new add region_id char(255);
4. create table locations (                                                location_id integer,                                                                    street_address varchar(40),                                                             postal_code varchar(12),                                                                city varchar(32),                                                                       state_province varchar(25),                                                             country_id varchar(2),                                                                  primary key(location_id));
5. alter table locations add region_id text;
6. alter table locations drop column city;
7. alter table locations rename column state_province to state;
8. add primary key (location_id, country_id);
9. alter table locations drop constraint locations_pkey;
10. 