import random
import threading
import time

from utils import calculate_hash, PROOF, TARGET, NTHREADS


def f(identify, t0, data):
    hash = calculate_hash(data)

    print("identify: {} t0: {} hash: {}".format(identify, t0, hash))


    while True:
        if hash[:PROOF] == TARGET:
            break

        hash = calculate_hash(hash)


    dt = time.perf_counter_ns() - t0
    print("identify: {} dt: {:.5f} hash: {}".format(identify, (dt*1E-9), hash))


    return None


if __name__ == "__main__":
    threads = []
    for i in range(NTHREADS):
        data = random.getrandbits(128)
        t0 = time.perf_counter_ns()
        threads.append(threading.Thread(target=f, args=(i, t0, data)))


    for thread in threads:
        thread.start()
