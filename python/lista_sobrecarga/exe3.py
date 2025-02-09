class Relogio:
    def __init__(self, hora:int, minuto:int, segundo:int):
        if (hora <= 23 and hora >= 0) and (minuto <= 59 and minuto >= 0) and (segundo <= 59 and segundo >= 0):
            self._hh = hora
            self._mm = minuto
            self._ss = segundo
        else:
            print("Horário inválido! Por favor, faça uma nova tentativa com valores válidos.")

    @property
    def hh(self):
        return self._hh
    
    @property
    def mm(self):
        return self._mm
    
    @property
    def ss(self):
        return self._ss

    def __add__(self, outro:'Relogio'):
        novo_s = self._ss + outro.ss
        novo_m = self._mm + outro.mm
        novo_h = self._hh + outro.hh
        
        while (novo_s >= 60):
            novo_s -= 60
            novo_m += 1
        
        while (novo_m >= 60):
            novo_m -= 60
            novo_h += 1

        if(novo_h >= 24):
            novo_h -= 24

        return Relogio(novo_h,novo_m,novo_s)

    def __sub__(self, outro:'Relogio'):
        
        if(self._hh < outro.hh):
            print("O primeiro horário deve ser maior que o segundo")
            return None
        
        novo_s = self._ss - outro.ss
        novo_m = self._mm - outro.mm
        novo_h = self._hh - outro.hh
        
        while (novo_s <= 0):
            novo_s += 60
            novo_m -= 1
        
        while (novo_m <= 0):
            novo_m += 60
            novo_h -= 1

        if(novo_h <= 0):
            novo_h += 24
        
        return Relogio(novo_h,novo_m,novo_s)

    def __eq__(self, outro:'Relogio'):
        
        if self._hh == outro.hh and self._mm == outro.mm and self._ss == outro.ss:
            print(True)
        else:
            print(False)
    
    def __gt__(self, outro:'Relogio'):
        
        if(self._hh != outro.hh):
            if(self._hh > outro.hh):
                print(True)
            else:
                print(False)
        else:
            if (self._mm != outro.mm):
                if (self._mm > outro.mm):
                    print(True)
                else:
                    print(False)
            else:
                if (self._ss > outro.ss):
                    print(True)
                else:
                    print(False)
    
    def __lt__(self, outro:'Relogio'):
        
        if(self._hh != outro.hh):
            if(self._hh < outro.hh):
                print(True)
            else:
                print(False)
        else:
            if (self._mm != outro.mm):
                if (self._mm < outro.mm):
                    print(True)
                else:
                    print(False)
            else:
                if (self._ss < outro.ss):
                    print(True)
                else:
                    print(False)


    def __repr__(self):
        return f'{self._hh:02}:{self._mm:02}:{self._ss:02}'

r0 = Relogio(16,61,54)
r1 = Relogio(18,37,32)
r2 = Relogio(20,0,30)

print(r1)
print(r2)
r3 = r1 + r2
print(r3)
r4 = r3 - r2
print(r4)
r4 = r2 - r3
print(r4)
r1 == r2
r1 == Relogio(18,37,32)
r3 > r3
r3 > r2
r2 > r3
r1 < r2
