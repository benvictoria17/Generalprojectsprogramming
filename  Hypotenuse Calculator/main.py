# The Hypotenuse Calculator

# Input for the length of the first leg
leg1 = float(input("Please enter the length of one of the legs of your triangle: "))

# Input for the length of the second leg
leg2 = float(input("Please enter the length of the other leg: "))

# Calculate the hypotenuse using the Pythagorean theorem
hypotenuse = (leg1**2 + leg2**2)**0.5

# Display the result
print(f"The length of your hypotenuse is: {hypotenuse}")
