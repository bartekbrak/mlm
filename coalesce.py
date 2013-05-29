#!/usr/bin/env python
# convert dict-formatted wiktionary extraction to tab-separated,
# inflections-enriched mlm-format
import sys
from time import gmtime, strftime

# arguments validation
if len(sys.argv) != 3:
    print "usage: %s from_wiktionary.dic conjugation.tsv" % sys.argv[0]
    sys.exit()

# add description
now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
print "000_description\t\tfrom %s %s on %s" % (sys.argv[1], sys.argv[1], now)

# inflections
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
# i=0
for line in open(sys.argv[1]):
    # i+=1
    # if i==10:
    #     break;
    try:
        lemma, pos, meaning = line.rstrip('\n').split('\t')
    except ValueError:
        sys.stderr.write("a broken line found: %s" % line)
    lp = "%s\t%s" % (lemma, pos)
    if lemma in wiktionary:
        if pos in wiktionary[lemma]:
            wiktionary[lemma][pos] = wiktionary[lemma][pos] + '; ' + meaning
        else:
            wiktionary[lemma].update({pos: meaning})
    else:
        wiktionary[lemma] = {pos: meaning}

for lemma in wiktionary.keys():
    # lemma, pos, meaning = line.split('\t')
    # root = str.split(line, ' {')[0]
    if True in [pos.startswith('v') for pos in wiktionary[lemma]] and lemma in derivatives_dictionary.keys():
        derivatives = derivatives_dictionary[lemma]
    else:
        derivatives = ''
    final_meaning = ''
    for pos, meaning in wiktionary[lemma].items():
        final_meaning += "%s: %s; " % (pos, meaning)
    print "%s\t%s\t%s" % (lemma, derivatives, final_meaning)
