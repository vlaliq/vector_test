import math
import matplotlib.pyplot as plt
from Program_1 import N,m

step = 0.1

# Чтение векторов из файла
vectors = []
with open('vectors.csv', 'r') as f:
    for line in f:
        vector = [float(x) for x in line.strip().split(',')]
        vectors.append(vector)


# Вычисление расстояний между парами векторов
distances = []
for i in range(N):
    for j in range(i+1, N):
        distance = math.sqrt(sum([(vectors[i][k] - vectors[j][k])**2 for k in range(m)]))
        distances.append(distance)


# Поиск минимального и максимального расстояний
min_distance = min(distances)
max_distance = max(distances)


# Построение гистограммы распределения расстояний
histogram = [0] * int(2/step)
for distance in distances:
    index = int((distance + 1) / step)
    if index >= len(histogram):
        index = len(histogram) - 1
    histogram[index] += 1


# Вывод результатов
print("Минимальное расстояние: {} (между векторами {} и {})".format(min_distance, distances.index(min_distance)//
                                                                    (N-1), distances.index(min_distance)%(N-1)))
print("Максимальное расстояние: {} (между векторами {} и {})".format(max_distance, distances.index(max_distance)//
                                                                     (N-1), distances.index(max_distance)%(N-1)))

plt.hist(distances, bins=int(2/step))
plt.xlabel('Расстояние')
plt.ylabel('Количество')
plt.title('Распределение расстояний')
plt.show()

