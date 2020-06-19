/* (по желанию) Из таблицы users необходимо извлечь пользователей, родившихся в августе и мае. 
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

-- пи соблюдении формата ввода даты birthday_at DATE COMMENT 'Дата рождения' , работает код:
-- SELECT id, name as May_and_August_birthday_names, birthday_at FROM users WHERE month(birthday_at) = 5 or 8;
