import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Bouncing Ball Simulator")
wn.tracer(0)

balls = []

for _ in range(20):
	balls.append(turtle.Turtle())


#colors = ["red", "blue", "orange", "yellow", "green", "white", "purple"]
#shapes = ["circle", "triangle", "square"]

for ball in balls:

	#ball.shape(random.choice(shapes))
	#ball.color(random.choice(colors))
	ball.color("green")
	ball.shape("circle")
	ball.penup()
	ball.speed(0)
	ball.goto(random.randint(-470, 460),random.randint(0,400))
	ball.dy = 0 #Delta y. Velocidade a que a bola varia a sua velocidade de movimentacao no eixo y.
	ball.dx = random.randint(-2, 2)
	ball.da = random.randint(-2,2)

gravity = 0.01


while True:

	wn.update()

	for ball in balls:

		ball.rt(ball.da)

		ball.dy -= gravity
		
		ball.sety(ball.ycor() + ball.dy)

		ball.setx(ball.xcor() + ball.dx)


		#Check for right wall colision
		if ball.xcor() > 460:
			ball.dx *= -1
			ball.da *= -1

		#Check for left wall colision
		if ball.xcor() < -470:

			ball.dx *= -1
			ball.da *= -1


		#Check for ground colision
		if ball.ycor() < -390:
			ball.sety(-390) #Para nao ficarem presas no fim da janela
			ball.dy *= -1


wn.mainloop()