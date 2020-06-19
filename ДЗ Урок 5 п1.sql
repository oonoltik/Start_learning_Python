drop table if exists hl_1;
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