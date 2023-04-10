create database netflix;

use netflix;

create table usuarios(
	id_usuario int auto_increment primary key,
	usuario varchar(150),
    email varchar(100),
    plano varchar(20),
    tipo varchar(20),
    idade int
);

create table filmes(
	id_filme int auto_increment primary key,
    filme varchar(200),
    plano varchar(50),
    descricao varchar(255),
    class int
);

insert into usuarios(usuario, email, plano, tipo, idade)
	values
    ('Julia', 'jugui@gmail.com', 'premium', 'admin', 18),
    ('Luis', 'lui@gmail.com', 'basic', 'user', 17);
    
select * from usuarios;

insert into filmes(filme, plano, descricao, class)
	values
    ('Gente Grande', 'premium', 'AAA', 12),
    ('Crepúsculo', 'premium', 'BBB', 16);
    
select * from filmes;
