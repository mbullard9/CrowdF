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
        max_ssid = max([len(ap.Ssid) for ap in aps]) + 1
        headerf = u"{0:<%i}{1:>6}{2:>20}{3:>5}{4:>8}{5:>8}{6:>5}{7:>5}{8:>8}{9:>10}" % max_ssid
        header = headerf.format('SSID',
                                'Signal',
                                'HwAddress',
                                'Mode',
                                'WEP40',
                                'WEP104',
                                'TKIP',
                                'PSK',
                                '802.1X',
                                'WpaFlags')
        print(header)
        print("-"*len(header))
        NM_802_11_AP_SEC_PAIR_WEP40 = 0x01
        NM_802_11_AP_SEC_PAIR_WEP104 = 0x02
        NM_802_11_AP_SEC_PAIR_TKIP = 0x04
        # NM_802_11_AP_SEC_PAIR_CCMP = 0x08
        # NM_802_11_AP_SEC_GROUP_WEP40 = 0x10
        # NM_802_11_AP_SEC_GROUP_WEP104 = 0x20
        # NM_802_11_AP_SEC_GROUP_TKIP = 0x40
        # NM_802_11_AP_SEC_GROUP_CCMP = 0x80
        NM_802_11_AP_SEC_KEY_MGMT_PSK = 0x100
        NM_802_11_AP_SEC_KEY_MGMT_802_1X = 0x200
        for ap in sorted(aps,
                         key=lambda ap: struct.unpack('B', ap.Strength)[0],
                         reverse=True):
            signal_strength = struct.unpack('B', ap.Strength)[0]
            flags = ap.WpaFlags & (~NM_802_11_AP_SEC_PAIR_TKIP)
            flags = flags & (~NM_802_11_AP_SEC_KEY_MGMT_PSK)
            flags = flags & (~NM_802_11_AP_SEC_KEY_MGMT_802_1X)
            print(headerf.format(ap.Ssid,
                                 str(signal_strength)+'%',
                                 ap.HwAddress,
                                 ap.Mode,
                                 (ap.WpaFlags & NM_802_11_AP_SEC_PAIR_WEP40 > 0),
                                 (ap.WpaFlags & NM_802_11_AP_SEC_PAIR_WEP104 > 0),
                                 (ap.WpaFlags & NM_802_11_AP_SEC_PAIR_TKIP > 0),
                                 (ap.WpaFlags & NM_802_11_AP_SEC_KEY_MGMT_PSK > 0),
                                 (ap.WpaFlags & NM_802_11_AP_SEC_KEY_MGMT_802_1X > 0),
                                 flags))


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
