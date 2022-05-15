from importlib.resources import path
import os
import pybullet as p
import pybullet_data as pd
import time
import genome
import creature
import random

p.connect(p.GUI)
p.setPhysicsEngineParameter(enableFileCaching=0)
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)

plane_shape = p.createCollisionShape(p.GEOM_PLANE)
floor = p.createMultiBody(plane_shape, plane_shape)
p.setGravity(0, 0, -10)
p.setRealTimeSimulation(1)

# generate a random creature
cr = creature.Creature(gene_count=3)
cr.update_position([0,0,0])

# save it to XML
with open('test.urdf', 'w') as f:
    # cr.get_expanded_links()
    f.write(cr.to_xml())

# load it into the sim
ur_file = '/test.urdf'
rob1 = p.loadURDF(os.path.abspath('') + ur_file)

# iterate 
while True:
    p.stepSimulation()

    motors = cr.get_motors()
    assert len(motors) == p.getNumJoints(rob1), "Something went wrong"
    for jid in range(p.getNumJoints(rob1)):
        mode = p.VELOCITY_CONTROL
        vel = 5 * (random.random() - 0.5)
        p.setJointMotorControl2(rob1, 
                        jid,  
                        controlMode=mode, 
                        targetVelocity=vel)
        pos, orn = p.getBasePositionAndOrientation(rob1)
        cr.update_position(pos)
        print(cr.get_distance_travelled())
                        
    time.sleep(1.0/240)