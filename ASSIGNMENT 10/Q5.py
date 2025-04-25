"""Write a program to make the length of each element 15 of a given Numpy array and the
string centred, left-justified, right-justified with paddings of _ (underscore)."""

import numpy as np

# Function to modify strings in the array
def format_strings(array):
    # Centered, Left-Justified, Right-Justified
    centred = [f"{str(item):_^15}" for item in array]
    left_justified = [f"{str(item):_<15}" for item in array]
    right_justified = [f"{str(item):_>15}" for item in array]

    return np.array(centred), np.array(left_justified), np.array(right_justified)

# Example Input Array
input_array = np.array(["Python", "Numpy", "AI", "Code", "Centered", "Left", "Right"])

# Formatting the strings
centred_array, left_array, right_array = format_strings(input_array)

# Printing Results
print("Original Array:")
print(input_array)

print("\nCentred Strings:")
print(centred_array)

print("\nLeft-Justified Strings:")
print(left_array)

print("\nRight-Justified Strings:")
print(right_array)