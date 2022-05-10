from importlib.resources import path
import os
import pybullet as p
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)

ur_file = '/test.urdf'
rob = p.loadURDF(os.path.abspath('') + "/GA" + ur_file)

for i in range(p.getNumJoints(rob)):
	p.setJointMotorControl2(rob, i, controlMode=p.VELOCITY_CONTROL, targetVelocity=1)

p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while True:
    p.stepSimulation()
    time.sleep(1.0/240)
