# File: Ch14-Sun.py
# Description: Figure 3-19 shows a simplified flowchart for troubleshooting a bad Wi-Fi connection. Use the flowchart to create a program that leads a person through the steps of fixing a bad Wi-Fi connection.

def main():
    user_answer = None
    count = 1
    while count <= 4 and user_answer != "yes" :
        print("Reboot the computer and try to connect.")
        user_answer = input("Did that fix the problem? ")
        if count == 2:
            print("Make sure the cables between the router and modem are plugged in firmly.")
        elif count == 3:
            print("Move the router to a new location.")
        elif count == 4:
            print("Get a new router.")
        count += 1

main()


# Reboot the computer and try to connect.
# Did that fix the problem? no
# Reboot the computer and try to connect.
# Did that fix the problem? no
# Make sure the cables between the router and modem are plugged in firmly.
# Reboot the computer and try to connect.
# Did that fix the problem? no
# Move the router to a new location.
# Reboot the computer and try to connect.
# Did that fix the problem? no
# Get a new router