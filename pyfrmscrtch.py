############## Course Material 4 Youtube Channel ##############

############## Bare Basics ##############

print("Hello World!")

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

print("Hello, " + full_name.title() + "!")

message  = "Hello, " + full_name.title() + "!"

print(message)

print("python is awesome!!")

print(">>>\n\tpython is awesome!!")

print("Languages:\n\tPython\nC#\nJava")

print("What is your favorite language?!")

message = " python 3 "

print(message.strip())

# strip(), rstrip(), lstrip()

##2-5. Famous Quote:
#Find a quote from a famous person you admire. Print the
#quote and the name of its author. Your output should look something like the
#following, including the quotation marks:
# albert Einstein once said, A person who never made a mistake never tried anything new.

message = 0.3 + 0.1

print(message)

age = 23

message = "Happy " + str(age) + " Birthday"

print(message)

'''
The main reason to write comments is to explain what your code is supposed
to do and how you are making it work. When you are in the middle of
working on a project, you understand how all of the pieces fit together. But
when you return to a project after some time away, you will likely have forgotten
some of the details. You can always study your code for a while and figure
out how segments were supposed to work, but writing good comments
can save you time by summarizing your overall approach in clear English.
34 Chapter 2
If you want to become a professional programmer or collaborate with
other programmers, you should write meaningful comments. Today, most
software is written collaboratively, whether by a group of employees at one
company or a group of people working together on an open source project.
Skilled programmers expect to see comments in code, so it is best to start
adding descriptive comments to your programs now. Writing clear, concise
comments in your code is one of the most beneficial habits you can form as
a new programmer.
When you are determining whether to write a comment, ask yourself if
you had to consider several approaches before coming up with a reasonable
way to make something work; if so, write a comment about your solution.
It is much easier to delete extra comments later on than it is to go back
and write comments for a sparsely commented program.
'''

# type import this in your python IDE


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

############## Working with Lists (Loops) ##############

    #Looping allows you to take the same action, or set of actions,
    #with every item in a list.

magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician) # Notice Indentation

## keep in mind:
    #the set of steps is repeated once for each item in the list,
    #no matter how many items are in the list.
    #when writing your own for loops that you can choose
    #any name you want for the temporary variable that holds each value in the
    #list. However, it is helpful to choose a meaningful name that represents a
    #single item from the list.
    #you can add as many lines of code as you like 
    #as long as it is indented under the loop

for magician in magicians:
    print(magician.title() + ", WOW.. that was a neat trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

print("Special Thanks to every Magician who participated with us today.")
## if there is something wrong with your indentation you will get an indentation error
## watch out for indentation and syntax errors

'''
Try It Yourself
4-1. Pizzas: Think of at least three kinds of your favorite pizza. Store these
pizza names in a list, and then use a for loop to print the name of each pizza.
-Modify your for loop to print a sentence using the name of the pizza
instead of printing just the name of the pizza. For each pizza you should
have one line of output containing a simple statement like I like pepperoni
pizza.
-Add a line at the end of your program, outside the for loop, that states
how much you like pizza. The output should consist of three or more lines
about the kinds of pizza you like and then an additional sentence, such as
I really love pizza!
4-2. Animals: Think of at least three different animals that have a common characteristic.
Store the names of these animals in a list, and then use a for loop to
print out the name of each animal.
-Modify your program to print a statement about each animal, such as
A dog would make a great pet.
-Add a line at the end of your program stating what these animals have in
common. You could print a sentence such as Any of these animals would
make a great pet!
'''

# using the range() makes it easy to generate a series of numbers.
for num in range(1, 5): # will print up to 4
    print(num)

# n is the number you want, n+1 is the number that you will put

num_list = list(range(1, 5))# using range to make a list of numbers
print(num_list)

#We can also use the range() to skip numbers in a given range.
even_nums = list(range(1, 11, 2))
print(even_nums)

# two asterisks (**) represent exponents.

square = []

for i in range(1, 5):
    i = i ** 2
    square.append(i)

print("Squares list", square)

#Simple Statistics with a List of Numbers

list_of_numbers = list(range(1, 17))
print(list_of_numbers)

min(list_of_numbers) # prints minimum value
max(list_of_numbers) # prints maximum value
sum(list_of_numbers) # prints sum of the digits in the list

## List Comprehensions:
    #The approach described earlier for generating the list squares consisted of
    #using three or four lines of code. A list comprehension allows you to generate
    #this same list in just one line of code. A list comprehension combines the
    #for loop and the creation of new elements into one line, and automatically
    #appends each new element.

squares = [value ** 2 for value in range(1, 11)]
print("A list of Squares Populated Using List Comprehensions", squares)

'''
Try It Yourself
4-3. Counting to Twenty: Use a for loop to print the numbers from 1 to 20,
inclusive.
4-4. One Million: Make a list of the numbers from one to one million, and then
use a for loop to print the numbers. (If the output is taking too long, stop it by
pressing ctrl-C or by closing the output window.)
4-5. Summing a Million: Make a list of the numbers from one to one million,
and then use min() and max() to make sure your list actually starts at one and
ends at one million. Also, use the sum() function to see how quickly Python can
add a million numbers.
4-6. Odd Numbers: Use the third argument of the range() function to make a list
of the odd numbers from 1 to 20. Use a for loop to print each number.
4-7. Threes: Make a list of the multiples of 3 from 3 to 30. Use a for loop to
print the numbers in your list.
4-8. Cubes: A number raised to the third power is called a cube. For example,
the cube of 2 is written as 2**3 in Python. Make a list of the first 10 cubes (that
is, the cube of each integer from 1 through 10), and use a for loop to print out
the value of each cube.
4-9. Cube Comprehension: Use a list comprehension to generate a list of the
first 10 cubes.
'''

## Working With Parts of The List
## Needs Practice
players = ["charles","martina","micheal","florence","eli"]
print(players[0:3]) # list_name[x-1, y-1] here 4 elements will be printed to the screen
print(players[:2]) # will print the first three elements from the list
print(players[2:]) # will cut first 3 elements
print(players[-3:]) # will present the last three elements in the list

# you can also loop through a slice

for player in players[:3]:
    print(player.title())

## Copying a list
    #To start with an existing list and make a copy of the first one. 
    #To copy a list, you make a slice that includes the entire original list
    #by omitting the first index and the second index ([:]). This tells Python to
    #make a slice that starts at the first item and ends with the last item,
    #producing a copy of the entire list.

myfoods = ["pizza", "falafel", "carrot cake"]
friends_foods = myfoods[:]

print("My Favorite Food is :", myfoods)
print("My Friend's Favorite Food is :", friends_foods)

'''
Try It Yourself
4-10. Slices: Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
-Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program's list.
-Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
-Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas .
Then, do the following:
-Add a new pizza to the original list.
-Add a different pizza to the list friend_pizzas .
-Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend's favorite pizzas are:, and then use a for loop to print the sec-
ond list. Make sure each new pizza is stored in the appropriate list.
4-12. More Loops: All versions of foods.py in this section have avoided using
for loops when printing to save space. Choose a version of foods.py, and
write two for loops to print each list of foods
'''

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

############## Conditional Tests ##############
'''
At the heart of every if statement is an expression that can be evaluated as
True or False and is called a conditional test. Python uses the values True and
False to decide whether the code in an if statement should be executed.
'''
# You can also ignore case when checking for equality

# == for equality check
# != for inequality
# <
# >
# <=
# >=

# You can also use -- and/or -- to check for multiple conditions
car_x = "mitsubishi"
# checking if the value is in the list
car_x in cars
# checking if value is not in the list

if car_x not in cars:
    cars.append(car_x)
    print(cars)

# Boolean Expressions
'''
A Boolean expression is just another name for a conditional test
used to keep track of certain conditions, such as whether a game
is running
Boolean values provide an efficient way to track the state of a program
or a particular condition that is important in your program.
'''
engine_on = True

'''
5-1. Conditional Tests: Write a series of conditional tests. Print a statement
describing each test and your prediction for the results of each test. Your code
should look something like this:
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
• Look closely at your results, and make sure you understand why each line
evaluates to True or False.
• Create at least 10 tests. Have at least 5 tests evaluate to True and another
5 tests evaluate to False.
5-2. More Conditional Tests: You don't have to limit the number of tests you
create to 10. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
-Tests for equality and inequality with strings
-Tests using the lower() function
-Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
-Tests using the and keyword and the or keyword
-Test whether an item is in a list
-Test whether an item is not in a list
'''
# The if-elif-else Chain // The else block is a catchall statement.

'''
The if-elif-else chain is powerful, but it’s only appropriate to use when you
just need one test to pass. As soon as Python finds one test that passes, it
skips the rest of the tests. This behavior is beneficial, because it’s efficient
and allows you to test for one specific condition.
However, sometimes it’s important to check all of the conditions of
interest. In this case, you should use a series of simple if statements with no
elif or else blocks. This technique makes sense when more than one condition
could be True, and you want to act on every condition that is True.
Try it your self: 4-way vs 8-way movement
'''

requested_toppings = ["mushrooms", "extra cheese"]

# Run Each of the test blocks individually

# block 1

if "mushrooms" in requested_toppings:
    print("Add Mushrooms")

if "extra cheese" in requested_toppings:
    print("Add Extra Cheese")

if "pepperoni" in requested_toppings:
    print("Add Pepperoni")

print("\nFinished Making Your Pizza")

# block 2

if "mushrooms" in requested_toppings:
    print("Add Mushrooms")

elif "extra cheese" in requested_toppings:
    print("Add Extra Cheese")

elif "pepperoni" in requested_toppings:
    print("Add Pepperoni")

print("\nFinished Making Your Pizza")


'''
Try It Yourself
5-3. Alien Colors #1: Imagine an alien was just shot down in a game. Create a
variable called alien_color and assign it a value of 'green', 'yellow', or 'red'.
• Write an if statement to test whether the alien’s color is green. If it is, print
a message that the player just earned 5 points.
• Write one version of this program that passes the if test and another that
fails. (The version that fails will have no output.)
5-4. Alien Colors #2: Choose a color for an alien as you did in Exercise 5-3, and
write an if-else chain.
• If the alien’s color is green, print a statement that the player just earned
5 points for shooting the alien.
• If the alien’s color isn’t green, print a statement that the player just earned
10 points.
• Write one version of this program that runs the if block and another that
runs the else block.
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse
chain.
• If the alien is green, print a message that the player earned 5 points.
• If the alien is yellow, print a message that the player earned 10 points.
• If the alien is red, print a message that the player earned 15 points.
• Write three versions of this program, making sure each message is printed
for the appropriate color alien.
5-6. Stages of Life: Write an if-elif-else chain that determines a person’s
stage of life. Set a value for the variable age, and then:
• If the person is less than 2 years old, print a message that the person is
a baby.
• If the person is at least 2 years old but less than 4, print a message that
the person is a toddler.
• If the person is at least 4 years old but less than 13, print a message that
the person is a kid.
• If the person is at least 13 years old but less than 20, print a message that
the person is a teenager.
• If the person is at least 20 years old but less than 65, print a message that
the person is an adult.
• If the person is age 65 or older, print a message that the person is an
elder.
5-7. Favorite Fruit: Make a list of your favorite fruits, and then write a series of
independent if statements that check for certain fruits in your list.
• Make a list of your three favorite fruits and call it favorite_fruits.
• Write five if statements. Each should check whether a certain kind of fruit
is in your list. If the fruit is in your list, the if block should print a statement,
such as You really like bananas!
'''

# using if statements with lists

requested_toppings = ["mushrooms", "green peppers", "extra cheese"]

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza")

for requested_topping in requested_toppings:
    if requested_topping == "green pepper":
        print("Sorry, we're out of green peppers.")

    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!!")

# Empty lists -- sometimes we need to check wether
# or not the list is empty to excute the code.

requested_toppings = []

if requested_toppings:
    for i in requested_toppings:
        print("Adding " + i + ".")

    print("\nFinished making your pizza!!")

else:
    print("Are you sure you want a plain pizza?!")


# you can also use multiple lists

available_toppings = ["mushrooms", "olives", "green peppers",
                    "french fries", "pineapple", "extra cheese"]

requested_toppings = ["mushrooms", "french fries", "extra cheese"]

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")

    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")

'''
Try It Yourself
5-8. Hello Admin: Make a list of five or more usernames, including the name
'admin'. Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a greeting to
each user:
• If the username is 'admin', print a special greeting, such as Hello admin,
would you like to see a status report?
• Otherwise, print a generic greeting, such as Hello Eric, thank you for logging
in again.
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
5-10. Checking Usernames: Do the following to create a program that simulates
how websites ensure that everyone has a unique username.
• Make a list of five or more usernames called current_users.
• Make another list of five usernames called new_users. Make sure one or
two of the new usernames are also in the current_users list.
• Loop through the new_users list to see if each new username has already
been used. If it has, print a message that the person will need to enter a
new username. If a username has not been used, print a message saying
that the username is available.
• Make sure your comparison is case insensitive. If 'John' has been used,
'JOHN' should not be accepted.
5-11. Ordinal Numbers: Ordinal numbers indicate their position in a list, such
as 1st or 2nd. Most ordinal numbers end in th, except 1, 2, and 3.
• Store the numbers 1 through 9 in a list.
• Loop through the list.
• Use an if-elif-else chain inside the loop to print the proper ordinal ending
for each number. Your output should read "1st 2nd 3rd 4th 5th 6th
7th 8th 9th", and each result should be on a separate line.
'''

'''
Try It Yourself
5-12. Styling if statements: Review the programs you wrote in this chapter, and
make sure you styled your conditional tests appropriately.
5-13. Your Ideas: At this point, you’re a more capable programmer than you
were when you started this book. Now that you have a better sense of how
real-world situations are modeled in programs, you might be thinking of some
problems you could solve with your own programs. Record any new ideas you
have about problems you might want to solve as your programming skills continue
to improve. Consider games you might want to write, data sets you might
want to explore, and web applications you’d like to create.
'''

############## Dictionaries ##############
# Dictionaries allow you to
# connect pieces of related information.
# access the information in a dictionary and modify it.
# store an almost limitless amount of information.
# model a variety of real-world objects more accurately.

alien_0 = {"color": "green", "points": 5}

print(alien_0["color"])
print(alien_0["points"])

# Dictionaries are dynamic structures,
# you can add new key-value pairs to a dictionary at any time.
# For example,
# to add a new key-value pair,
# you would give the name of the dictionary
# followed by the new key in square brackets with the new value.

alien_0['posx'] = 0
alien_0['posy'] = 25

print(alien_0)

# To modify a value in a dictionary,
# give the name of the dictionary with the key in square brackets
# and then the new value you want associated with that key.

alien_0 = {'color': 'green'}
print("The alien's color is " + alien_0['color'] + ".")

alien_0["color"] = 'yellow'
print("The alien's color is " + alien_0['color'] + ".")

alien_0 = {"x_position": 0, "y_position": 25, "speed": "medium"}
print("Original x-position: " + str(alien_0["x_position"]))

# move the alien to the right
# determine how far the alien is baed on current speed

if alien_0["speed"] == "slow":
    x_increment = 1

elif alien_0["speed"] == "medium":
    x_increment = 2

else: # I wouldn't use something like this in my code
    # it is not beautiful
    x_increment = 3

# the new position is the old position + the increment.
alien_0["x_position"] = alien_0["x_position"] + x_increment

print("New x-position: " + str(alien_0["x_position"]))

# we remove key values by the keyword del..

alien_0 = {"color": "green", "points": 5}

del alien_0["points"] # the deleted key value pair will be removed permeanently

# A Dictionary of Similar Objects

favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward': 'ruby',
    'phil': 'python'
}

print("Sarah's favorite language is " +
    favorite_languages['sarah'].title() + ".")


favorite_languages['sarah']

'''
Try It Yourself
6-1. Person: Use a dictionary to store information about a person you know.
Store their first name, last name, age, and the city in which they live. You
should have keys such as first_name, last_name, age, and city. Print each
piece of information stored in your dictionary.
6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
Think of five names, and use them as keys in your dictionary. Think of a favorite
number for each person, and store each as a value in your dictionary. Print
each person’s name and their favorite number. For even more fun, poll a few
friends and get some actual data for your program.
6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
However, to avoid confusion, let’s call it a glossary.
• Think of five programming words you’ve learned about in the previous
chapters. Use these words as the keys in your glossary, and store their
meanings as values.
• Print each word and its meaning as neatly formatted output. You might
print the word followed by a colon and then its meaning, or print the word
on one line and then print its meaning indented on a second line. Use the
newline character (\n) to insert a blank line between each word-meaning
pair in your output.
'''

# looping through a dictionary

# You can loop through all of a dictionary’s key-value pairs, through its
# keys, or through its values.

# Looping Through All Key-Value Pairs

user_o = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi'
}

for key, value in user_o.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'sarah': 'C',
    'edward': 'ruby',
    'phil': 'python'
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Looping through all the keys in dictionary

for name in favorite_languages.keys():
    print(name.title())


friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print( " Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

    if "erin" not in favorite_languages.keys():
        print("Erin, please take our poll!")


# Looping through a dictionary's keys in order
# the key values in a dictionary are never in order
# you can use the sorted() function to get a copy of the keys in order inside a loop

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", Thank you fo taking the poll.")

# Looping through all values in a dictionary
print("The following languages has been mentioned: ")
for language in favorite_languages.values():
    print(language.title())

#This approach (.values()) pulls all the values from the dictionary without checking
#for repeats. That might work fine with a small number of values, but in a
#poll with a large number of respondents, this would result in a very repetitive
#list.

# so if you don't want any repeated values all you have to do is use the set()

for language in set(favorite_languages.values()):
    print(language.title())


'''
Try It Yourself
6-4. Glossary 2: Now that you know how to loop through a dictionary, clean
up the code from Exercise 6-3 (page 102) by replacing your series of print
statements with a loop that runs through the dictionary’s keys and values.
When you’re sure that your loop works, add five more Python terms to your
glossary. When you run your program again, these new words and meanings
should automatically be included in the output.
6-5. Rivers: Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.
6-6. Polling: Use the code in favorite_languages.py (page 104).
• Make a list of people who should take the favorite languages poll. Include
some names that are already in the dictionary and some that are not.
• Loop through the list of people who should take the poll. If they have
already taken the poll, print a message thanking them for responding.
If they have not yet taken the poll, print a message inviting them to take
the poll.
'''

## Nesting
# sometimes you will want to store a set of dictionaries inside a list
# or a list of item values inside a dictionary..
# this is called nesting
# you can nest:
# a list in a dictionary
# and a set of a dictionariess in a list
#### question can I have a dictionary of dictionaries

# a list of dictionaries

alien_0 = {'color': 'green', 'points': '5'}
alien_1 = {'color': 'yellow', 'points': '10'}
alien_2 = {'color': 'red', 'points': '15'}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


#A more realistic example would involve more than three aliens
#like for example:

# make an empty list for storing aliens:

aliens = []

# make 30 or so aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)

# show the first 5 aliens
for alien in aliens[:5]:
    print(alien)


for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = '10'
        alien['speed'] = 'medium'
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['points'] = '15'
        alien['speed'] = 'fast'



print('...')

# show how many aliens have been created

print("Total number of aliens: " + str(len(aliens)))

# it is commonn to store a number of dictionaries in a list
# when each dictionary contain all sorts of information
# about one object. like for example:
# a dictionary for each user on a website that would be stores in a list called users
# but you should bear in mind that all dictionaries must have identical structure
# otherwise you will not be able to looop through them

# A list in a dictionary
# sometimes it is useful to do the opposite
# storing a list inside a dictionary

# store info about a pizza eing ordered

pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
}

# summarize te order
print("you ordered a " + pizza['crust'] + "-crust pizza" + "with the following toppings:")

for topping in pizza["toppings"]:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['haskell', 'python']
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())


# You should not nest lists and dictionaries too deeply. If you’re nesting items much
# deeper than what you see in the preceding examples or you’re working with someone
# else’s code with significant levels of nesting, most likely a simpler way to solve the
# problem exists.

# A dictionary inside a dictionary
# If I remember correctly I asked myself this question
# and now I know it is possible should have tried it though
# it would have been more fun and satisfying
# You can nest a dictionary inside another dictionary, but your code can get
# complicated quickly when you do. For example, if you have several users
# for a website, each with a unique username, you can use the usernames as
# the keys in a dictionary.

users = {
    'einstien': {
        'first': 'albert',
        'last': 'einstien',
        'location': 'princeton'
                },
     'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
               }
        }
        
for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']
    
    print("\tFull Name: " + full_name.title())
    print("\tLocation: " + location.title())
    
'''
Try It Yourself
6-7. People: Start with the program you wrote for Exercise 6-1 (page 102).
Make two new dictionaries representing different people, and store all three
dictionaries in a list called people . Loop through your list of people. As you
loop through the list, print everything you know about each person.
6-8. Pets: Make several dictionaries, where the name of each dictionary is the
name of a pet. In each dictionary, include the kind of animal and the owner’s
name. Store these dictionaries in a list called pets . Next, loop through your list
and as you do print everything you know about each pet.
6-9. Favorite Places: Make a dictionary called favorite_places . Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.
6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 102) so
each person can have more than one favorite number. Then print each person’s
name along with their favorite numbers.
6-11. Cities: Make a dictionary called cities . Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country , population , and fact . Print the name of each city and all of the infor-
mation you have stored about it.
6-12. Extensions: We’re now working with examples that are complex enough
that they can be extended in any number of ways. Use one of the example pro-
grams from this chapter, and extend it by adding new keys and values, chang-
ing the context of the program or improving the formatting of the output.
'''

############# User Input and While Loops #############
message = input("Tell me something, and I'll repeat it back to you: ")
print(message)

# Important Note:
# sublime doesn't run programs that prompts for user input
# you can write it in sublime then run it in a terminal

name = input("Please enter your name: ")
print("Hello, {}!!\n How was your day?".format(name))

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)

print("\nHello, {} !".format(name))

age = input("\nHow old are you? ")
age = int(age)

# check age
if age >= 10:
	print("\nOh, you are growing up so fast?")

# you can also keep age as a string for whatever reason

age = input("How old are you? ")

if int(age) >= 10:
	print("You are older than my ten years old son")

# roller coaster example

height = input("\nHow tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou are tall enough to ride.")

else:
	print("\nWait till you get older or taller")

# The magical and the beautiful modulus operator
# the modulus operator gives you the remainder
# you will use it a lot not just in conditionals but in moidfying output in certain ways
# specially in gaming

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
	print("\nThe number " + str(number) + " is even.")
else:
	print("\nThe number " + str(number) + " is odd.")

'''
Try It Yourself
7-1. Rental Car: Write a program that asks the user what kind of rental car they
would like. Print a message about that car, such as “Let me see if I can find you
a Subaru.”
7-2. Restaurant Seating: Write a program that asks the user how many people
are in their dinner group. If the answer is more than eight, print a message saying
they’ll have to wait for a table. Otherwise, report that their table is ready.
7-3. Multiples of Ten: Ask the user for a number, and then report whether the
number is a multiple of 10 or not.
'''

# The Indispensible While Loops
current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

# just a reminder
# while loops if not used correctly it will crash your program
# possibly your PC, I wrote a program that burnt my sound card because of a while loop

# letting the user choose when to quit

prompt = "\nTell me something, and I will repeat it back to you"
prompt += "\nEnter quit to end the program. "

message = " "
while message != "quit":
	message = input(prompt)
	print(message)

# notice that this program will continue running until the user
# inputs quit the same way you wrote it because inputs are also case sensitive

# using a flag popular in pygame :D
active = True
while active:
	message = input(prompt)

	if message == "quit":
		active = False

	else:
		print(message)


# using a break to exit a loop

prompt = "\nPlease enter the name of a city you visited: "
prompt += "\nEnter 'quit' when you are finished.."

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")

# you can also use a break in a for loop

### Continue ### Very Important ###
# You do not always want to exit the loop
# Rather than breaking out of a loop entirely without executing the rest of its
# code, you can use the continue statement to return to the beginning of the
# loop based on the result of a conditional test.

current_number = 0
even_nums = []

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		current_number *= 2
		even_nums.append(current_number)
		continue
	elif current_number % 2 != 0:
		print("\n{} is odd.".format(current_number))
print(even_nums)

# in the previous example if executed correctly
# it will only print odd numbers
# it will print  list of even numbers multiplied by 2

############## AVOID INFINITE LOOPS FOR THE LOVE OF YOUR PC ##############
# like this one
'''
num = 1
while num < 10:
	print("22")
'''
# if there is no code to break the loop
# the loop will break your code and your computer
# it is one of the ways to get an angy piece of code
# ctrl + c is the angry code kryptonite
# use it to exit out of the terminal
# Some editors, such as Sublime Text, have an embedded output window. This can
# make it difficult to stop an infinite loop, and you might have to close the editor to
# end the loop.

'''
Try It Yourself
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press
ctrl-C or close the window displaying the output.
'''

# while loops with lists and dictionaries

# to modify a list while working through it use a while loop
# using while loops with lists and dictionaries allows you
# to colect, store and organize a lot of input to examine
# and to report on later

# Moving Items for One List to Another

# start with users that need to be verified
# and an empty list to hold confirmed users
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# verify each user untill there is no more unconfirmed users
# move each verified user into the list of confirmed users
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title())
	confirmed_users.append(current_user)

# disply all confimed users
print("\nThe following users have been confirmed: ")
for user in confirmed_users:
	print(user.title())

# Removing All Instances of Specific Values from a List

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# Filling A Dictionary With User Input

responses = {}

# setting a flag to indicate poll is active
polling_active = True

while polling_active:
	# promt for the person's name and response
	# Key word
	name = input("\nWhat is your name? ")
	# value
	response = input("\nWhich mountain would you like to climb someday? ")

	# store the input in the dictionary
	responses[name] = response

	# finding if anyone else is going to take the poll
	repeat = input("Would you like to let another erson take the poll? (yes/no) ")
	if repeat == 'no':
		polling_active = False

# polling is complete. show results

print("\n---- Poll Results ----")
for name, response in responses.items():
	print(name + " would like to climb " + response + ".")

'''
Try It Yourself
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop
through the list of sandwich orders and print a message for each order, such
as I made your tuna sandwich. As each sandwich is made, move it to the list
of finished sandwiches. After all the sandwiches have been made, print a
message listing each sandwich that was made.
7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
the sandwich 'pastrami' appears in the list at least three times. Add code
near the beginning of your program to print a message saying the deli has
run out of pastrami, and then use a while loop to remove all occurrences of
'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
in finished_sandwiches.
7-10. Dream Vacation: Write a program that polls users about their dream
vacation. Write a prompt similar to If you could visit one place in the world,
where would you go? Include a block of code that prints the results of the poll.
'''

############## WHERE THE FUNction BEGINS ##############
# functions are blocks of code that are designed to do a specific job.
# when you want perform the task that you've defined in a function..
# you need to call the function reponsible for the task
# computer will execute the functions
# functions will either -output or -recieve and process
# functions can also be stored in seperate files called modules
# you can import or use this module and call it in your main file
# it will help you keep your code clean and organized

# Defining A Function

def greet_user():

	"""Display a Simple Greeting""" # this is a docstring
	# a docstring is string that describes the function
	print("Hello!")

greet_user()

# Passing Information to A Function
def greet_user_mod1(username):
	"""Takes username and Display a greeting"""
	# the information passed into the function is called
	# A Parameter
	print("Hello, " + username.title() + "!")

greet_user_mod1('jesse')

# Arguments and Parameters
# People sometimes speak of arguments and parameters interchangeably. Don’t be surprised
# if you see the variables in a function definition referred to as arguments or the
# variables in a function call referred to as parameters.

'''
Try It Yourself
8-1. Message: Write a function called display_message() that prints one sentence
telling everyone what you are learning about in this chapter. Call the
function, and make sure the message displays correctly.
8-2. Favorite Book: Write a function called favorite_book() that accepts one
parameter, title. The function should print a message, such as One of my
favorite books is Alice in Wonderland. Call the function, making sure to
include a book title as an argument in the function call.
'''

# Passing Arguments

# positional arguments
# When you call a function, Python must match each argument in the function
# call with a parameter in the function definition. The simplest way to
# do this is based on the order of the arguments provided. Values matched
# up this way are called positional arguments.

def describe_pet(animal_type, pet_name):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# Multiple function calls :
# You can do it by:
	# writing it multiple times
	# calling it inside a loop

# order matters in positional arguments

# Keyword Arguments
# it is a nmae value pair that you pass to a function
# your directly assiciate the name and the value within
# the argument so that when you pass the argument to the
# function, to avoid confusion
# keyword arguments free you from having to worry aboyt
# correctly passing your arguments in the function call

describe_pet(animal_type = 'Dog', pet_name = 'Harry')

# you don't have to worry about the order you assign the values

describe_pet(pet_name = 'Harry', animal_type = 'Frog')

# Note:
# when you use keywords arguments, be sure to use the exact name
# you used when you defined the function

# Default Values
# you can assign a default value for each parameter to avoid a program crash
# when you call the function

def describe_pet_DV(animal_type = None, pet_name = None):
	"""Display information about a pet"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

# now you can call the function with one parameter without worrying
# that the proram will crash

#### A Very Important Note ####
# when you use default values, any parameter with a default value needds to belisted
# after all the parameters that don't have default values. this allows python to continue
# interpreting positional arguments correctly

# Equivalent Function Calls

# it doesn't really matter what calling style you use
# just pickk a style that you are comfortable with..

# Avoiding Argument Errors

# Missing Reuired positional argument error

'''
Try It Yourself
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
8-5. Cities: Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.
'''

## Return Values
# some functions are not used to display out directly
# on the other hand the majority of functions will be
# used to process input and return a value
# int, str, boolean, float, double... and so on

# Returning a Simple Value

def get_formatted_name(first_name, last_name):
	"""Return a full name, neatly formatted"""
	full_name = first_name + " " + last_name
	return full_name.title()

musician = get_formatted_name("jimi", "hendrix")
print(musician)

# Making an Argument Optional
# sometimes you will need to make arguments optional
# in case oyu want to give the user a choice to either
# provide extra information about themselves
# or stick to only required information for example

def get_formated_name_mod1(first_name, middle_name = "", last_name):
	"""Return a full name, neatly formatted"""
	if middle_name:
		full_name = first_name + " " + middle_name + " " + last_name
	else:
		full_name = first_name + " " + last_name

	return full_name.title()

musician = get_formated_name_mod1("john","lee","hooker")
guitarist = get_formated_name_mod1("jimi", last_name = "hendrix")

print(musician, guitarist)

# Returning a Dictionary
# a function can return any value or set of values
# including lists and dictionaries

def build_person(first_name, last_name):
	"""Return a dictionary of information about a person"""
	person = {'first': first_name, 'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

# revise looping through a dictionary
# it looks like an enum
for fname, lname in musician.values():
	print(fname, lname)

def build_person_mod1(first_name, last_name, age=""):
	"""Return a dictioanry of information about a person"""
	person = {"first": first_name, "last": last_name}
	if age:
		person['age'] = age
	return person

musician = build_person_mod1('jimi', 'hendrix', age=27)
print(musician)

# Using a Function With a While Loop
def get_formatted_name_mod2(first_name, last_name):
	"""Return a full name, neatly formatted."""
	full_name = first_name + " " + last_name
	return full_name.title()

while True:
	prnt("\nTo Exit Enter q at any time")
	print("\nPlease tell me your name: ")
	f_name = input("First Name: ")
	l_name = input("Last Name: ")


	formatted_name = get_formatted_name_mod2(f_name, l_name)
	print("\nHello, " + formatted_name + "!")

	if f_name =='q' or l_name == 'q':
		break

"""
Try It Yourself
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
"""

# Passing a List
# it is useful to know you can pass lists into functions
# it will help you work wih functions more effeciently
def greet_users(names):
	"""Print a simple greeting to each user in a list"""
	for name in names:
		name.lower()
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['HaNNah', 'manar', 'sara']
greet_users(usernames)

# modufying a list in a function

### The program we want to add as a function ###
# Start with some designs that needs to be printed
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design
# move each design to completed_models after printing
while unprinted_designs:
	current_design = unprinted_designs.pop()

	# simulate creating a 3d print from the design
	print("Printing model: " + current_design)
	completed_models.append(current_design)

# display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
	print(completed_model)

# this program can be split to fit in two seperate functions
# the first will handle processing the input
# the second will handle the output

def print_models(unprinted_designs, completed_models):
	"""
	Simulate printing each design, untill none are left.
	Move each design to completed models after printing.
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()

		# simulate creating a 3d print from the design
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""Show all the models that were printed."""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)

# now you can just call the two functions
# just in case you are wondering I wrote 
# a lot of code what did I gain from writing a function
# well for starters you can use them over and over and over
# and you can store them into another file and import
# so the code main file will always be clean and neat
# and remember if the code doesn't look beautiful
# then it is bad code, good code will always be beautiful
# also remember you need to call the function to work
# it won't work if you didn't call her

# Preventing a Function from Modifying a list
# to prevent a function from changing your list
# all you need to do is to pass a copy of the original function
# that way you won't change the original list

# list_name[:]
# like so
print_models(unprinted_designs[:] ,completed_models)
show_completed_models(completed_models)

"""
Try It Yourself
8-9. Magicians: Make a list of magician’s names. Pass the list to a function
called show_magicians(), which prints the name of each magician in the list.
8-10. Great Magicians: Start with a copy of your program from Exercise 8-9.
Write a function called make_great() that modifies the list of magicians by adding
the phrase the Great to each magician’s name. Call show_magicians() to
see that the list has actually been modified.
8-11. Unchanged Magicians: Start with your work from Exercise 8-10. Call the
function make_great() with a copy of the list of magicians’ names. Because the
original list will be unchanged, return the new list and store it in a separate list.
Call show_magicians() with each list to show that you have one list of the original
names and one list with the Great added to each magician’s name.
"""

# Passing an Arbitrary Number of Arguments
# if you don't know how many arguments you can pass to a function
# python allows functions to have an arbitrary number of arguments
# from the calling statement

def make_pizza(*toppings):
	"""Print the list of toppings that have been requested"""
	print(toppings)

make_pizza("pepperoni")
make_pizza("cheese", "pepperoni", "cow_tits")

# the asteriskin the parameter name tells python to make
# an empty tuple in this case it is called toppings
# even if the function carries one value it will be packed
# into a tuple

def make_pizza_mod1(*toppings):
	"""summarize the pizza we are about to make"""
	print("\nMaking a pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

make_pizza_mod1("pepperoni")
make_pizza_mod1("cheese", "pepperoni", "cow_tits")

# This syntax works no matter how many arguments the function recieves

# Mixing Positional ad Arbitrary Arguments
def make_pizza_mod2(size, *toppings):
	"""summarise the pizza we are about to make"""
	print("\nMaking a " + size + "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)

make_pizza_mod1("pepperoni")
make_pizza_mod1("cheese", "pepperoni", "cow_tits")

# Using Arbitrary Keyword Arguments
# Sometimes you’ll want to accept an arbitrary number of arguments, but you
# won’t know ahead of time what kind of information will be passed to the
# function. In this case, you can write functions that accept as many key-value
# pairs as the calling statement provides. One example involves building user
# profiles: you know you’ll get information about a user, but you’re not sure
# what kind of information you’ll receive.

def build_profile(first, last, **user_info):
	"""build a dictionary containing everything we know about a user"""
	profile = {}
	profile["first_name"] = first_name
	profile["last_name"] = last_name
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile("albert", "einstien", location="princeton", field="physics")
print(user_profile)

# Just to be clear here
# ** creates a dictionary that stores any number of name value pairs
# as if you are writing
# first = value
# last = value
# where first is key word and variable name
# and value is the value of that variable

# Home Work: Write a function tat accepts an arbitrary number of arguments
"""
def function_dictionary(first, last, **data_type, **user_info):
	profile = {}
	profile[first] = input("Enter first name: ")
	profile[last] = input("Enter last name: ")
	for type in data_type:
		type = input("Enter data type: ")
		for value in user_info:
			value = input("Enter value")
			profile[type] = value
	# or something like that do it at home
"""

"""
Try It Yourself
8-12. Sandwiches: Write a function that accepts a list of items a person wants
on a sandwich. The function should have one parameter that collects as many
items as the function call provides, and it should print a summary of the sandwich
that is being ordered. Call the function three times, using a different number
of arguments each time.
8-13. User Profile: Start with a copy of user_profile.py from page 153. Build
a profile of yourself by calling build_profile(), using your first and last names
and three other key-value pairs that describe you.
8-14. Cars: Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
"""

# Storing Functions in Modules
# Easy peazy
# you will know that if you took any tut in pygame
# simply you can create a separate .py file
# then you call that file inside your main code
# import file
# or from file import *
# or import file as short_file_name
# or from file import function as short_function_name
# each import method is correct do whatever you are comfortable with
# just put into consideration that each method of import has a different
# calling method inside your main file

# Styling Functions
# The Styling part actually is all about taste
# and pep08 so we're going to skip it here in the text
# basically naming a function is like naming a variable
# if you have a lot of parameters treat like a list

"""
8-15. Printing Models: Put the functions for the example print_models.py in a
separate file called printing_functions.py. Write an import statement at the top
of print_models.py, and modify the file to use the imported functions.
8-16. Imports: Using a program you wrote that has one function in it, store that
function in a separate file. Import the function into your main program file, and
call the function using each of these approaches:
import module_name
from module_name import function_name
from module_name import function_name as fn
import module_name as mn
from module_name import *
8-17. Styling Functions: Choose any three programs you wrote for this chapter,
and make sure they follow the styling guidelines described in this section.
"""

############## Classes ##############


