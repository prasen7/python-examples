# program to calulate a car's fuel consumption
# In Europe, amount of fuel consumed per 100 kilometers - liters/100km
# In the USA, number of miles traveled by a car using one gallon of fuel - miles/gallon
# 1 american mile=1609.344 meters
# 1 american gallon=3.785411784 liters

# function to convert liters/100km into miles/gallon
def l100kmtompg(liters):
    miles=100/1.609344
    gallon=liters/3.785411784
    return miles/gallon
# function to convert miles/gallon into liters/100km
def mpgtol100km(miles):
    km=miles*1.609344
    l=3.785411784
    lkm=l/km
    return lkm*100

print("3.9 liters/100km =",l100kmtompg(3.9), "miles/gallon")
print("7.5 liters/100km =",l100kmtompg(7.5), "miles/gallon")
print("10.0 liters/100km =",l100kmtompg(10.), "miles/gallon")
print("60.3 miles/gallon =",mpgtol100km(60.3),"liters/100km")
print("31.4 miles/gallon =",mpgtol100km(31.4),"liters/100km")
print("23.5 miles/gallon =",mpgtol100km(23.5),"liters/100km")
