try:
     with open("TestData.txt", 'r') as file: # with is used to wrap the content
       content = file.read()
       print(content)
except FileNotFoundError as fnfr:
       print(fnfr)
finally:
       file.close()