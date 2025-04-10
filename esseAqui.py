import random
import time

numDan = input("Oii, Dan. Escolhe um número. PS: nem pensa em olhar o código antes!!!!\n")
sorteado = random.randint(0, 9)
if(numDan == sorteado):
    print("Congratalutionnnn!! Desbloqeou a Mileninha te mandando estudar !!")
    time.sleep(5)
    while(True):
        print("Vai estudar!!  S2")
else:
    print("Tenta de novo amanhã e sem olhar o código hein")
