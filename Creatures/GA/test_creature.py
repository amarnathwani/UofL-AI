import unittest
import creature
# import pybullet as p

class TestCreature(unittest.TestCase):
    def testCreatExists(self):
        self.assertIsNotNone(creature.Creature)

    def testCreatureGetFlatLinks(self):
        c = creature.Creature(gene_count=4)
        links = c.get_flat_links()
        self.assertEqual(len(links), 4)

    def testExpLinks(self):
        c = creature.Creature(gene_count=25)
        links = c.get_flat_links()
        exp_links = c.get_expanded_links()
        self.assertGreaterEqual(len(exp_links), len(links))

    def testToXMLNotNone(self):
        c = creature.Creature(gene_count=2)
        xml_str = c.to_xml()
        self.assertIsNotNone(xml_str)

    def testLoadXML(self):
        c = creature.Creature(gene_count=20)
        xml_str = c.to_xml()
        with open('test2.urdf', 'w') as f:
            f.write(xml_str)
        # p.connect(p.DIRECT)
        # cid = p.loadURDF('test.urdf')
        self.assertIsNotNone(xml_str)
      
    def testMotor(self):
        m = creature.Motor(0.1, 0.5, 0.5)
        self.assertIsNotNone(m)

    def testMotorVal(self):
        m = creature.Motor(0.1, 0.5, 0.5)
        self.assertEqual(m.get_output(), 1)

    def testMotorVal2(self):
        m = creature.Motor(0.6, 0.5, 0.5)
        m.get_output()
        m.get_output()     
        self.assertGreater(m.get_output(), 0)

    def testCMot(self):
        c = creature.Creature(gene_count=4)
        ls = c.get_expanded_links()
        ms = c.get_motors()
        self.assertEqual(len(ls) - 1, len(ms))

unittest.main()