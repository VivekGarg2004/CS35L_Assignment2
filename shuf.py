import random, sys
import argparse

parser = argparse.ArgumentParser("""Usage: shuf [OPTION]... [FILE]
                                 or:  shuf -e [OPTION]... [ARG]...
                                 or:  shuf -i LO-HI [OPTION]...
                                 Write a random permutation of the input lines to standard output.
                                 
                                 With no FILE, or when FILE is -, read standard input.

                                Mandatory arguments to long options are mandatory for short options too.
                                -e, --echo                treat each ARG as an input line
                                -i, --input-range=LO-HI   treat each number LO through HI as an input line
                                -n, --head-count=COUNT    output at most COUNT lines
                                -o, --output=FILE         write result to FILE instead of standard output
                                    --random-source=FILE  get random bytes from FILE
                                -r, --repeat              output lines can be repeated
                                -z, --zero-terminated     line delimiter is NUL, not newline
                                    --help        display this help and exit
                                    --version     output version information and exit""")


parser.add_argument("ARGS", nargs="*")
parser.add_argument("-e", "--echo", action="store_true")
parser.add_argument("-i", "--input-range", type=str)
parser.add_argument('-n', '--head-count', type=int, default=-1)
parser.add_argument("-r", "--repeat", action="store_true")


args = parser.parse_args()

