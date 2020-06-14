
## Tuples
    # a Tuple is a list that you can't change its elements
    # it mostly is used as coordinates, or color pallets
position = (10, 20)
print(position[0], position[1])
for coordinate in position:
    print(coordinate)
position = list(position) # converted to a list
position[0] = 20
position[1] = 400
position = tuple(position)
print(position)
position = (10, 20)
print(position)

'''
Try It Yourself
4-13. Buffet: A buffet-style restaurant offers only five basic foods. Think of five
simple foods, and store them in a tuple.
-Use a for loop to print each food the restaurant offers.
-Try to modify one of the items, and make sure that Python rejects the
change.
-The restaurant changes its menu, replacing two of the items with different
foods. Add a block of code that rewrites the tuple, and then use a for
loop to print each of the items on the revised menu.
'''

## Style :
# Look through the original PEP 8 style guide at https://python.org/dev/peps/pep-0008/

## If Statements ( I kind of miss the switches in C#)
'''
Programming often involves examining
a set of conditions and deciding which
action to take based on those conditions.
'''

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())

    else:
        print(car.title())

