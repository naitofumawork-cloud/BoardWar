
import random
def moveposition(playerposition:tuple,direction:str,clampedposition:tuple):#プレイヤーの座標、移動方向、移動限界座標
    #プレイヤーの座標を更新する関数
    posx,posy=playerposition
    uplimit,leftlimit,downlimit,rightlimit=clampedposition
    match direction:
        
        case "up":
            print("posy"+str(posy)+"uplimit"+str(uplimit))
            if posy>uplimit:
                posy-=1
                print("up")
                print(posy)
        case "left":
            print("posx"+str(posx)+"leftlimit"+str(leftlimit))
            if posx>leftlimit:
                posx-=1
                print("left")
        case "down":
            if posy<downlimit:
                posy+=1
                print("down")
        case "right":
            if posx<rightlimit:
                posx+=1
                print("right")
    returnplayerposition=(posx,posy)
    return returnplayerposition

def randomposreturn(area,objectlist):#出される座標の範囲
    #画面内のどのレクトとも干渉しないランダムな座標を返す関数
    is_ok=False
    #areaのイメージarea=((100,500),(500,900))横の範囲100~500縦の範囲500~900
    #areaの分解
    range_x,range_y=area
    min_x,max_x=range_x
    min_y,max_y=range_y
    while is_ok:
        #ランダムな値の選出
        pos_x=random.randint(min_x,max_x)
        #現在のオブジェクトリストを渡してその中のx座標がかぶっている
        """
        現在のオブジェクトリストの座標プロパティを取得
        d
        """
        