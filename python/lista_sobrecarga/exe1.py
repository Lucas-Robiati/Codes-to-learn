class Fracao():
    def __init__(self, numerador, denominador):
        if denominador == 0:
            raise ValueError("Denominador inválido!")
        self._numerador = numerador
        self._denominador = denominador
    
    @property
    def numerador(self):
        return self._numerador
    
    @property
    def denominador(self):
        return self._denominador
 
    def MDC(self, a:int, b:int):
        while b != 0:
            r = a%b
            a = b
            b = r
        return a

    def simplifica(self, num, den):
        mdc = self.MDC(num, den) 
        num = num//mdc
        den = den//mdc
        return Fracao(num, den)

    
    def __add__(self, outro:'Fracao'):
        numerador = (self._denominador * outro.numerador) + (outro.denominador * self._numerador)
        denominador = self._denominador * outro.denominador
        return self.simplifica(numerador, denominador)
    
    def __sub__(self, outro:'Fracao'):
        numerador = (outro.denominador * self._numerador) - (self._denominador * outro.numerador)
        denominador = self._denominador * outro.denominador
        return self.simplifica(numerador, denominador)

    
    def __mul__(self, outro: 'Fracao'):
        numerador = self._numerador * outro.numerador
        denominador = self._denominador * outro.denominador
        return self.simplifica(numerador, denominador)
    
    def __truediv__(self, outro:'Fracao'):
        numerador = self._numerador * outro.denominador
        denominador = self._denominador * outro.numerador
        return self.simplifica(numerador, denominador)

    def __repr__(self):
        return str(self._numerador) + '/' + str(self._denominador)

f1 = Fracao(1,2)
f2 = Fracao(2,4)
m = f1 * f2
a = f1 + f2
s = f1 - f2
d = f1/f2

print(a)
print(s)
print(m)
print(d)

ft = Fracao(1,0)
