print("Insert text : ", end="")
text = input()

textArray = list(text)
textLength = len(textArray)

for i in range(round(textLength / 2)):
    textArray[i], textArray[textLength - i - 1] = textArray[textLength - i - 1], textArray[i]

print("Result : " + ''.join(textArray))
