def main():
    pre_info = ask_user()
    total_sales = calculation(pre_info)
    display(total_sales)


def ask_user():
    sales = []
    for day in range(1, 8):
        sales.append(int(input("Enter sales for day#"+str(day)+": ")))
    return sales


def calculation(sales):
    return sum(sales)


def display(infomation):
    print(infomation)


# Design a program that lets the user enter the total rainfall for each of 12 months into a list. The program should calculate and display the total rainfall for the year, the average monthly rainfall, the months with the highest and lowest amounts.

def rainfall():
    pre_info = ask_user_rainfall()
    rainfall_data = calculation_rainfall(pre_info)
    display_rainfall(rainfall_data)
def ask_user_rainfall():
    rainfall_list = []
    for month in range(1,13):
        rainfall_list.append(float(input("Enter rainfall for month# "+str(month)+":")))
    return rainfall_list
def calculation_rainfall(user_input):
    total_rainfall = sum(user_input)
    average_rainfall = total_rainfall/12
    highest_rainfall = max(user_input)
    lowest_rainfall = min(user_input)
    return [total_rainfall, average_rainfall, highest_rainfall, lowest_rainfall]
def display_rainfall(data_show):
    text = ["total_rainfall", "average_rainfall",
            "highest_rainfall", "lowest_rainfall"]
    for data in range(len(data_show)):
        print(text[data],data_show[data])


rainfall()
