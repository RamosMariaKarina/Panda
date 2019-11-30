import pandas as karina

cars = karina.read_csv('cars.csv')

df_cars =karina.read_csv('cars.csv', nrows= 5).iloc[:,0::2]

print ("Answers to Letter A")
print(df_cars)

df_MazdaRX4_cars = cars[cars['Model']=='Mazda RX4']
print ("Answers to Letter B")
print (df_MazdaRX4_cars)

df_cyl_cars = cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
print ("Answers to Letter C")
print (df_cyl_cars)

df_cyl_gear_car1 = df_cyl_cars = cars.loc[cars['Model'] == 'Mazda RX4 Wag', ['Model', 'cyl', 'gear']]
df_cyl_gear_car2 = df_cyl_cars = cars.loc[cars['Model'] == 'Ford Pantera L', ['Model', 'cyl', 'gear']]
df_cyl_gear_car3 = df_cyl_cars = cars.loc[cars['Model'] == 'Honda Civic', ['Model', 'cyl', 'gear']]

Join=karina.concat([df_cyl_gear_car1, df_cyl_gear_car2])
Final= karina.concat([Join, df_cyl_gear_car3])

print ("Answers to D")
print (Final)