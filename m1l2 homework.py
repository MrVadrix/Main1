import random

online = True
password_safe = {}

online = True
password_safe = {}

while online:
    password_length = int(input("Впишите длинну пароля: "))

    password = []
    password_keys = ["+","-","/","*","&","$","?","=","@","a","b","c","d","e","f"
            "g","h","i","j","k","l","m","n","o","p","q","r","s","t","u"
            "v","w","x","y","z","A","B","C","D","E","F","G","H","I","J"
            "K","L","L","M","N","O","P","Q","R","S","T","U","V","W","X"
            "Y","Z"]

    for i in range(password_length):
        password.append(random.choice(password_keys))

    password_key_name = input("Введите имя пароля (для чего и т.т.): ")
    password_safe[password_key_name] = ''.join(password)
    print(" ")
    print("Ваш пароль:")
    print(password_safe)
    print(" ")
    go_off_q = input("Закончить программу? (д - да): ")
    if go_off_q == "д":
        online = False
    else:
        print("-")
