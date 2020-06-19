/* В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, 
если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, 
чтобы они выводились в порядке увеличения значения value. Однако, нулевые запасы должны выводиться в конце, после всех записей.
*/

DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
id SERIAL,
name VARCHAR (255) COMMENT 'Название',

value INT UNSIGNED COMMENT 'Запас товарной позиции на складе'
) COMMENT = 'Запасы на складе';

INSERT INTO `storehouses_products` (`name`, `value`) VALUES 
('eveniet', 8),
('nemo', 6),
('sapiente', 7),
('itaque', 7),
('blanditiis', 0),
('quis', 7),
('id', 0),
('et', 7),
('excepturi', 9),
('quod', 5),
('rerum', 4),
('ipsa', 9),
('ea', 4),
('neque', 0),
('aut', 4),
('qui', 8),
('tempore', 8),
('aut', 8),
('ipsum', 6),
('modi', 8);
 
SELECT * FROM storehouses_products;

SELECT `value` FROM `storehouses_products` ORDER BY IF(`value` = 0, 1, 0), `value`;