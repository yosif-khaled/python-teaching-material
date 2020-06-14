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
