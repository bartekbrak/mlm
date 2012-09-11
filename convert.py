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
    # strip unimportant
    replacements = {
        '/*': ' ',   # variants
        # '-': '',    # blank entries
        '[AmL]': '',  # regional variant
        '[Esp]': '',  # regional variant
        '/': ' '     # variants
    }
    line = reduce(lambda a, (b, c): a.replace(b, c), replacements.items(), line)
    line_as_list = line.rstrip('\n').split('\t')
    root = line_as_list[0]
    derivatives = '\t'.join(line_as_list[1:])
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
