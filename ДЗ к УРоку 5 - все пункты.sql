
/* 1.Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
*/
DROP table if exists hl_1;
CREATE TABLE hl_1 (
id SERIAL PRIMARY KEY ,
name VARCHAR ( 255 ) COMMENT 'Название' ,
description TEXT COMMENT 'Описание' ,
price DECIMAL ( 11 , 2 ) COMMENT 'Цена' ,
created_at DATETIME  ,
updated_at DATETIME  
) COMMENT = 'Товарные позиции' ;

INSERT INTO `hl_1` (`id`, `name`, `description`, `price`) VALUES
 ('1', 'natus', 'Vitae sed consequatur deserunt sapiente autem tenetur. Vel sit quibusdam officia et. Ullam quo qui ullam.', '471.56'),
 ('2', 'odio', 'Est est quisquam dolores ab delectus quae voluptatem. Aliquid rerum doloribus maiores sequi labore sed sit nihil. Cupiditate itaque fugiat aut nihil reiciendis facilis.', '0.00'),
 ('3', 'est', 'Illum aperiam veniam enim dolorem totam dolores dolorem occaecati. Officiis sed totam doloremque alias. Ut temporibus atque animi ducimus ullam cum dolorum.', '126580634.92'),
 ('4', 'quas', 'Quam sint consequatur eos sit dicta. Mollitia dolorem aut quam magni ut fugit. Laudantium eveniet aut ea qui architecto dignissimos rerum.', '375.33'),
 ('5', 'sed', 'Assumenda quia consectetur facilis omnis. Consequatur consequatur autem quisquam pariatur est qui ducimus. Rerum tenetur et ea et ea. Qui eius maiores ipsam ea reprehenderit reiciendis assumenda.', '600227.85'),
 ('6', 'reiciendis', 'Ratione impedit autem qui non. Aut non cum esse labore aut eveniet. Eos ab qui in quia dignissimos dolor.', '1.20'),
 ('7', 'tenetur', 'Id unde non deserunt veniam alias animi nobis perspiciatis. Consequatur amet similique tempore earum similique voluptas veritatis non. Similique omnis qui tenetur porro non incidunt amet. Non facere et ipsum cupiditate nobis. Nam et molestias corrupti.', '489322.02'),
 ('8', 'esse', 'Dolorum quo nihil perspiciatis incidunt totam tenetur. Quasi dicta ex quia voluptas nihil pariatur aut iure. Nemo suscipit qui aut architecto.', '76758.78'),
 ('9', 'corrupti', 'Ratione expedita neque incidunt quam similique ex. Ea aperiam iusto nulla sunt ipsam atque. Ducimus eum beatae quam. Porro sit voluptate sunt neque modi.', '8437447.45'),
 ('10', 'dolorem', 'Delectus accusantium sed sapiente eligendi. Id facilis repudiandae harum nobis nihil debitis beatae accusantium.', '0.00');


SELECT * FROM hl_1;
UPDATE hl_1 SET created_at = NOW() ;
UPDATE hl_1 SET updated_at = NOW() ;
SELECT * FROM hl_1;


/* 2. Таблица users была неудачно спроектирована. 
Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались 
значения в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, 
сохранив введеные ранее значения.
*/
DROP TABLE IF EXISTS users_hl_2;
CREATE TABLE users_hl_2 (
	id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY, 
    firstname VARCHAR(50),
    lastname VARCHAR(50) COMMENT 'Фамиль', -- COMMENT на случай, если имя неочевидное
    email VARCHAR(120) UNIQUE,
 	password_hash VARCHAR(100), -- 123456 => vzx;clvgkajrpo9udfxvsldkrn24l5456345t
	created_at VARCHAR(50),
    updated_at VARCHAR(50)   
) COMMENT 'юзеры';

INSERT INTO `users_hl_2` (`id`, `firstname`, `lastname`, `email`, `password_hash`, `created_at`, `updated_at`) VALUES
 ('1', 'Katrina', 'Boehm', 'vandervort.cordie@example.org', '375ff3af94ffde64384ded271523bf61c55c6d29', '2020-03-21 21:45', '2020-05-29 07:31'),
 ('2', 'Sibyl', 'Kassulke', 'jessika.paucek@example.com', '76574a4eb656b8f023afc42e882a7c1e0efe042e', '2019-10-25 23:10', '2020-05-31 18:05'),
 ('3', 'Vivianne', 'Olson', 'emil07@example.com', 'e7d65629b6c07a31bbe13193dfcb79b0adf26c21', '2019-11-23 04:44', '2020-06-08 07:56'),
 ('4', 'Corene', 'Runolfsdottir', 'luz98@example.net', 'ac99ad7586cc263d0f829f3cd7571c06022e0af8', '2020-05-18 23:10', '2020-06-10 02:04'),
 ('5', 'Adolphus', 'Aufderhar', 'gibson.roma@example.org', '657ade515631a3697081b2c396c4a505b5523191', '2019-07-27 15:01', '2020-06-07 09:49'),
 ('6', 'Marcelino', 'Miller', 'lhyatt@example.org', 'c9b8edb6ce8be09e434d4d12771690722552f14e', '2019-09-03 06:23', '2020-06-02 08:47'),
 ('7', 'Jazlyn', 'Bartoletti', 'evan34@example.net', 'e72382f9d4926a141b0ce50382d05d78a8b237f2', '2019-11-24 12:14', '2020-05-22 14:18'),
 ('8', 'Brendon', 'Reinger', 'perry79@example.net', '247210903c36423e9cb27e1616a6fb70812f9788', '2020-03-18 06:51', '2020-06-10 02:26'),
 ('9', 'Kenyon', 'Wintheiser', 'ellsworth37@example.com', 'b93a7d66c386f747a4efd323889e980886d41b41', '2019-12-03 09:12', '2020-06-10 17:50'),
 ('10', 'Delores', 'Schoen', 'jacobson.jada@example.org', '18bef71edc0888259d0d34dbdafe10d17bb49468', '2020-03-20 03:25', '2020-05-20 18:37'),
 ('11', 'Elfrieda', 'Farrell', 'terry.pearlie@example.net', 'a5fbf88f43772b7a5939563a625648ec846a1d6d', '2020-05-25 03:56', '2020-06-13 09:32'),
 ('12', 'Marcel', 'Lebsack', 'damon45@example.net', '5f7442ff2597fa338cf8911107ed27b250c34323', '2020-02-14 08:17', '2020-06-17 08:33'),
 ('13', 'Garrison', 'Jakubowski', 'dooley.andre@example.com', '8095604b32c48eeb0521d07bb8ef312391093b15', '2019-11-30 02:45', '2020-06-12 09:28'),
 ('14', 'Quincy', 'Padberg', 'tgleichner@example.net', 'e288a97bdef1638749923e2d0605383dfda548ea', '2020-02-23 19:01', '2020-06-02 14:51'),
 ('15', 'Suzanne', 'Purdy', 'kenton.borer@example.org', '08671b2488df3984bf6f5492be5deeef788f7f57', '2019-12-12 18:58', '2020-06-15 10:11'),
 ('16', 'Lamont', 'Hoeger', 'marquis.mayer@example.net', '72611841b31ec8130d993b85e44a2af71d0e0695', '2019-08-13 17:48', '2020-05-30 05:16'),
 ('17', 'Cheyenne', 'Carroll', 'antonetta.treutel@example.net', 'be220cdebcf3f11643bc9072f168c4bc76d3ec0a', '2020-01-02 03:27', '2020-05-22 20:49'),
 ('18', 'Bridgette', 'Rath', 'phermann@example.net', 'd36d39b628c4896e2c1362e631814f07897f69ad', '2020-03-03 04:56', '2020-06-12 11:53'),
 ('19', 'Frederique', 'Goodwin', 'boyd47@example.org', 'ef3866099f29c6818a6a18bc68fa76433981a3d1', '2020-02-09 21:46', '2020-05-19 15:20'),
 ('20', 'Pattie', 'Sipes', 'nakia.kuhic@example.net', '89f34f381ab2c89d73104a4f6bc75b83eda29ace', '2019-10-12 08:43', '2020-05-23 21:08');

SELECT * FROM users_hl_2;

ALTER TABLE users_hl_2 
CHANGE created_at created_at DATETIME,
CHANGE updated_at updated_at DATETIME;

SELECT * FROM users_hl_2;

/* 3. В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, 
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

/* 4. (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
Месяцы заданы в виде списка английских названий ('may', 'august')*/
DROP TABLE IF EXISTS users;

CREATE TABLE users (
id SERIAL,
name VARCHAR (255) COMMENT 'Имя покупателя' ,
birthday_at VARCHAR (255) COMMENT 'Дата рождения' ,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели' ;

INSERT INTO users (name, birthday_at) VALUES
( 'Геннадий' , '1990-10-05' ),
( 'Наталья' , '1984-11-12' ),
( 'Александр' , '1985-05-20' ),
( 'Сергей' , '1988-02-14' ),
( 'Иван' , '1998-01-12' ),
( 'Мария' , '1992-08-29' ),
('Alejandra Considine', '2012-05-22'),
('Vickie O\'Kon', '1984-04-08'),
('Delphine McDermott', '2015-08-06'),
('Prof. Dustin Leannon PhD', '1979-august-01'),
('Gretchen Aufderhar', '2011-12-11'),
('Linnea Jones', '1971-07-04'),
('Hank Weimann', '1991-06-04'),
('Dr. Spencer Volkman III', '1983-06-14'),
('Brady Mills', '2017-01-22'),
('Brandy Davis', '1988-03-11'),
('Jayde Schroeder', '1983-may-07'),
('Ben Lockman', '1975-09-09'),
('Mr. Cornell Toy IV', '2014-07-21'),
('Julio Hahn', '1997-02-04'),
('Carolyn Schiller I', '1987-03-16'),
('Daren Yundt', '1996-08-02'),
('Dr. Jon Casper', '1995-12-18'),
('Clay Gorczany', '2019-11-10'),
('Dr. Cheyanne Goldner Sr.', '1977-09-14'),
('Luigi Harris', '1991-06-20');



SELECT id, name, birthday_at FROM users WHERE (birthday_at LIKE '%may%' OR birthday_at LIKE '%august%');

-- здесь выводим все имена по групам (список): 
-- SELECT GROUP_CONCAT(name) as May_and_August_birthday_names FROM users WHERE (birthday_at LIKE '%may%' OR birthday_at LIKE '%august%');

-- при соблюдении формата ввода даты birthday_at DATE COMMENT 'Дата рождения' , работает код:
-- SELECT id, name as May_and_August_birthday_names, birthday_at FROM users WHERE month(birthday_at) = 5 or 8;

/*5. (по желанию) Из таблицы catalogs извлекаются записи при помощи запроса. SELECT * FROM catalogs WHERE id IN (5, 1, 2); 
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

/*п.1 Агрегация. Подсчитайте средний возраст пользователей в таблице users */
DROP TABLE IF EXISTS users;

CREATE TABLE users (
id SERIAL,
name VARCHAR ( 255 ) COMMENT 'Имя покупателя' ,
birthday_at DATE COMMENT 'Дата рождения' ,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели' ;

INSERT INTO users (name, birthday_at) VALUES
( 'Геннадий' , '1990-10-05' ),
( 'Наталья' , '1984-11-12' ),
( 'Александр' , '1985-05-20' ),
( 'Сергей' , '1988-02-14' ),
( 'Иван' , '1998-01-12' ),
( 'Мария' , '1992-08-29' );

SELECT id , CONCAT ( name , ' ' , TIMESTAMPDIFF ( YEAR , birthday_at, NOW())) AS name FROM users;
SELECT AVG(TIMESTAMPDIFF (YEAR , birthday_at, NOW())) as average_age FROM users ;

/*п.2 Агрегация Практическое задание теме “Агрегация данных”
Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. 
Следует учесть, что необходимы дни недели текущего года, а не года рождения.
*/
DROP TABLE IF EXISTS users;

CREATE TABLE users (
id SERIAL,
name VARCHAR ( 255 ) COMMENT 'Имя покупателя' ,
birthday_at DATE COMMENT 'Дата рождения' ,
created_at DATETIME DEFAULT CURRENT_TIMESTAMP ,
updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели' ;

INSERT INTO users (name, birthday_at) VALUES
( 'Геннадий' , '1990-10-05' ),
( 'Наталья' , '1984-11-12' ),
( 'Александр' , '1985-05-20' ),
( 'Сергей' , '1988-02-14' ),
( 'Иван' , '1998-01-12' ),
( 'Мария' , '1992-08-29' ),
('Alejandra Considine', '2012-05-22'),
('Vickie O\'Kon', '1984-04-08'),
('Delphine McDermott', '2015-08-06'),
('Prof. Dustin Leannon PhD', '1979-01-01'),
('Gretchen Aufderhar', '2011-12-11'),
('Linnea Jones', '1971-07-04'),
('Hank Weimann', '1991-06-04'),
('Dr. Spencer Volkman III', '1983-06-14'),
('Brady Mills', '2017-01-22'),
('Brandy Davis', '1988-03-11'),
('Jayde Schroeder', '1983-04-07'),
('Ben Lockman', '1975-09-09'),
('Mr. Cornell Toy IV', '2014-07-21'),
('Julio Hahn', '1997-02-04'),
('Carolyn Schiller I', '1987-03-16'),
('Daren Yundt', '1996-08-02'),
('Dr. Jon Casper', '1995-12-18'),
('Clay Gorczany', '2019-11-10'),
('Dr. Cheyanne Goldner Sr.', '1977-09-14'),
('Luigi Harris', '1991-06-20');

SELECT COUNT(*) as Birthday_quantaty, 
DAYOFWEEK(CONCAT((year(now())),'-', (month(birthday_at)), '-', (day(birthday_at)))) AS Weekday_This_Year 
FROM users 
GROUP BY Weekday_This_Year 
ORDER BY Birthday_quantaty DESC;

/*п.3 Агрегация  Практическое задание теме “Агрегация данных”
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




