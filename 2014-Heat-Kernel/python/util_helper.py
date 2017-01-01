import math


def get_sample_graph():
    with open('graph_eval_script.txt') as ifs:
        eval_line = ''.join(map(lambda ele: ele.strip(), ifs.readlines()))
    return eval(eval_line)


def compute_psis(N, t):
    psis = {N: 1.}
    for i in xrange(N - 1, 0, -1):
        psis[i] = psis[i + 1] * t / (float(i + 1.)) + 1.
    return psis


def compute_threshs(eps, N, psis):
    threshs = {}
    threshs[0] = (math.exp(1) * eps / float(N)) / psis[0]
    for j in xrange(1, N + 1):
        threshs[j] = threshs[j - 1] * psis[j - 1] / psis[j]
    return threshs