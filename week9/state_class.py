
import copy

class State():
    def __init__(self, n):
        self.queen_list = [-1]*n
        self.column = 0

if __name__ == "__main__":
    s = State(20)       # the argument n will be 20
    print(len(s.queen_list))     # will print 20
    s.queen_list[1] = 23
    u = copy.deepcopy(s)
    # u = s will create two refs to the same instance
    # so must copy in order to create separate instances
    u.queen_list[1] = 44         # s.a[1] remains 23

