import unittest

import sys
sys.path.append('..')

import king
import village
import points as pt
import buildings as bd

def test_attack_func(self):
    # check the attack on each target classes
    self.king.facing = 'right'
    hut = bd.Hut([0, 1], self.village)
    prevHutHealth = hut.health
    self.king.attack_target(hut, self.king.attack)
    if (self.king.alive == False):
        self.assertEqual(hut.health, prevHutHealth, "attack even when king is dead")
        return
    if (hut.health < 0):
        self.assertEqual(hut.health, 0, "incorrect health")
        return
    if (hut.health == 0):
        self.assertEqual(self.vmap[0][1], pt.BLANK, "incorrect map")
        self.assertEqual(hut.destroyed, True, "incorrect alive value")
        return
    self.assertEqual(hut.health, prevHutHealth - self.king.attack, "incorrect damage recieved")

class TestKingAttack(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        file = open("output_bonus.txt", "w+")
        file.close()

    def run(self, result=None):
        unittest.TestCase.run(self, result)
        print(len(result.failures) + len(result.errors))
        if(len(result.errors) + len(result.failures) >= 1):
            file2 = open("output_bonus.txt", "w+")
            file2.write("False")
            file2.close()
    
    @classmethod
    def tearDownClass(self):
        file = open("output_bonus.txt", "r")
        str = file.read()
        file.close()
        file = open("output_bonus.txt", "a+")
        if str != "False":
            file.write("True")
        file.close()

    
    def setUp(self):
        self.village = village.createVillage(1)
        self.vmap = self.village.map
        self.king = king.King([0, 0])

    def test_attack_when_king_dead(self):
        self.king.alive = False
        test_attack_func(self)

    def test_attack_when_king_alive(self):
        test_attack_func(self)
    resutl = unittest.TestResult()

unittest.main()