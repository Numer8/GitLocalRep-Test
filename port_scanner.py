# 'port_scanner.py'

# Ref/Source: https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python

# to run script:
# Windows 'port_scanner.py '
# Linux 'python3 port_scanner.py '

"""
A small and easy-to-use port scanner program using the built-in module Socket.

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

#!/usr/bin/env python
import socket
# import subprocess
import sys
from datetime import datetime


def is_port_open(host, port):
    """
    determine whether `host` has the `port` open
    """
    # creates a new socket
    s = socket.socket()
    try:
        # tries to connect to host using that port
        s.connect((host, port))
        # make timeout if you want it a little faster ( less accuracy )
        # s.settimeout(0.2)
    except:
        # cannot connect, port is closed
        # return false
        return False
    else:
        # the connection was established, port is open!
        return True

def main():
    """main does not execute when this file imported as a module."""
    # pylint: disable=too-many-branches
    # Clear the screen
#    subprocess.call('clear', shell=True)

    # Ask for input
    remote_server = input("Enter a remote host to scan: ")
    host = socket.gethostbyname(remote_server)

    # Print a nice banner with information on which host we are about to scan
    print("-" * 60)
    print("Please wait, scanning remote host", host)
    print("-" * 60)

    # Check what time the scan started
    time_start = datetime.now()

    # Using the range function to specify ports (here it will scans all ports between 1 and 1024)

    # We also put in some error handling for catching errors

    try:
        for port in range(1, 1025):
#            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#            result = sock.connect_ex((remote_server_IP, port))
#            if result == 0:
#                print("Port {}: 	 Open".format(port))
#            sock.close()
            if is_port_open(host, port):
                print(f"{host}:{port} is open")
            else:
                print(f"{host}:{port} is closed", end="\r")
    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    # Checking the time again
    time_end = datetime.now()

    # Calculates the difference of time, to see how long it took to run the script
    total = time_end - time_start

    # Printing the information to screen
    print('Scanning Completed in: ', total)
    # pylint: enable=too-many-branches

if __name__ == "__main__":
    # executes only if run as a script
    # sys.exit(main(sys.argv))
    main()
print("\nValue in built variable name is:  ", __name__, "\n")

# python installed in C:\Users\russt\AppData\Local\Programs\Python\Python38
# Open command window or Windows Powershell use cmd "py --version" to check install
# Use command "py -m pydoc [keyword]" for python documentation

# FILE:
# Typically, a Python file is any file that contains code. Most Python files have the extension .py.
# SCRIPT:
# A Python script is a file that you intend to execute from the command line to accomplish a task.
# MODULE:
# A Python module is a file that you intend to import from within another module or a script,
# or from the interactive interpreter. You can read more about modules in the Python documentation.

# Put most code into a function or class.
# Use __name__ to control execution of your code.
# Create a function called main() to contain the code you want to run.
# Call other functions from main().

# What is the order of operations in Python? The same as the US
# acronym PEMDAS which stands for
# Parentheses Exponents Multiplication Division Addition Subtraction

# Python Style guide: https://www.python.org/dev/peps/pep-0008/
# Use 4 spaces per indentation level.
# Spaces are the preferred indentation method (not tabs)
# Limit all lines to a maximum of 79 characters.
# break before binary operations
# 2 blank lines around top-level function and class definitions
# 1 blank lines around Method definitions inside a class
# blank lines in functions, sparingly, to indicate logical sections.
# Extra blank lines may be used (sparingly) to separate groups of related functions.
# Code in the core Python distribution should always use UTF-8
# IMPORTS should usually be on separate lines
# Naming Convention.............
# FUNCTION and VARIABLE names: lowercase words separated by underscores
# METHOD names and Instance Variables as function names.
# CONSTANTS: Words all capital letters separated by underscores.
# CLASS names: should normally use the CapWords convention.
