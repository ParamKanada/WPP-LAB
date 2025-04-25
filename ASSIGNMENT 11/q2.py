import pandas as pd 
 
# Given pandas series 
s = pd.Series(['X', 'Y', 'T', 'Aaba', 'Baca', 'CABA', None, 'bird', 'horse', 'dog']) 
 
# Convert to uppercase 
upper_case = s.str.upper().fillna('')
 
# Convert to lowercase 
lower_case = s.str.lower().fillna('')
 
# Find length of each string (handling None values) 
string_length = s.str.len().fillna(0)
 
# Print results 
print("Original Series:") 
print(s) 
print("\nUppercase:") 
print(upper_case) 
print("\nLowercase:") 
print(lower_case) 
print("\nString Lengths:") 
print(string_length)