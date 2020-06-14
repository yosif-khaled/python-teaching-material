##### A Huge Subject and Should Be Split Into Bits #####
##### Remember You Can't Cover Everything #####
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


#def get_formated_name_mod1(first_name, middle_name = "", last_name):
#SyntaxError: non-default argument follows default argument

def get_formated_name_mod1(first_name, last_name,  middle_name = ""):
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
for fname, lname in musician.items():
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
	print("\nTo Exit Enter q at any time")
	print("\nPlease tell me your name: ")
	f_name = input("First Name: ")
	if f_name == 'q':
	    break
	l_name = input("Last Name: ")


	formatted_name = get_formatted_name_mod2(f_name, l_name)
	print("\nHello, " + formatted_name + "!")
    
    #writing the function after asking the user for input
    #will keep the program running till it asks the user for the last input
    # in other words program will execute all lines of code till it reaches the logic and checks
    # whether this logic applies or not then execute   
    #if f_name =='q' or l_name == 'q':
		#break

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
	profile["first_name"] = first
	profile["last_name"] = last
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
