course = "Python for Beginners"
print(len(course))  # counts number of characters. General purpose function.
print(course.upper())  # makes all characters uppercase
print(course.lower())  # makes all characters lowercase
# will return the index of that character. Case sensitive. can parse sequence of characters eg:'for'
print(course.find('P'))
# case sensitive, replace characters.
print(course.replace('Beginners', 'Absolute Beginners'))
# true or false return, also case sensitive. does it exist or not.
print('Python' in course)
