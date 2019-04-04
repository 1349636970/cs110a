# Filename: Ch09-Sun.py
# Description Serendipity Booksellers has a book club that awards points to its customers based on the number of books purchased each month. The points are awarded as follows:

# If a customer purchases 0 books, he or she earns 0 points.
# If a customer purchases 2 books, he or she earns 5 points.
# If a customer purchases 4 books, he or she earns 15 points.
# If a customer purchases 6 books, he or she earns 30 points.
# If a customer purchases 8 or more books, he or she earns 60 points.
# Write a program that asks the user to enter the number of books that he or she has purchased this month, then displays the number of points awarded.

def main():
    books = int(input("Enter the number of books: "))
    points = 0
    if books > 8:
        points = 60
    elif books > 6:
        points = 30
    elif books > 4:
        points = 15
    elif books > 2:
        points = 5
    elif books < 0:
        print("ERROR")
    print("You awarded",points,"points")
main()

# Enter the number of books: 9
# You awarded 60 points
