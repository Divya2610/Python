print("Welcome to the rollercoaster !")
heigth = int(input("What is your height in cm? "))
if heigth>=120:
    print("You can ride the rollercoster !")
    age=int(input("What is your age?"))
    if age < 12:
            bill = 5
            print("child tickets are 100.")
    elif age<=18:
            bill = 7  
            print("Youth tickets are 120.")
    else:
            bill = 12
            print("Adult ticktes are 180.")

    wants_photo=(input("Do you want a photo taken? Y or N."))
    if wants_photo=="Y":
            bill += 3
            print(f"Your final bill is Rs{bill}")
else:
    print("sorry,you have to grow taller before you can ride the rollercoster !")