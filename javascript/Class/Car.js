function Car( license , drive ) {
	this.id
	this.license = license
	this.driver = drive
	this.passanger
}

Car.prototype.printDataCar = function () {
	console.log( this.driver.name,' ', this.license )
}
