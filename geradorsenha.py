import pandas as pd
from random import randint


class Generatorpassword:
    def __init__(self, ex, num, word=''):
        self.ex = ex
        self.num = num
        self.word = word

    def password(self):
        df_read = pd.read_excel(self.ex)
        lista = df_read['Palavras'].tolist()
        aleatorio = randint(0, len(lista))
        self.word = list((lista[aleatorio]).lower())
        if len(self.word) < self.num:
            listagem = self.metody1()
        else:
            listagem = self.metody2()

        number_ale = randint(1000, 9000)
        result = ''.join(listagem) + str(number_ale)
        return result

    def metody1(self):
        newlist = []
        legth = len(self.word)
        for index, n in enumerate(self.word):
            if index == legth - 1:
                newlist.append(n.upper())
            else:
                newlist.append(n)
        return newlist

    def metody2(self):
        newlist = []
        for index, n in enumerate(self.word):
            if index == self.num - 1:
                newlist.append(n.upper())
            else:
                newlist.append(n)
        return newlist


excel = r'C:\Users\Julio\Downloads\gerador_senhas.xlsx'
password = Generatorpassword(excel, 2)
print(password.password())
