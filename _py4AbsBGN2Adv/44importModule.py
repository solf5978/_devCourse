"""
Author: Jesse Warner
Date: August 1, 2023
"""
# Define a function that prints to the console. This function should only run
# if the script is executed explicity or the function is called by the 
# importing script, not when the script is imported as a module.
def main():
    print("This is the main function in the import_me.py file")

# This print statement will be executed when this script is executed explicitly 
# or when it is imported as a module.
print("This is a regular statement inside the script")

# The if conditional is used to determine if the script was executed explicitly 
# or imported as a module and calls the `main()` function.
if __name__ == "__main__":
    main()