print("Hola Mundo! Soy Rocher Avll")
print("Hola Mundo! Soy Rocher Avll")
#soy un comentario
print("Hola Mundo! Soy Rocher Avll")

#variable
texto = "Repaso de python con Victor"
nombre = "Rocher"
altura = "185cm"
year = 2024

print(f"{texto} - {nombre} - {str(altura)}")

#entrada
#sitioweb = input ("El sitio web del usuario es: " + sitioweb)

#Condiciones
"""
#altura = 187
altura = int(input("¿Cual es tu altura?:"))

if altura >= 180:
    print ("Eres una persona alta!")
else: 
    print("Eres bajito!")

"""
#Funciones
"""
var_altura = int(input("¿Cual es tu altura?:"))
def mostrAltura(altura):
    resultado = ""


    if altura >= 180:
       resultado = "Eres una persona alta!"
    else: 
       resultado = "Eres bajito!"

    return resultado

print(mostrAltura(var_altura))
"""
#listas
personas = ["Victor", "Paco", "Rocher"]
print(personas[2])

for persona in personas:
    print("-" + persona)