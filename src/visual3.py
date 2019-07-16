import vpython
from vpython import *

print('-' * 50)
print("물체의 낙하운동에서 물체의 반발 거리를 구한다")
print('-' * 50)
print('중력가속도 = 9.8m/s^2')
print('높이 단위 = m')
print('질량 단위 = kg')
print('-' * 50)
print('아래에 값을 입력하세요!')
h = int(input("물체의 높이 = "))
e = float(input("적용할 반발계수 = "))
m = int(input("물체의 질량 = "))
print('-' * 50)
print('중력가속도 = 10m/s^2')
print('높이 단위 = m')
print('질량 단위 = kg')
print('물체의 높이 = ' + str(h))
print('지면과의 반발계수 = ' + str(e))
print('물체의 질량 = ' + str(m))
print('-' * 50)


floor = box(pos=vector(0, -1, 0), length=4, height=0.5, width=4, color=color.blue)
ball = sphere(pos=vector(0, h, 0), radius=1, color=color.white)
ball.velocity = vector(0, -1, 0)
dt = 0.01
ball.mass = m
gd = graph(width=1500, height=300, x=60, y=0, title='height, time', xtitle='time', ytitle='height', ymax=20, ymin=-1,
           xmax=10)
gd2 = graph(width=1500, height=300, x=60, y=250, title='velocity, time', xtitle='time', ytitle='velocity', ymax=20,
            ymin=-20, xmax=10)
gd3 = graph(width=1500, height=300, x=60, y=400, title='accelerate vs time', xtitle='time', ytitle='accelerate',
            ymax=15, ymin=-15, xmax=10)

xt = gcurve(graph=gd, color=color.cyan)
vt = gcurve(graph=gd2, color=color.cyan)
at = gcurve(graph=gd3, color=color.cyan)

vel_arrow = arrow(pos=ball.pos, axis=ball.velocity, color=color.yellow)

t = 0
dt = 0.01
g = 9.8

label1 = label()
label2 = label()

if __name__ == '__main__':

    while True:
        rate(100)  # rate * dt = 1

        t += dt

        ball.pos = ball.pos + ball.velocity * dt

        if ball.pos.y <= 0:

            ball.velocity.y = abs(ball.velocity.y*(e))

        else:
            ball.velocity.y = (ball.velocity.y - 9.8 * dt)

        label1.pos = floor.pos + vector(0, -1.8, 0)
        label1.text = 'time : %.2f s' % t

        label2.poss = floor.pos + vector(0, -3.5, 0)
        label2.text = 'vel : %.2f m/s' % ball.velocity.y

        vel_arrow.pos = ball.pos
        vel_arrow.axis = ball.velocity * 0.3

        xt.plot(pos=(t, ball.pos.y))
        vt.plot(pos=(t, ball.velocity.y))
        at.plot(pos=(t, g))





