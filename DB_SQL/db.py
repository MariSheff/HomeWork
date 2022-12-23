
import sqlite3
import pandas as pd

sql = sqlite3.connect('DB_Bulldogs.db')

country = ['Россия', 'Беларуссия']

# создание таблицы Страны
country = pd.DataFrame({
    'title': country
})
country.to_sql('country', sql, index_label="CountryID", if_exists='replace') # Сохраним в базу
# pd.read_sql("SELECT * FROM country", sql) # Проверим, что сохранилось правильно. Чтение таблицы

# создание таблицы Города
countryID = [0, 0, 0, 0, 1]
city = ['Москва', 'Санкт-Петербург', 'Санкт-Петербург', 'Псков', 'Минск']
city = pd.DataFrame({
    'country': countryID,
    'title': city
})
city.to_sql('city', sql, index_label="cityID", if_exists='replace') # Сохраним в базу

# создание таблицы Люди (владельцы, заводчики, эксперты)
name = ['Инга', 'Марина', 'Виктор', 'Юлия', 'Наталия', 'Галина']
surname = ['Правикова', 'Шевченко', 'Астанин', 'Пожидаева', 'Винокурова', 'Стрелкова']
cityID = [0, 1, 1, 2, 4, 4]
breeder = [False, False, False, True, True, False]
expert = [False, False, False, False, False, True]

people = pd.DataFrame({
    'name': name,
    'surname': surname,
    'city': cityID,
    'breeder': breeder,
    'expert': expert

})
people.to_sql('people', sql, index_label="peopleID", if_exists='replace') # Сохраним в базу
# print(pd.read_sql("SELECT * FROM people", sql)) # Проверим, что сохранилось правильно. Чтение таблицы
print(people, end ="\n \n " )


# создание таблицы Собаки
dog_name = ['TRUVOR BULLS ADRENALIN', 'TRUVOR BULLS KOENIGSBERG KAMEE', 'SOVEREIGN KIDDY WIN\'S', 'GLADESTONE CARRIE BRADSHAW']
date_of_birth = ['28.03.2019', '22.08.2020', '05.10.2020', '10.03.2022']
ownerID = [2, 0, 1, 1]
co_ownerID = [1, None, None, 2]
owner_kennelID = [3, 3, 3, 3]
chip = ['000001', '000002', '000003', '000004']
stamp = ['KFL 6647', 'KFL 7242', 'KW 69', 'GDE 40']
pedigree_number = ['RKF 5610409', 'RKF 6012960', 'BCO 149-007770', 'Щ.К.']

dogs = pd.DataFrame({
    'name': dog_name,
    'db': date_of_birth,
    'owner': ownerID,
    'co_owner': co_ownerID,
    'owner_kennel': owner_kennelID,
    'chip': chip,
    'stamp': stamp

})

dogs.to_sql('dogs', sql, index_label="dogsID", if_exists='replace') # Сохраним в базу
print(pd.read_sql("SELECT * FROM dogs", sql))

# создание таблицы Ранг выставки
level_show =['CAC', 'CAC2gr', 'CAC2gr+Specialty', 'Mono CChC', 'Mono CChC in each class', 'CACIB']
level_show = pd.DataFrame({
    'level_title': level_show,
})
level_show.to_sql('level_show', sql, index_label='level_showID', if_exists='replace')

# создание таблицы Список выставок
show = ['NDS Eurasia', 'Монопородная выставка ранга КЧК', 'CAC II группы', 'Memorial Zavodchkova', 'Nevsky Winner - 1', 'Nevsky Winner - 2']
level_show =[0, 3, 1, 0, 0, 0]
cityID = [0, 1, 1, 1, 1, 1]
date_show = ['26.11.2022', '18.06.2022', '19.11.2022', '17.07.2022', '17.07.2022', '18.12.2022']

show = pd.DataFrame({
    'show_title': show,
    'level_show':level_show,
    'city':cityID,
    'date_show':date_show
})

show.to_sql('show', sql, index_label='showID', if_exists='replace')
print(pd.read_sql("SELECT * FROM show", sql))

# создание табл Класс выставки
class_show = ['baby', 'puppy', 'junior', 'intermediate', 'open', 'champion', 'champion NCP']

class_show = pd.DataFrame({
    'class_title': class_show,
})
class_show.to_sql('class_show', sql, index_label='class_showID', if_exists='replace')


# создание табл Оценки
score = ['satisfactory', 'good', 'very good', 'excellent 1', 'excellent 2','excellent 3',
         'not score', 'not present', 'very promissing 1', 'very promissing 2', 'very promissing 3', 'promissing', 'not promissing']

score = pd.DataFrame({
    'score_title': score
})
class_show.to_sql('score', sql, index_label='scoreID', if_exists='replace')


# создание табл Сертификаты
certificate = ['CAC', 'R.CAC', 'JCAC', 'R.JCAC', 'CC', 'JCC', 'CChC', 'CACIB', 'R.CACIB']

certificate = pd.DataFrame({
    'certificate_title': certificate
})
class_show.to_sql('certificate', sql, index_label='certificateID', if_exists='replace')


# создание табл Титулы
title = ['CW', 'BOB', 'BOS', 'BOB Junior', 'Best Male', 'Best Female', 'BOB Puppy', 'BOB Baby' ]
title = pd.DataFrame({
    'title': title
})
class_show.to_sql('title', sql, index_label='titleID', if_exists='replace')


# создание табл Результаты выставки
showID = [1, 1, 1, 1]
expertID = [4, 4, 4, 4]
dogID = [0, 1, 2, 3]
class_showID = [5, 4, 3, 1]
scoreID = [3, 3, 3, 8]
certificateID = [6, 6, 4, None]
# titleID = [[1, 4, 2], [1, 6], [0, 2], [0, 3], None, [0, 3]]
titleID = [1, 2, 0, None]

result_show = pd.DataFrame({
    'showID': showID,
    'expertID': expertID,
    'dogID': dogID,
    'class_showID': class_showID,
    'scoreID': scoreID,
    'certificateID': certificateID,
    'titleID': titleID
})
result_show.to_sql('result_show', sql, index_label='result_showID', if_exists='replace')

showID = [0, 0, 0, 0]
expertID = [5, 5, 5, 5]
dogID = [0, 1, 2, 3]
class_showID = [5, 4, 4, 2]
scoreID = [3, 3, 3, 3]
certificateID = [0, 0, 1, 2]
titleID = [1, 2, 0, 3]

result_show = pd.DataFrame({
    'showID': showID,
    'expertID': expertID,
    'dogID': dogID,
    'class_showID': class_showID,
    'scoreID': scoreID,
    'certificateID': certificateID,
    'titleID': titleID
})
result_show.to_sql('result_show', sql, index_label='result_showID', if_exists='append')

print(pd.read_sql("SELECT * FROM result_show", sql))

showID = [5, 5]
expertID = [5, 5]
dogID = [2, 3]
class_showID = [4, 2]
scoreID = [3, 3]
certificateID = [1, 2]
titleID = [2, 1]
result_show = pd.DataFrame({
    'showID': showID,
    'expertID': expertID,
    'dogID': dogID,
    'class_showID': class_showID,
    'scoreID': scoreID,
    'certificateID': certificateID,
    'titleID': titleID
})
result_show.to_sql('result_show', sql, index_label='result_showID', if_exists='append')

print(pd.read_sql("SELECT * FROM result_show", sql))

# Вывод читабельной таблицы результатов

query = """
SELECT s.show_title, s.date_show, s.city, s.level_show, (p.surname||' '||p.name) as expert, d.name,
s.date_show, s.city, s.level_title
FROM result_show AS res
LEFT JOIN show AS s ON res.showID =  s.showID 
LEFT JOIN people AS p ON  p.peopleID = res.expertID
LEFT JOIN dogs AS d ON  res.dogID = d.dogsID
LEFT JOIN level_show AS level ON  res.dogID = level.level_showID
ORDER BY s.date_show
"""
#   s.date_show, s.city, s.level_show,,
# class.class_title, sert.certificate_title, t.title
# LEFT JOIN class_show AS class ON  class.class_showID = res.class_showID
# LEFT JOIN score AS sc ON  sc.scoreID = res.scoreID
# LEFT JOIN certificate AS sert ON  sert.certificateID = res.certificateID
# LEFT JOIN title AS t ON  t.titleID = res.titleID
# ORDER BY s.date_show, class.class_title


result = pd.read_sql(query, sql)
print(result)
