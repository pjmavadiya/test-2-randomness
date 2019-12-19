
import unittest 
from randomness import lottery_game

class RandomnessTest(unittest.TestCase): 

    #Test case to check, its not returning duplicate ball number
    def test_repeat_ball(self):
        l_g_1 = lottery_game()
        if len(l_g_1) == len(set(l_g_1)):
            self.assertTrue(True)
        else:
            self.assertTrue(False)

    #Test case to check, both consicutive drow are not same
    def test_previous_output(self):
        l_g_1 = lottery_game()
        l_g_2 = lottery_game()
        if l_g_1 == l_g_2:
            self.assertTrue(False)
        else:
            self.assertTrue(True)

    #Test case to check, both consicutive drow has not more then 5 ball matching
    def test_intersection_output(self):
        l_g_1 = lottery_game()
        l_g_2 = lottery_game()
        intersection_length = len(list(set(l_g_1) & set(l_g_2)))
        if intersection_length > 5:
            self.assertTrue(False)
        else:
            self.assertTrue(True)


if __name__ == '__main__': 
    unittest.main() 