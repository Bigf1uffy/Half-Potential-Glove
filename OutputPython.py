global IsActive
IsActive = 1


#Libraries
import tkinter as tk
import serial # type: ignore
import subprocess
import pyautogui # type: ignore
import webbrowser
import threading

#types
global ButtonOneType
global ButtonTwoType
global ButtonThreeType
global ButtonFourType
ButtonOneType = ""
ButtonTwoType = ""
ButtonThreeType = ""
ButtonFourType = ""

#Bottom Sector (Image)
root = tk.Tk()

c = tk.Canvas(root, width=450, height=500)
c.pack()
c.config(background="#C8C8C8")
Bottom_Sector = c.create_rectangle(10,490,445,290, fill="#B2B2B2", outline="#6C6C6C", width=2)

#submite button for char Button One
Button1Remap = tk.Text(root, width="5", height="2")
Button1Remap.place(x=80,y=30)
def Button1RemapFunc():
    global ValueOne
    global ButtonOneType
    ValueOne = Button1Remap.get("1.0")
    print("New Action: ", {ValueOne})
    ButtonOneType = "Letter"
    print(ButtonOneType)

Button1 = tk.Button(
    root,
    text="Middle Button Rebind",
    command=Button1RemapFunc
    )
Button1.place(x=75, y=60)
Button1.config(highlightbackground="#CAC8C8")

print("test")

root.title("Glove Remaper")
root.resizable(width=False, height=False)
#Ending

duckclicker = "https://www.duckclicker.fun"
ser = serial.Serial("COM5", 9600)
print("Python Systems Active v2")

def Middle():
    if ButtonOneType == "Letter":
        print(ValueOne)
        pyautogui.keyDown(ValueOne)
    else:
        pyautogui.moveTo(1596, 262)

def Move_Duck():
    pyautogui.moveTo(867, 663)

def Check_Input():
    line = ser.readline().decode('latin1').strip()
    if line == "CLICK":
        if IsActive == 1:
            print("ALL SYSTEMS ACTIVE")
            IsActive = 0
        pyautogui.click()
        print("Click")
    elif line == "MIDDLE":
        print("Middle Finger Pressed")
        Middle()
    elif line == "RING":
        print("Ring Finger Pressed")
        Move_Duck()
    elif line == "OPEN_DC":
        print("Opening Duck Clicker")
        webbrowser.open(duckclicker)
    timer = threading.Timer(0.02, Check_Input)
    timer.start()

Check_Input()
root.mainloop()
#Coords:
#Bread: 1596, 262
#duck: 867, 663
#Gramps: 1558, 629