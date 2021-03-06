import abc, interface_veiculo

class Veiculo(interface_veiculo.InterfaceVeiculo, abc.ABC):
    """Essa é a classe Veiculo. Essa classe é utilizada para instanciar novos veiculos em nosso programa. """
    def __init__(self, cor, tipo_combustivel, potencia):
        self._cor = cor
        self.__tipo_combustivel = tipo_combustivel
        self.__potencia = potencia
        self._qtd_combustivel = 0
        self.__is_ligado = False
        self.__velocidade = 0

    def __del__(self):
        print("O objeto foi removido da memória. :)")

    @property
    def cor(self):
        return self._cor

    def pintar(self, cor):
        self._cor = cor

    def abastecer(self, qtd_combustivel):
        """O método abastecer recebe como parâmetro a quantidade de combustível e incrementa no atributo qtd_combustível do objeto Carro."""
        self._qtd_combustivel += qtd_combustivel

    def ligar(self):
        if not self.__is_ligado: 
            self.__is_ligado = True
            print("O veiculo foi ligado!")
        else: print("O veiculo já está ligado!")

    def desligar(self):
        if self.__is_ligado: 
            self.__is_ligado = False
            print("O veiculo foi desligado!")
        else: print("O veiculo já está desligado!")

    def acelerar(self, velocidade=10):
        if self.__is_ligado: self.__velocidade += velocidade
        else: print("O veiculo precisa estar ligado para ser acelerado.")
