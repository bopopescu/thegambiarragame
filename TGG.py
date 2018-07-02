from firebase.firebase import FirebaseAuthentication
from firebase.firebase import FirebaseApplication
from random import randint
import getpass
import time
import sys


class Character:
    def __init__(self):
        self.name = ''
        self.race = ''
        self.nv = 1
        self.hp = 0
        self.hpmax = 0
        self.sp = 0
        self.spmax = 0
        self.dano = 0
        self.atk = 0
        self.matk = 0
        self.defe = 0
        self.mdefe = 0
        self.pfor = 0
        self.pcon = 0
        self.pint = 0
        self.pdex = 0
        self.crit = 0
        self.esq = 0

    def armas(self):
        a = 2


class Player(Character):
    def __init__(self):
        Character.__init__(self)
        self.skill = 0
        self.skill2 = 0
        self.skill3 = 0
        self.skill4 = 0
        self.supreme = 0
        self.coin = 0
        self.bag = {}
        if self.race == "Politico":
            self.hpmax = 170
            self.hp = self.hpmax
            self.spmax = 160
            self.sp = self.spmax
        elif self.race == "Viking":
            self.hpmax = 200
            self.hp = self.hpmax
            self.spmax = 130
            self.sp = self.spmax
        elif self.race == "Jedi":
            self.hpmax = 180
            self.hp = self.hpmax
            self.spmax = 180
            self.sp = self.spmax
        elif self.race == "Palhaço":
            self.hpmax = 150
            self.hp = self.hpmax
            self.spmax = 200
            self.sp = self.spmax
        elif self.race == "Dark Safari":
            self.hpmax = 160
            self.hp = self.hpmax
            self.spmax = 190
            self.sp = self.spmax
        elif self.race == "Constantine":
            self.hpmax = 170
            self.hp = self.hpmax
            self.spmax = 190
            self.sp = self.spmax
        elif self.race == "Avenger":
            self.hpmax = 180
            self.hp = self.hpmax
            self.spmax = 180
            self.sp = self.spmax

    def choosewapon(self):
        a = ''
        while a == '':
            print("Escolha a Arma Inicial:")
            if self.race == "Politico":
                print("(1)Adaga de Ferro, (2)Punhal Dente de Urso, (3)Estilingue de Madeira")
                a = input("> ")
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Viking":
                print("(1)Machado De Ferro, (2)Marreta de Pedra, (3)Maça de Ferro")
                a = input("> ")
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Jedi":
                print("(1)Sabre Verde, (2)Sabre Azul, (3)Sabre Amarelo")
                a = input("> ")
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Palhaço":
                print("(1)Varinha de Madeira, (2)Luvas Brancas, (3)Balão Magico")
                a = input("> ")
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Dark Safari":
                print("(1)Chicote de couro, (2)Cajado de Madeira, (3)Laço de Couro")
                a = input("> ")
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Constantine":
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            elif self.race == "Avenger":
                self.atk = 0
                self.matk = 0
                self.defe = 0
                self.mdefe = 0

                self.dano = 0
            try:
                a = int(a)
            except ValueError:
                print("Ainda não temos essa Arma")
                a = ''



class Game:
    def __init__(self):
        print("Oi")
        self.p = None
        self.app = FirebaseApplication('https://thegambiarragame.firebaseio.com', authentication=None)
        self.authentication = FirebaseAuthentication('', '@gmail.com', extra={'id': 123})

    def carregarpersonagem(self, char):
        self.p.nv = self.app.get('/Personagens' + char, "Nv")
        self.p.hp = self.app.get('/Personagens' + char, "Hp")
        self.p.hpmax = self.app.get('/Personagens' + char, "HpMax")
        self.p.sp = self.app.get('/Personagens' + char, "Sp")
        self.p.spmax = self.app.get('/Personagens' + char, "SpMax")
        self.p.dano = self.app.get('/Personagens' + char, "Damage")
        self.p.atk = self.app.get('/Personagens' + char, "Atk")
        self.p.matk = self.app.get('/Personagens' + char, "MAtk")
        self.p.defe = self.app.get('/Personagens' + char, "Def")
        self.p.mdefe = self.app.get('/Personagens' + char, "MDef")
        self.p.pfor = self.app.get('/Personagens' + char, "For")
        self.p.pcon = self.app.get('/Personagens' + char, "Con")
        self.p.pint = self.app.get('/Personagens' + char, "Int")
        self.p.pdex = self.app.get('/Personagens' + char, "Dex")
        self.p.crit = self.app.get('/Personagens' + char, "Crit")
        self.p.esq = self.app.get('/Personagens' + char, "Esq")
        self.p.race = self.app.get('/Personagens' + char, "Class")
        self.p.skill = self.app.get('/Personagens' + char, "Skill")
        self.p.skill2 = self.app.get('/Personagens' + char, "Skill2")
        self.p.skill3 = self.app.get('/Personagens' + char, "Skill3")
        self.p.skill4 = self.app.get('/Personagens' + char, "Skill4")
        self.p.supreme = self.app.get('/Personagens' + char, "Supreme")
        self.p.coin = self.app.get('/Personagens' + char + '/Bag', "Coins")
        self.p.bag = self.app.get('/Personagens' + char + '/Bag', "Iten")

    def play(self):
        correto = False
        self.p = Player()
        while correto is False:
            self.p.name = str(input("User: "))
            result = self.app.get('/Personagens', self.p.name)
            if result is not None:
                print("Personagem existente")
                b = str(input("Senha: "))
                paz = self.app.get('/Personagens/' + self.p.name, "Pass")
                if paz == b:
                    self.carregarpersonagem(self.p.name)
                    print("Carregado")
                    correto = True
                else:
                    print("Senha Incorreta!")
                    correto = False
            else:
                print("Novo Personagem")
                senha = str(input("Senha: "))
                self.p.race = str(input("Classe: "))

                correto = True

