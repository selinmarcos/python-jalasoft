#password = ""  chars > 8 and chars <= 16
              # at least one capital letter (ASDDFG)
              # At least one number (0 - 9)
              # at least one lower letter
import random
import string
#usamos la libreria random para generar numeros aleatorios le estamos -2 para añadir las 2 letras

chars = random.randint(9, 16) - 2
# print(chars)
listPy = []
n = 0
while n < chars:

    listPy.append(random.randint(0, 9))    
    n = n + 1
#usamos la libreria random y string para generar letras aleatorias
capitalRandomLetter = random.choice(string.ascii_letters).upper()
lowerRandomLetter = random.choice(string.ascii_letters).lower()
listPy.append(capitalRandomLetter + lowerRandomLetter)

#mapeamos listPy para convertir a string
password = ''.join(map(str, listPy))
print(password)