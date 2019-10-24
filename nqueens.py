from collections import deque
import heapq
import sys
import time
import copy
import random
ans = list()
counter = 0
diag = {}
def makedia(n):
    for x in range(n):
        diag['h'+str(x)] = False
        diag['v'+str(x)] = False

def csp_backtracking(n):
    #global counter
    #counter +=1
    #if counter > 3000:
    #    return None
    if goal_test(n):
        global ans
        ans = n
        return n
    var = get_next_unassigned_var(n)
    #print(var)
    sor = get_sorted_values(n, var)
    #random.shuffle(sor)
    for val in sor:
        #print(val)
        cn = val
        result = csp_backtracking(cn)
        if result is not None:
            return result
    return None

def test_solution(state):
        for var in range(len(state)):
            left = state[var]
            middle = state[var]
            right = state[var]
            for compare in range(var + 1, len(state)):
                left -= 1
                right += 1
                if state[compare] == middle:
                    print(var, "middle", compare)
                    return False
                if left >= 0 and state[compare] == left:
                    print(var, "left", compare)
                    return False
                if right < len(state) and state[compare] == right:
                    print(var, "right", compare)
                    return False
        return True


def goal_test(n):
    for x in n:
        if x == -1000:
            return False
    return True

def get_next_unassigned_var(n):
    res = [i for i, value in enumerate(n) if value == -1000]
    #for x in res:
    #    find_low_res(x)
    return random.choice(res)

def get_sorted_values(n, val):
    ret = list()
    leng = len(n)
    for x in range(leng):
        if x not in n:
            good = True
            for dx in range(leng):
                if n[dx] + (val-dx) == x or n[dx] - (val-dx) == x or n[dx] + (dx-val) == x or n[dx]-(dx-val) == x:
                                                            # take each rows value, take difference of
                    good = False                            # val and that row index and find if the +-
                    break                                   # is equal to the number proposed
            if good:
                a = n[:]
                a[val] = x
                ret.append(a)
    #print(ret)
    return ret


n = [-1000]*8
start =time.perf_counter()
while True:
    a = csp_backtracking(n)
    if a == None:
        counter = 0
        print('fail')
    else:
        break
end = time.perf_counter()
print(f'Time is {(end-start)}')
print(ans)
print(test_solution(ans))
