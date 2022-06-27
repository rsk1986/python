#### Help
'''

Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newli
ne=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
    
    'r'       open for reading (default)
    'w'       open for writing, truncating the file first
    'x'       create a new file and open it for writing (dont open existing file)
    'a'       open for writing, appending to the end of the file if 
it exists
    'b'       binary mode
    't'       text mode (default)
    '+'       open a disk file for updating (reading and writing)
    'U'       universal newline mode (deprecated)

'''
'''

Cheatsheet (File Processing)
===============================

In this section, you learned that:

* You can read an existing file with Python:

with open("file.txt") as file:
    content = file.read()

* You can create a new file with Python and write some text on it:

with open("file.txt", "w") as file:
    content = file.write("Sample text")

* You can append text to an existing file without overwriting it:

with open("file.txt", "a") as file:
    content = file.write("More sample text")

* You can both append and read a file with:

with open("file.txt", "a+") as file:
    content = file.write("Even more sample text")
    file.seek(0)
    content = file.read()

'''

