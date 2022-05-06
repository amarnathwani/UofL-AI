import pybullet as p
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)

plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while True:
    p.stepSimulation()
    time.sleep(1.0/240)