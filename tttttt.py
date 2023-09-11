import socket
import time
import math

# 닉네임을 사용자에 맞게 변경해 주세요.
NICKNAME = 'A0004_1041475'

# 일타싸피 프로그램을 로컬에서 실행할 경우 변경하지 않습니다.
HOST = '127.0.0.1'

# 일타싸피 프로그램과 통신할 때 사용하는 코드값으로 변경하지 않습니다.
PORT = 1447
CODE_SEND = 9901
CODE_REQUEST = 9902
SIGNAL_ORDER = 9908
SIGNAL_CLOSE = 9909


# 게임 환경에 대한 상수입니다.
TABLE_WIDTH = 254
TABLE_HEIGHT = 127
NUMBER_OF_BALLS = 6
HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]

order = 0
balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]

sock = socket.socket()
print('Trying to Connect: %s:%d' % (HOST, PORT))
sock.connect((HOST, PORT))
print('Connected: %s:%d' % (HOST, PORT))

send_data = '%d/%s' % (CODE_SEND, NICKNAME)
sock.send(send_data.encode('utf-8'))
print('Ready to play!\n--------------------')


while True:

    # Receive Data
    recv_data = (sock.recv(1024)).decode()
    print('Data Received: %s' % recv_data)

    # Read Game Data
    split_data = recv_data.split('/')
    idx = 0
    try:
        for i in range(NUMBER_OF_BALLS):
            for j in range(2):
                balls[i][j] = float(split_data[idx])
                idx += 1
    except:
        send_data = '%d/%s' % (CODE_REQUEST, NICKNAME)
        print("Received Data has been currupted, Resend Requested.")
        continue

    # Check Signal for Player Order or Close Connection
    if balls[0][0] == SIGNAL_ORDER:
        order = int(balls[0][1])
        print('\n* You will be the %s player. *\n' % ('first' if order == 1 else 'second'))
        continue
    elif balls[0][0] == SIGNAL_CLOSE:
        break

    # Show Balls' Position
    print('====== Arrays ======')
    for i in range(NUMBER_OF_BALLS):
        print('Ball %d: %f, %f' % (i, balls[i][0], balls[i][1]))
    print('====================')

    angle = 0.0
    power = 0.0

    ##############################
    # 이 위는 일타싸피와 통신하여 데이터를 주고 받기 위해 작성된 부분이므로 수정하면 안됩니다.
    #
    # 모든 수신값은 변수, 배열에서 확인할 수 있습니다.
    #   - order: 1인 경우 선공, 2인 경우 후공을 의미
    #   - balls[][]: 일타싸피 정보를 수신해서 각 공의 좌표를 배열로 저장
    #     예) balls[0][0]: 흰 공의 X좌표
    #         balls[0][1]: 흰 공의 Y좌표
    #         balls[1][0]: 1번 공의 X좌표
    #         balls[4][0]: 4번 공의 X좌표
    #         balls[5][0]: 마지막 번호(8번) 공의 X좌표

    # 여기서부터 코드를 작성하세요.
    # 아래에 있는 것은 샘플로 작성된 코드이므로 자유롭게 변경할 수 있습니다.
    def calcul_dist(sx, sy, ex, ey):
        return (math.sqrt((sx-ex)**2 + (sy-ey)**2))

    def no_obstacle(i, sx, sy, ex, ey): 
        # 1.타겟볼과 흰공 사이에 다른 공이 있다면 return False
            # 1.타겟볼과 hole 사에에 다른 공이 있다면 return False
        # 2.타겟볼과 흰공 사이에 아무 공도 없다면 return True
            # 2. 타겟볼과 hole 사이에 아무 공도 없다면 return True
        # 나 빼고 다른 볼들을 알기 위해서 
        otherballs = [j for j in range(NUMBER_OF_BALLS) if not visited[j] and not j]

        # 직선과 점 사이의 공식으로 장애물 판단
        slope = sy - sx /sx - ex  if sx - ex > 0 else 0 # 기울기는 세로변화량/가로변화량
        intercept = sy - (slope * sx)# y = ax + b => b = y - ax 절편 구하기

        for k in otherballs:
            rx = balls[k][0]
            ry = balls[k][1]
            # 직선과 점 사이의 거리
            dist = abs(slope*rx - ry + intercept) / math.sqrt((slope ** 2) + 1)
            if sy - ey > 0 and ry > ey:
                 if dist < r * 2:
                    return False
            if sy - ey < 0 and ry < ey:
            # 만약 거리가 반지름 * 2 보다 작다면 장애물임
                if dist < r * 2:
                    return False
        return True # 위 for문에 하나도 걸리지 않았다면 장애물이 없는 것임

    def valid_hole(idx, tx, ty, hx, hy, wx, wy): #둔각삼각형 여부를 체크 하는 함수, 만약 유망하다면 true 반환
        # whiteball ~ hole의 거리 == whiteball ~ targetball거리 + targetball ~ hall 거리
        # 위의 경우 일직선인 경우이므로 바로 return
        wtoh = math.sqrt((wx -hx)**2 + (wy-hy)**2)
        wtot = math.sqrt((wx -tx)**2 + (wy-ty)**2)
        ttoh = math.sqrt((tx -hx)**2 + (ty-hy)**2)
        if wtoh == wtot + ttoh: # whiteball ~ hole의 거리 == whiteball ~ targetball거리 + targetball ~ hall 거리
            return True # 위의 경우 일직선인 경우이므로 바로 return
        if wtoh ** 2 <= wtot ** 2 + ttoh ** 2:  # 만약에 예각 삼각형이거나 직각삼각형이면 안됨
            return False
        else:
            return True
    
    #HOLES = [[0, 0], [127, 0], [254, 0], [0, 127], [127, 127], [254, 127]]   
    def padding_hole(hx, hy):
        if hx == 0 and hy == 0:
            return hx + 2, hy + 2
        elif hx == 127 and hy == 0:
            return hx, hy
        elif hx == 254 and hy == 0:
            return hx - 2, hy + 2
        elif hx == 0 and hy == 127:
            return hx + 2, hy - 2
        elif hx == 127 and hy == 127:
            return hx, hy
        elif hx == 254 and hy == 127:
            return hx - 2, hy - 2
        
    r = 5.73
    visited = [False] * 6
    # whiteBall_x, whiteBall_y: 흰 공의 X, Y좌표를 나타내기 위해 사용한 변수
    whiteBall_x = balls[0][0]
    whiteBall_y = balls[0][1]
    visited[0] = True

    
    if order == 1:
        target = [1, 3, 5]
        rival = [2, 4, 5]
    else:
        target = [2, 4, 5]
        rival = [1, 3, 5]
    
    
    targetballs = []
    rivalballs= []
    for i in range(NUMBER_OF_BALLS):
        if balls[i][0] == -1.000000: # 만약에 공이 없다면 
            visited[i] = True
        else:
            if i == 5:
                targetballs.append((i, balls[i][0], balls[i][1]))
                rivalballs.append((i, balls[i][0], balls[i][1]))
            elif i in target:
                targetballs.append((i, balls[i][0], balls[i][1]))
            else:
                rivalballs.append((i, balls[i][0], balls[i][1]))
    
    # 먄약에 검은 공이 아직 들어간 상태가 아니라면
    # 내 타겟볼을 우선적으로 쳐야함

    # if not visited[5]:
    for i, tx, ty in targetballs:
        # 만약에 내 타겟볼과 whiteball 사이에 장애물 없다면 타겟을 바꾸기
        if not visited[i] and no_obstacle(i, tx, ty, whiteBall_x , whiteBall_x):
            f_target_x = tx
            f_target_y = ty
            break
    else:
        # 만약 내 모든 타겟볼과 whiteball 사이에 장애물이 있다면
        for i, tx, ty in targetballs:
            # 그냥 내 타겟볼들 중에 아무거나 고르기
            if not visited[i]:
                idx = i
                f_target_x = tx
                f_target_y = ty
    
    # HOLE 선택하기
    valid_holes = []
    for hx, hy in HOLES:
        # 만약 유망한 hole이고, hole~target 사이에 장애물이 없으면 유망한 hole이다
        if valid_hole(idx, f_target_x, f_target_y, hx, hy, whiteBall_x, whiteBall_y):
            #타겟볼과 hole 사이에 아무 공도 없다면 return diff
            if no_obstacle(idx, f_target_x, f_target_y, hx, hy):
                diff = math.sqrt((f_target_x - hx) ** 2 + (f_target_y - hy) ** 2)
                valid_holes.append((hx, hy, diff))           

    # 차이가 가장큰(= 가장 가까운 큰 구멍 고르기)
    if valid_holes:
        valid_holes.sort(key= lambda x : x[2])
        for hx, hy, diff in valid_holes:
            if calcul_dist(tx, ty, hx, hy) > 2 * r:
                print("dist", calcul_dist(tx, ty, hx, hy))
                f_hole_x, f_hole_y = padding_hole(hx, hy)
            else:
                print("dist", calcul_dist(tx, ty, hx, hy))
                f_hole_x, f_hole_y = hx, hy
        
    else: # 만약에 유망한 hole이 하나도 없다면
        # 일단 가까운데 고르기
        random_holes = []
        for hx, hy in HOLES:
            diff = math.sqrt((f_target_x - hx) ** 2 + (f_target_y - hy) ** 2)
            random_holes.append((hx, hy, diff))
        
        random_holes = valid_holes.sort(key= lambda x : x[2])
        
        for hx, hy, diff in random_holes:
            if calcul_dist(tx, ty, hx, hy) > 2 * r:
                print("dist", calcul_dist(tx, ty, hx, hy))
                f_hole_x, f_hole_y = padding_hole(hx, hy)
            else:
                print("dist", calcul_dist(tx, ty, hx, hy))
                f_hole_x, f_hole_y = hx, hy

    
    print('chosedhole', f_hole_x, f_hole_y)
    w1 = abs(f_hole_x - f_target_x)
    h1 = abs(f_hole_y - f_target_y)
    theta1 = math.atan(w1 / h1) if h1 > 0 else 0##############????
    theta2= 90 - (180 / math.pi * theta1)
    # w2 =  2 * r * math.cos(theta2)
    # h2 =  2 * r * math.sin(theta2)
    w2 =  r * math.cos(theta2)
    h2 =  r * math.sin(theta2)

    
    if f_target_x > whiteBall_x and f_target_y > whiteBall_y: #wb기준 타겟볼이 1사분면
        hit_x = f_target_x - w2
        hit_y = f_target_y - h2
        width = abs(hit_x - whiteBall_x)
        height = abs(hit_y - whiteBall_y)
        radian = math.atan(width / height) if height > 0 else 0
        angle = 180 / math.pi * radian 
         # 만약 w ~ h 기울기 > w ~ t 이면 가중치
        if abs((whiteBall_y-f_hole_y) /(whiteBall_x-f_hole_x)) > abs((f_target_y-whiteBall_y) /(f_target_x-whiteBall_x)):
            angle += 1
        else:
            angle -= 1

    elif  f_target_x > whiteBall_x and f_target_y < whiteBall_y:
        hit_x = f_target_x - w2
        hit_y = f_target_y + h2
        width = abs(hit_x - whiteBall_x)
        height = abs(hit_y - whiteBall_y)
        radian = math.atan(width / height)  if height > 0 else 0
        angle = 90 + (90 - 180 / math.pi * radian)
        # 만약 w ~ h 기울기 > w ~ t 이면 가중치
        if abs((whiteBall_y-f_hole_y) /(whiteBall_x-f_hole_x)) > abs((f_target_y-whiteBall_y) /(f_target_x-whiteBall_x)):
            angle -= 1
        else:
            angle += 1
    elif  f_target_x < whiteBall_x and f_target_y < whiteBall_y: #
        hit_x = f_target_x + w2
        hit_y = f_target_y + h2
        width = abs(hit_x - whiteBall_x)
        height = abs(hit_y - whiteBall_y)
        radian = math.atan(width / height) if height > 0 else 0
        angle = 180 + 180 / math.pi * radian
        if abs((whiteBall_y-f_hole_y) /(whiteBall_x-f_hole_x)) > abs((f_target_y-whiteBall_y) /(f_target_x-whiteBall_x)):
            angle += 1
        else:
            angle -= 1
    
    elif  f_target_x < whiteBall_x and f_target_y > whiteBall_y: # 2사분면
        hit_x = f_target_x + w2
        hit_y = f_target_y - h2
        width = abs(hit_x - whiteBall_x)
        height = abs(hit_y - whiteBall_y)
        radian = math.atan(width / height) if height > 0 else 0
        angle = 270 + (90 -  180 / math.pi * radian)
        if abs((whiteBall_y-f_hole_y) /(whiteBall_x-f_hole_x)) > abs((f_target_y-whiteBall_y) /(f_target_x-whiteBall_x)):
            angle += 1
        else:
            angle -= 1
    
    elif whiteBall_x == f_target_x:
        if whiteBall_y < f_target_y:
            angle = 1
            hit_x = f_target_y
            hit_y = f_target_x
        else:
            hit_x = f_target_y
            hit_y = f_target_x
            angle = 181
    elif whiteBall_y == f_target_y:
        if whiteBall_x < f_target_x:
            hit_x = f_target_y
            hit_y = f_target_x
            angle = 91
        else:
            hit_x = f_target_y
            hit_y = f_target_x
            angle = 271

    width = abs(whiteBall_x - hit_x)
    height = abs(whiteBall_x - hit_y)       
    # distance: 두 점(좌표) 사이의 거리를 계산
    distance = math.sqrt(width**2 + height**2)

    # power: 거리 distance에 따른 힘의 세기를 계산
    power = distance * 0.7


    # 주어진 데이터(공의 좌표)를 활용하여 두 개의 값을 최종 결정하고 나면,
    # 나머지 코드에서 일타싸피로 값을 보내 자동으로 플레이를 진행하게 합니다.
    #   - angle: 흰 공을 때려서 보낼 방향(각도)
    #   - power: 흰 공을 때릴 힘의 세기
    # 
    # 이 때 주의할 점은 power는 100을 초과할 수 없으며,
    # power = 0인 경우 힘이 제로(0)이므로 아무런 반응이 나타나지 않습니다.
    #
    # 아래는 일타싸피와 통신하는 나머지 부분이므로 수정하면 안됩니다.
    ##############################


    merged_data = '%f/%f/' % (angle, power)
    sock.send(merged_data.encode('utf-8'))
    print('Data Sent: %s' % merged_data)

sock.close()
print('Connection Closed.\n--------------------')