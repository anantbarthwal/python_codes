#Like a string, list is a sequence of values. In a string, the values are characters,
#whereas in a list, they can be of any type.
thislist = ["apple", "banana", "cherry","apple"]
thislist1=["watermelon","mango"]
list2=[10,2,5,7,0]
print(thislist)
print("first item of the list=",thislist[0])
thislist.append(10)
print("thislist=",thislist)
thislist.extend(thislist1)
print("thislist=",thislist)
print("thislist.pop()=",thislist.pop(0))
print("thislist=",thislist)
print("del",thislist.remove("apple"))
print("thislist",thislist)
thislist.insert(3,12000)
print("thelist=",thislist)
thislist.reverse()
print("thislist=",thislist)
print("list2=",list2)
list2.sort()
print("list2=",thislist)
print("len(list2)=",len(list2))


