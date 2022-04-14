import pybullet
pybullet.connect(pybullet.GUI)
while (pybullet.isConnected()):
  pybullet.stepSimulation()