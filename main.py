import numpy as np
from time import time
import multiprocessing as mp
import pdb
from multiprocessing import Process


# Prepare data
np.random.RandomState(100)
arr = np.random.randint(0, 10, size=[200000, 5])
data = arr.tolist()
data[:5]

class Model:

    def __init__(self):
        self.result = []

    def contraint_programing(self, row, minimum, maximum):
        """Returns feasible solution"""
        # print(row)
        count = 0
        for n in row:
            if minimum <= n <= maximum:
                count = count + 1
        return count

model = Model()
results = []

pool = mp.Pool(mp.cpu_count())
# results = [pool.apply(model.contraint_programing, args=(row, 4, 8)) for row in data]
# pool.close()
for row in data:
    p = Process(target=model.contraint_programing, args=(row, 4, 8))
    p.start()
    p.join()

# print(results[:10])