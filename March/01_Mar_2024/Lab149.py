import csv

test_data =[
    ['Name', 'Age', 'City'],
    ['Rashmi','32', 'Hyd']
 ]
try:
      with open("testdata.csv", 'w') as file:
       writer = csv.writer(file)
       for data in test_data:
        writer.writerow(data)
except FileNotFoundError as f:
    print(f)
finally:
    print("CLose your Files!")
    # close the file code