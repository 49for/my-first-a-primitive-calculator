from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.RED)
x = input("Выбери действие ( + ; - ; * ; / ; % ): ")

a = float( input("Введи первое число: ") )
b = float( input("Введи второе число: ") )

if x == "+":
	x = a + b 
	print ("Результат:" + str(x))

elif x == "-":
	x = a - b 
	print ("Результат:" + str(x))
elif x == "*":
	x = a * b 
	print ("Результат:" + str(x))
elif x == "/":
	x = a / b
	print ("Результат:" + str(x))
elif x == "%":
	x = a % b 
	print ("Результат:" + str(x))
else:
	
	print(Fore.WHITE)
	print("Выбрано неправильное действие!")
input("")