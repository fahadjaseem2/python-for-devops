import requests

api_url = "https://jsonplaceholder.typicode.com/todos/1"

response = requests.get(url=api_url)

# # 1st example to check API status
# # if response == 200:
# #     print("API is reachable")
# # else:
# #     print ("API is not reachable")


# # 2nd example to print response details
# # print (dir(response))
# # print(response.json())
# # print(type(response.json()))

# # for key,value in response.json().items():
# #     print(key,value)


# # 3rd example to check specific userId
# # for key,value in response.json().items():
# #     if key == "userId":
# #         print("user id is : ", value)
# #     else:
# #           exit() 
       
for key,value in response.json().items():
    if key == "userId":
        if value in [100,200,300]:
            print("User found")
    else:
        print("User not found")
        exit()



