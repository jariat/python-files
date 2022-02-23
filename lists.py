#list uses indicis to access the values
my_intergers = [2,5,8,9,2]
print(my_intergers[4])
my_relatives = ["JuniorM","Janat","Jamilah","Fatia","Faridah","shifat","Kakyo"]
print(my_relatives[2])
my_intergers.append(10)
print(my_intergers)
my_friends = []
my_friends.append("Junior")
my_friends.append("Shamim")
my_friends.append("Kakyo")

print(my_friends[1])
print(my_friends)

#dictionary uses keys and values where by keys act as indicies
dictionary_tk ={"name":"Jariat", "nickname":"Prettie","Nationality":"Ugandan","age":23}
print("Am called: %s" %(dictionary_tk["name"]))
print("But u can call me: %s" % dictionary_tk["nickname"])
print("Am a:%s" % dictionary_tk["Nationality"],dictionary_tk["age"])
print("Am :%s" % dictionary_tk["age"] + " years old")
dictionary_tk['tribe'] = "Munyoro"
print(dictionary_tk)

#looping in a list
bookshelf = ["The Effective Engineer","The 4 hours work week", "Zero to One", "Lean Startup","Hooked"]
for book in bookshelf:
    print(book)
book = 1
while book <= 10:
    print(book)
    book += 1