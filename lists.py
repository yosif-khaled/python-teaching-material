############## Lists ##############
'''
What Is a List?
A list is a collection of items in a particular order. You can make a list that
includes the letters of the alphabet, the digits from 0-9, or the names of
all the people in your family. You can put anything you want into a list, and
38 Chapter 3
the items in your list do not have to be related in any particular way. Because
a list usually contains more than one element, it is a good idea to make the
name of your list plural, such as letters, digits, or names.
In Python, square brackets ([]) indicate a list, and individual elements
in the list are separated by commas.
'''

bicycles = ["treck", "cannondale", "redline", "specialized"]

print(bicycles)

print(bicycles[0])

for i in range(len(bicycles)- 1):
    print(bicycles[i])

print(bicycles[0].title())

# Index Positions Start at 0, Not 1

print(bicycles[-1])

message = "My first bicycle was a " + bicycles[-1] + "."

print(message)

#Most lists you create will be dynamic, meaning you will build a list and
#then add and remove elements from it as your program runs its course.

motorcycles = ["Honda", "Yamaha", "Suzuki"]

print(motorcycles)

motorcycles[0] = "Ducati"

print(motorcycles)

motorcycles.append("Hondaa")

print(motorcycles)

motorcycles = []

motorcycles.append("Yamaha")
motorcycles.append("Suzuki")
motorcycles.append("Honda")

print(motorcycles)

#You can add a new element at any position in your list by using the insert()
#method. You do this by specifying the index of the new element and the
#value of the new item.

motorcycles.insert(1, "Ducati")

print(motorcycles)

#You can remove an item according to its position in the list or according to its value.
#Using del statement, pop(), remove()

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]

print(motorcycles)

del motorcycles[2]

print(motorcycles, "third element removed")

#The pop() method removes the last item in a list, but it lets you work
#with that item after removing it.

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

# the popped element is the last element in the list

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned + ".")

last_owned = motorcycles.pop()
print("The last motorcycle I owned was a " + last_owned + ".")

#You can actually use pop() to remove an item in a list at any position by
#including the index of the item you want to remove in parentheses.

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]

print(motorcycles)

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned + ".")

first_owned = motorcycles.pop(0)
print("The first motorcycle I owned was a " + first_owned + ".")

# when the element is popped it is removed from the current list
# it is useful because the removed element is assigned to a variable
# so it can be used to populate another list

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]
owned_motorcycles = []

## is there an inverse loop
for i in range((len(motorcycles)-1), -1, -1):
    owned = motorcycles.pop(i)
    owned_motorcycles.append(owned)
    print(owned_motorcycles)

#If you only know the value of the item you want to remove, you
#can use the remove() method.

motorcycles = ["Honda", "Yamaha", "Yamaha", "Ducati"]

too_expensive = "Ducati"
motorcycles.remove(too_expensive)

print(motorcycles)

motorcycles.remove("Yamaha")

print(motorcycles)

for motorcycle in motorcycles:
    motorcycles[i].lower()

print(motorcycles)

'''
The following exercises are a bit more complex than those in Chapter 2, but
they give you an opportunity to use lists in all of the ways described.

3-4. Guest List: If you could invite anyone, living or deceased, to dinner, who
would you invite? Make a list that includes at least three people you would like to
invite to dinner. Then use your list to print a message to each person, inviting
them to dinner.

3-5. Changing Guest List: You just heard that one of your guests can not make the
dinner, so you need to send out a new set of invitations. You will have to think of
someone else to invite.
-Start with your program from Exercise 3-4. Add a print statement at the
end of your program stating the name of the guest who can not make it.
-Modify your list, replacing the name of the guest who can not make it with
the name of the new person you are inviting.
-Print a second set of invitation messages, one for each person who is still
in your list.

3-6. More Guests: You just found a bigger dinner table, so now more space is
available. Think of three more guests to invite to dinner.
-Start with your program from Exercise 3-4 or Exercise 3-5. Add a print
statement to the end of your program informing people that you found a
bigger dinner table.
-Use insert() to add one new guest to the beginning of your list.
-Use insert() to add one new guest to the middle of your list.
-Use append() to add one new guest to the end of your list.
-Print a new set of invitation messages, one for each person in your list.3-7. 
Shrinking Guest List: You just found out that your new dinner table will not
arrive in time for the dinner, and you have space for only two guests.
-Start with your program from Exercise 3-6. Add a new line that prints a
message saying that you can invite only two people for dinner.
-Use pop() to remove guests from your list one at a time until only two
names remain in your list. Each time you pop a name from your list, print
a message to that person letting them know you are sorry you can not invite
them to dinner.
-Print a message to each of the two people still on your list, letting them
know they are still invited.
-Use del to remove the last two names from your list, so you have an empty
list. Print your list to make sure you actually have an empty list at the end
of your program
'''

cars = ["BMW", "Audi", "Subaro", "Toyota"]
print(cars)
cars.sort()
print(cars, "-- sort()")

cars.sort(reverse=True)
print(cars, "-- sort(reverse=True)")

cars = ["BMW", "Audi", "Subaro", "Toyota"]

#The sorted() function lets you display your list
#in a particular order but does not affect the actual order of the list.
# it is different from sort() as sort() perminantly changes the list

print(cars, "-- the original list")

print(sorted(cars), "-- used the sorted(list) function")

print(cars, "-- didn't use it")

# Use the reverse() method to reverse the original order of a list.

cars.reverse()
print(cars)

print(len(cars))

'''
3-8. Seeing the World: Think of at least five places in the world you would like to
visit.
-Store the locations in a list. Make sure the list is not in alphabetical order.
-Print your list in its original order. Do not worry about printing the list neatly,
just print it as a raw Python list.
-Use sorted() to print your list in alphabetical order without modifying the
actual list.
-Show that your list is still in its original order by printing it.
-Use sorted() to print your list in reverse alphabetical order without chang-
ing the order of the original list.
-Show that your list is still in its original order by printing it again.
-Use reverse() to change the order of your list. Print the list to show that its
order has changed.
-Use reverse() to change the order of your list again. Print the list to show
it is back to its original order.
-Use sort() to change your list so it is stored in alphabetical order. Print the
list to show that its order has been changed.
-Use sort() to change your list so it is stored in reverse alphabetical order.
Print the list to show that its order has changed.

3-9. Dinner Guests: Working with one of the programs from Exercises 3-4
through 3-7 (page 46), use len() to print a message indicating the number
of people you are inviting to dinner.

3-10. Every Function: Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or any-
thing else you would like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.
'''

## Note
    #If an index error occurs and you can not figure out how to resolve it, try printing your
    #list or just printing the length of your list. Your list might look much different than
    #you thought it did, especially if it has been managed dynamically by your program.
    #Seeing the actual list, or the exact number of items in your list, can help you sort out
    #such logical errors.

