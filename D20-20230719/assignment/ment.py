file=open("/home/sivarajan/karka.txt","a")
file.write("i am siva,\n")
file.close()
file=open("/home/sivarajan/karka.txt","r")
#pint(file.read())
for line in file:
   print(line.split())
