from classes.car import Car
from classes.account import Account


if __name__ == "__main__":
	car = Car( 'HOla', Account('Duvan', '123311') )
	print(vars(car))
	print(vars(car.driver))