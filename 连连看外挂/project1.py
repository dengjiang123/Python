import win32gui
import win32api
import pyautogui  # 加入pyautogui库能让ImageGrab正常截屏
from PIL import ImageGrab
import cv2

blocks_x = 19
blocks_y = 11
name = "QQ游戏 - 连连看角色版"
hwnd = win32gui.FindWindow(None, name)
if hwnd:
    print("成功找到")
else:
    print("没有找到窗口，请重试!")
    exit()

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
win32gui.SetForegroundWindow(hwnd, )
left, top, right, bottom = win32gui.GetWindowRect(hwnd)

window_width = right - left
window_height = bottom - top
game_left = left + 14.0 / 800.0 * window_width
game_right = left + 603 / 800.0 * window_width
game_top = top + 181.0 / 600.0 * window_height
game_bottom = top + 566 / 600.0 * window_height
game_width = game_right - game_left
game_height = game_bottom - game_top
grid_width = game_width / blocks_x
grid_height = game_height / blocks_y

game_image = ImageGrab.grab((game_left, game_top, game_right, game_bottom))

M_Image = []
for i in range(blocks_x):
    temp_M = []
    for j in range(blocks_y):
        temp_image = game_image.crop((i * grid_width, j * grid_height, (i + 1) * grid_width, (j + 1) * grid_height))
        temp_M.append(
            temp_image.crop((1 / 10 * grid_width, 1 / 10 * grid_height, 9 / 10 * grid_width, 9 / 10 * grid_height)))

    M_Image.append(temp_M)


def Get_V(x, i, j):
    return i + j


def Get_M_value():
    M = []
    for i in range(blocks_x):
        temp = []
        for j in range(blocks_y):
            temp.append(Get_V(M_Image[i][j], i, j))
        M.append(temp)
    return M


def judge(x1, x2):  # 判断两图片相应指标是否一致
    maxdiffer = 10
    if (x1 - x2) < maxdiffer and (x1 - x2) >= 0:
        return 1
    elif (x2 - x1) < maxdiffer and (x2 - x1) >= 0:
        return 1
    else:
        return 0


def Mark_M(x):
    start = 0
    mark = []
    hash_m = []
    M = []
    for i in range(blocks_x):
        M_T = []
        for j in range(blocks_y):
            f = 0
            for k in hash_m:
                if (judge(x[i][j], k) == 1):
                    f = 1
                    M_T.append(mark[hash_m.index(k)])
                    break  # 合适时机跳出k循环
            if (f == 0):
                mark.append(start)
                M_T.append(start)
                hash_m.append(x[i][j])
                start += 1
        M.append(M_T)
    return M


M_Get = Get_M_value()

for i in range(blocks_x):
    for j in range(blocks_y):
        print(M_Get[i][j], end=" ")
    print()

M = Mark_M(M_Get)

for i in range(blocks_x):
    for j in range(blocks_y):
        print(M[i][j], end=" ")
    print()

'''
def dHash(img):
    # 缩放8*8
    img = cv2.resize(img, (9, 8), interpolation=cv2.INTER_CUBIC)
    # 转换灰度图
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    hash_str = ''
    # 每行前一个像素大于后一个像素为1，相反为0，生成哈希
    for i in range(8):
        for j in range(8):
            if gray[i, j] > gray[i, j + 1]:
                hash_str = hash_str + '1'
            else:
                hash_str = hash_str + '0'
    return hash_str

def cmpHash(hash1, hash2):
    n = 0
    # hash长度不同则返回-1代表传参出错
    if len(hash1) != len(hash2):
        return -1
    # 遍历判断
    for i in range(len(hash1)):
        # 不相等则n计数+1，n最终为相似度
        if hash1[i] != hash2[i]:
            n = n + 1
    return n

def get_image_matrix():
    y_m=[]
    for j in range(blocks_y):
        x_m=[]
        for i in range(blocks_x):
            M_Image[i][j].save("test4.jpg","JPEG")
            img1 = cv2.imread("test4.jpg")
            hash_1 = dHash(img1)
            x_m.append(hash_1)
        y_m.append(x_m)
    return y_m

def M_mark(Mori,imax,jmax):
    start=0
    mark=[]
    hash_m=[]
    M=[]
    Max_diff=12
    f=0
    for i in range(jmax): #11
        M_T=[]
        for j in range(imax):   #19
            f=0
            for k in hash_m:
                dif=cmpHash(Mori[i][j],k)
                if dif<Max_diff:
                    M_T.append(mark[hash_m.index(k)])
                    f=1
            if(f==0):
                mark.append(start)
                M_T.append(start)
                hash_m.append(Mori[i][j])
                start+=1
                print(start)
        M.append(M_T)
    return M

matrix=get_image_matrix()

print(len(matrix),len(matrix[0]))
for i in range(blocks_y):
    for j in range(blocks_x):
        print(matrix[i][j],end=" ")
    print()

M=M_mark(matrix,blocks_x,blocks_y)

for i in range(blocks_y):
    for j in range(blocks_x):
        print(M[i][j],end=" ")
    print()

'''