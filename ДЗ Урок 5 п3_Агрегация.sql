/*Практическое задание теме “Агрегация данных”
(по желанию) Подсчитайте произведение чисел в столбце таблицы
*/
drop table if exists multiply;
create table multiply(
id SERIAL ,
table_value INT COMMENT 'число'
);

INSERT INTO `multiply` (`table_value`) VALUES 
(ROUND (RAND() * 100)),
(ROUND (RAND() * 100)),
(ROUND (RAND() * 100)),
(ROUND (RAND() * 100));

SELECT * FROM multiply;
select 'произведение чисел в столбце таблицы',
exp(sum(ln(table_value))) from multiply;


