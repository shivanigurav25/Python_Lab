#Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 
#Input:
#temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])




import numpy as np

# Given temperature data
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])

#Identify hot days (temperatures > 35)
hot_day_indices = np.where(temperatures > 35)


#Identify hot days (temperatures < 5)
cold_day_indices = np.where(temperatures < 5)

#Print the result
print ("Hot Days:")
print ("Day\tTemperature (in degree celcius)")
for index in hot_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")


print ("Cold Days:")
print ("Day\tTemperature (in degree celcius)")
for index in cold_day_indices[0]:
    print(f"{index+1}\t{temperatures[index]:.1f}")



#Output
#Hot Days:
#Day	Temperature (in degree celcius)
#3	36.8
#6	38.7
#10	37.2
#Cold Days:
#Day	Temperature (in degree celcius)
#11	4.0
#14	-4.0
#15	-12.0
