import re 
with open ('text.txt','r',encoding='Latin-1') as file :
    texto = file.read()


#texto_prueba = input (" Introduce un texto : ") # se crea una variable a la cual se le puede introducir un texto con cualquier valor 

# se crean las variables correspondientes para cada tipo de busqueda y se les asigna el comando para encontar los respectivos tipos de datos 
enteros = r"\b-?\d+\b"
flotantes= r"\b-?\d+\.\d+\b"
booleanos = r"\b(True|False)\b"
strings = r'"(.*?)"'
listasNumericas = r"\[\s*\d+(?:\s*,\s*\d+)*\s*\]"
listasGenerales = r"\[\s*[A-Za-z0-9]+(?:\s*,\s*[A-Za-z0-9]+)*\s*\]"

buscar_enteros = re.findall(enteros,texto) 
buscar_flotantes = re.findall( flotantes,texto)
buscar_booleanos = re.findall( booleanos,texto)
buscar_strings= re.findall( strings,texto)
buscar_listas_num = re.findall(listasNumericas,texto)
buscar_listas_gen = re.findall(listasGenerales, texto)
# se imprimen  los resultados de cada busqueda y tambien se imprime la cantidad total de elmentos encontrados para cada tipo de dato
print(" LOS RESULTADOS SON :")
print("se encontraron los enteros   :",buscar_enteros,"    una cantidad total de :", len(buscar_enteros),  " numeros enteros en el texto ")
print("se encontraron los flotantes :",buscar_flotantes,"  una cantidad total de :", len(buscar_flotantes)," numeros flotantes en el texto")
print("se encontraron los booleanos :",buscar_booleanos,"  una cantidad total de :", len(buscar_booleanos)," valores booleanos en el texto")
print("se encontraron los strings   :",buscar_strings,"    una cantidad total de :", len(buscar_strings),  " strings en el texto")
print("se encontraron las listas    :",buscar_listas_num," una cantidad total de :", len(buscar_listas_num),"listas en el texto")
print("se encontraron las listas    :",buscar_listas_gen," una cantidad total de :", len(buscar_listas_gen),"listas en el texto")