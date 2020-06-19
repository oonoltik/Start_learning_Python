/*(по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
Отсортируйте записи в порядке, заданном в списке IN.
*/
DROP TABLE IF EXISTS shop.catalogs;
CREATE TABLE shop.catalogs (
id INT UNSIGNED ,
name VARCHAR ( 255 ) COMMENT 'Название раздела'
) COMMENT = 'Разделы интернет-магазина' ;
INSERT INTO catalogs VALUES 
( 1 , 'Процессоры' ),
 ( 2 , 'Мат.платы' ),
 ( 3 , 'Видеокарты' ),
 ( 4 , 'Процессоры1' ),
 (5 , 'Мат.платы1' ),
 ( 6 , 'Видеокарты1' ),
 ( 7 , 'Процессоры2' ),
 ( 8 , 'Мат.платы2' ),
 ( 9 , 'Видеокарты2' );


SELECT * FROM catalogs WHERE id IN(5, 1, 2) 
order by case
when id = 5 then 1
when id = 1 then 2
when id = 2 then 3
END;