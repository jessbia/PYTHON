#Simple madlibs using different ways of string concatenation
name =input("Your name:")
age =input("Your age:")
country =input("Your country:")

print("Hi! My name is {}, I am {} years old and I am from {}! Nice to meet you!".format(name,age,country))

madlib = f"Meu nome é {name}, eu tenho {age} anos e venho do {country}! Prazer em te conhecer!"
print(madlib)