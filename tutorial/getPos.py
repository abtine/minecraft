##Author: Raphael Holzer
##Organisation: Gymnase du Bugnon
##Date: 4. 1. 2018

from mcpi import minecraft

mc = minecraft.Minecraft.create()

mc.postToChat("Get position")
pos = mc.player.getPos()
print(pos)
mc.postToChat(pos)
