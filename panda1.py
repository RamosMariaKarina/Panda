import pandas as karina

df_cars =karina.read_csv('cars.csv')

carsTop=karina.read_csv('cars.csv', nrows = 5)
carsBottom = df_cars.tail(5)

Join=karina.concat([carsTop, carsBottom])

print(Join)