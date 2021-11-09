from operator import attrgetter

class Drink:
    def __init__(self, name, price, percent, capacity):
        self.name = name
        self.price = price
        self.percent = percent
        self.capacity = capacity
        self.percent2price = percent / capacity

def alcoholCount(percentOne, percentTwo, alcohol1, alcohol2):
    alco1 = 0
    alco2 = 0
    if percentOne != 0:
        alco1 = alcohol1 * percentOne/ 100
    if percentTwo != 0:
        alco2 = alcohol2 * percentTwo/ 100
    if alco1 + alco2 == 0:
        return 0
    else:
        return (alco1 + alco2) / (alcohol1 + alcohol2) * 100

def makeDrink(drinkOne, drinkTwo):
    name = "{} with {}".format(drinkOne.name, drinkTwo.name)
    price = drinkOne.price + drinkTwo.price
    percent = alcoholCount(drinkOne.percent, drinkTwo.percent, drinkOne.capacity, drinkTwo.capacity)
    capacity = drinkOne.capacity + drinkTwo.capacity
    newDrink = Drink(name, price, percent, capacity)
    return newDrink

def returnString(drink):
    name = drink.name
    price = drink.price
    percent = drink.percent
    capacity = drink.capacity
    stringOfDrink = '{} kosztuje {} zl, ma {} procent, i {} ml pojemnosci.\n'

    return stringOfDrink.format(name, price, percent, capacity)

vodka = Drink("Vodka", 8, 40, 50)
rum = Drink("Rum", 9, 60, 50)
coke = Drink("Coke", 2, 0, 100)
ice = Drink("Ice", 0, 0, 30)
whisky = Drink("Whisky", 12, 45, 50)

vodkaWithIce = makeDrink(vodka, ice)
vodkaWithCoke = makeDrink(vodka, coke)
rumWithIce = makeDrink(rum, ice)
cubaLibre = makeDrink(rum, coke)
whiskyWithIce = makeDrink(whisky, ice)
lemmy = makeDrink(whisky, coke)

listOfDrinks = [
    vodkaWithIce,
    vodkaWithCoke,
    rumWithIce,
    cubaLibre,
    whiskyWithIce,
    lemmy
    ]

for el in listOfDrinks:
    print(returnString(el))

listOfDrinks.sort(key=(attrgetter('percent2price')))

print("Best drinks for a party (from the best to worse choice:\n")
for ele in range(len(listOfDrinks)):
    print(listOfDrinks[ele].name)