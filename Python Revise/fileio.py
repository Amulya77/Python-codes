s="amulya is a good boy"

# with open("test.txt","w") as f:
#     f.write(s)
#     f.close()

# fp=open("test.txt","w")
# fp.write(s)
# fp.close()

# with open("test.txt","r") as f:
#     a=f.read()
#     print(a)
#     f.close()

#APPEND to a file

with open("test.txt","a") as f:
    f.write("\nI am appending this line")
    f.close()