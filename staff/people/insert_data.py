import sqlite3

from faker import Faker
import random

faker = Faker(locale='ru_RU')


def conn(creator):
    connect = sqlite3.connect('../db.sqlite3')
    cursor = connect.cursor()
    cursor.execute(creator)
    connect.commit()
    cursor.close()


def add_user(name, position, date_employment, salary):
    try:
        creator = f"INSERT INTO people_person(name, position, date_employment, salary, image) " \
                  f"VALUES ('{name}', '{position}', '{date_employment}', '{salary}', 'photo');"
        conn(creator)
    except Exception as err:
        print( err)


def director():
    name = faker.name()
    date_employment = faker.date()
    salary = faker.random_int(100500, 400000000)
    position = 'Директор'
    add_user(name, position, date_employment, salary)


def managers(deps):
    for i in range(len(dep)):
        name = faker.name()
        date_employment = faker.date()
        salary = faker.random_int(200000, 400000)
        position = f'Начальник отдела "{deps[i]}"'
        add_user(name, position, date_employment, salary)
    print('managers done')


def department(deps, quantity_man):
    for i in range(quantity_man):
        name = faker.name()
        date_employment = faker.date()
        salary = faker.random_int(70000, 400000)
        position = f'{faker.job()} отдела "{random.choice(deps)}"'
        add_user(name, position, date_employment, salary)
    print('Done')


dep = ['Контроля качества', 'Маркетинга', 'Разработки',
       'Быта', 'Бугалтерии', 'Контороля рынка']

#director()
#managers(dep)
department(dep, 24)