import vpython
from vpython import *



floor = box(pos=vector(0,-1 ,0), length = 4, height = 0.5, width = 4, color = color.blue)
ball = sphere(pos=vector(0,10,0),radius=1,color=color.white)
ball.velocity = vector(0,-1,0)
dt = 0.01


gd = graph(width=500, height=300, x=610, y=0, title='y vs t', xtitle='t', ytitle='x', ymax=20, ymin=-1, xmax=10)
gd2 = graph(width=500, height=300, x=610, y=250, title='v vs t', xtitle='t', ytitle='vel', ymax=20, ymin=-20, xmax=10)
gd3 = graph(width=500, height=300, x=610, y=400, title='a vs t', xtitle='t', ytitle='acc', ymax=10, ymin=-10, xmax=10)

xt = gcurve(graph=gd, color=color.cyan)
vt = gcurve(graph=gd2, color=color.cyan)
at = gcurve(graph=gd3, color=color.cyan)




vel_arrow=arrow(pos=ball.pos, axis=ball.velocity, color = color.yellow)

t = 0
dt = 0.01
g = 9.8

label1 = label()
label2 = label()

if __name__ == '__main__':
    while True:
        rate(100) # rate * dt = 1

        t += dt

        ball.pos = ball.pos + ball.velocity*dt

        if ball.pos.y <= 0:
            ball.velocity.y =abs(ball.velocity.y)
        else :
            ball.velocity.y = ball.velocity.y - 9.8*dt

        label1.pos = floor.pos + vector(0,-1.8,0)
        label1.text = 'time : %.2f s' % t
        label2.pos = floor.pos + vector(0,-3.5,0)
        label2.text = 'vel : %.2f m/s' % ball.velocity.y

        vel_arrow.pos = ball.pos
        vel_arrow.axis = ball.velocity*0.3

        xt.plot(pos=(t, ball.pos.y))
        vt.plot(pos=(t,ball.velocity.y))
        at.plot(pos=(t,g))
 




