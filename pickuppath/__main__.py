import logging
import os.path
from pickuppath import pickup_path


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("-c", "--current", default=None)
    parser.add_argument("--default", default=None)
    parser.add_argument("--debug", action="store_true")
    args = parser.parse_args()
    current = args.current or os.getcwd()
    default = args.default or os.path.join("~", args.filename)
    if args.debug:
        logging.basicConfig(level=logging.DEBUG)
    print(pickup_path(current, args.filename, default=default))


if __name__ == "__main__":
    main()
