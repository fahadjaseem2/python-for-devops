# a = [100, 200, 300]
# #print (type(a))
# a.append(400)
# #print(a)

clouds = list()

# print (type(clouds))

clouds.append("AWS")
clouds.append("Azure")
clouds.append("GCP")
clouds.append("Alibaba Cloud")
clouds.append("IBM")


# print(clouds[2])
# print("lenth of clouds is;", len(clouds))
# print("World best cloud service provider is:", clouds[0])
# clouds.remove("IBM")
# clouds.append("IBM")
# print(clouds)
# print(clouds[-1])

# print(dir(clouds))
# print(clouds.append.__doc__)

# print(clouds.pop.__doc__)


for cloud in clouds:
    if cloud == "AWS":
        print(f"{cloud} world leading cloud service provider")
    elif cloud == "Azure":
        print(f"{cloud} 2nd best cloud service provider")
    elif cloud == "GCP":
        print(f"{cloud} 3rd best cloud service provider")
    elif cloud == "IBM":
        print(f"{cloud} 5th best cloud service provider")
    else:
        print(f"{cloud} cloud service provider is based in China")