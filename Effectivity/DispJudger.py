class DispJudger(object):
    def is_show(self, seq, effect_range):
        if effect_range == 'ANY':
            return True

        for chk_elemt in effect_range:

            chk_elemt = chk_elemt if isinstance(chk_elemt, range) else [chk_elemt]

            if seq in chk_elemt:
                return True

        return False
