import turtle

sc = turtle.Screen()
sc.setup(width=600, height=400)
sc.bgcolor("cyan")
t = turtle.Turtle()

firstnumber = turtle.textinput("First Number", "first number")

operation = turtle.textinput("operation", "multiply*, divide/, subtract-, add +")

secondnumber = turtle.textinput("second number", "second number")

if "+" in operation:
    answer = float(firstnumber) + float(secondnumber)
    print(answer)
    t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
    
if "-" in operation:
    answer = float(firstnumber) - float(secondnumber)
    print(answer)
    t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
if "*" in operation:
    answer = float(firstnumber) * float(secondnumber)
    print(answer)
    t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
if "/" in operation:
    answer = float(firstnumber) / float(secondnumber)
    print(answer)
    t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
secondcalculation = turtle.textinput("would you like to go again", "would you like to go again")

if "yes" in secondcalculation:
    t.clear()
    firstnumber = turtle.textinput("First Number", "first number")

    operation = turtle.textinput("operation", "multiply*, divide/, subtract-, add +")

    secondnumber = turtle.textinput("second number", "second number")

    if "+" in operation:
        answer = float(firstnumber) + float(secondnumber)
        print(answer)
        t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
    
    if "-" in operation:
        answer = float(firstnumber) - float(secondnumber)
        print(answer)
        t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
    if "*" in operation:
        answer = float(firstnumber) * float(secondnumber)
        print(answer)
        t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    
    if "/" in operation:
        answer = float(firstnumber) / float(secondnumber)
        print(answer)
        t.write("answer: " + str(answer), font=("Arial", 30, "normal"))
    t.clear()
    t.write("no more free tryal", font=("Arial", 30, "normal"))
    
    
