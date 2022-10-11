import argparse
import os
import sys

from kind import start_kind, stop_kind
from tools import run_command


def requirements_check():
    exit_code = 0
    
    kind_status = run_command("kind --version")
    if kind_status["return_code"] != 0:
        print("kind not found, please install kind.")
        exit_code = 1

    kubectl_status = run_command("kubectl version")
    if kubectl_status["return_code"] != 0:
        print("kubectl not found, please install kubectl.")
        exit_code = 1

    if exit_code:
        sys.exit(exit_code)


def playground_start(base_path):
    start_kind(base_path)


def main(): 
    requirements_check()

    parser = argparse.ArgumentParser(description='Kind Playground')
    subparsers = parser.add_subparsers(dest='subparser', metavar="command")

    parser_start = subparsers.add_parser('start')
    parser_start.add_argument('path', type=str, help='Playground path')

    parser_stop = subparsers.add_parser('stop')
    parser_stop.add_argument('path', type=str, help='Playground path')

    subparsers.required = True

    args = parser.parse_args()

    base_path = os.path.realpath(args.path)

    if args.subparser == "start":
        playground_start(base_path)

    if args.subparser == "stop":
        stop_kind(base_path)


if __name__ == "__main__":
    main()
