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