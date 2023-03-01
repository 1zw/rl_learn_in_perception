import pyautogui
from  GetWindow import *
# print(pyautogui.size())
# pyautogui.moveTo(100,300)   
# pyautogui.moveRel(100,500,duration=0.1)   # 第一个参数是左右移动像素值，第二个是上下，
# print(pyautogui.position())   # 得到当前鼠标位置；输出：Point(x=200, y=800)
class model():
    def __init__(self):
        pass
        
class mouseauto(GetWindow):
    def __init__(self) -> None:
        super().__init__()
        self.mode_choose      = False # 模式是否选择
        self.__mapinitial     = False # 游戏地图是否初始化
        self.__square         = [None]*4 # [左上，右上，左下，右下]
        self.__Death_Area     = (0,0,0) # 黑色的RGB
        self.__orignal_point  = None
        self.player_position  = None
    def __click(self,picture_name = "player.png",play_game = False):
        if not play_game:
            for pic in picture_name:
                btm = pyautogui.locateOnScreen(os.path.join(self.dir,pic))
                if btm == None:
                    print("{} get error".format(pic))
                else:
                    break
            if btm == None:
                return False
            center = pyautogui.center((btm.left,btm.top,btm.width,btm.height))
            pyautogui.click(center,duration=0.5)
            return True
        else:
            if not self.__mapinitial:
                self.__initmap()
            else:
                btm = pyautogui.locateOnScreen(os.path.join(self.dir,'player_1.png'))
                if btm != None:
                    self.player_position = np.array(pyautogui.center((btm.left,btm.top,btm.width,btm.height)))
    def __initmap(self):
        intial_pic = tuple(['game_name.png','make_map_1.png','make_map_2.png'])
        intial_position = [[(220,-30),(-220,-30),(220,-880),(-220,-880)],
                           [(320,-30),(-120,-30),(320,-880),(-120,-880)],
                           [(390,-30),(-50,-30),(390,-880),(-50,-880)]]
        for pic,position in zip(intial_pic,intial_position):
            btm = pyautogui.locateOnScreen(os.path.join(self.dir,pic))
            if btm == None:
                print("{} get error".format(pic))
            else:
                break
        if btm == None:
            return False
        center = pyautogui.center((btm.left,btm.top,btm.width,btm.height))
        for position,index in zip(position,list(range(4))):
            self.__square[index] = np.array(center) - np.array(position)
        self.__mapinitial = True
        print("square position = ", self.__square)
        print("game map initialize successed!")
        return True
    def begin_game(self):
        if not self.mode_choose:
            classical_mode = tuple(['classical_mode_{}.png'.format(i) for i in range(1,4)])
            if self.__click(classical_mode):
                print("mode choose finished!")
                self.mode_choose = True
        touch_begin = tuple(['touch_begin.png','player.png'])
        if self.__click(touch_begin):
            print("touch begin finished!")
    def game_is_over(self):
        again = tuple(['again_{}.png'.format(i) for i in range(1,4)])
        game_over = self.__click(again)
        if game_over :
            print("game over and now restart game")
            return True
    def play_game(self):
        while not self.game_is_over():
            self.__click(play_game=True)
            print(self.player_position)
            
        pass
    def capture(self):
        self.__orignal_point = self.__square[0]
        region = (self.__orignal_point[0],self.__orignal_point[1],
                  self.window_width,self.window_height)
        im = pyautogui.screenshot(region = region)
        print(im.getpixel(tuple(self.player_position[0],self.player_position[1])))
        im.save(self.path)      
mouse = mouseauto()
mouse.get_handle()
# mouse.game_is_over()
mouse.play_game()
# time.sleep(5)
# print(pyautogui.position())
