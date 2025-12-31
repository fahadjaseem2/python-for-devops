def read_logs():
    file = open("app.log")
    print(file.readlines())
    file.close()

read_logs() 