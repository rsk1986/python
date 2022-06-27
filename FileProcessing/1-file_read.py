### Method - 1 (without any optional parameters)
file = open("fruits.txt")
#file=open("/Users/sathiskumarraju/Desktop/Google-Drive/Python_Projects/Sec11_File_Processing/fruits.txt")
print (file.read())
print (file.read())   ### will print nothing as the curson at the end of file
file.seek(0)       ### move the cursor to the beginning of the file
print (file.read())  ### now it will read
file.close()


#### help(file)
'''
Help on built-in function open in module io:

open(file, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
'''

### Method - 2 (with an additional optional parameter)
file2 = open("fruits.txt","r") ### This one & first definition both are same
print (file2.read())
file2.close()

### Method - 3 (Read file under sub-directory)
file3 = open ("testdir/veg.txt")
print (file3.read())


### Method - 4 (Open file using with) - this will close the file automatically after coming out of the block

with open("fruits.txt") as file4:
    content = file4.read()

print(content)


#### Method - 5 (Print first 20 characters)

file5 = open("fruits.txt")
op = file5.read()

print (op[:20])

##### Method - 5 (Function to print no. of occurences of a character)

def calc_occurance(ch,filepath):
    file = open(filepath)
    op = file.read()
    return op.count(ch)

print(calc_occurance("a","fruits.txt"))
print(calc_occurance("e","fruits.txt"))



with open("0-file_help.py") as f:
    ff = f.read()
    f.read()
    f.seek(0)
    fff = f.read()

print (fff)
