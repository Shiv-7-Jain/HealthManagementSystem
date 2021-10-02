def select_feature():
    print("Press 'D' to open your Diet File")
    print("Press 'E' to open your Exercise File")
    choice_ = input("Enter your choice : ")
    if choice_.lower() == "d":
        return "diet"
    else:
        return "exercise"


def select_mode():
    print("Press 'W' to write in the file")
    print("Press 'R' for reading the file")
    mode_ =  input("Enter your choice : ")
    if mode_.lower() == "w":
        return "a"
    else:
        return "r"


def getdate():
    import datetime
    return datetime.datetime.now()


print("Welcome to the Health Management System...")
print("Press 'G' for Gavi")
print("Press 'P' for Pragti")
print("Press 'S' for Shiv")
name = input("Select your name : ")
if name.lower() == "g":
    name_ = "Gavi_"
elif name.lower() == "p":
    name_ = "Pragti_"
else:
    name_ = "Shiv_"
choice = select_feature()
mode = select_mode()
if mode == "a":
    with open(name_ + choice + ".txt", mode) as file:
        time_ = getdate()
        file.write(f"[{time_}]\t")
        if choice == "diet":
            file.write(input("Enter your Diet : "))
        else:
            file.write(input("Enter your Exercise : "))
        file.write("\n")
else:
    with open(name_ + choice + ".txt", mode) as file:
        print(file.read())



