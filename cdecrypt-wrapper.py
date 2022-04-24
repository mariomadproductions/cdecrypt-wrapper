#!/usr/bin/env python3
import argparse
import binascii
from pathlib import Path
import subprocess
import tempfile

def get_dummy_tik_data(titlekey):
    return binascii.unhexlify(('00' * 0x1BF) + titlekey + '00')

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-k', '--titlekey', type=str)
    parser.add_argument('tmd')
    return parser.parse_args()
    
def main():
    args = get_args()
    title_dir_path = Path(args.tmd).parent
    titlekey = args.titlekey
    tmd_path = args.tmd
    
    with tempfile.NamedTemporaryFile(dir=title_dir_path) as ticket_file:
        ticket_file.write(get_dummy_tik_data(titlekey))
        ticket_file.flush()
        mysubprocess = subprocess.run(['cdecrypt',
                                       tmd_path,
                                       ticket_file.name],
                                      cwd=title_dir_path,
                                      check=True)

if __name__ == '__main__':
    main()
