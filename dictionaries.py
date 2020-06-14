
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

