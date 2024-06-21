import pandas as pd

# Прочтем файл .csv с помощью библиотеки pandas
df = pd.read_csv('sample_data/california_housing_train.csv')
# Посмотреть первые 5 строк
df.head(8)
# Посмотреть последние 5 строк
df.tail(15)
# Возвращает размеры таблицы: кортеж из 2 значений, 1 кол-во строк, 2 - кол-во столбцов
df.shape

# DataFrame.isnull() - обнаруживает пустые значения
# DataFrame.sum(axis=None, skipna=None, level=None, numeric_only=None, min_count=0, **kwargs) - возвращает сумму значений по выбраной оси
# Параметры:
# axis: int {index (0), columns (1)} - ось(0 - вертикальная, 1 - горизонтальная)
# По умолчанию 0
# Посмотреть есть ли у нас пустые значения
# В данном случае пустых значений нет
df.isnull().sum()

# Проверить тип данных в столбцах
# В данных случаях везде float, число 64 указывает на разрядность(Используется 64 байта для хранения значения в памяти,
# чем меньше разрядность, тем меньший диапазон могут принимать числа и тем меньше тратится памяти на хранение.
df.dtypes

# Посмотреть все столбцы
# Возвращает список со строками строк - названиями столбцов в таблице
df.columns

# Выбор нескольких столбцов [широта, кол-во жителей]
df[['latitude', 'population']]

# Выбор определенного кол-ва рядов
# Синтаксис df[df[col] !=|==|>|<| значение]
df[df['housing_median_age'] < 8]

# Для отбора можно использовать несколько условий одновременно
# Знак & означает 'and', а знак | 'or'
df[(df['housing_median_age'] > 20) & (df['total_rooms'] > 2000)]

df[df['housing_median_age'] < 10][['total_bedrooms', 'total_rooms']]

df.loc[df['population'] < 100, ['total_bedrooms', 'total_rooms']]

# Создание DataFrame

data = {'A': [1, 2, 3, 4, 5],
        'B': [6, 7, 8, 9, 10]}
df = pd.DataFrame(data, index=['a', 'b', 'c', 'd', 'e'])

# Выбор строки по метке
print(df.loc['b'])

# Выбор столбца по метке
print(df.loc[:, 'A'])

# Выбор определенной ячейки
print(df.loc['c', 'B'])

# Использование среза
print(df.loc['b':'d', 'A'])

# Выбор по условию
print(df.loc[df['A'] > 2])

# Изменение значения
df.loc['c', 'B'] = 100
print(df)

# Максимальное значение
print(df['population'].max())
# Минимальное значение
print(df['population'].min())
# Среднее значение
print(df['population'].mean())
# Сумма
print(df['population'].sum())

# Медианное значение
df[['population', 'total_rooms']].median()

#Получить общую картину можно простой командой describe
df.describe()

# Самостоятельная практика №3
# 1.Определить какое максимальное и минимальное значение median_house_value
# 2.(Доп) Показать максимальное median_house_value, где median_income = 3.1250
# 3.(Доп) Узнать какая максимальная population в зоне минимального значения median_house_value
#1
print(df1['median_house_value'].max(),df1['median_house_value'].min())
[df1['median_house_value'].max(),df1['median_house_value'].min()]
max(df1['median_house_value']) 
min(df1['median_house_value']) 
df1['median_house_value'].agg(['min', 'max']) #функция агрегатор

#2
df1[df['median_income']==3.1250][['median_house_value']].max()

#3
df1[df1.median_house_value == df1.median_house_value.min()][['population']].max()

#DZ
# Дан файл california_housing_train.csv. Определить среднюю стоимость дома , где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
# Используйте модуль pandas.
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
avg = df[(df['population'] > 0) & (df['population'] < 500)]['median_house_value'].mean()  # Средняя стоимость дома, где количество людей от 0 до 500

# Дан файл california_housing_train.csv.
# Найти максимальное значение переменной "households" в зоне минимального значения переменной min_population и сохраните это значение в переменную max_households_in_min_population.
# Используйте модуль pandas.
import pandas as pd

df = pd.read_csv('california_housing_train.csv')
# Найти минимальное значение 'population'
min_population = df['population'].min()

# Отфильтровать строки с минимальным значением 'population' и найти максимальное значение 'households'
max_households_in_min_population = df[df['population'] == min_population]['households'].max()


# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

# import random
# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
#lambda x: x[0] * x[1] if x[0] != x[1] else 0
#Вызываемый объект, который возвращает логическую серию
#df.loc[lambda df: df['shield'] == 8]
#data.loc[lambda data: 
data['robot']=0
data['human']=0
data.loc[data['whoAmI'] == 'robot','robot'] = 1
data.loc[data['whoAmI'] == 'human', 'human'] = 1
data
#pd.get_dummies(data['whoAmI'])
# data['tmp'] = 1
# data.set_index([data.index, 'whoAmI'], inplace=True)
# data = data.unstack(level=-1, fill_value = 0).astype(int)
# data.columns = data.columns.droplevel()
# data.columns.name = None
# data