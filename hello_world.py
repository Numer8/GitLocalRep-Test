# hello_world.py

# Ref/Source: based on Python Tutorials https://docs.python.org/3/tutorial/

# to run script:
# Windows 'hello_world.py '
# Linux 'python3 hello_world.py '

"""
Outputs text "Hello World!" to the monitor.

It must be the first statement in the object’s (module, function, class, and method) definition.
You can access docstrings  using the following special variable: myobj.__doc__
e.g. print(theFunction.__doc__)
They should not be descriptive should describe what the function does, not how
and end with a period.
"""
#to view the docstring start Python
# C\:> py
# >>> import moduleName
# >>> help(moduleName)

# define function
def print_hello():
    """prints Hello World to screen"""
    print("Hello World!")


def main():
    """Calls print_hello to output "Hello World!" to the monitor """
    # pylint: disable=too-many-branches
    # call function defined above
    print_hello()
    # pylint: enable=too-many-branches

if __name__ == "__main__":
    # executes only if run as a script
    # sys.exit(main(sys.argv))
    main()

