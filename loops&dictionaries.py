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

