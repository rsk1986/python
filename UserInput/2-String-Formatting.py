
user_input = input("Enter Some Phrase#: ")
message = "Hello %s" % user_input
print (message)

message2 = f"Hello {user_input}" ### This format works only Python 3.6+ Versions
print (message2)

name = input("First Name: ")
surname = input("Surname: ")
when = "today"

message3 = "Hello %s %s" % (name, surname)
print (message3)

message4 = f"Hello {name} {surname}"
print (message4)

namex = "Hi %s" % name.title()
print(namex)

