f= open("D://xyz//Python Code Files//book2.txt","w")
f.write("\nI love Java too")
f.close()

f= open("D://xyz//Python Code Files//book2.txt","r")
s=f.read()
print(s)