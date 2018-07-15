import numpy as np
import os
import sys
import argparse
dir_path = os.path.dirname(os.path.realpath(__file__))




def main(args):
    dictionary = {"s":args.allspeed,"m":args.max_enemies,"e":args.Enemy_exist_sametime}
    np.save(dir_path + "/config",dictionary)


def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--allspeed','-s', type=int, 
        help='Speed of all element in game', default=1)
    parser.add_argument('--max_enemies', '-m', type=int, 
        help='Max enemies exist same time ')
    parser.add_argument('--Enemy_exist_sametime', '-e', type=bool, choices=[True, False],
        help='All enemies exist same time at the beginning?')

    return parser.parse_args(argv)

if __name__ == '__main__':
    main(parse_arguments(sys.argv[1:]))