meme_dict = {
    "КРИНЖ": "Что-то очень странное или стыдное",
    "ЛОЛ": "Что-то очень смешное",
    "КРИПОВЫЙ": "страшный, пугающий",
    "АГРИТЬСЯ": "злиться",
    "РОФЛ": "шутка"
}

while True:
    word = input("Введите непонятное слово: ").upper()

    if word in meme_dict.keys():
        if word == "КРИНЖ":
            print(meme_dict[word])
            q = input("Остановить? д/н: ")
        if word == "ЛОЛ":
            print(meme_dict[word])
            q = input("Остановить? д/н: ")
        if word == "РОФЛ":
            print(meme_dict[word])
            q = input("Остановить? д/н: ")
        if word == "КРИПОВЫЙ":
            print(meme_dict[word])
            q = input("Остановить? д/н: ")
        if word == "АГРИТЬСЯ":
            print(meme_dict[word])
            q = input("Остановить? д/н: ")       
        
    elif word not in meme_dict.keys():
        print("НЕВЕРНОК СЛОВО или НЕПРАВИЛЬНО НАПИСАНО")
        q = input("Остановить? д/н: ")
    
    if q == "д":
        print("------")
    if q == "н":
        break

#End
