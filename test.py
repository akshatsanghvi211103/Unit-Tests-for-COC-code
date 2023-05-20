import unittest

import sys
sys.path.append('..')

import king
import village
import points as pt
import buildings as bd

class TestKingMovement(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        file = open("output.txt", "w+")
        file.close()

    def run(self, result=None):
        unittest.TestCase.run(self, result)
        print(len(result.failures) + len(result.errors))
        if(len(result.errors) + len(result.failures) >= 1):
            file2 = open("output.txt", "w+")
            file2.write("False")
            file2.close()
    
    @classmethod
    def tearDownClass(self):
        file = open("output.txt", "r")
        str = file.read()
        file.close()
        file = open("output.txt", "a+")
        if str != "False":
            file.write("True")
        file.close()

    def setUp(self):
        self.village = village.createVillage(1)
        self.vmap = self.village.map
    
    def test_moving_left(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                finalPos = [i, j]
                self.king.move('left', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0]
                    c = finalPos[1] - 1
                    if(c < 0):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[1] -= 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'left', "incorrect facing direction")
    
    def test_moving_right(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                finalPos = [i, j]
                self.king.move('right', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0]
                    c = finalPos[1] + 1
                    if(c >= len(self.vmap[0])):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[1] += 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'right', "incorrect facing direction")

    def test_moving_up(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                finalPos = [i, j]
                self.king.move('up', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0] - 1
                    c = finalPos[1]
                    if(r < 0):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[0] -= 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'up', "incorrect facing direction")

    def test_moving_down(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                finalPos = [i, j]
                self.king.move('down', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0] + 1
                    c = finalPos[1]
                    if(r >= len(self.vmap)):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[0] += 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'down', "incorrect facing direction")

    def test_moving_left_dead_king(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                self.king.alive = False
                finalPos = [i, j]
                self.king.move('left', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0]
                    c = finalPos[1] - 1
                    if(c < 0):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[1] -= 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'left', "incorrect facing direction")
    
    def test_moving_right_dead_king(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                self.king.alive = False
                finalPos = [i, j]
                self.king.move('right', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0]
                    c = finalPos[1] + 1
                    if(c >= len(self.vmap[0])):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[1] += 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'right', "incorrect facing direction")

    def test_moving_up_dead_king(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                self.king.alive = False
                finalPos = [i, j]
                self.king.move('up', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0] - 1
                    c = finalPos[1]
                    if(r < 0):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[0] -= 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'up', "incorrect facing direction")

    def test_moving_down_dead_king(self):
        for i in range(len(self.vmap)):
            for j in range(len(self.vmap[0])):
                self.king = king.King([i, j])
                self.king.alive = False
                finalPos = [i, j]
                self.king.move('down', self.village)
                if (self.king.alive == False):
                    self.assertEqual(finalPos, self.king.position, "dead king is attacking")
                    continue
                for k in range(self.king.speed):
                    r = finalPos[0] + 1
                    c = finalPos[1]
                    if(r >= len(self.vmap)):
                        continue
                    if(self.vmap[r][c] != pt.BLANK and self.vmap[r][c] != pt.SPAWN):
                        break
                    finalPos[0] += 1
                
                self.assertEqual(self.king.position, finalPos, "incorrect position")
                self.assertEqual(self.king.facing, 'down', "incorrect facing direction")


unittest.main()
# runner = unittest.TextTestRunner(verbosity=0, stream=file)
# unittest.main(testRunner=runner)
