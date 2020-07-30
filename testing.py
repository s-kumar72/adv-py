apple = "a"
ball = "b"
cat = "c"
dog = "d"
elephant = "e"

list = [apple, ball, cat]
list.append(dog)
list.append(elephant)

list_1 = ["apple", "ball"]
list_1 = list_1 + list

print (list_1) #should print ["apple", "ball", "a", "b", "c", "d", "e"]
