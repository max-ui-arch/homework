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

data_card = [
{ # данные Максим
    'Name': 'Максим',
    'Age': '46',
    'New Age': '46',
    'Is Student': 'Fals'
},
 { # данные Софья
    'Name': 'Софья',
    'Age': '16',
    'New Age': '16',
    'Is Student': 'True'
},
 { # данные Саша
    'Name': 'Саша',
    'Age': '26',
    'New Age': '26',
    'Is Student': 'True'
}]

for i in range(0, len(data_card)):
        information_card(data_card[i])
