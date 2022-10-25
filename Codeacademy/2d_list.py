# Your code below: 
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
preferred_size = ["Small", "Large", "Medium"]
preferred_size.append("Medium")
print(preferred_size)
customer_data =[]
x = 0
while x <= 3:
  customer_data.append([first_names[x], preferred_size[x], x%2==0])  #appends a 2D list!!!!!!!!!!!!
  x += 1
print(customer_data)