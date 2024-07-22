class Pessoa:
  def __init__(self, nomep, cpfp, enderecop):
    self.nome = nomep
    self.__cpf = cpfp
    self._endereco = enderecop

  def getNome(self):
    print(f'Nome: {self.nome}')


  def get_cpf(self):
    return self.__cpf
  
  def getEndereco(self):
    return self._endereco
  

