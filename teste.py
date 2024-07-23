from main import Pessoa
from aluno import Aluno

pessoa= Pessoa(
    'João Otávio',
    '123.456.789-00',
    'Rua 13 de Maio'
)

print(pessoa.get_cpf())
print(pessoa.getEndereco())
pessoa.getNome()

aluno=Aluno(
    'Heloyse',
    '085.728.654-90',
    'Encanto RN',
    '4 ano',
    'INFO'
)

print(aluno.get_cpf())
print(aluno.getEndereco())
aluno.getNome()
aluno.getCurso()
aluno.getTurma()