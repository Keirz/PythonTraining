import math

class conta:
    def __init__(self, nome, extrato, cartaoLimite, cheque, id, totalDisp):
        self.titular = nome
        self.__saldo = extrato
        self.__limite = cartaoLimite
        self.__check = cheque
        self.__numero = id
        self.__total = totalDisp

    @property
    def nome(self):
        return self.titular
    @property
    def extrato(self):
        return self.__saldo
    @property
    def cartaoLimite(self):
        return self.__limite
    @property
    def cheque(self):
        return self.__check
    @property
    def id(self):
        return self.__numero
    @property
    def totalDisp(self):
        return self.__total
    @totalDisp.setter
    def totalDisp(self):
        self.totalDisp = self.extrato + self.cartaoLimite
    @cheque.setter
    def cheque(self):
        if self.totalDisp >= 0:
            self.cheque == False
        else:
            self.cheque == True
    
            
def especial(self):
    if self.cheque == True:
        print('-------------------------ATENÇÃO-----------------------------------')
        print('Conta {} se encontra com saldo NEGATIVo e utilizando o CHEQUE ESPECIAL'.format(self.id))
        self.especial == True
    else:
        self.especial == False

def sacavel(self, sacavel):
    if self.totalDisp >= self.extrato + self.cartaoLimite and especial == False:
        return sacavel == True
    else:
        return sacavel == False
   
    
def checagemExtrato(self, value):
    value = self.extrato + self.cartaoLimite
    print('Olá {}, sobre a solicitação de checagem de saldo disponível, seguem informações da conta {}:'.format(self.nome, self.id))
    especial(self)
    if(value > self.cartaoLimite and value > self.extrato):
        print('Você possui um total de saldo de R$ {}, sendo que deste valor, R$ {} é referente ao saldo disponível em conta e R$ {} disponível em limite de cartao.'.format(value, self.extrato, self.cartaoLimite))       
    else:
        print('Você não possui valor suficiente para efetuar o saque. O seu extrato atual é de R$ {}' .format(self.extrato))



def saca(self, valor):
    self.totalDisp -= valor
    print('Olá {}, seja bem vindo, calculando a possibilidade de saque da conta {}'.format(self.nome, self.id))
    sacavel(self)
    if sacavel == False:
        especial(self)
        print('Você não possui saldo suficiente em conta')
        checagemExtrato(self)
    else:    
        especial(self)
        print("Saque de R$ {} realizado com sucesso na conta de número {}".format(valor, self.id))
        checagemExtrato(self)