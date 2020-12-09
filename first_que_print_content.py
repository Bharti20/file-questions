my_file3 = open("people1-exercise.txt","r")
my_file= my_file3.read()
new_file= my_file.split("\n")
i=0
count=0
while i<len(new_file):
    count=count+1
    i=i+1
print("line", count)
my_file3.close()