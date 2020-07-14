print("Insert text : ", end="")
text = input()

textArray = list(text)
textLength = len(textArray)

newText = [None] * textLength

for i in range(round(textLength / 2)):
    newText[textLength - i - 1] = textArray[i]
    newText[i] = textArray[textLength - i - 1]
    if (textLength % 2) != 0:
        newText[round(textLength / 2)] = textArray[round(textLength / 2)]

print("Result : " + ''.join(newText))
