#! /usr/bin/env python
# -*- coding: utf-8 -*-
from collections import Counter
import re
 
suffixes = Counter()
re_anob = re.compile(u'(?P<A>.+[^の])の(?P<B>[^の].+)')
re_hiragana = re.compile(u'[ぁ-&#12438;]+')
 
def extract_anob(text):
    match = re_anob.match(text)
    if match and is_valid_b(match.group('B')):
        suffixes[match.group('B')] += 1
 
def is_valid_entry(entry):
    return False if '_(' in entry else True
 
def is_valid_b(b):
    return False if re_hiragana.match(b) else True
 
if __name__ == '__main__':
    import optparse
 
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filename", help="the path of input file")
    (opts, args) = parser.parse_args()
 
    for line in open(opts.filename, 'r'):
        line = line.strip().decode('utf8')
        if is_valid_entry(line):
            extract_anob(line)
    for k,v in suffixes.most_common(200):
        print k,v
