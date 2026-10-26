# Enunciado: pedir 3 notas al usuario, calcular el promedio 
# e informar si el alumno aprobó (promedio mayor o igual a 6). 
 
def calcular(a, b, c): 
    x = (a + b + c) / 3 
    return x 
 
n1 = float(input("Nota 1: ")) 
n2 = float(input("Nota 2: ")) 
n3 = float(input("Nota 3: ")) 
 
p = calcular(n1, n2, n3) 
 
if p >= 6: 
    print("Aprobado") 
else: 
    print("Desaprobado")
