#!/bin/python
from __future__ import annotations

def remove_brackets(s: str) -> str:
    return str(s).replace("[", "", -1).replace("]", "", -1)

def no_blanks(s: str) -> int:
    return -1 if len(s) <= 0 else int(s)

def split_to_int_list(s: str, pred: callable  = no_blanks) -> list:
    return list(map(pred, s.split(",")))

arr1 = "[[1],[2,3,4]]"
arr2 = "[[1],4]"

arr1 = "[[[8,2],2,[[10],[],6,10,[10,10,3,10,3]]],[],[]]"
arr2 = "[[[[7,3,5],10,[4,1,0,8,7],9],10,[]]]"

remove_brackets(arr1)
# [[[8,2],2,[[10],[],6,10,[10,10,3,10,3]]],[],[]]
# [[[[7,3,5],10,[4,1,0,8,7],9],10,[]]]

def r(s: str) -> str:
    if s[0] == "[" and s[-1] == "]":
        return r(s[1:-1])
        
    

if __name__ == "__main__":

    idx: int = 1
    pair = list()
    ok_comps = list()
    with open("data.in") as f:
        for line in list(f):
            line = line[:-2]
            # print(pair)
            if len(line) > 0:
                pair.append(line)
            else:
                p1, p2 = pair

                p1_count, p2_count = p1.count("["), p2.count("[")
                
                p1, p2 = remove_brackets(p1), remove_brackets(p2)
                # print(p1, " ", p2)

                # a1, a2 = p1.split(","), p2.split(",")
                a1, a2 = split_to_int_list(p1), split_to_int_list(p2)
                n1, n2 = len(a1), len(a2)
                # print(a1, "\n", a2)
                # print()

                if n1 == 0 and n2 == 0 and p1_count < p2_count:
                    ok_comps.append(idx)

                elif n1 == 0 and n2 > 0:
                    ok_comps.append(idx)

                elif all(a==b for a, b in zip(a1, a2)):
                    if n1 < n2:
                        ok_comps.append(idx)                    

                else:

                    for i in range(max(n1, n2)):
                    # for i, v in enumerate(a1):
                        if i < n1 and i < n2:
                            # print(a1[i], a2[i])
                            if a1[i] < a2[i]:
                                # print(a1[i], a2[i])
                                ok_comps.append(idx)
                                break
                        # elif i >= n1:
                        #     ok_comps.append(idx)
                        #     break
                        # else:
                        #     break
                        # if i < n2:
                        #     if v == a2[i]:
                        #         continue
                        #     elif v < a2[i]:
                        #         ok_comps.append(idx)
                        #         break
                # print(f"{a1}\n{a2}")
                idx += 1
                pair = list()

        # 10_693 is too high.    
        print(ok_comps)
        print(sum(ok_comps))
