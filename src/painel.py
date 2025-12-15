class PainelEscolar:
    def __init__(self, aluno, responsavel):
        self.aluno = aluno
        self.responsavel = responsavel

    def exibir_painel(self):
        print("CONNECTEDU")
        print(f"Aluno: {self.aluno.nome}")
        print(f"Data de Nascimento: {self.aluno.data_nascimento}")
        print(f"Sexo: {self.aluno.sexo}")
        print(f"Turma: {self.aluno.turma}")
        print(f"Código do Aluno: {self.aluno.codigo}")
        print(f"Escola: {self.aluno.escola}")
        print(f"Ano/Série: {self.aluno.ano_cursando}")
        print(f"Data da Matrícula: {self.aluno.data_matricula}")
        print(f"Responsável: {self.responsavel.nome} ({self.responsavel.parentesco})")
        print(f"Notas das Provas: {self.aluno.notas_prova}")
        print(f"Nota de Comportamento: {self.aluno.nota_comportamento}")
        print(f"Média Final: {self.aluno.calcular_media():.2f}")
        print(f"Frequência: {self.aluno.frequencia}%")
        print(f"Situação: {self.aluno.situacao()}")
        print(f"Advertências: {self.aluno.advertencias if self.aluno.advertencias else 'Nenhuma'}")
