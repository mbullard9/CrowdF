#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Get information about nearby / used networks."""

import logging
import NetworkManager
import struct

# See https://developer.gnome.org/NetworkManager/0.9/spec.html


def print_nearby_networks():
    for dev in NetworkManager.NetworkManager.GetDevices():
        if dev.DeviceType != NetworkManager.NM_DEVICE_TYPE_WIFI:
            continue
        aps = [ap for ap in dev.SpecificDevice().GetAccessPoints()]
        header = u"{0:<20}{1:>6}{2:>20}".format('SSID',
                                                'Signal',
                                                'HwAddress')
        print(header)
        print("-"*len(header))
        for ap in sorted(aps,
                         key=lambda ap: struct.unpack('B', ap.Strength)[0],
                         reverse=True):
            signal_strength = struct.unpack('B', ap.Strength)[0]
            # print(u"%s::%s::%s" % (ap.Ssid,
            #                        signal_strength,
            #                        ap.HwAddress))
            print(u"{0:<20}{1:>6}{2:>20}".format(ap.Ssid,
                                                 str(signal_strength)+'%',
                                                 ap.HwAddress))


def main():
    """Get information about the networks."""
    print_nearby_networks()


def get_parser():
    from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter
    parser = ArgumentParser(description=__doc__,
                            formatter_class=ArgumentDefaultsHelpFormatter)
    return parser


if __name__ == '__main__':
    args = get_parser().parse_args()
    main()
