#!/usr/bin/python3
import logging
import argparse
import sys

# orex build debug all -d cmake
# orex build release scorumd -d cmake
# orex docker mainnet build


def build(argv):
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('build_type', type=str, help='')
    parser.add_argument('action', type=str, help='')

    args = parser.parse_args(args=argv)

    print("building")
    print(argv)


def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('action', type=str, help='')
    parser.add_argument('action', type=str, help='')
    # parser.add_argument('-c', '--config', action='store', help='Path to config file')
    # parser.add_argument('-v', '--verbose', action='count', help='Verbose level')
    args = parser.parse_args(args=sys.argv[:2])

    if args.action == "build":
        build(sys.argv[2:])
    elif args.action == "valgrind":
        pass




if __name__ == "__main__":
    main()
