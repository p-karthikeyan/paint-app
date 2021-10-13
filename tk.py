from tkinter import *

clr='black'
thick=1
mode=True
cur_x,cur_y=0,0
def locate(event):
	global cur_x,cur_y
	cur_x,cur_y=event.x,event.y
def drawline(event):
	global cur_x,cur_y
	canvas.create_line((cur_x,cur_y,event.x,event.y),fill=clr,width=thick)
	if mode:
		cur_x,cur_y=event.x,event.y
def thickness(recent):
	global thick
	thick=recent
def show_clr(new_clr):
	global clr
	clr=new_clr
def advance():
	global mode
	mode=False
def beginers():
	global mode
	mode=True
def new_scrn():
	canvas.delete('all')
	global clr,thick,mode
	mode=True
	clr='black'
	thick=1
	colour_plate()

window=Tk()
window.title('Your Art')
window.state('zoomed')
window.rowconfigure(0,weight=1)
window.columnconfigure(0,weight=1)

menubar=Menu(window)
window.config(menu=menubar)
submenu=Menu(menubar)
nxtmenu=Menu(menubar)
menubar.add_cascade(label='File',menu=submenu)
menubar.add_cascade(label='Mode',menu=nxtmenu)
submenu.add_command(label='New Art',command=new_scrn)
nxtmenu.add_command(label='beginers',command=beginers)
nxtmenu.add_command(label='Advanced',command=advance)
canvas=Canvas(window,background='white')
canvas.grid(row=0,column=0,sticky='nsew')

def colour_plate():
	id=canvas.create_rectangle((10,10,30,30),fill='white')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('white'))
	id=canvas.create_rectangle((10,40,30,60),fill='blue')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('blue'))
	id=canvas.create_rectangle((10,70,30,90),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('black'))
	id=canvas.create_rectangle((10,100,30,120),fill='gray')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('gray'))
	id=canvas.create_rectangle((10,130,30,150),fill='orange')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('orange'))
	id=canvas.create_rectangle((10,160,30,180),fill='brown')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('brown'))
	id=canvas.create_rectangle((10,190,30,210),fill='green')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('green'))
	id=canvas.create_rectangle((10,220,30,240),fill='yellow')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('yellow'))
	id=canvas.create_rectangle((10,250,30,270),fill='purple')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('purple'))
	id=canvas.create_rectangle((10,280,30,300),fill='pink')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('pink'))
	id=canvas.create_rectangle((10,310,30,330),fill='violet')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('violet'))
	id=canvas.create_rectangle((10,340,30,360),fill='red')
	canvas.tag_bind(id,'<Button-1>',lambda x:show_clr('red'))
	id=canvas.create_rectangle((19,400,21,402),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:thickness(2))
	id=canvas.create_rectangle((17,420,23,426),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:thickness(6))
	id=canvas.create_rectangle((15,440,25,450),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:thickness(10))
	id=canvas.create_rectangle((10,470,30,490),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:thickness(20))
	id=canvas.create_rectangle((5,510,35,540),fill='black')
	canvas.tag_bind(id,'<Button-1>',lambda x:thickness(30))


canvas.bind('<Button-1>',locate)
canvas.bind('<B1-Motion>',drawline)

colour_plate()
window.mainloop()
