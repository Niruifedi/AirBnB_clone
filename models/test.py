import argparse
parser = argparse.ArgumentParser(description = "An Addition program")

parser.add_argument("add", nargs = "*", metavar = "num", type = int,
                    help = "All the numbers separated by space will be added")

args = parser.parse_args()


if len(args.add) != 0:
    print(sum(args.add))