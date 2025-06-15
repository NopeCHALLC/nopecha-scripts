#!/usr/bin/env python
import subprocess
import sys

def main():
    sys.exit(subprocess.call(["pytest"] + sys.argv[1:]))

if __name__ == "__main__":
    main()