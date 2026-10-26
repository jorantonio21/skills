# Errores comunes en Python de primer año 
 
## 1. No convertir lo que devuelve input() 
input() siempre devuelve un texto (str). 
Pista para el alumno: ¿de qué tipo es lo que devuelve input()? 
 
## 2. print en lugar de return 
Una función que hace print no devuelve nada: quien la llama recibe None. 
 
## 3. Condiciones redundantes 
if aprobado == True:  ->  alcanza con: if aprobado: 