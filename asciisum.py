#wap for ascii sum
inputList = ["hello", "tutorialspoint", "python", "platform"]
print("Input List:", inputList)
resultList = []
asciiValsSum = 0
for i in inputList:
    asciiValsSum = sum(map(ord, i))
resultList.append(asciiValsSum)
print(resultList)

#ascii sum by function
# def asciiSums(sentence):
#     words = sentence.split(' ')
#     result = {}
#     for i in words:
#         Sum = sum(map(ord, i))
#         result[i] = Sum
#     sumsOfAscii = [result[i] for i in words]
#     print(' '.join(map(str, sumsOfAscii)))
#     print(sum(sumsOfAscii))#the sum
# sentence = 'I am a geek'
# asciiSums(sentence)

