class Unit:
    def __init__(self,):
        self.hp=10
        self.atk=4
        self.id=0
        #呼び出しのときに引数として今の状態
        #どこに誰がいるか？を持った方が　○○がいるときに出ると○○が作れる
        #それと一意にしたいから出されたユニットインスタンスはすべてリストに入れて
        #リストに入ったやつのidは必ず被らないように調整されてゲームごとに割り振られるべき
        #これで何番か？が分かる
class Board:
    def __init__(self,x,y):#引数で縦横長を受け取る
        self.x=x
        self.y=y
        self.grid=[[0 for j in range(x)] for i in range(y)]
        
    def gridinit(self,):
        self.grid=[]

    def showgrid(self,):
        print(self.grid)
        #配列を走査して中にユニットがいればokいないとNoを出すようにする
        for x in range(self.x):
            for y in range(self.y):
                if type(self.grid[x-1][y-1])==Unit:
                    print(str(x+1)+"行目の"+str(y+1)+"列目はUnit")
                else:
                    print(str(x+1)+"行目の"+str(y+1)+"列目はUnitじゃない")
                    
            
    def putunit(self,unit,x,y):
        self.grid[x-1][y-1]=unit
def main():
    board=Board(3,2)
    board.showgrid()
    
    unitA=Unit()
    
    board.putunit(unitA,1,1)
    board.showgrid()
main()