class DispJudger(object):
    def is_show(self, seq, eff_range):
        if eff_range == 'ANY':
            return True

        for chk in eff_range:

            if isinstance(chk, range):
                if seq in chk:
                    return True

            if seq == chk:
                return True

        return False
