from collections import OrderedDict

d = OrderedDict()
number_of_items = int(input().strip())
for i in range(number_of_items):
    item, delimeter, price = input().strip().rpartition(" ")
    price = int(price)
    if (item in d):
        previous_total_purchased = d.get(item)
        next_total_purchased = previous_total_purchased + price
        d[item] = next_total_purchased
    else:
        d[item] = price


for item, price in d.items():
    print (f'{item} {price}')
