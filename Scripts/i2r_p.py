#!/usr/bin/env python
# Version 0.04 for Pandoc

"""A simple python script that removes spaces before and 
after dollar signs in inline Latex code inside .ipynb files
and also produce a .rst file from the new .ipynb file by Using `Pandoc`
"""

import os
import sys
import argparse # clear
import re

def main(arguments):

    parser = argparse.ArgumentParser(
        description=__doc__,                                                # text to display before the argument help
        formatter_class=argparse.RawDescriptionHelpFormatter)               
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-m', '--median', help="Intermediate Output file",
                        default=sys.stdout, type=argparse.FileType('w+'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w+'))
    args = parser.parse_args(arguments)
    #improve navigation and error catching to file in case user includes directory not in home of file
    with args.infile as f:
        content=f.read()
    with args.median as new_f:
        new_content=content
        new_content=re.sub(r'(\$.*)\s(\$)',r'\1\2', new_content)
        new_content=re.sub(r'(\$)\s(.*\$)',r'\1\2', new_content)
        new_f.write(new_content)
    os.system('pandoc -f ipynb -t rst %s -o %s' % (args.median.name, args.outfile.name))
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
