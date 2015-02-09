#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
from SimpleCV import Camera


def main(filename):
    """Make a picture with the internal camera."""
    cam = Camera()
    logging.info(cam)
    img = cam.getImage()
    img.save(filename)


def get_parser():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-f", "--file",
                        dest="filename",
                        required=True,
                        help="write report to FILE",
                        metavar="FILE")
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    main(args.filename)
