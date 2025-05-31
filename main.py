import turtle

sc = turtle.Screen()
sc.setup(width=600, height=400)
sc.bgcolor("cyan")
t = turtle.Turtle()

expression = turtle.textinput("expression", "expression")
calculate = turtle.textinput("calculate(y,n)","calculate")




t.clear()
t.write("no more free tryal", font=("Arial", 30, "normal"))