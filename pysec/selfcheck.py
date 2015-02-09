#!/usr/bin/env python

"""Check if all necessary modules / programs / files for pysec are there and
   if the version is ok.
"""

import imp
import sys
import platform
import os
import pkg_resources


class bcolors(object):
    """Terminal colors with ANSI escape codes."""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def which(program):
    """Get the path of a program or ``None`` if ``program`` is not in path."""
    def is_exe(fpath):
        """Check for windows users."""
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None


def check_python_version():
    """Check if the currently running Python version is new enough."""
    # Required due to multiple with statements on one line
    req_version = (2, 7)
    cur_version = sys.version_info
    if cur_version >= req_version:
        print("Python version... %sOK%s (found %s, requires %s)" %
              (bcolors.OKGREEN, bcolors.ENDC, str(platform.python_version()),
               str(req_version[0]) + "." + str(req_version[1])))
    else:
        print("Python version... %sFAIL%s (found %s, requires %s)" %
              (bcolors.FAIL, bcolors.ENDC, str(cur_version),
               str(req_version)))


def check_python_modules():
    """Check if all necessary / recommended modules are installed."""
    print("\033[1mCheck modules\033[0m")
    required_modules = ['argparse', 'SimpleCV', 'NetworkManager']
    found = []
    for required_module in required_modules:
        try:
            imp.find_module(required_module)
            check = "module '%s' ... %sfound%s" % (required_module,
                                                   bcolors.OKGREEN,
                                                   bcolors.ENDC)
            print(check)
            found.append(required_module)
        except ImportError:
            print("module '%s' ... %sNOT%s found" % (required_module,
                                                     bcolors.WARNING,
                                                     bcolors.ENDC))

    if "argparse" in found:
        import argparse
        print("argparse version: %s (1.1 tested)" % argparse.__version__)
    if "SimpleCV" in found:
        import SimpleCV
        print("SimpleCV version: %s (1.3.0 tested)" % SimpleCV.__version__)
    if "NetworkManager" in found:
        import NetworkManager
        print("NetworkManager version: %s (0.9.8.8 tested)" % NetworkManager.NetworkManager.Version)


def main():
    """Execute all checks."""
    check_python_version()
    check_python_modules()
    home = os.path.expanduser("~")
    print("\033[1mCheck files\033[0m")
    rcfile = os.path.join(home, ".pysecrc")
    if os.path.isfile(rcfile):
        print("~/.pysecrc... %sFOUND%s" %
              (bcolors.OKGREEN, bcolors.ENDC))
    else:
        print("~/.pysecrc... %sNOT FOUND%s" %
              (bcolors.FAIL, bcolors.ENDC))
    # misc_path = pkg_resources.resource_filename('pysecrc', 'misc/')
    # print("misc-path: %s" % misc_path)


if __name__ == '__main__':
    main()
