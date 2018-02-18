#----------------------------------------------
# Stay Alive!
# More programs at UsingPython.com/programs
#----------------------------------------------

#import the modules we need, for creating a GUI
import tkinter

#only press return once
okToPressReturn = True

#the player's attributes.
happiness = 100
hunger = 20

#-------------------------------------------------------------------

def startGame(event):

    global okToPressReturn

    if okToPressReturn == False:
        pass    
        
    
    else:
        #update the time left label.
  
        #start updating the values
        updateHunger()
        updateDay()
        updateDisplay()

        okToPressReturn = False

#-------------------------------------------------------------------
 
def updateDisplay():

    #use the globally declared variables above.
    global happiness
    global hunger

    if happiness <= 50: 
        catPic.config(image = hungryphoto)
        startLabel.config(text="Not a happy cat anymore!")
    if  hunger <= 95 and hunger >= 50 and happiness >= 50 and happiness <= 100:
        catPic.config(image = normalphoto)
        startLabel.config(text=" ")

    #update the time left label.
    hungerLabel.config(text="happiness: " + str(happiness))

    #update the day' label.
    dayLabel.config(text="hunger: " + str(hunger))   

    #run the function again after 100ms.       
    catPic.after(100, updateDisplay)

#-------------------------------------------------------------------
 
def updateHunger():

    #use the globally declared variables above.
    global happiness

    #decrement the hunger.
    happiness -= 1

    if isAlive():
        #run the function again after 500ms.
        hungerLabel.after(500, updateHunger)

#-------------------------------------------------------------------

def updateDay():

    #use the globally declared variables above.
    global hunger

    #decrement the hunger.
    hunger -= 1

    if isAlive():
        #run the function again after 5 seconds.
        dayLabel.after(500, updateDay)

#-------------------------------------------------------------------

def play():

    global happiness
    
    if happiness <= 100:
        happiness += 20
    else:
               startLabel.config(text="Too much playing will make her tired!")
               catPic.config(image = sleepyphoto)
#-------------------------------------------------------------------
def feed():

    global hunger
    
    if hunger <= 95:
        hunger += 20
    else:
        startLabel.config(text="She is food babying right now")
        catPic.config(image = foodphoto)
#-------------------------------------------------------------------


def isAlive():

    global happiness
    
    if happiness <= 0 or hunger <= 0:
        #update the start info label.
        startLabel.config(text="GAME OVER! She doesn't love you anymore")     
        return False
    else:
        return True
        
#-------------------------------------------------------------------


#create a GUI window.
root = tkinter.Tk()
#set the title.
root.title("Happy Cat")
#set the size.
root.geometry("600x500")

#add a label for the start text.
startLabel = tkinter.Label(root, text="Press 'Enter' to start playing!", font=('Helvetica', 12))
startLabel.pack()

#add a hunger label.
hungerLabel = tkinter.Label(root, text="Happy Cat: " + str(happiness), font=('Helvetica', 12))
hungerLabel.pack()

#add a 'day' label.
dayLabel = tkinter.Label(root, text="Hunger: " + str(hunger), font=('Helvetica', 12))
dayLabel.pack()

sadphoto = tkinter.PhotoImage(file="sad.gif")
normalphoto = tkinter.PhotoImage(file="normal.gif")
foodphoto = tkinter.PhotoImage(file="foodbaby.gif")
sleepyphoto = tkinter.PhotoImage(file="sleepy.gif")

#add a cat image
catPic = tkinter.Label(root, image=normalphoto)
catPic.pack()

btnFeed = tkinter.Button(root, text="Play", command=play)
btnFeed.pack()
btnFeed = tkinter.Button(root, text="Feed", command=feed)
btnFeed.pack()

#run the 'startGame' function when the enter key is pressed.
root.bind('<Return>', startGame)

#start the GUI
root.mainloop()
