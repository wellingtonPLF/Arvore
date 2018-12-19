class No:
    def __init__(self,left = None,right = None,ano = None,titulo = None):
        self._ano = ano
        self._titulo = titulo
        self._left = left
        self._right = right

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def set_left(self,no):
        self._left = no

    def set_right(self,no):
        self._right = no

    def get_ano(self):
        return self._ano

    def get_titulo(self):
        return self._titulo

    def set_ano(self,ano):
        self._ano = ano

    def set_titulo(self,titulo):
        self._titulo = titulo

    def __str__(self):
        return f"............................\nAno = {self._ano}\nTitulo = {self._titulo}\n............................"

class Arvore:
    def __init__(self, arvore = None, check = None):
        self._arvore = arvore
        self._check = check

    def inserir(self,ano,titulo):
        put = No()
        put.set_ano(ano)
        put.set_titulo(titulo)
        if self._arvore == None:
            self._arvore = put
            self._check = put
        else:
            while True:
                if put.get_titulo()>self._check.get_titulo():
                    if self._check.get_right()!=None:
                        self._check = self._check.get_right()
                    else:
                        self._check.set_right(put)
                        self._check = self._arvore
                        put = None
                        break
                else:
                    if self._check.get_left()!=None:
                        self._check = self._check.get_left()
                    else:
                        self._check.set_left(put)
                        self._check = self._arvore
                        put = None
                        break
        self.balanceamento(self._arvore,-1)

    def busca_titulo(self,arvore,dado):
        if arvore is not None:
            if arvore.get_titulo() == dado:
                return arvore
            a = self.busca_titulo(arvore.get_left(),dado)
            b =self.busca_titulo(arvore.get_right(),dado)
            if a == None and b == None:
                return None
            else:
                if a != None:
                    return a
                if b!= None:
                    return b
        else:
            return None

    def busca_ano(self,arvore,dado):
        if arvore is not None:
            if arvore.get_ano() == dado:
                return arvore
            a = self.busca_ano(arvore.get_left(),dado)
            b =self.busca_ano(arvore.get_right(),dado)
            if a == None and b == None:
                return None
            else:
                if a != None:
                    return a
                if b!= None:
                    return b
        else:
            return None

    def remover(self,arvore,dado,valor):
        if arvore is not None:
            valor+=1
            if arvore.get_titulo() == dado:
                if arvore.get_right()!=None and arvore.get_left()!=None:
                    self.left(arvore,dado,arvore.get_ano)
                else:
                    if valor==1:
                        if arvore.get_left()!=None:
                            self._arvore = arvore.get_left()
                        if arvore.get_right() != None:
                            self._arvore = arvore.get_right()
                        self._check = self._arvore
                        return None
                    else:
                        return dado
            a = self.remover(arvore.get_left(),dado,valor)
            b =self.remover(arvore.get_right(),dado,valor)
            if a == None and b == None:
                return None
            else:
                if a != None:
                    if arvore.get_left().get_left()!=None:
                        arvore.set_left(arvore.get_left().get_left())
                    elif arvore.get_left().get_right()!=None:
                        arvore.set_left(arvore.get_left().get_right())
                    else:
                        arvore.set_left(None)
                    return b
                if b!= None:
                    if arvore.get_right().get_left()!=None:
                        arvore.set_right(arvore.get_right().get_left())
                    elif arvore.get_right().get_right()!=None:
                        arvore.set_right(arvore.get_right().get_right())
                    else:
                        arvore.set_right(None)
                    return a
        else:
            return None

    def left(self,arvore,titulo,ano):
        a = arvore.get_right()
        while True:
            if a.get_left()!=None:
                a = a.get_left()
            else:
                c = a.get_ano()
                d = a.get_titulo()
                a.set_ano(ano)
                a.set_titulo(titulo)
                arvore.set_ano(c)
                arvore.set_titulo(d)
                a = None
                c = None
                d = None
                break

    def altura(self,arvore,valor):
        if arvore is not None:
            valor +=1
            a = self.altura(arvore.get_left(),valor)
            b = self.altura(arvore.get_right(),valor)
            if a==None and b==None:
                return valor
            if a!=None and b!=None:
                if a>b or a==b:
                    return a
                else:
                    return b
            if not(a!=None and b!=None) and (a!=None or b!=None):
                if a!=None:
                    return a
                if b!=None:
                    return b
        else:
            return None

    def lista(self,arvore,lista):
        if arvore is not None:
            lista.append(arvore.get_titulo())
            a = self.lista(arvore.get_left(),lista)
            b =self.lista(arvore.get_right(),lista)
            if a==None and b==None:
                return lista
            if a!=None and b!=None:
                if len(a)>len(b):
                    return a
                else:
                    return b
            if not(a!=None and b!=None) and (a!=None or b!=None):
                if a!=None:
                    return a
                if b!=None:
                    return b
        else:
            return None

    def balanceamento(self,arvore,valor):
        if arvore is not None:
            x = self.altura_B(arvore,valor)
            y = self.altura_B(arvore.get_left(), valor)
            z = self.altura_B(arvore.get_right(), valor)
            if x == 2 or x == -2:
                if y!=0 or z!=0:
                    if y ==2 or y==-2:
                        self.balanceamento(arvore.get_left(),valor)
                        return None
                    if z ==2 or z ==-2:
                        self.balanceamento(arvore.get_right(), valor)
                        return None
                    if (x==2 and y ==1):
                        self.turn_right(arvore)
                        return None
                    if (x==2 and y ==-1):
                        self.turn_all(arvore,0)
                        return None
                    if (x == -2 and z == 1) or (x == -2 and z == 0):
                        self.turn_all(arvore,1)
                        return None
                    if (x == -2 and z == -1):
                        self.turn_left(arvore)
                        return None
            if z == None and y == None:
                return None
            a = self.balanceamento(arvore.get_left(), valor)
            b = self.balanceamento(arvore.get_right(), valor)
            if a==None and b ==None:
                return None
        else:
            return None

    def altura_B(self,arvore,valor):
        if arvore is not None:
            valor+=1
            x = self.altura(arvore.get_left(),valor)
            y = self.altura(arvore.get_right(), valor)
            if x == None and y==None:
                return 0
            if x ==None and y !=None:
                return -y
            if x!=None and y == None:
                return x
            if x!=None and y!=None:
                return x-y
        else:
            return None

    def turn_right(self,arvore):
        put = No()
        put.set_titulo(arvore.get_titulo())
        put.set_ano(arvore.get_ano())
        if arvore.get_right() != None:
            put.set_right(arvore.get_right())
            arvore.set_right(None)

        if arvore.get_left().get_right() == None:
            arvore.get_left().set_right(put)
        else:
            if put.get_right() == None:
                put.set_right(arvore.get_left().get_right())
            else:
                put.set_left(arvore.get_left().get_right())
            arvore.get_left().set_right(put)
        self.remover(self._arvore, arvore.get_titulo(), 0)

    def turn_left(self,arvore):
        put = No()
        put.set_titulo(arvore.get_titulo())
        put.set_ano(arvore.get_ano())
        if arvore.get_left()!=None:
            put.set_left(arvore.get_left())
            arvore.set_left(None)

        if arvore.get_right().get_left() == None:
            arvore.get_right().set_left(put)
        else:
            if put.get_left()==None:
                put.set_left(arvore.get_right().get_left())
            else:
                put.set_right(arvore.get_right().get_left())
            arvore.get_right().set_left(put)
        self.remover(self._arvore,arvore.get_titulo(),0)

    def turn_all(self,arvore,valor):
        if valor ==0:
            segundo = No()
            segundo.set_left(arvore.get_left().get_right())
            arvore.get_left().set_right(arvore.get_left().get_right().get_left())
            segundo.set_right(arvore.get_left())
            arvore.set_left(segundo.get_left())
            segundo.get_left().set_left(segundo.get_right())
            segundo = None
            self.turn_right(arvore)
        else:
            segundo = No()
            segundo.set_right(arvore.get_right().get_left())
            arvore.get_right().set_left(arvore.get_right().get_left().get_right())
            segundo.set_left(arvore.get_right())
            arvore.set_right(segundo.get_right())
            segundo.get_right().set_right(segundo.get_left())
            segundo = None
            self.turn_left(arvore)