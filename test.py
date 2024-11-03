from tkinter import *
from PIL import ImageTk, Image
import random
import pygame

# 기본 창
win = Tk()
pygame.init()
win.geometry('1540x1280')
win.title("영화 검색")
win.option_add("*Font", "궁서체")
win.iconphoto(False, PhotoImage(file="images\재욱송.png"))

# 크기 설정 불가
win.resizable(False, False)

# 프레임
msf = Frame(win, width=1540, height=1280, relief="solid", bd=0, bg="white")
f = Frame(win, width=1000, height=500, relief="solid", bd=2, bg="gray")
msf.place(x=0, y=0)
f.place(x=270,y=200)
msf.grid()
f.grid()

# 오디오, 이미지
sound = pygame.mixer.Sound("bgms\pedro-song.wav")
intotheunknown = pygame.mixer.Sound("bgms\Idina Menzel, AURORA - Into the Unknown (From ＂Frozen 2＂).wav")
pororo = pygame.mixer.Sound("bgms\[뽀로로 1기] 오프닝 송♪ 노는 게 제일 좋아♪.wav")
jangiha = pygame.mixer.Sound("bgms\장기하와 얼굴들 - 풍문으로 들었소 (범죄와의 전쟁： 나쁜놈들 전성시대 OST).wav")
duckply = pygame.mixer.Sound("bgms\체리필터 (cherryfilter) - 오리 날다 [가사⧸Lyrics].wav")
seeyouagain = pygame.mixer.Sound("bgms\故폴 워커 추모곡 See You Again Wiz Khalifa (ft. Charlie Puth) 가사 번역 뮤직비디오 (분노의 질주 더 세븐 OST).wav")
homealone = pygame.mixer.Sound("bgms\나홀로집에 Home Alone OST - Somewhere in My Memory [가사해석 번역].wav")
jojoost = pygame.mixer.Sound("bgms\Giornos Theme, but only the best part.wav")
jjangguost = pygame.mixer.Sound("bgms\짱구는 못말려 OST - 오프닝1.wav")
aotost = pygame.mixer.Sound("bgms\진격의 거인 1기 op.wav")
homealoneImage = Image.open("images\나홀로집에.jpeg")
homealoneImage = homealoneImage.resize((400,400))
homealoneImage = ImageTk.PhotoImage(homealoneImage)
bunnyo = Image.open("images\분뇨의 질주.jpeg")
bunnyo = bunnyo.resize((400,400))
bunnyo = ImageTk.PhotoImage(bunnyo)
pororoImage = Image.open("images\뽀로로.jpeg")
pororoImage = pororoImage.resize((400,400))
pororoImage = ImageTk.PhotoImage(pororoImage)
opendJaeuk = Image.open("images\재욱송.png")
opendJaeuk = opendJaeuk.resize((650,500))
piJaeuk = ImageTk.PhotoImage(opendJaeuk)
iconjaeuk = opendJaeuk.resize((100,50))
iconjaeuk = ImageTk.PhotoImage(iconjaeuk)
haerin = Image.open("images\마름모.jpg")
haerin = haerin.resize((400,400))
haerin = ImageTk.PhotoImage(haerin)

sound.play(-1)

# 로직 세팅
global getCountry
global getJangr

gotten = list()

def change_volume(vol):
    volume = float(vol) / 100
    sound.set_volume(volume)

def removemsfframe():
    sound.stop()
    msf.destroy()

def getEntity():
    selectMovie = list()
    getCountry = country.get()
    getJangr = jangr.get()
    country.delete(0, 100)
    jangr.delete(0, 100)

    if getCountry == "한" or getCountry == "미" or getCountry == "일":
        pass
    else: getCountry = '0'
    if getJangr == "애니메이션" or getJangr == "액션" or getJangr == "코미디":
        pass
    else: getJangr = '0'

    try:
        for i in movies:
            if getCountry == '0' and getJangr != '0':
               if i[1] == getJangr:
                   selectMovie.append(i)
            elif getCountry != '0' and getJangr == '0':
                if i[0] == getCountry:
                    selectMovie.append(i)
            else:
                if i[0] == getCountry and i[1] == getJangr:
                    selectMovie.append(i)

        movie = random.choice(selectMovie)
    except Exception as e:
        print("영화를 찾을 수 없습니다.", e)
    
    print(movie)

angle = 0
size = 0

nara = ["한","일","미"]
jang = ["애니메이션", "액션", "코미디"]
frozen = ["미", "애니메이션", "겨울왕국2"]
zilzubunno = ["미", "액션", "분노의 질주"]
alonehome = ["미", "코미디", "나 홀로 집에"]
warwithcrime = ["한", "액션", "범죄와의 전쟁"]
penguin = ["한", "애니메이션", "뽀롱뽀롱 뽀로로"]
namunheui = ["한", "코미디", "권순분 여사 납치사건"]
jojo = ["일", "액션", "죠죠의 기묘한 모험"]
aot = ["일", "애니메이션", "진격의 거인"]
jjanggu = ["일", "코미디", "짱구는 못말려"]

movies = [frozen, penguin, warwithcrime, namunheui, zilzubunno]

# 삽입

# 메인 스크린 프레임
Label(msf, text="영화 검색", width=10, height=0, font=("궁서체", 70) ,bg="white").place(x=590,y=30)
labelJaeuk = Label(msf, image=piJaeuk)
labelJaeuk.place(x=480,y=200)
Button(msf, text="Play", font=("궁서체", 20), bg="gray", bd=2, command=removemsfframe, padx=70, pady=40).place(x=485, y=500)
Button(msf, text="Exit", font=("궁서체", 20), bg="gray", bd=2, command=exit, padx=70, pady=40).place(x=915, y=500)

# 메인 프레임
Label(f, text="나라이름입력(한,미,일)", bg="gray").grid(row=0,column=0, sticky="e")
country = Entry(f)
jangr = Entry(f)
moviee = Entry(f, state="readonly")
musicn = Entry(f, state="readonly")
country.grid(row=0, column=1, padx=50, pady=30, sticky="e")
jangr.grid(row=1,column=1, padx=50, pady=30, sticky="e")
moviee.grid(row=2, column=1, padx=50, pady=30, sticky="e")
musicn.grid(row=3, column=1, padx=50, pady=30, sticky="e")
Label(f, text="장르검색(액션,애니메이션,코미디)", padx=30, pady=10, bg="gray").grid(row=1,column=0,sticky="w")
Button(f, text="입력", width=3, height=1, padx=30, pady=10, command=getEntity, bg="gray").grid(row=1, column=2, sticky="e")
Button(f, text="Play Song", width=9, height=2, bg="gray").grid(row=3, column=2, sticky="w")
Label(f, text="영화제목", width=8, height=1, padx=30, pady=10, bg="gray").grid(row=2, column=0, sticky="w")
Label(f, text="음악제목", width=8, height=1, padx=30, pady=10, bg="gray").grid(row=3, column=0, sticky="w")
Label(f, text="소리조절", width=8, height=1, bg="gray").grid(row=4, column=0)
Label(f, image=iconjaeuk, bg="gray").grid(row=4, column=0, sticky="e")
volumn_slider = Scale(win, from_=0, to=100, orient=HORIZONTAL, width=30, command=change_volume, bg="gray", bd=0)
volumn_slider.set(50)
volumn_slider.place(x=1000, y = 0)
volumn_slider.grid(row=0, column=15, sticky="w", padx=15)

# 애니메이션
def spinJaeuk():
    global angle, opendJaeuk, piJaeuk, labelJaeuk
    rotatedJaeuk = opendJaeuk.rotate(angle=angle)
    piJaeuk = ImageTk.PhotoImage(rotatedJaeuk)
    labelJaeuk.config(image=piJaeuk)
    angle += 10
    win.after(50, spinJaeuk)

spinJaeuk()

win.mainloop()
