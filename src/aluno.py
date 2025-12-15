import random
from datetime import date

class Aluno:
    def __init__(self, nome, data_nascimento, sexo, turma, escola, ano_cursando):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.sexo = sexo
        self.turma = turma
        self.escola = escola
        self.ano_cursando = ano_cursando
        self.data_matricula = date.today()
        self.codigo = self.gerar_codigo_aluno()
        self.notas_prova = []
        self.nota_comportamento = 0
        self.frequencia = 0
        self.advertencias = []

    def gerar_codigo_aluno(self):
        ano = date.today().year
        sufixo = random.randint(1000, 9999)
        return f"{ano}{sufixo}"

    def adicionar_nota_prova(self, nota):
        self.notas_prova.append(nota)

    def definir_comportamento(self, nota):
        self.nota_comportamento = nota

    def definir_frequencia(self, frequencia):
        self.frequencia = frequencia

    def adicionar_advertencia(self, advertencia):
        self.advertencias.append(advertencia)

    def calcular_media(self):
        if not self.notas_prova:
            return 0
        media_provas = sum(self.notas_prova) / len(self.notas_prova)
        return (media_provas + self.nota_comportamento) / 2

    def situacao(self):
        media = self.calcular_media()
        if media >= 7 and self.frequencia >= 75:
            return "Aprovado"
        elif media >= 5:
            return "Recuperação"
        else:
            return "Reprovado"
