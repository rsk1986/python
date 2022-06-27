def calcweather(temp):
    if temp > 7:
        return "Hot"
    else:
        return "warm"

#user_input = int(input("Enter Input: "))

user_input = float(input("Enter Input: "))

print(type(user_input), user_input)

print (calcweather(user_input))