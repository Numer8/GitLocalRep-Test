# Open command window or Windows Powershell
# change to directory with Python Scripts in
# venue        cd C:\Users\russt\OneDrive\Documents\Prog
# e5440        cd C:\Users\russ\OneDrive\Documents\Prog
# Opti760      cd /
# SCRIPTS:
# venue   c:\users\russt\appdata\local\programs\python\python36-32\lib\site-packages
# e5440   C:\Users\russ\AppData\Local\Programs\Python\Python38\Scripts
# Opti760      cd /var/samba/shares/public
#
# use pylint to check code

# to run script:
# e5440    'system_parameters.py'
# Opti760  'python3 system_parameters.py''

# A comment is anything after the # hash/octothorpe/pound sign and is ignored by python.
# Comments are so you can read your program later.

# based on https://www.thepythoncode.com/article/get-hardware-system-information-python

"""
First line should be a short description & becomes the module's docstring when the file is imported.

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

import os.path
import pathlib
import platform
from datetime import datetime

import psutil

def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

def main():
    """main does not execute when this file imported as a module."""
    # pylint: disable=too-many-branches

    # get system information
    print("="*30, "System Information ", "="*30)
    print(f"Uname: {platform.uname()}")     

    print(f"OS name: {os.name}")
    print(f"System: {platform.system()}")
    print(f"Platform Node: {platform.node()}")
    print(f"Platform Release: {platform.release()}")      
    print(f"Version: {platform.version}")
    print(f"Machine: {platform.machine()}")
    print(f"Processor: {platform.processor()}")
    print(f"Architecture: {platform.architecture()}")
    print(f"Platform: {platform.platform()}")
    #Get python information
    print("="*30, "Python Information ", "="*30)    
    print(f"Python Build: {platform.python_build()}")
    print(f"Python Compiler: {platform.python_compiler()}")
    print(f"Python Branch: {platform.python_branch()}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Revision: {platform.python_revision()}")
    print(f"Python Version: {platform.python_version()}")
    # Boot Time
    print("="*30, "Boot Time", "="*30)
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)
    print(f"Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")
    # CPU information
    print("="*30, "CPU Info", "="*30)
    # number of cores
    print("Physical cores:", psutil.cpu_count(logical=False))
    print("Total cores:", psutil.cpu_count(logical=True))
    # CPU frequencies
    cpufreq = psutil.cpu_freq()
    print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
    print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
    print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
    # CPU usage
    print("CPU Usage Per Core:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
        print(f"Core {i}: {percentage}%")
    print(f"Total CPU Usage: {psutil.cpu_percent()}%")

    # Memory Information
    print("="*30, "Memory Information", "="*30)
    # get the memory details
    svmem = psutil.virtual_memory()
    print(f"Total: {get_size(svmem.total)}")
    print(f"Available: {get_size(svmem.available)}")
    print(f"Used: {get_size(svmem.used)}")
    print(f"Percentage: {svmem.percent}%")
    print("="*20, "SWAP", "="*20)
    # get the swap memory details (if exists)
    swap = psutil.swap_memory()
    print(f"Total: {get_size(swap.total)}")
    print(f"Free: {get_size(swap.free)}")
    print(f"Used: {get_size(swap.used)}")
    print(f"Percentage: {swap.percent}%")

    # Disk Information
    print("="*30, "Disk Information", "="*30)
    print("Partitions and Usage:")
    # get all disk partitions
    partitions = psutil.disk_partitions()
    for partition in partitions:
        print(f"=== Device: {partition.device} ===")
        print(f"  Mountpoint: {partition.mountpoint}")
        print(f"  File system type: {partition.fstype}")
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint)
        except PermissionError:
            # this can be catched due to the disk that
            # isn't ready
            continue
        print(f"  Total Size: {get_size(partition_usage.total)}")
        print(f"  Used: {get_size(partition_usage.used)}")
        print(f"  Free: {get_size(partition_usage.free)}")
        print(f"  Percentage: {partition_usage.percent}%")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")
    # get IO statistics since boot
    disk_io = psutil.disk_io_counters()
    print(f"Total read: {get_size(disk_io.read_bytes)}")
    print(f"Total write: {get_size(disk_io.write_bytes)}")

    # Network information
    print("="*30, "Network Information", "="*30)
    # get all network interfaces (virtual and physical)
    if_addrs = psutil.net_if_addrs()
    for interface_name, interface_addresses in if_addrs.items():
        for address in interface_addresses:
            print(f"=== Interface: {interface_name} ===")
            if str(address.family) == 'AddressFamily.AF_INET':
                print(f"  IP Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast IP: {address.broadcast}")
            elif str(address.family) == 'AddressFamily.AF_PACKET':
                print(f"  MAC Address: {address.address}")
                print(f"  Netmask: {address.netmask}")
                print(f"  Broadcast MAC: {address.broadcast}")
    # get IO statistics since boot
    net_io = psutil.net_io_counters()
    print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
    print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")

    # Directory Information
    print("="*30, "Directory nformation", "="*30)
    print(f"Home directory: {pathlib.Path.home()})")
    print(f"Current directory: {pathlib.Path.cwd()}")

    is_windows = os.name == 'nt'
    windows_exts = os.environ['PATHEXT'].split(";") if is_windows else None
    path_dirs = os.environ['PATH'].split(":")
    print("Directory Paths:", path_dirs)
    search_dirs = path_dirs + [os.getcwd()] # cwd is last in the list
    print("Search Directories:", search_dirs)
#    for dir in search_dirs:
#        path = os.path.join(dir, name)
#        if is_windows:
#            for extension in windows_exts:
#                path_with_ext = path + extension
#                if os.path.isfile(path_with_ext) and os.access(path_with_ext, os.X_OK):
#                    return path_with_ext
#        else:
#            if os.path.isfile(path) and os.access(path, os.X_OK):
#                return path


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
