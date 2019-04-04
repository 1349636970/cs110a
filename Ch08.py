# A cookie recipe calls for the following ingredients:

# 1.5 cups of sugar

# 1 cup of butter

# 2.75 cups of flour

# The recipe produces 48 cookies with this amount of the ingredients. Write a program that asks the user how many cookies he or she wants to make, then displays the number of cups of each ingredient needed for the specified number of cookies.

# def main():
#     amount_cookie = ask_user()
#     amount_ingredients = calculation(amount_cookie)
#     display(amount_ingredients)

# def ask_user():
#     return int(input("Enter how many cookies you want: "))


# def calculation(amount_cookie):
#     sugar = (amount_cookie/48)*1.5
#     butter = (amount_cookie/48)
#     flour = (amount_cookie/48)*2.75
#     return {"sugar": sugar, "butter":butter,"flour":flour}


# def display(amount_ingredients):
#     for amount_ingredient in amount_ingredients:
#         print(amount_ingredient, amount_ingredients[amount_ingredient])


# A car's miles-per-gallon(MPG) can be calculated with the following formula:

# MPG = Miles driven / Gallons of gas used

# Write a program that asks the user for the number of miles driven and the gallons of gas used. It should calculate the car's MPG and display the result.

# def Miles_per_Gallon():
#     pre_info = ask_user()
#     result = calculation(pre_info)
#     display(result)

# def ask_user():
#     miles_driven = float(input("Enter the number of miles driven: "))
#     gallons_gas = float(input("Enter the gallons of gas used: "))
#     return {"miles_driven":miles_driven, "gallons_gas":gallons_gas}


# def calculation(pre_info):
#     return pre_info['miles_driven']/pre_info['gallons_gas']

# def display(result):
#     print(format(result,'.2f'))


# Write a program that converts Celsius temperatures to Fahrenheit temperatures. The formula is as follows:

# LaTeX: F\: =\: \frac{9}{5}C\: +\: 32F = 95C+32

# The program should ask the user to enter a temperature in Celsius, then display the temperature converted to Fahrenheit.

def main():
	celsius = ask_user()
	fahrenheit = converter(celsius)
	create_table(fahrenheit, celsius)

def ask_user():
	celsiuses = []
	celsius = float(input("Enter celsius: "))
	celsiuses.append(celsius)
	while celsius != "exit":
		celsius = input("Enter celsius: ")
		if celsius != "exit":
			celsius = float(celsius)
			celsiuses.append(celsius)
	return celsiuses

def converter(celsiuses):
	fahrenheits = []
	for celsius in celsiuses:
		formula = (9/5)*celsius+32
		fahrenheits.append(formula)
	return fahrenheits


def create_table(fahrenheits, celsiuses):
	print("celsius\t", "fahrenheit")
	print("|-------|------------|")
	for fahrenheit, celsius in zip(fahrenheits, celsiuses):
		print(format(celsius,'6.2f'),format(fahrenheit, '10.2f'))
		print("|-------|------------|")
main()
