
file = open('sample.txt','r')
reader = file.read()
print(reader)

file = open('sample.txt','w')
file.write("Write mode removes all existing file content")

