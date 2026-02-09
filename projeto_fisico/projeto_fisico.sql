-- #Projeto Físico do Banco de Dados - ConnectEdu


CREATE DATABASE IF NOT EXISTS connectedu;
USE connectedu;


-- Tabela: RESPONSAVEL

CREATE TABLE responsavel (
    id_responsavel INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    parentesco VARCHAR(50) NOT NULL
);

-- Tabela: ALUNO

CREATE TABLE aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    codigo VARCHAR(10) NOT NULL UNIQUE,
    nome VARCHAR(100) NOT NULL,
    data_nascimento DATE NOT NULL,
    sexo VARCHAR(15),
    turma VARCHAR(10),
    escola VARCHAR(120),
    ano_cursando VARCHAR(20),
    data_matricula DATE NOT NULL,
    nota_comportamento DECIMAL(4,2),
    frequencia INT,
    id_responsavel INT NOT NULL,

    CONSTRAINT fk_responsavel
        FOREIGN KEY (id_responsavel)
        REFERENCES responsavel(id_responsavel)
        ON UPDATE CASCADE
        ON DELETE RESTRICT
);

-- Tabela: NOTA_PROVA

CREATE TABLE nota_prova (
    id_nota INT AUTO_INCREMENT PRIMARY KEY,
    nota DECIMAL(4,2) NOT NULL,
    id_aluno INT NOT NULL,

    CONSTRAINT fk_nota_aluno
        FOREIGN KEY (id_aluno)
        REFERENCES aluno(id_aluno)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);

-- Tabela: ADVERTENCIA

CREATE TABLE advertencia (
    id_advertencia INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255) NOT NULL,
    id_aluno INT NOT NULL,

    CONSTRAINT fk_advertencia_aluno
        FOREIGN KEY (id_aluno)
        REFERENCES aluno(id_aluno)
        ON UPDATE CASCADE
        ON DELETE CASCADE
);
