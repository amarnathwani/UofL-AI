import pybullet as p 
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setAdditionalSearchPath(pd.getDataPath())

p.createCollisionShape(p.GEOM_PLANE) # the floor
p.createMultiBody(0, 0)

ur_file = 'r2d2.urdf'
creatureId = p.loadURDF(ur_file)

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while True:
    p.stepSimulation()
    time.sleep(1.0/240)