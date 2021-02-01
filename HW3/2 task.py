def person(first_name, surname, year, city, email, phone_num):
    print(first_name, surname, year, city, email, phone_num)


person(first_name=input('Имя: '),
       surname=input('Фамилия: '),
       year=input('Год рождения: '),
       city=input('Город проживания: '),
       email=input('email: '),
       phone_num=input('Номер телефона: '))
