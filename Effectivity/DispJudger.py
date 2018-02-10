class DispJudger(object):

    def is_show(self,seq,range):
        if range == 'ANY':
            return True

        if seq == range:
            return True
