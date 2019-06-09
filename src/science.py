import math
from matplotlib import pyplot as plt

if __name__ == '__main__':
    print('-'*50)
    print("물체의 낙하운동에서 물체의 반발 거리를 구한다")
    print('-'*50)
    print('중력가속도 = 10m/s^2')
    print('높이 단위 = m')
    print('질량 단위 = kg')
    print('-'*50)
    print('아래에 값을 입력하세요!')
    h = int(input("물체의 높이 = "))
    e = float(input("적용할 반발계수 = "))
    m = int(input("물체의 질량 = "))
    print('-'*50)
    print('중력가속도 = 10m/s^2')
    print('높이 단위 = m')
    print('질량 단위 = kg')
    print('물체의 높이 = '+ str(h))
    print('지면과의 반발계수 = '+ str(e))
    print('물체의 질량 = '+str(m))
    print('-'*50)
    E_array = []

    t = math.sqrt((2 * h)/10 )
    E = int(( m * 10 ) * h)
    E_array.append(E)
    print("물체가 0m에 도달하는데 걸리는 시간 = "+str(t) + "s")
    print("물체의 역학적에너지의 총 합 = "+ str(E)+"J")
    cnt = 1
    while(True):
        E_array.append( int((e*e) * E))
        E = int((e*e) * E)
        cnt +=1
        if(E <= 0.001):
            break
    print(E_array)
    for i in E_array:
        print(str(i)+"J")
    Ex = [a for a in range(cnt)]
    print(Ex)
    plt.stackplot(Ex,E_array)
    plt.ylabel("Energy(J)")
    plt.title("Energy-graph")

    plt.grid(True)
    plt.show()
#    print("지면과 충돌 후 역학적 에너지 = "+str(E2)+"J")
    
#    print("2차 높이 :"+ str((E2/(m * 10))))