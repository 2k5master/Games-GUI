# Import modules
from tkinter import *
from tkinter import filedialog
import subprocess
import random
import winsound
import tkinter
import webbrowser
import os
from tkinter import Menu, Frame
import time
from plyer import notification
import timer
from PIL import Image, ImageTk

os.system("del Preview.png")
os.system("del background.png")

# Variables
output_counter = 1
# Text File
ThemeText = open(r"theme.txt","r")
ReadableText = ThemeText.readlines()
# Font Color
fontColor = ReadableText[0]
f = fontColor.strip()
# Primary Color
primaryColor = ReadableText[1]
p = primaryColor.strip()
# Secondary Color
secondaryColor = ReadableText[2]
s = secondaryColor.strip()
# Background Image
backgroundImage = ReadableText[3]
b = backgroundImage.strip()

ThemeText.close()

# Screen Setup
root = Tk()
root.title('Games Launcher v3.00')
root.geometry("990x600+10+10")
root.iconbitmap("gamepadpng.ico")
root.resizable(width = False, height = False)

# Image
background = Image.open(b)
bg = background.resize((990, 610), Image.ANTIALIAS)
bg.save("background.png", "PNG")
BackgroundImage = PhotoImage(file = "background.png")

# Create Canvas
canvas1 = Canvas( root, width = 400,
                    height = 400)
  
canvas1.pack(fill = "both", expand = True)
  
# Display image
canvas1.create_image( 0, 0, image = BackgroundImage, 
                        anchor = "nw")

# Add Text
lbl2 = Label( root, text="Games", bg=s, fg=f, height=1, width=15)
lbl2.configure(font=("Arial", 19))
lbl2.place(x=10, y=15)
lbl4 = Label( root, text="Mods", bg=s, fg=f, height=1, width=15)
lbl4.configure(font=("Arial", 19))
lbl4.place(x=747, y=15)
lbl5 = Label( root, text="Random Game", bg=s, fg=f, height=1, width=15)
lbl5.configure(font=("Arial", 19))
lbl5.place(x=747, y=375)
lbl6 = Label( root, text="Welcome, Ben!", bg=s, fg=f, height=1, width=23)
lbl6.configure(font=("Arial", 20))
lbl6.place(x=308, y=15)
local_lbl1 = Label( root, text="Output", bg=s, fg=f, height=1, width=15)
local_lbl1.configure(font=("Arial", 19))
local_lbl1.place(x=747, y=465)

# Create Buttons
button1 = Button( root, text = "OOTP 23", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Program Files\\Out of the Park Developments\\OOTP Baseball 23\\ootp23_x64.exe'))
button2 = Button( root, text = "RPCS3", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Users\\blayt\\Desktop\\PS3\\RPCS3\\rpcs3.exe'))
button3 = Button( root, text = "PCSX2", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Program Files (x86)\\PCSX2\\pcsx2.exe'))
button4 = Button( root, text = "Valorant", bg=p, fg=f, command=lambda:
                    subprocess.Popen('"C:\\Riot Games\\Riot Client\\RiotClientServices.exe"'))
button5 = Button( root, text = "Rocket League", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Program Files\\Epic Games\\rocketleague\\Binaries\\Win64\\RocketLeague.exe'))
button6 = Button( root, text = "Minecraft", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Users\\blayt\\AppData\\Local\\Programs\\lunarclient\\Lunar Client.exe'))
button7 = Button( root, text = "FHM 6", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Program Files (x86)\\Out of the Park Developments\\Franchise Hockey Manager 6\\fhm6.exe'))
buttonA = Button( root, text="GTA: San Andreas", bg=p, fg=f, command=lambda:
                 os.startfile("C:\\Users\\blayt\\Desktop\\gta san andreads"))
buttonB = Button( root, text="MVP 05", bg=p, fg=f, command=lambda:
                 subprocess.Popen('C:\\Users\\blayt\\Desktop\\mvp05pc\\mvp2005.exe'))

buttonC = Button( root, text="NFL 2K5 Resurrected", bg=p, fg=f, command=lambda:
                 subprocess.Popen("C:\\Users\\blayt\\Desktop\\NFL 2K23\\pcsx2-qtx64-avx2.exe"))

button8 = Button( root, text = "Generate Random Game", bg=p, fg=f, command=lambda:
                    randomGame(output_counter, local_lbl1))

button9 = Button( root, text="OOTP Forums", bg=s, fg=f, command=lambda:
                    webbrowser.open('http://forums.ootpdevelopments.com/index.php'))

button10 = Button( root, text="Operation Sports", bg=s, fg=f, command=lambda:
                    webbrowser.open('http://forums.operationsports.com/forums'))

button11 = Button( root, text="Discord", bg=s, fg=f, command=lambda:
                    subprocess.Popen('"C:\\Users\\blayt\\AppData\\Local\\Discord\\app-1.0.9004\\Discord.exe"'))

button12 = Button( root, text="ESPN Scorebug Switcher", bg=p, fg=f, command=lambda:
                    os.startfile(r"C:\Users\blayt\Desktop\PS3\RPCS3\dev_hdd0\game\BLUS30444\USRDIR\data\ui\game\overlays\espn"))

button13 = Button( root, text="CBS Scorebug Switcher", bg=p, fg=f, command=lambda:
                    os.startfile(r"C:\Users\blayt\Desktop\PS3\RPCS3\dev_hdd0\game\BLUS30444\USRDIR\data\ui\game\overlays\cbs"))

button14 = Button( root, text="Court Switcher", bg=p, fg=f, command=lambda:
                    subprocess.Popen('C:\\Users\\blayt\\Desktop\\PS3\\RPCS3\\dev_hdd0\\game\\BLUS30444\\USRDIR\\data\\gfx\\sceneassets\\fxsimple\\stadium\\MarchMadnessCourtSwitcher.exe'))

button15 = Button( root, text="NCAA 14 Mods", bg=p, fg=f, command=lambda:
                    os.startfile(r"C:\Users\blayt\Desktop\NCAA 14 Mods (created by me)"))

button16 = Button( root, text="NCAA Utility Tool", bg=p, fg=f, command=lambda:
                    os.startfile("C:\\Users\\blayt\\AppData\\Local\\Programs\\NCAA 14 Utility Tool 2.0"))

button17 = Button( root, text="NCAA Dynasty Tool", bg=p, fg=f, command=lambda:
                    subprocess.Popen("C:\\Program Files\\NCAA 14 Dynasty Tool\\NCAA 14 Dynasty Tool.exe"))

button18 = Button( root, text="ESPN NFL 2K5 Mod Enabler", bg=p, fg=f, command=lambda:
                    os.startfile(r"C:\\Users\\blayt\\Desktop\\2K5 MODS\\XBv1.5Full\\PCSX2_NFL2KR"))

button19 = Button( root, text="Hypixel Forums", bg=s, fg=f, command=lambda:
                    webbrowser.open('https://hypixel.net/forums/'))

button20 = Button( root, text="Set a Timer", bg=p, fg=f, command=lambda:
                    setTimer())

button21 = Button( root, text="Customize Theme", bg=p, fg=f, command=lambda:
                  customizeTheme())

# Customize Theme Function
def customizeTheme():
    theme = tkinter.Toplevel()
    theme.title("Customize Theme")
    theme.geometry('400x415')
    theme.iconbitmap("paintPalette.ico")
    canvas3 = Canvas( theme, width=400,
                     height=400)
    canvas3.pack(fill = "both", expand = False)
    # Text
    introText = Label( theme, text="Enter a valid hexedecimal color code. Remember to start with a # sign!", fg="#000000")
    introText.place(x=13, y=10)
    fontText = Label( theme, text="Font Color", fg="#000000")
    fontText.place(x=13, y=40)
    primaryText = Label( theme, text="Primary Color", fg="#000000")
    primaryText.place(x=13, y=70)
    secondaryText = Label( theme, text="Secondary Color", fg="#000000")
    secondaryText.place(x=13, y=100)
    imageText = Label( theme, text="Image Directory", fg="#000000")
    imageText.place(x=13, y=130)
    themePresets = Label( theme, text="Default Theme Presets")
    themePresets.place(x=132, y=280)
    # Font
    currentFontText = Label( theme, text=f, fg="#000000")
    currentFontText.place(x=200, y=190)
    fontLabel = Label( theme, text="Current Font Color:", fg="#000000")
    fontLabel.place(x=13, y=190)
    currentFont = Label( theme, text="sample", fg=f, bg=f)
    currentFont.place(x=155, y=190)
    # Primary
    currentPrimaryText = Label( theme, text=p, fg="#000000")
    currentPrimaryText.place(x=200, y=220)
    primaryLabel = Label( theme, text="Current Primary Color:", fg="#000000")
    primaryLabel.place(x=13, y=220)
    currentPrimary = Label( theme, text="sample", fg=p, bg=p)
    currentPrimary.place(x=155, y=220)
    # Secondary
    currentSecondaryText = Label( theme, text=s, fg="#000000")
    currentSecondaryText.place(x=200, y=250)
    secondaryLabel = Label( theme, text="Current Secondary Color:", fg="#000000")
    secondaryLabel.place(x=13, y=250)
    currentSecondary = Label( theme, text="sample", fg=s, bg=s)
    currentSecondary.place(x=155, y=250)
    # Image
    bgPreview = Image.open(b)
    bg1 = bgPreview.resize((135, 82), Image.ANTIALIAS)
    bg1.save("Preview.png", "PNG")
    PreviewImage = PhotoImage(file = "C:\\Users\\blayt\\Desktop\\programs\\Games GUI\\Preview.png")
    a = Label( theme)
    a.configure(image=PreviewImage)
    a.place(x=250, y=190)
    # Entry Fields
    fontEntry = Entry( theme)
    fontEntry_canvas = canvas3.create_window(120, 40, anchor="nw", window=fontEntry, width=263)
    primaryEntry = Entry( theme)
    primaryEntry_canvas = canvas3.create_window(120, 70, anchor="nw", window=primaryEntry, width=263)
    secondaryEntry = Entry( theme)
    secondaryEntry_canvas = canvas3.create_window(120, 100, anchor="nw", window=secondaryEntry, width=263)
    imageEntry = Entry( theme)
    imageEntry_canvas = canvas3.create_window(120, 130, anchor="nw", window=imageEntry, width=170)
    # Buttons
    changeTheme = Button( theme, text="Change theme (Restart Required)", fg="#000000", bg="#f1f1f1", command=lambda:
                         setNewTheme(fontEntry, primaryEntry, secondaryEntry, imageEntry))
    changeTheme_canvas = canvas3.create_window(13, 160, anchor="nw", window=changeTheme, width=374)
    openFolders = Button( theme, text="Browse Folders", fg="#000000", bg="#f1f1f1", command=lambda:
                         os.startfile(r"C:\Users"))
    openFolders_canvas = canvas3.create_window(295, 130, anchor="nw", window=openFolders, height=20)
    darkTheme = Button( theme, text="Dark Theme", bg="#1f1f1f", fg="#aaaaaa", command=lambda:
                      setDarkTheme())
    darkTheme_canvas = canvas3.create_window(13, 305, anchor="nw", window=darkTheme, height=30, width=185)
    tropicalTheme = Button( theme, text="Tropical Theme", bg="#2371b3", fg="#f1f1f1", command=lambda:
                           setTropicalTheme())
    tropicalTheme_canvas = canvas3.create_window(205, 305, anchor="nw", window=tropicalTheme, height=30, width=185)
    lightTheme = Button( theme, text="Light Theme", bg="#f1f1f1", fg="#1f1f1f", command=lambda:
                        setLightTheme())
    lightTheme_canvas = canvas3.create_window(13, 340, anchor="nw", window=lightTheme, height=30, width=185)
    nightTheme = Button( theme, text="Night Theme", bg="#000437", fg="#f1f1f1", command=lambda:
                        setNightTheme())
    nightTheme_canvas = canvas3.create_window(205, 340, anchor="nw", window=nightTheme, height=30, width=185)
    sunsetTheme = Button( theme, text="Sunset Theme", bg="#fb9932", fg="#f1f1f1", command=lambda:
                         setSunsetTheme())
    sunsetTheme_canvas = canvas3.create_window(13, 375, anchor="nw", window=sunsetTheme, height=30, width=185)
    winterTheme = Button( theme, text="Winter Theme", bg="#2377a4", fg="#f8f8f8", command=lambda:
                         setWinterTheme())
    winterTheme_canvas = canvas3.create_window(205, 375, anchor="nw", window=winterTheme, height=30, width=185)

def setWinterTheme():
    winterThemeText = open(r"theme.txt", "w")
    winterThemeText.write("#f8f8f8" + "\n")
    winterThemeText.write("#2377a4" + "\n")
    winterThemeText.write("#50a3c6" + "\n")
    winterThemeText.write("winter.png")

def setSunsetTheme():
    sunsetThemeText = open(r"theme.txt", "w")
    sunsetThemeText.write("#f1f1f1" + "\n")
    sunsetThemeText.write("#ff6c42" + "\n")
    sunsetThemeText.write("#fb9932" + "\n")
    sunsetThemeText.write("sunset.png")

def setNightTheme():
    nightThemeText = open(r"theme.txt", "w")
    nightThemeText.write("#f1f1f1" + "\n")
    nightThemeText.write("#000437" + "\n")
    nightThemeText.write("#2b2f77" + "\n")
    nightThemeText.write("night.png")

def setLightTheme():
    lightThemeText = open(r"theme.txt", "w")
    lightThemeText.write("#1f1f1f" + "\n")
    lightThemeText.write("#f1f1f1" + "\n")
    lightThemeText.write("#dcdcdc" + "\n")
    lightThemeText.write("light.png")

def setDarkTheme():
    darkModeText = open(r"theme.txt", "w")
    darkModeText.write("#f1f1f1" + "\n")
    darkModeText.write("#3f3f3f" + "\n")
    darkModeText.write("#1f1f1f" + "\n")
    darkModeText.write("darktheme.png")

def setTropicalTheme():
    tropicalThemeText = open(r"theme.txt", "w")
    tropicalThemeText.write("#f1f1f1" + "\n")
    tropicalThemeText.write("#2371b3" + "\n")
    tropicalThemeText.write("#1f8217" + "\n")
    tropicalThemeText.write("tropical.png")

def setNewTheme(fontEntry, primaryEntry, secondaryEntry, imageEntry):
    font = fontEntry.get()
    primary = primaryEntry.get()
    secondary = secondaryEntry.get()
    imageNew = imageEntry.get()
    newThemeText = open(r"theme.txt", "w")
    newThemeText.write(font + "\n")
    newThemeText.write(primary + "\n")
    newThemeText.write(secondary + "\n")
    newThemeText.write(imageNew)
    
# Timer Function
def setTimer():
    settings = Tk()
    settings.title('Timer')
    settings.geometry('300x135')
    settings.iconbitmap("clock.ico")
    canvas2 = Canvas( settings, width = 400,
                    height = 400)
    canvas2.pack(fill = "both", expand = True)
    # Entry Fields
    minutesEntry = Entry( settings)
    minutesEntry_canvas = canvas2.create_window(70, 10,
                                                anchor="nw",
                                                window=minutesEntry, width=215)
    secondsEntry = Entry( settings)
    secondsEntry_canvas = canvas2.create_window(70, 40,
                                                anchor="nw",
                                                window=secondsEntry, width=215)
    customMessage = Entry( settings)
    customMessage_canvas = canvas2.create_window(70, 70,
                                                    anchor="nw",
                                                    window=customMessage, width=215)       
    # Text
    minutesText = Label( settings, text="Minutes", fg="#000000")
    minutesText.place(x = 10, y = 10)
    secondsText = Label( settings, text="Seconds", fg="#000000")
    secondsText.place(x = 10, y = 40)
    messageText = Label( settings, text="Message", fg="#000000")
    messageText.place(x = 10, y = 70)
    # Buttons
    setTimer = Button( settings, text="Soft Timer", fg="#000000", bg="#f1f1f1", command=lambda:
                        timerFunction(minutesEntry, secondsEntry, customMessage))
    setTimer_canvas = canvas2.create_window(10, 100,
                                            anchor="nw",
                                            window=setTimer, width=135, height=25)
    setTimerHard = Button( settings, text="Hard Timer", fg="#000000", bg="#f1f1f1", command=lambda:
                        timerFunctionHard(minutesEntry, secondsEntry, customMessage))
    setTimerHard_canvas = canvas2.create_window(155, 100,
                                            anchor="nw",
                                            window=setTimerHard, width=135, height=25)
    settings.mainloop()

def timerFunctionHard(minutesEntry, secondsEntry, customMessage):
    minPrimary=int(minutesEntry.get())
    min = int(minPrimary* 60)
    sec=int(secondsEntry.get())
    totalSeconds = min + sec
    timerMessage = customMessage.get()
    time.sleep(int(totalSeconds))
    os.system("shutdown /s /t 1")

def timerFunction(minutesEntry, secondsEntry, customMessage):
    minPrimary=int(minutesEntry.get())
    min = int(minPrimary* 60)
    sec=int(secondsEntry.get())
    totalSeconds = min + sec
    timerMessage = customMessage.get()
    time.sleep(int(totalSeconds))
    winsound.Beep(1000, 3000)
    notification.notify(
        title = "Timer Expired!",
        message = timerMessage,
    )

# Display Buttons
button1_canvas = canvas1.create_window( 10, 60, 
                                        anchor = "nw",
                                        window = button1, height=35, width=232)
  
button2_canvas = canvas1.create_window( 10, 105,
                                        anchor = "nw",
                                        window = button2, height=35, width=232)
  
button3_canvas = canvas1.create_window( 10, 150, anchor = "nw",
                                        window = button3, height=35, width=232)

button4_canvas = canvas1.create_window( 10, 195,
                                        anchor = "nw",
                                        window = button4, height=35, width=232)

button5_canvas = canvas1.create_window( 10, 240,
                                        anchor = "nw",
                                        window = button5, height=35, width=232)

button6_canvas = canvas1.create_window( 10, 285,
                                        anchor = "nw",
                                        window = button6, height=35, width=232)

button7_canvas = canvas1.create_window( 10, 330,
                                        anchor = "nw",
                                        window = button7, height=35, width=232)

buttonA_canvas = canvas1.create_window( 10, 375,
                                        anchor = "nw",
                                        window = buttonA, height=35, width=232)

buttonB_canvas = canvas1.create_window( 10, 420,
                                        anchor = "nw",
                                        window = buttonB, height=35, width=232)

buttonC_canvas = canvas1.create_window( 10, 465,
                                        anchor = "nw",
                                        window = buttonC, height=35, width=232)

button8_canvas = canvas1.create_window( 747, 420,
                                        anchor="nw",
                                        window = button8, height=35, width=232)

button9_canvas = canvas1.create_window( 10, 550,
                                        anchor="nw",
                                        window=button9, height=40, width=235)

button10_canvas = canvas1.create_window( 255, 550,
                                        anchor="nw",
                                        window=button10, height=40, width=235)

button11_canvas = canvas1.create_window( 500, 550,
                                        anchor="nw",
                                        window=button11, height=40, width=235)

button12_canvas = canvas1.create_window( 747, 60,
                                        anchor="nw",
                                        window=button12, height=35, width=232)

button13_canvas = canvas1.create_window( 747, 105,
                                        anchor="nw",
                                        window=button13, height=35, width=232)

button14_canvas = canvas1.create_window( 747, 150,
                                        anchor="nw",
                                        window=button14, height=35, width=232)

button15_canvas = canvas1.create_window( 747, 195,
                                        anchor="nw",
                                        window=button15, height=35, width=232)

button16_canvas = canvas1.create_window( 747, 240,
                                        anchor="nw",
                                        window=button16, height=35, width=232)

button17_canvas = canvas1.create_window( 747, 285,
                                        anchor="nw",
                                        window=button17, height=35, width=232)

button18_canvas = canvas1.create_window( 747, 330,
                                        anchor="nw",
                                        window=button18, height=35, width=232)

button19_canvas = canvas1.create_window( 745, 550,
                                        anchor="nw",
                                        window=button19, height=40, width=235)

button20_canvas = canvas1.create_window( 10, 508,
                                        anchor="nw",
                                        window=button20, height=35, width=480)

button21_canvas = canvas1.create_window( 500, 508,
                                        anchor="nw",
                                        window=button21, height=35, width=480)


def randomGame(output_counter, local_lbl1):
    output = random.randint(1, 10)
    output_counter = 2
    if output_counter > 1:
        local_lbl1.place(x=0, y=1000)
    if output == 1:
        local_lbl1 = Label( root, text="OOTP 23", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 2:
        local_lbl1 = Label( root, text="RPCS3", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 3:
        local_lbl1 = Label( root, text="PCSX2", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 4:
        local_lbl1 = Label( root, text="Valorant", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 5:
        local_lbl1 = Label( root, text="Rocket League", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 6:
        local_lbl1 = Label( root, text="Minecraft", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 7:
        local_lbl1 = Label( root, text="FHM6", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 8:
        local_lbl1 = Label( root, text="GTA:SA", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 9:
        local_lbl1 = Label( root, text="MVP 05", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)
    if output == 10:
        local_lbl1 = Label( root, text="NFL 2k5", bg=s, fg=f, height=1, width=15)
        local_lbl1.configure(font=("Arial", 19))
        local_lbl1.place(x=747, y=465)

# Execute tkinter
root.mainloop()