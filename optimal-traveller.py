#!/usr/bin/env python3

import argparse
import sys

from optimal-traveller import cli

def main():
    parser = argparse.ArgumentParser()
    
    action = parser.add_mutually_exclusive_group()

    action.add_argument("-l", "--load", help = "load a *.txt or *.json file into the solver", action = "store")
    action.add_argument("-s", "--solve", help = "compute an optimal path with the given method", action = "store")
    action.add_argument("-d", "--display", help = "display a previously computed path", action = "store")

    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    try:
        args = parser.parse_args()
    except:
        parser.print_help()
        sys.exit(0)

    if args.load:
        print("load is working!")
        print(args.load)
    if args.solve:
        print("solve is working!")
    if args.display:
        print("display is working!")

if __name__ == "__main__":
    main()
