from importlib.resources import path
import os
import pwd
import pybullet as p
import pybullet_data as pd
import time

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
p.setAdditionalSearchPath(pd.getDataPath()) #used by loadURDF

# while (p.isConnected()):
#   p.stepSimulation()

plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)

ur_file = '/temp3.urdf'
rob2 = p.loadURDF(os.path.abspath('') + "/urdf" + ur_file)
# rob2 = p.loadURDF("temp.urdf")
# rob1 = p.loadURDF(pd.getDataPath() + "/cartpole.urdf")
# print(pd.getDataPath())
print(os.path.abspath('') + "/urdf" + ur_file)

# p.setJointMotorControl2(rob2, 0, controlMode=p.VELOCITY_CONTROL, targetVelocity=0.5)
# p.setJointMotorControl2(rob2, 1, controlMode=p.VELOCITY_CONTROL, targetVelocity=0.5)
for i in range(p.getNumJoints(rob2)):
	p.setJointMotorControl2(rob2, i, controlMode=p.VELOCITY_CONTROL, targetVelocity=1)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

while True:
    p.stepSimulation()
    time.sleep(1.0/240)