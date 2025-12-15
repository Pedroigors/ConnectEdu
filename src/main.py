from aluno import Aluno
from responsavel import Responsavel
from painel import PainelEscolar

aluno = Aluno(
    nome="Lara Maria Cavalcante",
    data_nascimento="15/07/2014",
    sexo="Feminino",
    turma="6A",
    escola="E.E.I.F. Joaquim Libério",
    ano_cursando="6º Ano"
)

aluno.adicionar_nota_prova(7.5)
aluno.adicionar_nota_prova(8.0)
aluno.definir_comportamento(9)
aluno.definir_frequencia(85)
aluno.adicionar_advertencia("Usando celular em sala de aula. Não é permitido.")

responsavel = Responsavel("Isis Maria Cavalcante", "Mãe")

painel = PainelEscolar(aluno, responsavel)
painel.exibir_painel()
