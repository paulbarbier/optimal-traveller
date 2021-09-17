#!/usr/bin/env python3

import argparse
import sys

from optimal_traveller.cli import Cli


def main():
    # Create a parser
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    # Create commands
    load_parser = subparser.add_parser("load")
    solve_parser = subparser.add_parser("solve")
    display_parser = subparser.add_parser("display")

    # Add arguments to commands
    load_parser.add_argument("-f", "--filename", help="FILENAME.txt or FILENAME.json to be loaded in the solver", type=str, required=True)
    load_parser.add_argument("-m", "--metric", help="metric used to compute the distance matrix: euclidean or orthodromic", type=str, choices=["euclidean", "orthodromic"], default="orthodromic")

    solve_parser.add_argument("-f", "--filename", help="FILE.opt containing previsoulty computed distance matrix and data of the problem",
                              type=str, required=True)
    solve_parser.add_argument("-m", "--method", help="select the method used to solve: ", type=str, choices=["exact", "nearest-neighbors", "genetic"], required=True)
    solve_parser.add_argument("--percentage", help="percentage of population automatically removed for the genetic method", type=float, default=0.2)
    solve_parser.add_argument("--maxsteps", help="max number of iteration for the genetic method", type=int, default=20)
    solve_parser.add_argument("--size", help="size of the population for the genetic method", type=int, default=30)

    display_parser.add_argument("-f", "--filename", help="FILENAME.opt, file of the solution(s) to be displayed", type=str, required=True)

    # Print the help menu when there is no typed commands
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Parse arguments
    arguments = parser.parse_args()

    # Create a cli object to handle commands
    app = Cli()

    if arguments.command == "load":
        app.load(arguments.filename, arguments.metric)
    elif arguments.command == "solve":
        app.solve(arguments.filename, arguments.method, arguments.percentage, arguments.maxsteps, arguments.size)
    elif arguments.command == "display":
        app.display(arguments.filename)


if __name__ == "__main__":
    main()
