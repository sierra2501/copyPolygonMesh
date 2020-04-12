def checkDirection(dir, dis):
    if dir is "RIGHT":
        loc = (dis,0,0,1)
    elif dir is "LEFT":
        loc = (-1*dis,0,0,1)
    elif dir is "TOP":
        loc = (0,dis,0,1)
    elif dir is "BOTTOM":
        loc = (0,-1*dis,0,1)
    elif dir is "FRONT":
        loc = (0,0,dis,1)
    elif dir is "BACK":
        loc = (0,0,-1*dis,1)
    else:
        loc = (0,0,0,1)
    
    return loc

def main():

    # 繰り返しの回数
    num = 10

    # 並べる方向
    # RIGHT or LEFT or TOP or BOTTOM or FRONT or BACK
    direction = "RIGHT"

    # 移動距離
    distance = 100

    location = checkDirection(direction, distance)

    for i in range(num):

        xshade.scene().active_shape().copy_object(((1,0,0,0),(0,1,0,0),(0,0,1,0),location))
        xshade.scene().active_shape().bro.select()

main()