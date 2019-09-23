import Constant as c
import argparse
import sys

class Arguments:
    def __init__(self):
        self.ap = argparse.ArgumentParser(description=c.PROG_DESC)
        self.ap.add_argument(c.M_KEY, c.M_LONG_KEY, metavar=c.M_METAVAR, 
                            nargs='?', default=c.M_DEFAULT, help=c.M_METAVAR)
        self.ap.add_argument(c.C_KEY, c.C_LONG_KEY, metavar=c.C_METAVAR, 
                            type=argparse.FileType(c.C_WR_TYPE), required=True, help=c.C_HELP)
        self.ap.add_argument(c.I_KEY, c.I_LONG_KEY, metavar=c.I_METAVAR, 
                            type=argparse.FileType(c.I_WR_TYPE), required=True, help=c.I_HELP)
        self.ap.add_argument(c.O_KEY, c.O_LONG_KEY, metavar=c.O_METAVAR, 
                            type=argparse.FileType(c.O_WR_TYPE), required=True, help=c.O_HELP)

    def getArgs(self):
        args = self.ap.parse_args()
        return args.mode, args.code, args.input, args.output