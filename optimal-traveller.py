#!/usr/bin/env python3

import argparse
import sys

from optimal_traveller.cli import cli

def main():
    # Create a parser
    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest = "command")

    # Create commands
    load_parser = subparser.add_parser("load")
    solve_parser = subparser.add_parser("solve")
    display_parser = subparser.add_parser("display")

    # Add arguments to commands
    load_parser.add_argument("-f", "--filename", help = "FILENAME.txt or FILENAME.json to be loaded in the solver", type = str, required = True)
    load_parser.add_argument("-m", "--metric", help = "metric used to compute the distance matrix: euclidian, ...", type = str, required = True)

    solve_parser.add_argument("-g", "--graph", help="name of the cities graph previously computed by the load command",
                              type=str, required=True)
    solve_parser.add_argument("-m", "--method", help = "select the method used to solve: ", type = str, required = True)

    display_parser.add_argument("-s", "--solution", help = "SOLUTION is the name of the solution to be displayed",type = str, required = True)

    # Print the help menu when there is no typed commands
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)

    # Parse arguments
    arguments = parser.parse_args()

    # Create a cli object to handle commands
    app = cli()

    if arguments.command == "load":
        app.load(arguments.filename, arguments.metric)
    elif arguments.command == "solve":
        app.solve(arguments.graph, arguments.method)
    elif arguments.command == "display":
        app.display(arguments.solution)


if __name__ == "__main__":
    main()
