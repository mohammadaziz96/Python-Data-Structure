#counts the number of words in a line

counts=dict()
line=input("Enter a line of text: ")
words=line.split()
print(words)
print("Counting each words")
for word in words:
    counts[word]=counts.get(word,0)+1
print(counts)
