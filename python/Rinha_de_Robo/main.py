from robo import Robo
from robo_medico import RoboMedico
from robo_lutador import RoboLutador
from random import uniform,randint

lRobo = [Robo("Alfredo"), Robo("Arnaldo")]
lMedico = [RoboMedico("Paloma"), RoboMedico("Paula"), RoboMedico("Gabriel")]
lLutador = [RoboLutador("Cleithon"), RoboLutador("Silvestre"), RoboLutador("Rosa")]

print(lRobo)
print(lMedico)
print(lLutador)

print('\n')

R1 = lRobo[1] + lMedico[0]
print(R1)
print(type(R1))
print(R1.precisa_de_medico())

R2 = lLutador[1] + lMedico[2]
print(R2)
print(type(R2))

R3 = R1 + R2
print(R3)
print(type(R3))

print('\n')

print(lRobo[0])
print(lMedico[2])
lMedico[2].curar(lRobo[0])
print(lRobo[0])

print("\nLutadores...")
print(lLutador[1])
print(lLutador[2])


while(lLutador[2].vida > 0 and lLutador[1].vida > 0):

    print("\nLutadores...")
    print(lLutador[1])
    print(lLutador[2])

    if((lLutador[1].vida <= 0.1) and (randint(0,1) == 0)):
       print(lMedico[0])
       lMedico[0].curar(lLutador[1])
    
    if((lLutador[2].vida <= 0.1) and (randint(0,1) == 0)):
       print(lMedico[2])
       lMedico[2].curar(lLutador[2])

    lLutador[2].atacar(lLutador[1])
    
    print("\nLutadores...")
    print(lLutador[1])
    print(lLutador[2])
   





