#!/usr/bin/env python
import sys
from time import gmtime, strftime

if len(sys.argv) != 3:
    print "usage: %s from_wiktionary.dic conjugation.tsv" % sys.argv[0]
    sys.exit()

now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "000_description\t\tfrom %s %s on %s" % (sys.argv[1], sys.argv[1], now)

mydic = {}
mydic2 = {}
for line in open(sys.argv[2]):
    linelist = line.rstrip('\n').split('\t')
    root = linelist[0]
    # csv
    #derivatives = ', '.join(linelist[1:])
    derivatives = '\t'.join(linelist[1:])
    mydic2[root] = derivatives

for line in open(sys.argv[1]):
    a, b = line.rstrip('\n').split('::')
    a = a.strip()
    b = b.strip()
    if a in mydic:
        mydic[a] = mydic[a] + '; ' + b.strip()
    else:
        mydic[a] = b.strip()

for line in mydic.keys():
    root = str.split(line, ' {')[0]
    if '{v' in line and root in mydic2.keys():
        derivatives = mydic2[root]
    else:
        derivatives = ''
    # csv
    # print '"%s";"%s";"%s"' % (line, derivatives, mydic[line])
    print "%s\t%s\t%s" % (line, derivatives, mydic[line])
