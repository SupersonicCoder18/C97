text = input("Enter your Introduction")
charactercount = 0
wordcount = 1
for i in text:
    charactercount+=1
    if (i == " "):
        wordcount+=1
print("No. of words in this script is ")
print(wordcount)
print("No. of characters in this string is ")
print(charactercount)