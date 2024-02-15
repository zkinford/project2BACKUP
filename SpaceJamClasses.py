from direct.showbase.ShowBase import ShowBase
from panda3d.core import *

class Planet(ShowBase):
    self.modelNode = loader.loadmodel(modelPath)
    self.modelNode.reparentTo(parentNode)
    self.modelNode.setPos(posVec)
    self.modelNode.setScale(scaleVec)

    self.modelNode.setName(nodeName)
    tex = loader.loadTexture(texPath)
    self.modelNode.setTexture(tex, 1)

class Drone(ShowBase):
    droneCount = 0