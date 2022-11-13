print("if you have account log in if you dont have account sign in")
a = input("sign in or log in:")
if a == "sign in":
    name = input("username:")
    password = input("password:")
    age = input("age:")
    print("hello",name)
elif a == "log in":
    name = input("username:")
    password = input("password:")
    print("welcome back",name)