cup_cakes = open('CupcakeInvoices.csv')

for each in cup_cakes:
  print(each)

cup_cakes.seek(0, 0)

for every in cup_cakes:
    every = every.split(',')
    print(every[2])

cup_cakes.seek(0, 0)

invoices = []

for each in cup_cakes:
    each = each.split(',')
    quantity = float(each[3])
    amount = float(each[4])
    total = (quantity * amount)
    new_total = round(total, 2)
    print(new_total)
    invoices.append((quantity * amount))

total = sum(invoices)

new_total = round(total, 2)

print(new_total)

cup_cakes.seek(0, 0)

chocolate = []
vanilla = []
strawberry = []

# for each in cup_cakes:
#     each = each.split(',')
#     if (each[2] == 'Chocolate'):
#         chocolate.append(float(each[3]) * float(each[4]))
#     elif (each[2] == 'Vanilla'):
#         vanilla.append(float(each[3]) * float(each[4]))
#     elif (each[2] == 'Strawberry'):
#         strawberry.append(float(each[3]) * float(each[4]))

# print(sum(chocolate))
# print(sum(vanilla))
# print(sum(strawberry))

#finds totals of price for each flavor ^^

import matplotlib.pyplot as plt
x = ['Chocolate', 'Vanilla', 'Strawberry']
y = [267.1, 388.6, 159.69]
plt.bar(x, y) 
plt.xlabel('flavors')
plt.ylabel('Income')


plt.title('My Cupcake Sales')
plt.show() 

#makes bar graph for cup cake flavor prices

