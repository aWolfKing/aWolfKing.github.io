
def drawObj(object):
    try:
        object.render()
        
    except AttributeError:
        pass
def drawall():
    global objects
    for curr_obj  in objects:
        drawObj(objects[curr_obj])
    

class PixelRect():
    PosX = 0
    PosY = 0
    CamouflageRate = 4 #4
    def __init__(self, x=PosX,y=PosY, crate=CamouflageRate):
         self.PosX = x
         self.PosY = y 
         self.CamouflageRate = crate 
         
    def render(self):
        #fill(255,255,255)
        
        for int_iX in range(0,30):
            for int_iY in range (0,30):
                noStroke()
                fill( get(int(self.PosX+int_iX), int(self.PosY+int_iY)) + color(self.CamouflageRate,self.CamouflageRate,self.CamouflageRate))
                rect(self.PosX+int_iX, self.PosY+int_iY, 1,1)
                
                
class Notification():
    txt = ""
    PosX = 200
    PosY = 30
    def __init__(self, t=txt, x=PosX,y=PosY):
        self.txt = t
        self.PosX = x
        self.PosY = y
    def render(self):
        textSize(30)
        fill(0,0,0)
        text(self.txt, self.PosX, self.PosY)
    
        
def setup():
    global objects, bgColors, paused, canClaim, bans, claimedBy, foundBy, DebugMode, BoxSpeed, DebugVal
    
    BoxSpeed = 1
    
    #Debugging
    
    DebugMode = True
    DebugVal = [
                False, #XAxisLine
                False, #YAxisLine
                ]
    
    #end Debugging
    
    foundBy = 0
    claimedBy = 0
    bans = [False,False]
    canClaim = True
    paused = False
    
    objects = {
               "PixelRect_Main" : PixelRect(100,100, 2),  #100,100,2
               "Notification_Main" : Notification(""),
               "score1" : Notification("0", 50,30),
               "score2" : Notification("0",width-50,30),
               }
    
    size(800,800)
    bgColors = [
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200))
                ]
    
    #pix1 = PixelRect(100,100)
    #drawObj(pix1)
    drawall()
  
    
def Reset():
    global objects, bgColors, paused, bans, claimedBy, foundBy, canClaim, BoxSpeed
    bans = [False,False]
    claimedBy = 0
    foundBy = 0
    
    BoxSpeed = 1
    
    paused = False
    canClaim = True
    
    objects["Notification_Main"].txt = ""
    
    objects["PixelRect_Main"].PosX = 0
    objects["PixelRect_Main"].PosY = int(random(0,height-30))
    bgColors = [
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200)),
                color(random(0,200),random(0,200),random(0,200))
                ]
          
def draw():
    
    background(0,0,0)
    global objects, bgColors, paused, foundBy, BoxSpeed, DebugVal, DebugMode
    
    if(paused == False):
        objects["PixelRect_Main"].PosX += BoxSpeed
        
    
    for int_ii in range(0,4):
        fill(bgColors[int_ii])
        rect(width/4*int_ii, 0,width/4, height)
        
    
    if(DebugMode):
        if(DebugVal[0] == True):
            #noStroke()
            stroke(240)
            fill(230,230,230)
            line(0, objects["PixelRect_Main"].PosY, width, objects["PixelRect_Main"].PosY)
            line(0, objects["PixelRect_Main"].PosY + 30, width, objects["PixelRect_Main"].PosY + 30)
    if(DebugVal[1] == True):
            stroke(240)
            fill(230,230,230)
            line(objects["PixelRect_Main"].PosX, 0, objects["PixelRect_Main"].PosX, height)
            line(objects["PixelRect_Main"].PosX + 30, 0, objects["PixelRect_Main"].PosX + 30, height)  
    
    
    drawall()
    
    if(foundBy != 0 or (bans[0] == True and bans[1] == True)):
        fill(255,255,255)
        rect(objects["PixelRect_Main"].PosX,objects["PixelRect_Main"].PosY, 30,30) 
        BoxSpeed = 3
    
    if(objects["PixelRect_Main"].PosX > width):
        Reset()
        
        
def keyPressed():
    global paused, objects, canClaim, bans, claimedBy, DebugVal, DebugMode
    if(key == 'w' and (canClaim and not bans[0] and claimedBy != 2)):
        paused = True
        canClaim = False
        objects["Notification_Main"].txt = "Player1 thinks he found the box!"
        claimedBy = 1
    if(keyCode == UP and (canClaim and not bans[1] and claimedBy != 1)):
        paused = True
        canClaim = False
        objects["Notification_Main"].txt = "Player2 thinks he found the box!"
        claimedBy = 2
        
    #debug
    if(key == ' ' and (DebugMode)):
        Reset()
    if(key == 'b' and (DebugMode)):
        DebugVal[0] = not DebugVal[0]
    if(key == 'n' and (DebugMode)):
        DebugVal[1] = not DebugVal[1]
            
    
        
def keyReleased():
    global paused, objects, canClaim, bans, claimedBy, DebugMode, DebugVal
    if(key == 's' and (not canClaim and claimedBy == 1 and foundBy == 0)):
        paused = False
        canClaim = True
        objects["Notification_Main"].txt = "Player1 changed his mind..."
        claimedBy = 0
        bans[0] = True
    if(keyCode == DOWN and (not canClaim and claimedBy == 2 and foundBy == 0)):
        paused = False
        canClaim = True
        objects["Notification_Main"].txt = "Player2 changed his mind..."
        bans[1] = True
        claimedBy = 0
        
def mouseClicked():
    global foundBy, claimedBy, paused, canClaim, objects, bans
    if(claimedBy > 0):
        if((bans[claimedBy-1] == False and claimedBy != 0 and paused == True) and (mouseX > objects["PixelRect_Main"].PosX and mouseX < objects["PixelRect_Main"].PosX+30) and (mouseY > objects["PixelRect_Main"].PosY and mouseY < objects["PixelRect_Main"].PosY+30)):
                foundBy = claimedBy
                objects["Notification_Main"].txt = "Player" + str(foundBy) + " found the box!"
                objects["score" + str(foundBy)].txt = str(int(objects["score" + str(foundBy)].txt) + 1)
                paused = False
                bans = [True,True]
        else:
            if(bans[claimedBy-1] == False):
                bans[claimedBy-1] = True
                objects["Notification_Main"].txt = "Player" + str(claimedBy) + " was wrong..."
                paused = False
                claimedBy = 0
                canClaim = True