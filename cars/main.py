from car import Car
from db import CarDB

# define some variables

def main():
    ford = Car({'name': "mustang"})
    ford.addFuel(0.5)
    ford.start()
    ford.drive(250.0)
    print("ford=" + str(ford))

    nissan = Car({'name':"rouge"})
    nissan.fuel = 0.75

    carDB = CarDB()
    carDB.createCarTable()

    carDB.save(nissan)
    carDB.save(ford)

    for carId in carDB.getCarIds():
        car = Car()
        carDB.loadById(car,carId)
        print(car)

if __name__ == '__main__':
    main()





