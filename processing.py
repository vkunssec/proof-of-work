import random
import time
from multiprocessing import Pool

from utils import NPROCESSES, PROOF, TARGET, calculate_hash


def f(identify, t0, data):
    hash = calculate_hash(data)

    print("identify: {} t0: {} hash: {}".format(identify, t0, hash))


    while True:
        if hash[:PROOF] == TARGET:
            break

        hash = calculate_hash(hash)


    dt = time.perf_counter_ns() - t0
    print("identify: {} dt: {:.5f} hash: {}".format(identify, (dt*1E-9), hash))


    return hash


if __name__ == "__main__":
    inarrays = []
    for i in range(NPROCESSES):
        inarrays.append([i, random.getrandbits(128)])


    p = Pool(processes=NPROCESSES, initializer=None, initargs=None, maxtasksperchild=None)
    t0 = time.perf_counter_ns()
    outarrays = p.starmap(f, [(data[0], t0, data[1])
                            for data in inarrays], chunksize=1)
