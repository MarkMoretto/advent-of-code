#!/bin/python



if __name__ == "__main__":
    points = list()
    with open("data-sm.in") as f:
        for line in list(f):
            line = line[:-1]
            points.append(line.split(","))
    for pt in sorted(points):
        print(pt)
