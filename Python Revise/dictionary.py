dict={}
#dict are mutable
# s=set()
print(type(dict))
# print(type(s))

dict1={"good":"Something Pleasant","1":"The number one"}
print(dict1)

marks={"Amul":100,
       "Rahul":90,
       "Raj":80,
       "Rohan":70,
       "Rahul":60}
print(marks)
print(marks["Amul"])
marks["Priyanka"]=34
print(marks)

print(marks.get("Rahul"))
print(marks.get("AYush")) #this will show none i.e. key is not present
#print(marks["AYush"])#this will show error
#because we have used get method which returns None if the given key is not present in dictionary
print(marks["Rahul"])

print(marks.keys())
print(marks.values())
print(marks.items())
