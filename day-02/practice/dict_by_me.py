info = {
    "name" : "Fahad",
    "City" : "Gurgaon",
    "Pincode" : 122002,
    "married" : False,
    "skills" : ["linux", "python", "git", "docker"],
    "Salary" : 22.9 
}
# print (info["name"])
# print ("My name is: ", info["name"])

# print ("I live in : ", info["City"])
# print ("my pincode is: ", info.get("pincode", "Not Found"))

for key,value in info.items():
    print(key,value)