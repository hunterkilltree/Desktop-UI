

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

myLabel = Label(root, text="Hello world!")

myLabel.pack()

root.mainloop()






