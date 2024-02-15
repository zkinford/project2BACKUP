from direct.showbase.ShowBase import ShowBase
import DefensePaths as defensePaths
import SpaceJamClasses as spaceJamClasses


class SpaceJam(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.SetScene()

    def SetScene(self):
        self.Universe = self.loader.loadModel("./Assets/Universe/Universe.x")
        self.Universe.reparentTo(self.render)
        self.Universe.setScale(15000)
        tex = self.loader.loadTexture("./Assets/Universe/Universe.jpg")
        self.Universe.setTexture(tex, 1)

        self.Planet1 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet1.reparentTo(self.render)
        self.Planet1.setPos(150, 5000, 67)
        self.Planet1.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet1.jpg")
        self.Planet1.setTexture(tex, 1)

        self.Planet2 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet2.reparentTo(self.render)
        self.Planet2.setPos(1500, -4000, -67)
        self.Planet2.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet2.jpg")
        self.Planet2.setTexture(tex, 1)

        self.Planet3 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet3.reparentTo(self.render)
        self.Planet3.setPos(1550, 13000, 20)
        self.Planet3.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet3.jpg")
        self.Planet3.setTexture(tex, 1)
        
        self.Planet4 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet4.reparentTo(self.render)
        self.Planet4.setPos(550, 1000, 0)
        self.Planet4.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet4.jpg")
        self.Planet4.setTexture(tex, 1)

        self.Planet5 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet5.reparentTo(self.render)
        self.Planet5.setPos(-400, -6000, 150)
        self.Planet5.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet5.jpg")
        self.Planet5.setTexture(tex, 1)

        self.Planet6 = self.loader.loadModel("./Assets/Planets/protoPlanet.x")
        self.Planet6.reparentTo(self.render)
        self.Planet6.setPos(2457, 5000, 100)
        self.Planet6.setScale(350)
        tex = self.loader.loadTexture("./Assets/Planets/Planet6.jpg")
        self.Planet6.setTexture(tex, 1)

        self.Station = self.loader.loadModel("./Assets/Space Station/spaceStation.x")
        self.Station.reparentTo(self.render)
        self.Station.setPos(1000, 2000, 67)
        self.Station.setScale(10)
        tex = self.loader.loadTexture("./Assets/Space Station/SpaceStation1_Dif2.png")
        self.Station.setTexture(tex, 1)

        self.Ship = self.loader.loadModel("./Assets/Spaceships/theBorg.x")
        self.Ship.reparentTo(self.render)
        self.Ship.setPos(150, 2000, 67)
        self.Ship.setScale(1)
        tex = self.loader.loadTexture("./Assets/Spaceships/theBorg.jpg")
        self.Ship.setTexture(tex, 1)

        fullCycle = 60
        for j in range(fullCycle):
            spaceJamClasses.Drone.droneCount += 1
            nuckName = "Drone" + str(spaceJamClasses.Drone.droneCount)
            self.DrawcloudDefense(self.Planet1, nickName)
            unitVec = defensePaths.Cloud()
            unitVec.normalize()
            position = unitVec * 500 + centralObject.modelNode.getPos()
            spaceJamClasses.Drone(self.loader, "./Assets/DroneDefender/DroneDefender.obj", self.render, droneName, "")
        


        

app = SpaceJam()
app.run()
