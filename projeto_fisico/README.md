# Projeto Físico do Banco de Dados – ConnectEdu 
Este diretório apresenta o projeto físico de banco de dados do ConnectEdu, desenvolvido. O foco deste entregável é demonstrar como o modelo conceitual do sistema foi transformado em uma estrutura real de banco de dados.

## Sobre o Sistema
O ConnectEdu é um sistema de acompanhamento escolar voltado para responsáveis, com o objetivo de centralizar informações importantes do aluno, como dados pessoais, notas, frequência e advertências. O banco de dados foi projetado para dar suporte a essas funcionalidades de forma organizada e coerente com o funcionamento do sistema.

## Definição do Projeto Físico

A construção do projeto físico teve início a partir do modelo conceitual do sistema, no qual foram identificadas as principais entidades envolvidas no contexto do ConnectEdu. A partir dessa análise, foi possível definir quais informações precisariam ser armazenadas e como elas se relacionam.
Essas entidades foram convertidas em tabelas do banco de dados, com a definição de seus respectivos campos, tipos de dados e chaves. O diagrama do projeto físico foi elaborado para representar visualmente essa estrutura.

## Decisões de Modelagem

As tabelas do banco de dados foram definidas de forma a representar apenas as entidades essenciais do sistema, os tipos de dados foram escolhidos de acordo com a natureza das informações armazenadas. Campos textuais utilizam o tipo VARCHAr, datas utilizam o tipo DATE e valores numéricos, como notas, utilizam DECIMAL.

Todas as tabelas possuem chaves primárias, responsáveis por identificar cada registro. As chaves estrangeiras foram utilizadas para representar os relacionamentos entre as tabelas. Também foram aplicadas restrições, como NOT NULL em campos obrigatórios e UNIQUE no código do aluno, assegurando que informações essenciais não sejam duplicadas ou armazenadas de forma incompleta. 

## Componente Extensionista – Projeto Físico de Banco de Dados
O projeto físico de banco de dados é a fase em que o sistema deixa de ser apenas uma ideia ou um desenho e passa a ser organizado de forma concreta para funcionar em um banco de dados. É nesse momento que decidimos como os dados serão realmente guardados, criando tabelas, definindo os tipos de cada informação e estabelecendo como elas se relacionam.

Para quem está aprendendo a programar, entender o projeto físico é muito importante porque ele ajuda a ligar o que é feito no código com o que acontece no banco de dados. Muitas vezes o iniciante consegue escrever o código, mas não entende como os dados são armazenados corretamente. Aprender projeto físico faz com que o estudante desenvolva uma visão mais completa do sistema, entendendo que programar não é apenas escrever código, mas também organizar bem os dados. 

