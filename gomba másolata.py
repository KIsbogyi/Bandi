def printer():
    print("nem tudom mit fog csinálni!")
def creatorcreator():
    button=tk.Button(mw, text='Nem vagyok buzi' , width=75, command=mw.destroy)
    button.pack()

def ablakk():
    mw=tk.Tk()

    mw.option_add("*Button.Background", "pink")
    mw.option_add("*Button.Foreground", "purple")

    mw.title('NÉV')

    mw.geometry('500x500')
    mw.resizable(0,0)

    button3= tk.Button(mw, text='A sült kacsa finom', width=42, command=printer)
    button4= tk.Button(mw, text='Elmentem enni!', width=42, command=mw.destroy)
    button4.pack()
    button3.pack()
    mw.mainloop()
    
##r = Tk()
##r.geometry = (800,800)
##r.title('Making Buttons')
##r.geometry("800x800")
##r.resizable(0,0)
####back = Frame(master=r, width=500, height=500, bg='black')
####back.pack()
##button = Button(r, text='Stop', width=50, command=r.destroy)
##button2 = Button(r, text='Source', width=50, command=createcreator()) 
##button.pack()
##button2.pack()
##r.mainloop()

import tkinter as tk

def startgame():

    pass

mw = tk.Tk()

#If you have a large number of widgets, like it looks like you will for your
#game you can specify the attributes for all widgets simply like this.
mw.option_add("*Button.Background", "purple")
mw.option_add("*Button.Foreground", "pink")

mw.title('Az magyar fordítása rossz')
#You can set the geometry attribute to change the root windows size
mw.geometry("500x500") #You want the size of the app to be 500x500
mw.resizable(0, 0) #Don't allow resizing in the x or y direction


button2 = tk.Button(mw, text='Kacsa', width=50, command=ablakk)
button3= tk.Button(mw, text='You are gay', width=50, command=creatorcreator)

button2.pack()
button3.pack()
mw.mainloop()

