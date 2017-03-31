# -*-  coding=utf-8 -*-
#
import time
from threading import Thread


class CountdownThread(Thread):
    """docstring for CountdownThread"""

    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        while self.n > 0:
            print('T-minue', self.n)
            self.n -= 1
            time.sleep(2)

import multiprocessing
c = CountdownThread(5)
p = multiprocessing.Process(target=c.run)
p.start()
