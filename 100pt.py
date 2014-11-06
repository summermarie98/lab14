#########################################
#
#    100pt - Putting it together!
#
#########################################

# Animate the target area to bounce from left to right.
# Add in buttons for movement left, right, up and down
# Add in boundary detection for the edges (don't let the player move off screen)
# Add in colision detection - and STOP the target when you catch it!

from Tkinter import *
root = Tk()
# Create our drawpad and oval
drawpad = Canvas(root, width=480,height=320, background='white')
targetx1 = 200
targety1 = 20
targetx2 = 280
targety2 = 80
target = drawpad.create_rectangle(targetx1,targety1,targetx2,targety2, fill="blue")
player = drawpad.create_rectangle(240,240,260,260, fill="pink")



class MyApp:
	def __init__(self, parent):
	        # Make sure the drawpad is accessible from inside the function
	        global drawpad
		self.myParent = parent  
		self.myContainer1 = Frame(parent)
		self.myContainer1.pack()
		
		self.button1 = Button(self.myContainer1)
		self.button1.configure(text="Up", background= "green")
		self.button1.grid(row=0,column=0)
		
		self.button2 = Button(self.myContainer1)
		self.button2.configure(text="Left", background= "purple")
		self.button2.grid(row=0,column=0)
		self.button2.bind("<Button-1>", self.button2Click)
		
		self.button3 = Button(self.myContainer1)
		self.button3.configure(text="Down", background= "pink")
		self.button3.grid(row=0,column=0)
		self.button3.bind("<Button-1>", self.button3Click)
		
		self.button4 = Button(self.myContainer1)
		self.button4.configure(text="Right", background= "blue")
		self.button4.grid(row=0,column=0)	
		# "Bind" an action to the first button												
		self.button4.bind("<Button-1>", self.button4Click)

		  
		# This creates the drawpad - no need to change this 
		drawpad.pack()
		

		
	def button1Click(self, event):   
                # "global" makes sure that we can access our oval and our drawpad
		global player
		global drawpad
                drawpad.move(player,0,-20)
		
		# Get the coords of our target


		# Ensure that we are doing our collision detection
		# After we move our object!
                didWeHit = collisionDetect()
                if(didWeHit == True):
                    # We made contact! Stop our animation!
                    print "Do something"
	# Use a function to do our collision detection
	# This way we only have to write it once, and call it from
	# every button click function.
	def collisionDetect(self):
                global oval
		global drawpad
                x1,y1,x2,y2 = drawpad.coords(player)
                if x1 == 0 or x2>=drawpad.winfo_width() or y1==0 or y2>=drawpad.winfo_height():

                # Do your if statement - remember to return True if successful!
            
myapp = MyApp(root)

root.mainloop()