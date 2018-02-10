class DispJudger(object):
    def is_show(self, seq, effect_range):
        if effect_range == 'ANY':
            return True

        for chk_elemt in effect_range:

            if seq in list(chk_elemt if isinstance(chk_elemt, range) else [chk_elemt]):
                return True

        return False
