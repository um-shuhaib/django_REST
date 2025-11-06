import json

# dump - py to json
# load - json to py


f=open("posts.json","r")
# print(f.read())
# print(type(f.read())) #str
data=json.load(f)
# print(data)
# print(type(data)) #list
# p = 0
# for i in data:
#     if i["userId"] == 1:
#         p+=1
# print(p)

# count=[i for i in data if i["userId"] == 1]
# print(len(count))

# post=[i for i in data if i["postId"] == 1]
# print(post)

for i in data:
    if i["postId"] == 3:
        print(len(i["liked_by"]))

likes = [len(i["liked_by"]) for i in data if i["postId"] == 3]
print(likes)