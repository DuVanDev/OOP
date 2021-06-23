from classes.car import Car

if __name__ == "__main__":
	car = Car()
	car.license = 'AMS234'
	car.driver = 'Juan H'
	print(vars(car))

	car2 = Car()
	car2.license = 'AAAA'
	car2.driver = 'Miguel'
	print(vars(car2))
