class Car:
 color = None
 model = None

 def cardetails(self):
  print("car details are ",self.color,self.model)

car_color = input("enter car color \n")
car_model = input("enter car model \n")

car_obj_ref = Car()
car_obj_ref.color = car_color
car_obj_ref.model = car_model

print(car_obj_ref.color)
print(car_obj_ref.model)
car_obj_ref.cardetails()