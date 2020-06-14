############# User Input and While Loops #############
##### Add Input with printing #####
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

