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
f = Frame(win, width=1540, height=1280, relief="solid", bd=2, bg="gray")
# f.place(x=0,y=0)
f.grid(column=0, row=0, sticky="n")
movieInfo = Frame(win, width=1540, height=1280, relief="solid", bd=2, bg="gray")
movieInfo.grid(column=1, row=0)
# movieInfo.place(x=800,y=0)
msf.place(x=0, y=0)
msf.tkraise()

# 오디오, 이미지
sound = pygame.mixer.Sound(r"bgms\pedro-song.wav")
intotheunknown = pygame.mixer.Sound(r"bgms\Idina Menzel, AURORA - Into the Unknown (From Frozen 2 ).wav")
pororo = pygame.mixer.Sound(r"bgms\[뽀로로 1기] 오프닝 송♪ 노는 게 제일 좋아♪.wav")
jangiha = pygame.mixer.Sound(r"bgms\장기하와 얼굴들 - 풍문으로 들었소 가사 (Synced Lyrics).wav")
duckply = pygame.mixer.Sound(r"bgms\체리필터 (cherryfilter) - 오리 날다 [가사 Lyrics].wav")
seeyouagain = pygame.mixer.Sound(r"bgms\Wiz Khalifa - See You Again ft. Charlie Puth [Official Video] Furious 7 Soundtrack.wav")
homealone = pygame.mixer.Sound(r"bgms\나홀로집에 Home Alone OST - Somewhere in My Memory [가사해석 번역].wav")
jojoost = pygame.mixer.Sound("bgms\\Giornos Theme best part but perfect ending.wav")
jjangguost = pygame.mixer.Sound("bgms\\짱구는 못말려 OST - 오프닝1.wav")
niggacat = pygame.mixer.Sound("bgms\\meow-meow-n-gga.wav")
aotost = pygame.mixer.Sound(r"bgms\진격의 거인 1기 op.wav")
niggacatImage = ImageTk.PhotoImage(Image.open(r"images\black cat.jpg").resize((1000,800)))
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
frozenImage = Image.open("images\겨털2.jpeg")
frozenImage = frozenImage.resize((400,400))
frozenImage = ImageTk.PhotoImage(frozenImage)
grandmaImage = Image.open("images\나문희.jpg")
grandmaImage = grandmaImage.resize((400,400))
grandmaImage = ImageTk.PhotoImage(grandmaImage)
wtcImage = Image.open("images\깡패.jpeg")
wtcImage = wtcImage.resize((400,400))
wtcImage = ImageTk.PhotoImage(wtcImage)
jojoImage = Image.open("images\ㅈㅈ.jpg")
jojoImage = jojoImage.resize((400,400))
jojoImage = ImageTk.PhotoImage(jojoImage)

sound.play(-1)

# 로직 세팅
global getCountry
global getJangr

def soundPlay(m): 
    currentMusic.stop()
    m.play(-1)

def quitApp():
    sound.stop()
    sound.set_volume(100)
    label = Label(win, image=niggacatImage)
    label.place(x=300,y=0)
    niggacat.play()
    label.tkraise()
    win.after(1205, exit)

def change_volume(vol):
    volume = float(vol) / 100
    sound.set_volume(volume)

def removemsfframe():
    sound.stop()
    msf.destroy()

def getEntity():
    global currentMusic

    for i in movieInfo.winfo_children(): i.destroy()
    movie = '0'
    selectMovie = list()
    selectMovie.clear()
    getCountry = country.get()
    getJangr = jangr.get()
    country.delete(0, END)
    jangr.delete(0, END)

    if getCountry == "한" or getCountry == "미" or getCountry == "일": pass
    else: getCountry = '0'

    if getJangr == "애니메이션" or getJangr == "액션" or getJangr == "코미디": pass
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

        if selectMovie:
            movie = random.choice(selectMovie)
            moviee.config(state="normal")
            moviee.delete(0, END)
            moviee.insert(0, movie[2])
            moviee.config(state="readonly")
            musicn.config(state="normal")
            musicn.delete(0, END)
            musicn.insert(0, movie[3])
            musicn.config(state="readonly")

    except Exception as e:
        print("영화를 찾을 수 없습니다.", e)
    
    if movie[2] == "겨울왕국2":
        Label(movieInfo, image=frozenImage).grid()
        currentMusic = intotheunknown
    elif movie[2] == "분노의 질주":
        Label(movieInfo, image=bunnyo).grid()
        currentMusic = seeyouagain
    elif movie[2] == "나 홀로 집에":
        Label(movieInfo, image=homealoneImage).grid()
        currentMusic = homealone
    elif movie[2] == "범죄와의 전쟁":
        Label(movieInfo, image=warwithcrime).grid()
        currentMusic = jangiha
    elif movie[2] == "뽀롱뽀롱 뽀로로":
        Label(movieInfo, image=pororoImage)
        currentMusic = pororo
    elif movie[2] == "권순분 여사 납치사건":
        Label(movieInfo, image=namunheui)
        currentMusic = duckply
    elif movie[2] == "죠죠의 기묘한 모험":
        Label(movieInfo, image=jojoImage)
        currentMusic = jojoost
    elif movie[2] == "진격의 거인":
        Label(movieInfo, image=aot)
        currentMusic = aotost
    elif movie[2] == "짱구는 못말려":
        Label(movieInfo, image=jjanggu)
        currentMusic = jjangguost
    else: currentMusic = FALSE

angle = 0

nara = ["한","일","미"]
jang = ["애니메이션", "액션", "코미디"]
frozen = ["미", "애니메이션", "겨울왕국2", "Into the unknown"]
zilzubunno = ["미", "액션", "분노의 질주", "See you again"]
alonehome = ["미", "코미디", "나 홀로 집에", "Somewhere In My Memory"]
warwithcrime = ["한", "액션", "범죄와의 전쟁", "풍문으로 들었소"]
penguin = ["한", "애니메이션", "뽀롱뽀롱 뽀로로", "노는 게 제일좋아"]
namunheui = ["한", "코미디", "권순분 여사 납치사건", "오리 날다"]
jojo = ["일", "액션", "죠죠의 기묘한 모험", "Ill vento d\'oro"]
aot = ["일", "애니메이션", "진격의 거인", "홍련의 화살"]
jjanggu = ["일", "코미디", "짱구는 못말려", "천방지축 어리둥절"]

movies = [frozen, penguin, warwithcrime, namunheui, zilzubunno, alonehome, jojo, aot, jjanggu]

# 삽입

# 메인 스크린 프레임
Label(msf, text="영화 검색", width=10, height=0, font=("궁서체", 70) ,bg="white").place(x=590,y=30)
labelJaeuk = Label(msf, image=piJaeuk)
labelJaeuk.place(x=480,y=200)
Button(msf, text="Play", font=("궁서체", 20), bg="gray", bd=2, command=removemsfframe, padx=70, pady=40, cursor="circle").place(x=485, y=500)
Button(msf, text="Exit", font=("궁서체", 20), bg="gray", bd=2, command=quitApp, padx=70, pady=40, cursor="circle").place(x=915, y=500)

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
Button(f, text="입력", width=3, height=1, padx=30, pady=10, command=getEntity, bg="gray", cursor="circle").grid(row=1, column=2, sticky="e")
Button(f, text="Play Song", width=9, height=2, bg="gray", cursor="circle", command=lambda: soundPlay(currentMusic)).grid(row=3, column=2, sticky="w")
Label(f, text="영화제목", width=8, height=1, padx=30, pady=10, bg="gray").grid(row=2, column=0, sticky="w")
Label(f, text="음악제목", width=8, height=1, padx=30, pady=10, bg="gray").grid(row=3, column=0, sticky="w")
Label(f, text="소리조절", width=8, height=1, bg="gray").grid(row=4, column=0)
Label(f, image=iconjaeuk, bg="gray").grid(row=4, column=0, sticky="e")
volumn_slider = Scale(f, from_=0, to=100, orient=HORIZONTAL, width=30, command=change_volume, bg="gray", bd=0)
volumn_slider.set(50)
volumn_slider.place(x=450, y=330)
volumn_fslider = Scale(msf, from_=0, to=100, orient=HORIZONTAL, width=30, command=change_volume, bg="white", bd=0)
volumn_fslider.set(50)
volumn_fslider.place(x=1300, y=0)

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

