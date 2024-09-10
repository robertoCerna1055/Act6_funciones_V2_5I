print("Mas sobre funciones")
print("")

# Aqui se escriben las funciones

def suma_ab(a,b):
    s = a + b
    return s

def resta_ab(a,b):
    s = a - b
    return s

def multiplicacion_ab(a,b):
    s = a * b
    return s

def division_ab(a,b):
    s = a / b
    return s
    
    
# Llamadas a funciones

print("Calculando suma")
n1 = int(input("Ingresa el primer numero"))
n2 = int(input("Ingresa el segundo numero"))
suma = suma_ab(n1,n2)
print(f"La suma de {n1} + {n2} es: {suma}")

print("")
print("Calculando resta")
n11 = int(input("Ingresa el primer numero"))
n22 = int(input("Ingresa el segundo numero"))
resta = resta_ab(n11,n22)
print(f"La resta de {n11} - {n22} es: {resta}")

print("")
print("Calculando multiplicacion")
n111 = int(input("Ingresa el primer numero"))
n222 = int(input("Ingresa el segundo numero"))
multiplicacion = multiplicacion_ab(n111,n222)
print(f"La multiplicacion de {n111} * {n222} es: {multiplicacion}")

print("")
print("Calculando division")
n1111 = int(input("Ingresa el primer numero"))
n2222 = int(input("Ingresa el segundo numero"))
division = division_ab(n1111,n2222)
print(f"La division de {n1111} / {n2222} es: {division}")