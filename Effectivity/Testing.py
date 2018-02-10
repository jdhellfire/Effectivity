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
        self.assertTrue(self.judger.is_show(1, 'ANY'))

    def test_002_step_show_judgement_by_single_seq(self):
        """
        GIVEN : single seq of effect range : 1
        WHEN  : input airplane seq equal effect range : 1
        THEN  : return judge result true
        """
        self.assertTrue(self.judger.is_show(1, [1]))

    def test_003_step_show_judgement_by_single_seq(self):
        """
        GIVEN : single seq of effect range : 1
        WHEN  : input airplane seq not equal effect range : 2
        THEN  : return judge result false
        """
        self.assertFalse(self.judger.is_show(2, [1]))

    def test_004_step_show_judgement_by_multi_seq(self):
        """
        GIVEN : multi seq of effect range : 1,100,200
        WHEN  : input airplane seq in effect range : 100
        THEN  : return judge result true
        """
        self.assertTrue(self.judger.is_show(100, [1, 100, 200]))


if __name__ == '__main__':
    unittest.main()
