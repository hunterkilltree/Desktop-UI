

### button
### Stop
### Reset
### Generate (create random obstacles)
### Move (moving by click step by step)
### Start (find the path to the destination)



### drop down menu
### Start coordinate (setup postion of robots by mouse)
### Goal coordinate (setup postion (blue point of destination by mouse)
### Obstacle Coordinate (setup multiple ostacles in by mouse)
### Station Coordinate  (The  robot will pick up the product at the blue point and carry the
### to the stations with the shortest path.


### text box
### robot coordinate [x y]
### goal coordinate [x y]

### Note 1:
'''
In the start coordinate mode, I can setup many robot as I want to.
The server will find the best robot to the goal coordinate.
if robot > destination some robot will not move.
'''


### This is example of the very general case
### I will narrow the problem by setup the specific warehouse with given positon of  station, pick up place,
### charge station

### Should random custome or fix postion of station and  where is the object pick up
from tkinter import *

# root widget
root = Tk()
root.title("ControlUI")
root.iconbitmap("images/Robot2.ico")
e = Entry(root, width=50, borderwidth=5) # input field

# e.insert
# e.delete
# my_img = ImageTk.PhotoImage(Image.open("images/Robot2.png")) ## UI label
# my_label = Label(image=my_img)
# my_label.pack()

def printHello():
    print("Hello on terminal {}".format(e.get())) # .get get the value in the input field


frame = LabelFrame(root, text="This is frame", padx=50, pady=50)
frame.pack(padx=10, pady=10)

myLabel1 = Label(root, text="Hello world!")
myLabel2 = Label(root, text="Hello VietNam!")
myButton1 = Button(root, text="Click here", command=printHello)
# myButton1 = Button(root, text="Click here", command= Lambda: printHello())


# myLabel1.grid(row=0, column=0) # grid or pack
# myLabel2.grid(row=1, column=0)
# myButton1.grid(row=2, column=0)
# e.grid(row=3, column=0)

r = IntVar()
Radiobutton(root, text="Option 1", variable=r, value="1").pack()
Radiobutton(root, text="Option 1", variable=r, value="2").pack()



button_quit = Button(frame, text="Exit", command=root.quit)
button_quit.pack()
root.mainloop()






