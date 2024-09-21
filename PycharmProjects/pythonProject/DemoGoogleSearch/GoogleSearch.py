# importing the module
import pywhatkit    #
# use Try Except to
# handle the Exceptions
try:

# it will perform the Google search
    pywhatkit.search("apple") # search criteria given in quotes
    print("Searching...")

except:

# Printing Error Message
    print("An unknown error occured")
