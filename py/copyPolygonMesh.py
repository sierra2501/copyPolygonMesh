def checkDirection(dir, dis):
    if dir is 1:
        loc = (dis,0,0,1)
    elif dir is 2:
        loc = (0,dis,0,1)
    elif dir is 3:
        loc = (0,0,dis,1)
    else:
        loc = (0,0,0,1)
    
    return loc

def main():

    # 繰り返しの回数
    num = TARGET_NUM

    # 並べる方向
    # RIGHT or LEFT or TOP or BOTTOM or FRONT or BACK
    direction = TARGET_DIRECTION

    # 移動距離
    distance = TARGET_DISTANCE

    location = checkDirection(direction, distance)

    for i in range(num):

        xshade.scene().active_shape().copy_object(((1,0,0,0),(0,1,0,0),(0,0,1,0),location))
        xshade.scene().active_shape().bro.select()

main()