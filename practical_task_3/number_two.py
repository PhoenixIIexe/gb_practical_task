def data(data):
    print(f"Имя: {data['name']}, Фамилия: {data['surname']}, Год рождения: {data['year_of_birth']}, Город проживания: {data['city_of_residence']}, email: {data['email']}, Телефон: {data['phone']}.")


datas = {
    'name': 'Саня',
    'surname': 'Ергучев',
    'year_of_birth': 2006,
    'city_of_residence': 'Москва',
    'email': 'sashaerg10.07.6@mail.ru',
    'phone': 89151242885
}

data(datas)