'''
try: something that might cause an exception

except: do this if there was an exception

else: do this if there are no exceptions

finally: do this regardless of what happens
'''

# lets make our own exceptions

# try:
    # file = open("a_file.txt") # without the file, this will raise an error
    # a_dictionary = {"Key":"value"}
    # print(a_dictionary["sdsfs"])
# except FileNotFoundError:
    # print("There was an error") # the above file does not exist
    # file = open("a_file.txt", "w")
    # file.write("Something")
#else:
 # if everything goes well, this block will execute when there is no exception
# finally:
  # this will run regardless of whether an exception was raised

#=====================================================================================================#

height = float(input("Height: "))
weight = int(input("Weight: "))

if height >= 3:
    raise ValueError("Humans should not be taller than 3 meters") # Raise makes the error message appear

# bmi = weight / height ** 2
# print(bmi)













