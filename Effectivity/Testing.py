import unittest


class DisplayJudger(object):

    def is_show(self,seq,range):
        return True


class FTOfJudger(unittest.TestCase):

    def test_001_step_show_judgemnet_by_range_any(self):
        """
        GIVEN : effect range : ANY
        WHEN  : input any airplane seq
        THEN  : return judge result true
        """
        judger = DisplayJudger()
        self.assertTrue(judger.is_show(1,'ANY'))




if __name__ == '__main__':
    unittest.main()
