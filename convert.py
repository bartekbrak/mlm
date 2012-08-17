#!/usr/bin/env python

mydic = {}
mydic2 = {}
for line in open('es-conjugation-utf8-1.3.1.tsv'):
    linelist = line.rstrip('\n').split('\t')
    root = linelist[0]
    derivatives = ', '.join(linelist[1:])
    mydic2[root] = derivatives

for line in open('es-en.dic'):
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
