#!/usr/bin/python3
import logging
import argparse
import sys
import subprocess
import os

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

def call(args):
    print(" ".join(str(i) for i in args))
    return subprocess.call(args)

def run_cmake_debug():
    return call(["cmake", "..",
                "-DCMAKE_BUILD_TYPE=Debug",
                "-DSCORUM_LIVE_TESTNET=OFF",
                "-DSCORUM_LOW_MEMORY_NODE=OFF",
                "-DSCORUM_CLEAR_VOTES=ON",
                "-DSCORUM_SKIP_BY_TX_ID=ON",
                "-DENABLE_COVERAGE_TESTING=ON"])


def run_cmake_release_default():
    return call(["cmake", "..",
                 "-DCMAKE_BUILD_TYPE=Release",
                 "-DSCORUM_LIVE_TESTNET=OFF",
                 "-DSCORUM_LOW_MEMORY_NODE=ON",
                 "-DSCORUM_CLEAR_VOTES=ON",
                 "-DSCORUM_SKIP_BY_TX_ID=ON"])


def run_cmake_release_full():
        return call(["cmake", "..",
                     "-DCMAKE_BUILD_TYPE=Release",
                     "-DSCORUM_LIVE_TESTNET=OFF",
                     "-DSCORUM_LOW_MEMORY_NODE=OFF",
                     "-DSCORUM_CLEAR_VOTES=OFF",
                     "-DSCORUM_SKIP_BY_TX_ID=OFF"])

def main():
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('action', type=str, help='')
    parser.add_argument('action', type=str, help='')
    # parser.add_argument('-c', '--config', action='store', help='Path to config file')
    # parser.add_argument('-v', '--verbose', action='count', help='Verbose level')
    args = parser.parse_args(args=sys.argv[:2])

    if args.action == "build":
        build(sys.argv[2:])
    elif args.action == "run_cmake_debug":
        run_cmake_debug()
    elif args.action == "run_cmake_release_default":
        run_cmake_release_default()
    elif args.action == "run_cmake_release_full":
        run_cmake_release_full()


if __name__ == "__main__":
    main()
