class Musica:

    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David', duracao=248)
musica = Musica(nome='the trooper', artista='iron Maiden', duracao=245)
musica = Musica(nome='Hotel california', artista='Eagles', duracao=390)


class Carro:
    def __init__(self, modelo='', cor='', ano=''):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

carro1 = Carro(modelo= 'Fiat', cor='Azul', ano='2000')
carro2 = Carro(modelo= 'BMW', cor='Amarelo', ano='2015')
carro3 = Carro(modelo= 'Ferrari', cor='Vermelho', ano='2020')

class Cliente:
    Clientes = []
    def __init__(self, nome='', idade='', altura='', peso=''):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.peso = peso
        Cliente.Clientes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.altura} | {self.peso}'
    
    def listar_clientes():
        for Clientes in Cliente.Clientes:
            print(f'{Clientes.nome} | {Clientes.idade} | {Clientes.altura} | {Clientes.peso}')

cliente1 = Cliente(nome='André', idade='23', altura='1.78', peso='95.kg')
cliente2 = Cliente(nome='Marcia', idade='20', altura='1.50', peso='50.kg')
cliente3 = Cliente(nome='Felipe', idade='30', altura='1.69', peso='67.kg')
cliente4 = Cliente(nome='Matheus', idade='18', altura='1.70', peso='60.kg')

print(dir(Cliente))