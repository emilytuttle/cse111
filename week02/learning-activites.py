# def main():
#     # Get an odometer value in U.S. miles from the user.

#     # Get another odometer value in U.S. miles from the user.

#     # Get a fuel amount in U.S. gallons from the user.

#     # Call the miles_per_gallon function and store
#     # the result in a variable named mpg.

#     # Call the lp100k_from_mpg function to convert the
#     # miles per gallon to liters per 100 kilometers and
#     # store the result in a variable named lp100k.

#     # Display the results for the user to see.
#     pass


# def miles_per_gallon(start_miles, end_miles, amount_gallons):
#     """Compute and return the average number of miles
#     that a vehicle traveled per gallon of fuel.

#     Parameters
#         start_miles: An odometer value in miles.
#         end_miles: Another odometer value in miles.
#         amount_gallons: A fuel amount in U.S. gallons.
#     Return: Fuel efficiency in miles per gallon.
#     """
#     return


# def lp100k_from_mpg(mpg):
#     """Convert miles per gallon to liters per 100
#     kilometers and return the converted value.

#     Parameter mpg: A value in miles per gallon
#     Return: The converted value in liters per 100km.
#     """
#     return


# Call the main function so that
# this program will start executing.
# main()

 # """Compute and print the volume of a right circular cone."""
    
    # Import the standard math module so that
    # math.pi can be used in this program.
import math
    
    
def main(radius, height):
    # Call the cone_volume function to compute
    # the volume of an example cone.
    ex_radius = 2.8
    ex_height = 3.2
    ex_vol = cone_volume(radius, height)

    # Print several lines that describe this program.
    print("This program computes the volume of a right")
    print("circular cone. For example, if the radius of a")
    print(f"cone is {ex_radius} and the height is {ex_height}")
    print(f"then the volume is {ex_vol:.1f}")
    print()

    # Get the radius and height of the cone from the user.
    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    # Call the cone_volume function to compute the volume
    # for the radius and height that came from the user.
    vol = cone_volume(radius, height)

    # Print the radius, height, and
    # volume for the user to see.
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {vol:.1f}")


def cone_volume(radius, height):
    """Compute and return the volume of a right circular cone."""
    volume = math.pi * radius**2 * height / 3
    return volume


# Start this program by
# calling the main function.
main(5.0, 8.2)