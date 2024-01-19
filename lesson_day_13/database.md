# DataBase queries exercises

1. select from customer where first_name = 'Jamie';
2. select from customer where first_name = 'Jamie'and last_name = 'Rice';
3. select from customer where last_name = 'Rodriguez' or last_name = 'Adam';
4. select from  country where country = 'Afghanistan' and country = 'Mongolia';
5. select country_id from country where country = 'Germany';
6. select city from city where city_id = 38;
7. select language_id from language where name = 'English';
   select title from film where language_id = 1;
8. select from film where title = 'Apollo Teen';
9. select film_id from film where title = 'Apollo Teen';
   select actor_id from film_actor where film_id = 33;
10. select category_id from film_category where film_id = 33;
    select name from category where category_id = 7;
