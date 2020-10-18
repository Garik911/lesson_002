#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Переопределять my_favorite_movies и использовать .split() нельзя.
# Запятая не должна выводиться.

favorite_movies = ''.join(my_favorite_movies)
favorite = favorite_movies[0:10]
favorite2 = favorite_movies[12:25]
favorite3 = favorite_movies[35:40]
favorite4 = favorite_movies[42:56]


print(favorite)
print(favorite4)
print(favorite2)
print(favorite3)
