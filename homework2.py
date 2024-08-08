def information_card(data):
    for key, volues in data.items():
        if key == 'Name':
            name = volues  # обьявление переменной {name}
            print(f"{key}: {name}")
        elif key == 'Age':
            age = volues   # обьявление переменной {age}
            print(f"{key}: {age}")
        elif key == 'New Age':
            new_age = int(volues) + 1 # в сумме + 1 год = New Age 
            print(f"{key}: {new_age}")
        else:
            is_student = volues # обьявление переменной {is_student} 
            print(f"{key}: {is_student}")

data_card_01 =  { # данные Максим
    'Name': 'Максим',
    'Age': '46',
    'New Age': '46',
    'Is Student': 'Fals'
}
data_card_02 =  { # данные Софья
    'Name': 'Софья',
    'Age': '16',
    'New Age': '16',
    'Is Student': 'True'
}
data_card_03 =  { # данные Саша
    'Name': 'Саша',
    'Age': '26',
    'New Age': '26',
    'Is Student': 'True'
}

for i in range(1, 4):
    if i == 1:
        information_card(data_card_01)
    elif i == 2:    
        information_card(data_card_02)
    elif i == 3:    
        information_card(data_card_03)
    else:
        print(f'Ошибка: {i}')


