email = input("What is your email address? ")
org = [".com", ".org", ".net"]

if len(email) > 254:
    print("Too Long")
elif len(email) == 0:
    print("Too Short")
else:
    if "." in email and  "@" in email:
        if email.count('@') > 1:
            print("Invalid email address too many @'s")
        else:
            if email contains item in org:




