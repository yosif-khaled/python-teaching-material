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

