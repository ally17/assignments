age =  int(input("Enter your age: ")) >= 75
chronic = input("Do you have any chronic disease? ").lower() == "yes"
immune =  input("Is your immune system too weak? ").lower() == "yes"

if age or chronic or immune:
    print("You are in risky group")
else:
    print("You are not in risky group")
    
# this is my second assignment and I push it to GitHub from VsCode