import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

def fetch_data():
    response = requests.get(url=api_url)
    if response.status_code == 200:
        return response.json()
        
    else:
        print("Failed to retrive data")
        return[]
    
def process_complete_todos(data):
    complete_todos = []
    for item in data:
        if item.get("completed") == True:
            print(
                f"ID: {item['id']} | "
                f"Title: {item['title']} | "
                f"Status: {item['completed']}"
            )

            complete_todos.append({
                "ID": item["id"],
                "Title": item["title"],
                "Status": item["completed"]
                })
            
    return complete_todos

def save_to_json(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print ("f\n data saved to: {filename}")

def main():
    data = fetch_data()
    complete_todos = process_complete_todos(data)
    save_to_json("completed_todos.json", complete_todos)

main()
   
