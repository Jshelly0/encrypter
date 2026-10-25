def binaryConverter(text):
    total = ""
    for char in text:
        if char == "A": total += "01000001/"
        elif char == "B":total += "01000010/"
        elif char == "C":total += "01000011/"
        elif char == "D":total += "01000100/"
        elif char == "E":total += "01000101/"
        elif char == "F":total += "01000110/"
        elif char == "G":total += "01000111/"
        elif char == "H":total += "01001000/"
        elif char == "I":total += "01001001/"
        elif char == "J":total += "01001010/"
        elif char == "K":total += "01001011/"
        elif char == "L":total += "01001100/"
        elif char == "M":total += "01001101/"
        elif char == "N":total += "01001110/"
        elif char == "O":total += "01001111/"
        elif char == "P":total += "01010000/"
        elif char == "Q":total += "01010001/"
        elif char == "R":total += "01010010/"
        elif char == "S":total += "01010011/"
        elif char == "T":total += "01010100/"
        elif char == "U":total += "01010101/"
        elif char == "V":total += "01010110/"
        elif char == "W":total += "01010111/"
        elif char == "X":total += "01011000/"
        elif char == "Y":total += "01011001/"
        elif char == "Z":total += "01011010/"
        elif char == "a":total += "01100001/"
        elif char == "b":total += "01100010/"
        elif char == "c":total += "01100011/"
        elif char == "d":total += "01100100/"
        elif char == "e":total += "01100101/"
        elif char == "f":total += "01100110/"
        elif char == "g":total += "01100111/"
        elif char == "h":total += "01101000/"
        elif char == "i":total += "01101001/"
        elif char == "j":
            total += "01101010/"
        elif char == "k":
            total += "01101011/"
        elif char == "l":
            total += "01101100/"
        elif char == "m":
            total += "01101101/"
        elif char == "n":
            total += "01101110/"
        elif char == "o":
            total += "01101111/"
        elif char == "p":
            total += "01110000/"
        elif char == "q":
            total += "01110001/"
        elif char == "r":
            total += "01110010/"
        elif char == "s":
            total += "01110011/"
        elif char == "t":
            total += "01110100/"
        elif char == "u":
            total += "01110101/"
        elif char == "v":
            total += "01110110/"
        elif char == "w":
            total += "01110111/"
        elif char == "x":
            total += "01111000/"
        elif char == "y":
            total += "01111001/"
        elif char == "z":
            total += "01111010/"
    return total
    
# def shiftFunction(text, original_text_len):
#     alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#     shift_amount = original_text_len % 25
#     shifted_result = ""
    
#     for char in text:
#         # Check if the character is in our lowercase alphabet list to shift it
#         if char in alphabet:
#             current_index = alphabet.index(char)
#             new_index = (current_index + shift_amount) % len(alphabet)
#             shifted_result += alphabet[new_index]
#         else:
#             # Keep non-alphabet characters (like slashes '/') as they are
#             shifted_result += char
            
#     return shifted_result
        

    

def customEncrypter(text):
    binary_string, aphabet, newTotal = binaryConverter(text), ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"], ""
    binary_blocks = [block for block in binary_string.split('/') if block]
    total = ""
    for block in binary_blocks:
        modified_block = block[4:] + block[:4]
        for i in range(4):
            tempVar = ""
            tempVar = modified_block[-1]
            modified_block = modified_block[:4] + tempVar + modified_block[4:-1]
        total += modified_block + "/"
    for i in range(len(total)):
        # total += shiftFunction(total[i], len(total))
        newTotal += aphabet[total[i]]
    return newTotal

print(customEncrypter("jack"))

