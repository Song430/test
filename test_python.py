# to learn how to use git
# the second commit
import argparse
parser = argparse.ArgumentParser(description="Process some intergers")
parser.add_argument("integers",metavar="N",type=int, nargs="+",
        help="an inter for the accumulator")
parser.add_argument("--sum", dest="accumulate", action="store_const",
        const = sum, default=max,
        help="sum the integers(default: find the max)")
args = parser.parse_args()
print(args.accumulate(args.integers))
print("I am a monkey")
print("I do")
print("Hello")
