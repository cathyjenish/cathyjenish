# import sys
# import numpy as np
# import argparse
# from classes import PRMController, Obstacle, Utils


# def main(args):

#     parser = argparse.ArgumentParser(description='PRM Path Planning Algorithm')
#     parser.add_argument('--numSamples', type=int, default=1000, metavar='N',
#                         help='Number of sampled points')
#     args = parser.parse_args()

#     numSamples = args.numSamples

#     env = open("environment.txt", "r")
#     l1 = env.readline().split(";")

#     current = list(map(int, l1[0].split(",")))
#     destination = list(map(int, l1[1].split(",")))

#     print("Current: {} Destination: {}".format(current, destination))

#     print("****Obstacles****")
#     allObs = []
#     for l in env:
#         if(";" in l):
#             line = l.strip().split(";")
#             topLeft = list(map(int, line[0].split(",")))
#             bottomRight = list(map(int, line[1].split(",")))
#             obs = Obstacle(topLeft, bottomRight)
#             obs.printFullCords()
#             allObs.append(obs)

#     utils = Utils()
#     utils.drawMap(allObs, current, destination)

#     prm = PRMController(numSamples, allObs, current, destination)
#     # Initial random seed to try
#     initialRandomSeed = 0
#     prm.runPRM(initialRandomSeed)


# if __name__ == '__main__':
#     main(sys.argv)
# main.py

import sys
import numpy as np
import argparse
from classes import PRMController, Obstacle, Utils, Obstacle2


def main(args):
    parser = argparse.ArgumentParser(description="PRM Path Planning Algorithm")
    parser.add_argument(
        "--numSamples",
        type=int,
        default=1000,
        metavar="N",
        help="Number of sampled points",
    )
    args = parser.parse_args()

    numSamples = args.numSamples

    env = open("environment.txt", "r")
    l1 = env.readline().split(";")

    current = list(map(int, l1[0].split(",")))
    destination = list(map(int, l1[1].split(",")))

    print("Current: {} Destination: {}".format(current, destination))

    print("****Obstacles****")
    allObs = []
    for l in env:
        if ";" in l:
            # line = l.strip().split(";")
            # topLeft = list(map(int, line[0].split(",")))
            # bottomRight = list(map(int, line[1].split(",")))
            # obs = Obstacle(topLeft, bottomRight)

            # allObs.append(obs)
            line = l.strip().split(";")
            vertices = [list(map(int, point.split(","))) for point in line]
            obst = Obstacle2(vertices)
            obst.print_properties()
            allObs.append(obst)

        elif ":" in l:
            # line = l.strip().split(":")
            # vertices = [list(map(int, point.split(","))) for point in line]
            # obst = Obstacle2(vertices)
            # obst.print_properties()
            # allObs.append(obst)
            print("Nothing")

    utils = Utils()
    utils.drawMap(allObs, current, destination)

    prm = PRMController(numSamples, allObs, current, destination)
    # Initial random seed to try
    initialRandomSeed = 0
    prm.runPRM(initialRandomSeed)


if __name__ == "__main__":
    main(sys.argv)
