import tkinter as tk #use tkinter package

class Game(tk.Frame):
    def _init_(self,master):#_init_ is similar to constructor
        super(Game,self)._init_(master)
        self.lives=3
        self.width=610#改
        self.height=400#改
        self.convas=tk.Convas(self,bg='#aaaaff',width=self.width,height=self.height)
        self.convas.pack()
        self.pack() #show in parents containter
        self.item={}#
        self.ball=None #
        self.paddle=Paddle(self.convas,self.width/2,326)#改
        self.item[self.paddle.item]=self.paddle#
        for x in range(5,self.width-5,75)
            self.add_brick(x+37.5,50,2)#
            self.add_brick(x+37.5,70,1)#
            self.add_brick(x+37.5,90,1)#
        self.hud=None#
        self.setup_game()
        self.convas.focus_set()
        self.convas.bind('<Left>'lamba_:self.paddle.move(-10))
        self.convas.bind('<Right>'lambda_:self.paddle.move(10))

    def setup_game(self):
            self.add_ball()
            self.update_lives_text()
            self.text=self.draw_text(300,200,'Press Space to Start')
            self.canvas.bind('<space>',lambda_:self.start_game())

if __name__ == '__main__':#check the running module
    root=tk.Tk()
    root.title("Let's play!Pang!Pang!Pang!")
    game=Game(root)
    game.mainloop()


class GameObject(object): #set the basic object
    def _init_(self,convas,item):
        self.convas=convas
        self.item=item

    def get_position(self):
        return self.convas.coords(self.item)#return the coordinate of item

    def move(self,x,y):
        self.convas.move(self.item,x,y)

    def delete(self):
        self.convas.delete(self.item)

class Ball(GameObject):#set the ball
    def _init_(self,convas,x,y):
        self.redius=15#改
        self.direction=[1,-1]#往右上
        self.speed=10#給使用者設定
        item=convas.create_oval(x-self.redius,y-self.redius,x+self.radius,y+radius,fill='while',tags="little ball")#create the circle
        #前面兩位為左上角座標 左上角[-1,-1] ,後兩位為右下角座標 右上角[1,1] 所以往左上角要用減的，右下角要用加的 減/加的值為半徑
        super(Ball,self).__init__(convas,item)

class Paddle(GameObject):
    def __init__self(self,canvas,x,y):#x,y is the inital coordinate
        self.width=80
        self.height=10
        self.ball=None#
        item=canvas.create_rectangle(x-self.width/2,y-self.height,x+self.width/2,x+self.height,fill='blue',tags='paddle')
        super(Paddle,self).__init__(convas,item)

    def set_ball(self,ball):
        self.ball=ball #用來儲存對球的參考，讓球在遊戲開始前移動

    def move(self,offset):
        coordinate=self.get_position() #get the coodinate of paddle
        width=self.convas.winfo_width() #get the width of convas
        if coordinate[0]+offset>=0 and  coordinate[2]+offset<=width: #The minimum and maximum value of X plus the displacement must be in the canvas
            super(Paddle,self).move(offset,0)
            if self.ball is not None:#如果滑桿仍然有對球的參考[這發生在遊戲還未開始前]，球扔然會移動。
                self.ball.move(offset,0)

class Brick(GameObject):
    COLORS={1:'#999999',2:'#55555',3:'#22222'}#[dictionary] includes key and value

    def _init_(self,canvas,x,y,hits):
        self.width=75#改
        self.height=20#改
        self.hits=hits
        color=Brick.COLORS[hits] #call the function that change the color of bricks as long as it is hit
        item=convas.create_rectangle(x-self.width/2,y-self.width/2,x+self.width/2,y+self.width,fill=color,tags='brick')
        super(Brick,self)._init_(convas,item)

    def hit(self):
    self.hits -=1 #as long as brick is hit then minus 1
    if self.hits==0:
        self.delete() #Bricks disappear
    else:
        self.canvas.itemconfig(self.item,fill=Brick.COLORS[self.hits]) #change the color of bricks as long as it is hit

    








        
