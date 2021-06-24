from ..car import Car

class  Uber_X(Car):
	brand = str
	model = str

	def __init__(self, license, driver, brand , model) -> None:
		super().__init__(license, driver)
		self.model = model
		self.brand = brand