# This program determines whether or not a word is palindrome

word = input("Please enter a word: ")
word = str(word)
flip = ""
pal_found = True

# genetating the backward identity of the string by the user
for i in range (1, len(word)+1):
    flip += word[-i]    # concatenation the charaters of
                        # word to flip strating from the last index (-1)
    
#
for i in range (len(flip)):
    if flip[i]!=word[i]:    # this will check for unmatched character
        pal_found = False         # 
        break
    
print("Backward Identity: " + flip) # printing the backword(reversed) string
    
if pal_found == True: # palindrome word found
    print(" Your word is a palindrome word")
else:
    print("Your word is not a palindorme word")
