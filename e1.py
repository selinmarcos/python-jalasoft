#password = ""  chars > 8 and chars <= 16
              # at least one capital letter (ASDDFG)
              # At least one number (0 - 9)
              # at least one lower letter
import random
import string

#usamos la libreria random para generar numeros aleatorios le estamos -2 para añadir las 2 letras


pass_name = []
def generate_passoword():
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
    return password

def name_pass_saver(n):
    
    new_pass = generate_passoword()
    pass_name_dic = {"app_name":n, "app_pass":new_pass}
    pass_name.append(pass_name_dic)
    print('SUCCESFUL !')

def get_app_pass(n):
    return next(x for x in pass_name if x["app_name"] == n)

while True:
    user_input = input("Choose an option: \n 1. Generate Password \n 2. Get Password \n 3. Exit \n")
    # print(user_input)
    if user_input == '1':
        new_password = input("Type an App Name:")
        name_pass_saver(new_password)


    elif user_input == '2':
        # print(password)
        app_to_get = input("Type the App Name that you want to get te password:")
        print('Your App Name & Password are: \n'+ str(get_app_pass(app_to_get)))
        # NOTA: Como obtener el Key y Value de un Diccionario ? (No funciona hacerlo como en JS :-( ) 

        # print('Your App Name & Password are: '+ app_pwd.app_name + '\n' + app_pwd.app_pass)

    elif user_input == '3':
        break    
