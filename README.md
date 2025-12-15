# ConnectEdu – Painel de Acompanhamento Escolar

## Descrição do Projeto

O ConnectEdu é um sistema simples de acompanhamento escolar desenvolvido em Python. Ele organiza informações acadêmicas e pessoais do aluno em um único painel, permitindo uma visão clara do desempenho escolar a partir de notas, frequência e comportamento.

O projeto foi pensado para ser direto, compreensível e bem estruturado, priorizando clareza do código, aplicação correta da Programação Orientada a Objetos e explicações acessíveis sobre o funcionamento do sistema.


## Funcionalidades

Cadastro de aluno com dados pessoais e escolares;
Registro de notas de provas;
Registro de nota de comportamento;
Registro de frequência escolar;
Cálculo automático da média final;
Definição da situação do aluno (Aprovado, Recuperação ou Reprovado);
Exibição organizada das informações no terminal.

## Classes Principais

### Classe Aluno

É a classe central do sistema. Armazena os dados pessoais e acadêmicos do aluno e implementa as principais regras de negócio.

Principais responsabilidades:

Armazenar informações do aluno;
Registrar notas, frequência e comportamento;
Calcular a média final;
Definir a situação escolar do aluno.

### Classe Responsavel

Representa o responsável legal pelo aluno, permitindo relacionar o estudante a um contexto familiar.

### Classe PainelEscolar

Responsável apenas pela exibição das informações, garantindo a separação entre a lógica do sistema e a apresentação dos dados.

## Lógica do Sistema

A média final do aluno é calculada a partir da média das provas e da nota de comportamento. A situação escolar é definida considerando a média final e a frequência:

**Aprovado**: média maior ou igual a 7 e frequência mínima de 75%;
**Recuperação**: média entre 5 e 6,9;
**Reprovado**: média inferior a 5.

Essa lógica foi adotada por ser simples, coerente com o contexto escolar e fácil de compreender.

## Possíveis usos da nossa solução

* Sistemas simples de acompanhamento escolar em pequenas instituições;
* Ferramentas internas para professores organizarem informações dos alunos;
* Projetos educacionais voltados à transparência do desempenho acadêmico;

Em pequenas ou grandes escolas, dados como notas, frequência e comportamento acabam sendo registrados de forma dispersa, muitas vezes em livros de atas ou diários de classe que podem ser danificados ou perdidos, o que dificulta uma visão completa e organizada do desempenho do estudante.

O ConnectEdu pode servir como base para sistemas simples de acompanhamento escolar, auxiliando professores e gestores a organizarem informações essenciais em um único local. A solução também pode apoiar a comunicação com responsáveis, oferecendo informações com clareza sobre a situação acadêmica do aluno.

## Status do Projeto

Projeto em desenvolvimento, com foco em aprendizado e aplicação prática dos conceitos.

## Autor

Projeto desenvolvido por Pedro Igor Mendes de Sousa.
