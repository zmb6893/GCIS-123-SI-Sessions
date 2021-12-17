"""
Session 12A: Classes and constructors
@author: Zoe Bingham
"""

# TODO: Create a method to return a formatted string for a FavoriteHobby.
# you will be using this in the next step

# TODO: Create a method that prints the information for a person.
# use this for printing output instead of the prints in main.

# TODO: Refactor all the classes to use private fields and create accessors
# accordingly.

# TODO: Add some accessors to the clsses

# TODO: Come up with some things that a person might do. Example: wake up,
# excercise, attend class, sleep, eat ...
# Make methods in the person class for a few of these.

# Make a person class that holds the state for a name, age, and mood
class Person:
    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class
    pass

    


# Make a course class that holds the state for course_name, course_number, and number_of_students
# Once you have completed the above step, add a state for courses to the person class
class Course:
    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class
    pass

# Make a class for a favorite hobby that has fields for hobby_name and description
# Once you've have completed this step, add the state for favorite hobby to the person class
class FavoriteHobby:
    # Refactor the code so that the person class only accepts use of the variables defined above.

    # Make a constructor for this class
    pass

def main():
    # Instantiate a person class with default values
    person = Person()

    # This will print out the appropriate string
    print("Person: %s\n"%person)
    print("Person: name: %s\tmood: %s\tage: %d\thobby: %s\tcourses %s\n"%(person.name, person.mood, person.age, person.favoriteHobby.hobby_name, person.courses[0].course_id))
    
    # Make some RIT courses

    # Make a dictionary of courses accessed by the course id.

    # Prompt the user for a course id and search the dictionary for the course. Print out the name
    # of the course, the professor, and the number of students in the class
            

if __name__ == "__main__":
    main()
