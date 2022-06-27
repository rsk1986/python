# File Write
'''
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a stream.  Raise OSError upon failure.
'''

### Method 1 - Simple Write
### write also overwrite existing files

file1 = open("w1.txt","w")
file1.write("14\n")
file1.write("25\n33\n")
file1.write("77")
    
### Method 2 - Write Using with

with open("w2.txt","w") as file2:
    file2.write("hi\n")
    file2.write("hello")


#### Method 3 - Read & Write diff files

with open("readfrom.txt") as fileread:
    content = fileread.read()

with open("writeto.txt","w") as filewrite:
    filewrite.write(content[:90])


#### Method 4 - File Append
# x - create new file for writing (dont open existing file)
# a -> append
# + -> both read & write

with open("append.txt","a+") as fileappend:
    fileappend.write("\nbye")
    fileappend.seek(0)
    content2 = fileappend.read()

print (content2)

### Method 6 - Append the contents of bear1.txt to bear2.txt
with open("bear1.txt") as fread:
    content3 = fread.read()

with open("bear2.txt","a") as fwrite:
    fwrite.write(content3)

#### Method 7 - Read the contents of a file twice in the same file    
with open("data.txt","a+") as rwfile:
    rwfile.seek(0)
    content4 = rwfile.read()
    rwfile.seek(0)
    rwfile.write(content4)
    rwfile.write(content4)
    
    