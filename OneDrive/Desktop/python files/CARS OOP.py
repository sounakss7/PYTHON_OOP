print("This is the petrol car section")
print()
class cars:
  def __init__(self, brand, model, year):
    self.brand = brand
    self.model = model
    self.year = year
  def _showdetails(self):
    print("Brand: ", self.brand)
    print("Model: ", self.model)
    print("Year : ", self.year)  
results = cars("Ford", "Mustang", 2022,)
results._showdetails()
class additional(cars):
  def __init__(self, brand, model, year, color,speed):
    super().__init__(brand, model, year)
    self.color = color
    self.speed = speed

  def _showdetails(self):
    
    print("Color: ", self.color)
    print("the top speed:",self.speed)
    
results=additional("Ford", "Mustang", 2022, "Red","264km/hr")
results._showdetails()
print()
print("This  is the electric cars section")
print()
class electric:
  def __init__(self, brand, model, year, battery,speed):
    self.brand = brand
    self.model = model
    self.year = year
    self.battery = battery
    self.speed=speed
  def _showdetails(self):
    print("Brand: ", self.brand)
    print("model: ", self.model)
    print("year: ", self.year)
    print("battery: ", self.battery)
    print("the top speed :",self.speed)
results = electric("Tesla" ,"Model 3", 2022 ,"100kWh","200km/hr")
results._showdetails()