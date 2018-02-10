import unittest
from DispJudger import DispJudger



class FTOfJudger(unittest.TestCase):

    def setUp(self):
        self.judger = DispJudger()

    def test_001_step_show_judgemnet_by_range_any(self):
        """
        GIVEN : effect range : ANY
        WHEN  : input any airplane seq
        THEN  : return judge result true
        """
        self.assertTrue(self.judger.is_show(1,'ANY'))

    def test_002_step_show_judgement_by_single_seq(self):
        """
        GIVEN : single seq of effect range : 1
        WHEN  : input airplane seq equal effect range : 1
        THEN  : return judge result true
        """
        self.assertTrue(self.judger.is_show(1,1))


if __name__ == '__main__':
    unittest.main()
