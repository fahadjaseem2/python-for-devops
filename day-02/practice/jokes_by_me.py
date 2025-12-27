# import requests

# jokes_url = "https://official-joke-api.appspot.com/random_joke" # API URL for random jokes
# dad_jokes_url ="https://icanhazdadjoke.com/" # API URL for dad jokes


# def get_jokes():
#     response = requests.get(url=jokes_url)
#     final_joke = response.json()["setup"] + response.json()["punchline"]   # Concatenate setup and punchline
#    # print(final_joke)
#     return final_joke # Return the joke instead of printing it directly


# final_joke = get_jokes() #  Call the function and store the returned joke

import requests

pj_url = "https://official-joke-api.appspot.com/random_joke" 
dad_jokes_url = "https://icanhazdadjoke.com/"


def get_joke(url_type,mood):
    # headers = {
    #     "Accept": "application/json"
    # }
    response = requests.get(url=url_type,headers={"Accept": "application/json"})
    if mood == "dad":
        final_joke = response.json()["joke"]

    if mood == "pj":
        final_joke = response.json()["setup"] + "..." + response.json()["punchline"]

    return final_joke

mood = input("which joke would you like to read? (pj or dad)")
if mood == "dad":
    url_type = dad_jokes_url
elif mood == "pj":
    url_type = pj_url
else:
    mood = input("please enter a valid mood (pj or dad)")

final_joke = get_joke(url_type,mood)
print(final_joke)
