#!/usr/bin/env python3
import hashlib
import argparse
import itertools
import string

def get_args():
    parser = argparse.ArgumentParser(description='Looks for a hash that ends/begins with a given pattern.')
    parser.add_argument('--algorithm', type=str, required=True, help='Algorithm to use (md5, sha1, sha256, ...)')
    parser.add_argument('--pattern', type=str, required=True, help='Pattern to match')
    parser.add_argument('--start', action='store_true', default=False, help='The pattern should match the hash prefix')
    parser.add_argument('--end', action='store_true', default=False, help='The pattern should match the hash suffix')
    parser.add_argument('--binary', action='store_true', default=False, help='''Set this if the hash is converted from hex to binary (specific to PHP ! E.g. "4142" -> "AB")''')
    return parser.parse_args()

def hash(mystr, algo):
    if (algo.lower() == 'md5'):
        return hashlib.md5(mystr.encode('utf-8')).hexdigest()
    elif (algo.lower() == 'sha1'):
        return hashlib.sha1(mystr.encode('utf-8')).hexdigest()
    elif (algo.lower() == 'sha224'):
        return hashlib.sha224(mystr.encode('utf-8')).hexdigest()
    elif (algo.lower() == 'sha256'):
        return hashlib.sha256(mystr.encode('utf-8')).hexdigest()
    elif (algo.lower() == 'sha384'):
        return hashlib.sha384(mystr.encode('utf-8')).hexdigest()
    elif (algo.lower() == 'sha512'):
        return hashlib.sha512(mystr.encode('utf-8')).hexdigest()

args = get_args()
charset = string.ascii_letters + string.digits
found = False
counter = 1
#combinations = itertools.combinations_with_replacement(charset, r=counter)
print("[+] Looking for a matching hash...")
while True:
    #for h_input in combinations:
    h_input = counter
    h_output = hash(str(h_input), args.algorithm)
    if args.binary:
        if args.start:
            if h_output.startswith("".join([hex(ord(x))[2:] for x in args.pattern])):
                found = True
        if args.end:
            if h_output.endswith("".join([hex(ord(x))[2:] for x in args.pattern])):
                found = True
    else:
        if args.start:
            if h_output.startswith(args.pattern):
                found = True
        if args.end:
            if h_output.endswith(args.pattern):
                found = True
    counter += 1
    if found:
        print(f"""[+] {args.algorithm}('{h_input}') = {h_output}""")
        exit()

