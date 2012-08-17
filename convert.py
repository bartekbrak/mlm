#!/usr/bin/env python
import sys

print sys.argv
if len(sys.argv) != 3:
    print "usage: %s from_wiktionary.dic conjugation.tsv" % sys.argv[0]
    sys.exit()

mydic = {}
mydic2 = {}
for line in open(sys.argv[2]):
    linelist = line.rstrip('\n').split('\t')
    root = linelist[0]
    derivatives = ', '.join(linelist[1:])
    mydic2[root] = derivatives

for line in open(sys.argv[1]):
    a, b = line.rstrip('\n').split('::')
    a = a.strip()
    b = b.strip()
    if a in mydic:
        mydic[a] = mydic[a] + '\\n' + b.strip()
    else:
        mydic[a] = b.strip()

for line in mydic.keys():
    root = str.split(line, ' {')[0]
    if '{v' in line and root in mydic2.keys():
        derivatives = mydic2[root]
    else:
        derivatives = ''
    print '"%s";"%s";"%s"' % (line, derivatives, mydic[line])
