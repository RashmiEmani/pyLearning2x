class XYZ:

    def f1(self):
        try:
            a = int(input("Enter the number \n"))
        except Exception as e:
            print("Enter integer value only!")
        else:
            print(a)
        finally:
            print("Anyhow i will be printed")

x = XYZ()
x.f1()