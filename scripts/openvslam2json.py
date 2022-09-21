#!/usr/bin/env python3

# requirements
#  pip install -U msgpack

import argparse
import json
try:
    import msgpack
except ImportError:
    import sys
    print('Please install msgpack:')
    print(' pip install msgpack')
    sys.exit(1)


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_filepath', help='openvslam file')
    parser.add_argument('output_filepath', help='output json file')

    return parser.parse_args()


def main():
    args = get_args()

    with open(args.input_filepath, 'rb') as input_stream:
        content = input_stream.read()

    data = msgpack.unpackb(content, raw=False)

    with open(args.output_filepath, 'w') as output_stream:
        json.dump(data, output_stream, indent=2, sort_keys=True)


if __name__ == '__main__':
    main()
