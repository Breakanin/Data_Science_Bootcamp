sentence = "I'm learning Data Science at Hyperion bootcamp."

# code to make each alternate character an UPPERCASE 
# and each other alternate character a lowercase
var = ""
for char in range(len(sentence)):
    if not char % 2:
        var += sentence[char].upper()
    else:
        var += sentence[char].lower()
print(var)

# split sentence to make  each alternative word
# lower and upper case
var2 = sentence.split()
var3 = ""
for word in range(len(var2)):
    if not word % 2:
        var3 += var2[word].lower() + " "
    else:
        var3 += var2[word].upper() + " "
print(var3)