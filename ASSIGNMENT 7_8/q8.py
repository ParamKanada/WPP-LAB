# Decode

def decode(encoded, index=0, current_decoding="", results=None):
    if results is None:
        results = []
    
    if index == len(encoded):
        results.append(current_decoding)
        return
    
    num1 = int(encoded[index])
    if 1 <= num1 <= 9:
        decode(encoded, index + 1, current_decoding + chr(64 + num1), results)
    
    if index + 1 < len(encoded):
        num2 = int(encoded[index:index + 2])
        if 10 <= num2 <= 26:
            decode(encoded, index + 2, current_decoding + chr(64 + num2), results)
    
    return results

a = input("Enter MSG to encode = \n")

b = decode(a)

print("\n Display Ways ...\n")
for i,j in enumerate(b,1):
    print(f"{i} {j}")