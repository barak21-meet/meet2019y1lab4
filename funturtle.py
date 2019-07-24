import turtle
turtle.shape('turtle')
finn=turtle.clone()
finn.shape('square')
finn.goto(100,0)
finn.goto(100,100)
finn.goto(0,100)
finn.goto(0,0)

charlie=turtle.clone()
charlie.shape('triangle')
charlie.goto(200,0)
charlie.goto(100,100)
charlie.goto(0,0)

finn.goto(400,400)
finn.stamp()
finn.goto(150,150)
finn.stamp()
finn.goto(400,150)
finn.clearstamps()



turtle.mainloop()
