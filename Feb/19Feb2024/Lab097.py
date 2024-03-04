# Automation Tester Blueprint (Py System
# Class -Students,Courses, Payments - Razorpay, Stipe, Instamojo
# Object
# Student (A/B) - > Vivek, Shreeram, Vani
# Course (A/B) -> PyAtb, MTB, ATBJ, APIAT
# Payments (A/B) - Razorpay, Stipe, Instamojo

class Student:
    name = None
    phone_no = None
    roll_no = None

    def live_classes(self):
         print("Yes", self.name, "can watch live classes")

    def watch_recordings(self):
         print("Yes", self.name, "can watch recordings")

    def assignments(self):
         print("Yes", self.name, "can do assignments")

obj_shreeram = Student()
obj_shreeram.name = "shreeram"
print("Name:", obj_shreeram.name)

obj_shreeram = Student()
obj_shreeram.phone_no = "9862531712"
print("Phone_no:", obj_shreeram.phone_no)

obj_shreeram = Student()
obj_shreeram.roll_no = "1234"
print("Roll_no:",obj_shreeram.roll_no)

obj_shreeram.live_classes()
obj_shreeram.watch_recordings()
obj_shreeram.assignments()

obj_vivek = Student()
obj_vivek.name = "vivek"
print(obj_vivek.name)

obj_vivek = Student()
obj_vivek.phone_no = "8962531752"
print(obj_vivek.phone_no)

obj_vivek = Student()
obj_vivek.roll_no = "1235"
print(obj_vivek.roll_no)

obj_vani = Student()
obj_vani.name = "vani"
print(obj_vani.name)

obj_vani = Student()
obj_vani.phone_no = "7762531752"
print(obj_vani.phone_no)

obj_vani = Student()
obj_vani.roll_no = "1236"
print(obj_vani.roll_no)

class Courses:

    name = None

    def pyatb_classes(self):
        print(self.name, "can attend python classes")
    def pyatb_recordings(self):
        print(self.name, "can watch python classes")

obj_pyatb = Courses()
obj_pyatb.name = "shreeram"
print(obj_pyatb.name)
obj_pyatb.pyatb_classes()
obj_pyatb.pyatb_recordings()