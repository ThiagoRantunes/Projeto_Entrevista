CREATE DATABASE curriculos_bd;

USE curriculos_bd;

CREATE TABLE usuarios(
    id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255),
    telefone INT,
    minibio VARCHAR(255),
    entrevista INT CHECK (entrevista >= 1 AND entrevista <= 10),
    teste_teorico INT CHECK (teste_teorico >= 1 AND teste_teorico <= 10),
    teste_pratico INT CHECK (teste_pratico >= 1 AND teste_pratico <= 10),
    soft_skills INT CHECK (soft_skills >= 1 AND soft_skills <= 10)
);

INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Thiago', 15999999999, 'Sou programador', 10, 9, 8, 10);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Gloria', 15999999999, 'Sou programador', 1, 9, 6, 2);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Nivaldo', 15999999999, 'Sou programador', 10, 4, 2, 7);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('VItor', 15999999999,'Sou programador', 10, 9, 8, 9);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Luiz', 15999999999, 'Sou programador', 8, 5, 2, 3);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Muril', 15999999999, 'Sou programador', 1, 3, 5, 2);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Dolly', 15999999999, 'Sou programador', 10, 9, 10, 10);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('João', 15999999999, 'Sou programador', 7, 9, 3, 10);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Otavio', 15999999999, 'Sou programador', 10, 2, 3, 6);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Ana', 15999999999, 'Sou programador', 3, 9, 8, 3);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Friser', 15999999999, 'Sou programador', 6, 3, 7, 1);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Carlos', 15999999999, 'Sou programador', 3, 5, 8, 4);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Giovana', 15999999999, 'Sou programador', 2, 5, 8, 10);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Patric', 15999999999, 'Sou programador', 4, 9, 8, 6);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Fernando', 15999999999, 'Sou programador', 10, 9, 4, 3);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Ashley', 15999999999, 'Sou programador', 6, 5, 4, 10);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Camile', 15999999999, 'Sou programador', 8, 6, 8, 3);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Pedro', 15999999999, 'Sou programador', 4, 9, 8, 3);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Gordola', 15999999999, 'Sou programador', 8, 9, 8, 5);
INSERT INTO usuarios (nome, telefone, minibio, entrevista, teste_teorico, teste_pratico, soft_skills) VALUES ('Magrão', 15999999999, 'Sou programador', 4, 6, 8, 7);
