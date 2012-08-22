#!/usr/bin/env python
import sys
from time import gmtime, strftime

# arguments validation
if len(sys.argv) != 3:
    print "usage: %s from_wiktionary.dic conjugation.tsv" % sys.argv[0]
    sys.exit()
# add description
now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "000_description\t\tfrom %s %s on %s" % (sys.argv[1], sys.argv[1], now)

# conjugation
derivatives_dictionary = {}
for line in open(sys.argv[2]):
    # some verbs have their variants, marked as such: ser/*seer, we don't want these and treat ruler as a derivative
    linelist = line.rstrip('\n').replace('/*', '\t').split('\t')
    root = linelist[0]
    derivatives = '\t'.join(linelist[1:])
    derivatives_dictionary[root] = derivatives

wiktionary = {}
for line in open(sys.argv[1]):
    lemma, meaning = line.rstrip('\n').split('::')
    lemma = lemma.strip()
    meaning = meaning.strip()
    if lemma in wiktionary:
        wiktionary[lemma] = wiktionary[lemma] + '; ' + meaning.strip()
    else:
        wiktionary[lemma] = meaning.strip()

# stdout printing
for line in wiktionary.keys():
    root = str.split(line, ' {')[0]
    if '{v' in line and root in derivatives_dictionary.keys():
        derivatives = derivatives_dictionary[root]
    else:
        derivatives = ''
    print "%s\t%s\t%s" % (line, derivatives, wiktionary[line])
