import random

N=random.randint(500,1000)
m=random.randint(10,50)

#Запись в файл
with open('vectors.csv','w') as f:
    for i in range(N):
        vector = [str(random.uniform(-1, 1)) for j in range(m)]
        f.write(','.join(vector) + '\n')