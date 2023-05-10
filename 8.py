personas=int(input("personas:"))
pizzas=int(input("pizzas:"))

porciones=0
sobras=0

porciones = personas
porciones_divididas= porciones%2
if porciones_divididas != 0:
    sobras = sobras +1

r_porciones=porciones*pizzas
r_porciones=r_porciones/personas
r_sobras=sobras*pizzas

print(r_porciones,r_sobras)