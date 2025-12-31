import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

incomplete_todos = []

def fetch_data():
    response = requests.get(url=api_url)
    if response.status_code == 200:
        data = response.json()

    for item in data:
        if item.get("completed") == False:
            print(
                f"ID: {item['id']} | "
                f"Title: {item['title']} | "
                f"Status: {item['completed']} "

            )

            incomplete_todos.append({
                "ID" : item["id"],
                "Title" : item["title"],
                "Status" : item["completed"]
            
            })
    
    with open("incompleted_todo.json", "w") as file:
        json.dump(incomplete_todos, file, indent=4)
    print("\nIncomplete todos saved to incomplete_todos.json")

fetch_data()