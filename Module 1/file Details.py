file = open ("Details.txt","a")

file.write("\ni love boobs")
file.close()
file = open("Details.txt","r")

content = file.read()


print(content)