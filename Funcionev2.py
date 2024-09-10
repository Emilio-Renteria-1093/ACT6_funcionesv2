print("\n")
print("mas sobre funciones")
print("--------------------")
# Aqui se escriben las funciones
def suma_ab(a,b):
    s=a+b
    return s
def resta_cd(c,d):
    res=c-d
    return res
def multiplicacion_ef(e,f):
    mul=e*f
    return mul
def divicion_gh(g,h):
    div=g/h
    return div

#llamar a las funciones
n1=int(input("Ingresa el primer numero : "))
n2=int(input("ingresa el segundo numero : "))

#aqui le asigo los valores ingresados de los ususarios para ingresarlos en las funciones
suma=suma_ab(n1,n2)
resta=resta_cd(n1,n2)
multiplicacion=multiplicacion_ef(n1,n2)
divicion=divicion_gh(n1,n2)

#Aqui es donde se muestra los resultados 
print("calculando suma")
print(f"la suma de {n1} + {n2} es : {suma}")
print("\n")
print("--------------------")

print("calculando resta")
print(f"la suma de {n1} - {n2} es : {resta}")
print("\n")
print("--------------------")

print("calculando multiplicacion")
print(f"la suma de {n1} * {n2} es : {multiplicacion}")
print("\n")
print("--------------------")

print("calculando divicion")
print(f"la suma de {n1} / {n2} es : {divicion}")
print("\n")
print("--------------------")