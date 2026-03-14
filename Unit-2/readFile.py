# Reading a file and printog the total number of words in that file

f = open("sample.txt", "r")
content = f.read()

print("=" * 45)
print("File COntents : ")
print("=" * 45)
print(content)

words = content.split()
print("=" * 45)
print("Total Number of Words : ", len(words))
print("=" * 45)
