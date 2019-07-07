import vpython
from vpython import *

'''
sphere_ = sphere(pos=vector(0,0,0),radius=0.25, color=color.green)
theThing = gcurve(color=color.blue)
t = 0 
dt = 0.1

while t < 20 :
    sphere_.pos.x = 1.0*t - 10
    t = t + dt
    rate(30)
    theThing.plot((t,sphere_.pos.x))
    '''
#my_curve = gcurve(color = color.red)
floor = box(pos=vector(0,0,0), length = 4, height = 0.5, width = 4, color = color.blue)
ball = sphere(pos=vector(0,10,0),radius=1,color=color.red)
ball.velocity = vector(0,-1,0)
dt = 0.01

while 1:
    rate (100)
    ball.pos = ball.pos + ball.velocity*dt
    if ball.pos.y < ball.radius:
        ball.velocity.y = abs(ball.velocity.y)
    else:
        ball.velocity.y = ball.velocity.y - 9.8*dt
   # my_curve.plot(pos=(ball.pos.y))