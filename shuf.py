#!/usr/bin/python
import random, sys
import argparse


def input_range(arg):
    try:
        lo, hi = map(int, arg.split('-'))
        return lo, hi
    except ValueError:
        raise argparse.ArgumentTypeError("Invalid input range format. Use LO-HI.")
class shuffler:
    def __init__(self,contents,repeat,head_count):
        self.content = contents
        self.repeats = repeat
        self.limit = head_count
    def shuf(self):
        random.shuffle(self.content)
        count = 0
        while(self.content and (count < self.limit or self.limit == -1)):
            if self.repeats:
                pick = random.choice(self.content)
                sys.stdout.write(pick if pick.endswith('\n') else pick + '\n')
            else:
                pick = self.content.pop()
                sys.stdout.write(pick if pick.endswith('\n') else pick + '\n')

            count += 1
def main():    
    parser = argparse.ArgumentParser("""Usage: shuf [OPTION]... [FILE]
                                    or:  shuf -e [OPTION]... [ARG]...
                                    or:  shuf -i LO-HI [OPTION]...
                                    Write a random permutation of the input lines to standard output.
                                    
                                    With no FILE, or when FILE is -, read standard input.

                                    Mandatory arguments to long options are mandatory for short options too.
                                    -e, --echo                treat each ARG as an input line
                                    -i, --input-range=LO-HI   treat each number LO through HI as an input line
                                    -n, --head-count=COUNT    output at most COUNT lines
                                    -r, --repeat              output lines can be repeated
                                        --help        display this help and exit""")


    parser.add_argument("ARGS", nargs="*")

    group = parser.add_mutually_exclusive_group()

    group.add_argument("-e", "--echo", nargs='*', default=None, help="treat each ARG as an input line")
    group.add_argument("-i", "--input-range", type= input_range, action="store", default=None,
                        help="treat each number LO through HI as an input line")

    parser.add_argument('-n', '--head-count', type=int, action="store", default=-1, help="output at most COUNT lines")
    parser.add_argument("-r", "--repeat", action="store_true", default=False, help="output lines can be repeated")


    args = vars(parser.parse_args())

    args_option = args.get("ARGS")
    echo_option = args.get("echo")
    repeat_option = args.get("repeat")
    input_range_option = args.get("input_range")
    head_count_option = args.get("head_count")


    contents = []
    if echo_option is None and not input_range_option:
        if len(args_option) > 1:
            parser.error(f"shuf: extra operand '{args_option[1]}'")
        elif len(args_option) == 1:
            filename = args_option[0]
            if(filename == '-'):
                try:
                    contents = sys.stdin.readlines()
                except FileNotFoundError:
                    parser.error(f"no such file or directory: {sys.stdin}")
            else:
                try:
                    with open(filename, 'r') as f:
                        contents = f.readlines()
                except FileNotFoundError:     
                    parser.error(f"{filename}: No such file or directory")
        else:
            filename = None
            try:
                contents = sys.stdin.readlines()
            except FileNotFoundError:
                parser.error(f"no such file or directory: {sys.stdin}")

    elif echo_option is not None:
        filename = None
        contents = args_option.copy()
        contents.extend(echo_option)

    elif input_range_option:
        lo, hi = input_range_option
        contents = list(map(str, range(lo, hi+1)))
        if len(args_option) > 0:
            parser.error("extra operand '%s'" % args_option[0])


    output = shuffler(contents,repeat_option, head_count_option)
    output.shuf()



if __name__ == "__main__":
    main()

