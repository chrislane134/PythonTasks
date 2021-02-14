
name = input("What is your name?")
count = len(name)

if count < 3:
    print("name must be at least 3 charcters long")
elif count > 50:
    print("name can be a maximum of 50 characters")
else:
    print("name looks good")


# ACTUAL SOLUTION (not bad i just has an extra varible)
# name = input("What is your name?")

# if len(name) < 3:
#     print("name must be at least 3 charcters long")
# elif len(name) > 50:
#     print("name can be a maximum of 50 characters")
# else:
#     print("name looks good")
