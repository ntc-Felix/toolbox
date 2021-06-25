
def copy(src, dst):
    """
    Copy the contents of one file to another.
    
    Args:
    src(str): File name of the file to be copied.
    dst(str): Where to write the new file
    """

    # Open the source file and read in the contents

    with open(src) as f_src:
        contents = f_src.read()

    # Open the destination file and write out the contents
    with open(dst, 'w') as f_dst:
        f_dst.write(contents)


"""
The problem with this function is that it will stop work
once we try to copy a file that is too large to fit in memory.

What would be ideal is if we could open both files at once and copy over one line at a time
Fortunately for us, the file object that the "open()" context manager returns can be
iterated over in a for loop
"""
# like this

with open('my_file.txt') as file:
    for line in my_file:
        #do something

# so our function will be written as:

def copy(src, dst):
    """
    Copy the contents of one file to another.
    
    Args:
    src(str): File name of the file to be copied.
    dst(str): Where to write the new file
    """

    # Open the source file and read in the contents

    with open(src) as f_src:
        with open(dst, 'w') as f_dst:
            # Read and write each line, one at a time
            for line in f_src:
                f_dst.write(line)


# Handling Errors

"""
Imagine someone creates a function named get_printer() as shown below.
Someone decides to use your get_printer() function to print the text of their document.
However, they weren't paying attention and accidentally typed 'txt' insted of 'text'

This will raise a KeyError Because 'txt' is not in the 'doc' dictionary.
And that means p.disconnect() doesn't get called.

So what we can do ?

try:
    # code that might raise an error

except:
    # do something about the error

finally:
    # this code runs no matter what
"""

def get_printer(ip):
    p = connect_to_printer(ip)

    yield 

    # This MUST be called or no one else will
    # be able to connect to the printer

    p.disconnect()
    print('disconnected from printer')

doc = {'text': 'This is my text.'}

with get_printer('10.0.34.111') as printer:
    printer.print_page(doc['txt'])


# writing a better function

def get_printer(ip):
    p = connect_to_printer(ip)

    try:
        yield 
    
    finally:
    # This MUST be called or no one else will
    # be able to connect to the printer

    p.disconnect()
    print('disconnected from printer')


