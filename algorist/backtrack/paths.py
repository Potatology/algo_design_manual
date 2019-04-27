from algorist.backtrack.backtrack import BacktrackCallback, NMAX


class Paths(BacktrackCallback):
    """
    Enumerate the paths in a graph via backtracking.
    """

    def __init__(self, g):
        self.g = g
        self.solutionCount = 0

    def is_a_solution(self, a, k, t):
        return a[k] == t

    def process_solution(self, a, k, n):
        self.solutionCount += 1

        print("{", end='')
        for i in range(1, k + 1):
            print(" %d" % a[i], end='')
        print(' }')

    def construct_candidates(self, a, k, n):
        c = [0] * NMAX

        in_sol = [False] * NMAX  # what's already in the solution?
        for i in range(k):
            in_sol[a[i]] = True

        if k == 1:  # always start from vertex 1
            c[0] = 1
            ncandidates = 1
        else:
            ncandidates = 0
            last = a[k - 1]  # last vertex on current path
            for p in self.g.edges[last]:
                if not in_sol[p.y]:
                    c[ncandidates] = p.y
                    ncandidates += 1

        return c, ncandidates