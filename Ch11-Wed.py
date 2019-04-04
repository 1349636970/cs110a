# File: Ch11-Wed.py
# # Description: In physics, an object that is in motion is said to have kinetic energy. The following formula can be used to determine a moving object’s kinetic energy:
# KE = 0.5*mv2
# The variables in the formula are as follows: KE is the kinetic energy, m is the object’s mass in kilograms, and v is the object’s velocity in meters per second.

# Write a function named kinetic_energy that accepts an object’s mass(in kilograms) and velocity(in meters per second) as arguments. The function should return the amount of kinetic energy that the object has. Write a program that asks the user to enter values for mass and velocity, then calls the kinetic_energy function to get the object’s kinetic energy.


def kinetic_energy(mass, velocity):
    return 0.5*mass*(velocity**2)

def main():
    input_mass = user_input("mass")
    input_velocity = user_input("velocity")
    display(kinetic_energy(input_mass, input_velocity))


def user_input(object_property):
    return float(input("Enter your object " + object_property +": "))


def display(kinetic_energy):
    print("Your object kinetic energy is ",kinetic_energy)

main()

# Enter your object mass: 2
# Enter your object velocity: 2
# Your object kinetic energy is 4.0
