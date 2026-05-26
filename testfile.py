def write_log(message):
    with open(r"C:\Users\evans\app.log", "a") as file:
        file.write(message + "\n")

write_log("App Started")
write_log("User logged in")
write_log("App Stopped")
