############## Classes ##############

# or in other words... OOP

# classes represent represent real world things and situations
# and you can create objects based on these situations.
# when you write a class, you define the general behavior that a whole category
# of objects can have
# like for example class animal has charactaristics all animals can share
# Alive, breathing feeding
# and a class can inherit another class
# like class mammals will inherit form main animal class
# the possibilities are limitless
# though some people don't like it and if you are one of them
# you are in luck because python is a multi-paradigm language
# and you can only use functions but your code will not be beautiful
# you should use pick the way that suits the project
# Making an object from a class is called instantiation and you work
# with instances of a class

### first steps ###
## Creating and Using a Class

class Dog():
    """A simple attempt to model a dog"""
    
    def __init__(self, name, age):
        """Initialize Attributes"""
        self.name = name;
        self.age = age;
        
    def sit(self):
        """simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting");
        
    def roll_over(self):
        """simulate a dog rolling over in response to command"""
        print(self.name.title() + " rolled over!!");
        

## To Use A class you need to create an instance of said class like so
_dog1 = Dog(Billy, 20);
## You can create as many instances as you want you can even use a loop

## You can access attributes by (access operator -- don't what it is called) the . like _dog1.name _dog1.age

## after you create a class you call the methods by using the dot notation also like so _dog1.roll_over();
_dog1.roll_over();

##Even if we used the same name and age for the second dog, Python
##would still create a separate instance from the Dog class. You can make
##as many instances from one class as you need, as long as you give each
##instance a unique variable name or it occupies a unique spot in a list or
##dictionary.

"""
Try It Yourself
9-1. Restaurant: Make a class called Restaurant. The __init__() method for
Restaurant should store two attributes: a restaurant_name and a cuisine_type.
Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating
that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes
individually, and then call both methods.
9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three
different instances from the class, and call describe_restaurant() for each
instance.
9-3. Users: Make a class called User. Create two attributes called first_name
and last_name, and then create several other attributes that are typically stored
in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints
a personalized greeting to the user.
Create several instances representing different users, and call both methods
for each user.
"""

## Working with Classes and Instances
## Notice that the parameters or the attributes are passed through init function which is built in python
## Notice that you need to pass the object itself inside its functions

class Car():
    """A simple attempt to represnt a car"""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        # you can also set a default value for an attribute like so
        self.odometer_reading = 0
        
    def get_describtive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()
        
    def read_odometer(self):
        """Print a statement that shows the mileage on the car"""
        print("This car has " + str(self.odometer_reading) + " mile on it.")
        
    def update_odometer(self, mileage):
        """Updates Odometer Value
        Rejects Value manipulation"""
        if self.odometer_reading <= mileage:
            self.odometer_reading = mileage
        else:
            print("You can not roll back the odometer")
            
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        # add if statement to prevent users from entering negative values to manipulate or decrease values
        # add a conditional to deal if the value was zero
        self.odometer_reading += miles

# Object Instantiation
new_car = Car('audi','a4','2016')

# Method Calls
new_car.read_odometer()

## Modifying the values of attributes

#Modifying an Attribute’s Value Directly
new_car.odometer_reading = 23
new_car.read_odometer()


#Modifying an Attribute’s Value Through a Method
new_car.update_odometer(23)
new_car.read_odometer()

new_car.update_odometer(3)
new_car.read_odometer()

#Incrementing an Attribute’s Value Through a Method
new_car.increment_odometer(4)


"""
Try It Yourself
9-4. Number Served: Start with your program from Exercise 9-1 (page 166).
Add an attribute called number_served with a default value of 0. Create an
instance called restaurant from this class. Print the number of customers the
restaurant has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number
of customers that have been served. Call this method with a new number and
print the value again.
Add a method called increment_number_served() that lets you increment
the number of customers who’ve been served. Call this method with any number
you like that could represent how many customers were served in, say, a
day of business.
9-5. Login Attempts: Add an attribute called login_attempts to your User
class from Exercise 9-3 (page 166). Write a method called increment_
login_attempts() that increments the value of login_attempts by 1. Write
another method called reset_login_attempts() that resets the value of login_
attempts to 0.
Make an instance of the User class and call increment_login_attempts()
several times. Print the value of login_attempts to make sure it was incremented
properly, and then call reset_login_attempts(). Print login_attempts again to
make sure it was reset to 0.
"""

## Inheritance ##
# This is what make OOP important
#You don’t always have to start from scratch when writing a class. If the class
#you’re writing is a specialized version of another class you wrote, you can
#use inheritance. When one class inherits from another, it automatically takes
#on all the attributes and methods of the first class. The original class is
#called the parent class, and the new class is the child class. The child class
#inherits every attribute and method from its parent class but is also free to
#define new attributes and methods of its own.

class ElectricCar(car):
    """Represents Aspects of a Car, Specific to Electric Cars"""
    def __init__(self, make, model, year):
        """Initialize attributes of the parents class"""
        super().init(make, model, year)
        self.battery_size =  70

    def describe_battery(self):
        """Print a statement describing the battery size"""
        print("This car has a " + str(self.battery_size) + "-kwh battery.")

# creating an instance of a child class is the same as parent class
tesla_car = ElectricCar('tesla', 'model s', 2016)
print(tesla_car.get_descriptive_name())
tesla_car.describe_battery()
# the child class will access the methods of the parent class in addition to its own methods


#  Over riding methods from the parent class
# define a method
# in the child class with the same name as the method you want to override
# in the parent class. Python will disregard the parent class method and only
# pay attention to the method you define in the child class.

# Instances as Attributes
# When modeling something from the real world in code, you may find that
# you’re adding more and more detail to a class. You’ll find that you have a
# growing list of attributes and methods and that your files are becoming
# lengthy. In these situations, you might recognize that part of one class can
# be written as a separate class. You can break your large class into smaller
# classes that work together.
# For example, if we continue adding detail to the ElectricCar class, we
# might notice that we’re adding many attributes and methods specific to
# the car’s battery. When we see this happening, we can stop and move those
# attributes and methods to a separate class called Battery.

'''
Try It Yourself
9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
a class called IceCreamStand that inherits from the Restaurant class you wrote
in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called
flavors that stores a list of ice cream flavors. Write a method that displays
these flavors. Create an instance of IceCreamStand, and call this method.
9-7. Admin: An administrator is a special kind of user. Write a class called
Admin that inherits from the User class you wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on.
Write a method called show_privileges() that lists the administrator’s set of
privileges. Create an instance of Admin, and call your method.
9-8. Privileges: Write a separate Privileges class. The class should have one
attribute, privileges, that stores a list of strings as described in Exercise 9-7.
Move the show_privileges() method to this class. Make a Privileges instance
as an attribute in the Admin class. Create a new instance of Admin and use your
method to show its privileges.
9-9. Battery Upgrade: Use the final version of electric_car.py from this section.
Add a method to the Battery class called upgrade_battery(). This method
should check the battery size and set the capacity to 85 if it isn’t already.
Make an electric car with a default battery size, call get_range() once, and
then call get_range() a second time after upgrading the battery. You should
see an increase in the car’s range.
'''

# Importing Classes
# imports are the easiest part
# just name the files, classes and functions in an orderly way
# two ways to import:
# from file-module import * (star means all)
# from file-import class or function
# import file-module
