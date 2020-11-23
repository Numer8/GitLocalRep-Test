# testbed.py

# Ref/source: 

# to run script:
# win    'python_module_template.py'
# Linux  'python3 python_module_template.py'

"""
First line should be a short description & becomes the module's docstring when the file is imported.

It must be the first statement in the object’s (module, function, class, and method) definition.
You can access docstrings  using the following special variable: myobj.__doc__
e.g. print(theFunction.__doc__)
They should not be descriptive should describe what the function does, not how
and end with a period.
"""


import platform

def find_platform():
    """This function detremine the operating system and prints it"""
    print("platform.platform(): returns:", platform.platform())
    print("platform.node(): returns computers network name:", platform.node())
    if platform.system() == "Linux" or platform.system() == "Linux2":
        print("Platform is: Linux")
    elif platform.system() == "darwin":
        print("Platform is: MAC OS X")
    elif platform.system() == "win32":
        print("Platform is: Windows 32 bit")
    elif platform.system() == "win64":
        print("Platform is: Windows 64-bit")


def main():
    """main does not execute when this file imported as a module."""
    # pylint: disable=too-many-branches
    find_platform()
    print("Hello World!")
    # pylint: enable=too-many-branches

if __name__ == "__main__":
    # executes only if run as a script
    # sys.exit(main(sys.argv))
    main()
print("\nValue in built variable name is:  ", __name__, "\n")


