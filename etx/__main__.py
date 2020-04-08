import sys
import argparse
from . import __version__
from .summeriser import Summary

def main(args=None):
  """The main routine."""
  if args is None:
    args = sys.argv[1:]

  parser = argparse.ArgumentParser(description="ext-sum.py is intended to be a small utillity script that gives a few greate stats on your daytrading results",)
  parser.add_argument('file', metavar="<file path>", nargs=1, help="path to your ETX capital histroy csv file")
  parser.add_argument('--version', '-v', action='version', version=__version__)
  args = parser.parse_args()


  sum = Summary(args.filePath)
  sum.summarize()


if __name__ == "__main__":
  main()