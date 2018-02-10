from functools import reduce


class DispJudger(object):
    def is_show(self, seq, effect_elemts):

        return True if effect_elemts == 'ANY' \
                    else reduce(lambda x, y: x | y,
                         map(lambda elemt: True if seq in list(elemt if isinstance(elemt, range) else [elemt]) else False,
                         effect_elemts))
