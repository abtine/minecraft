from mcpi.minecraft import Minecraft
mc=Minecraft.create()
xp,yp,zp=mc.player.getTilePos()

def airx(x,y):
    mc.setBlocks(x,y,zp,x,y+2,zp,0)


def airz(z,y):
    mc.setBlocks(xp,y,z,xp,y+2,z,0)


def isAirx(x,y):
    if mc.getBlock(x,y,zp) == 0:
        return True
    else:
        return False

def isAirz(z,y):
    if mc.getBlock(xp,y,z) == 0:
        return True
    else:
        return False
    
    
    

def Mine(x,y,z,direction,size):
    if size >= yp+50:
        mc.postToChat("it is too big")
    if direction == "North":
        for i in range(size):
            airz(z-(i+1),y-(i+1))
            mc.setBlock(x,y-(i+2),z-(i+1),67,2) #stairs
        mc.setBlock(x,y-1,z,67,2)
        for i in range(size//5):
            mc.setBlock(x,y-(1+i)*5,z-(1+i)*5,50,2) #torches
        for i in range(size):
            if isAirz(z-(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        mc.postToChat("Work Done")
    if direction == "South":
        for i in range(size):
            airz(z+(i+1),y-(i+1))
            mc.setBlock(x,y-(i+2),z+(i+1),67,3)
        mc.setBlock(x,y-1,z,67,3)
        for i in range(size//5):
            mc.setBlock(x,y-(1+i)*5,z+(1+i)*5,50,1) 
        for i in range(size):
            if isAirz(z+(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        mc.postToChat("Work Done")
    if direction == "East":
        for i in range(size):
            airx(x+(i+1),y-(i+1))
            mc.setBlock(x+(i+1),y-(i+2),z,67,1)
        mc.setBlock(x,y-1,z,67,1)
        for i in range(size//5):
            mc.setBlock(x+(1+i)*5,y-(1+i)*5,z,50,4) 
        for i in range(size):
            if isAirx(x-(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        mc.postToChat("Work Done")
    if direction == "West":
        for i in range(size):
            airx(x-(i+1),y-(i+1))
            mc.setBlock(x-(i+1),y-(i+2),z,67,0)
            mc.setBlock(x,y-1,z,67,0)
        for i in range(size//5):
            mc.setBlock(x-(1+i)*5,y-(1+i)*5,z,50,3)
        for i in range(size):
            if isAirx(x-(1+i),y-(1+i)) is False:
                Mine(x,y,z,direction,size)
        mc.postToChat("Work Done")


#Mine(xp,yp,zp,"South",23) Exemple


            
    
            
        
            
            
            
        