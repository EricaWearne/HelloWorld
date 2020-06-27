shoplist = ["apples", "oranges", "bananas", "cheese"]
print(shoplist)
print(shoplist[2])
print(shoplist[0:2])
shoplist.append("blueberries")
print(shoplist)
shoplist[0] = "cherries"
print(shoplist)
del shoplist[1]
print(shoplist)
print(len(shoplist))
shoplist2 = ["bread", "jam", "peanut butter"]
print(shoplist+shoplist2)
print(shoplist*2)
listnum = [len(shoplist), len(shoplist2)]
print(max(listnum))
print(min(listnum))
listnum2 = [1,7,27,86,5]
print(max(listnum2))
print(min(listnum2))
