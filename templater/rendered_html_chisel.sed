s,aaa">,aaa">*,g # mark grey coloured words(incorrect forms of defective verbs) with a star
s/<[^>][^>]*>//g # remove html tags
s,\(\[\|\]\),,g  # remove wiki links
s,{{{,{,g        # template positional variables to python .format format
s,}}},},g        # as above
s,^',    ',g     # indent dictionary keys