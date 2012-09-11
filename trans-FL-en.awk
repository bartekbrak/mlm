# gawk script to create a Foreign_Language-English dictionary from
# the Foreign_Language sections of en.wiktionary.org
#
# (c) 2011-2012 by Matthias Buchmeier
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#
# TODO:
# rm lines with {{past participle of| ?
# detect gender from {{es-proper noun|
# include IPA?
#
# Command-line options:
########################
#  required gawk command-line switches:
#
#    name of the language to be extracted, or bar-separated list of languages:
#    -v LANG=language
#
#  optional gawk command-line switches:
#
#    remove wiki-links and wiki-style bolding, italicizing:
#    -v REMOVE_WIKILINKS=y --re-interval
#
#########################

BEGIN {
#########################
# User defined variables:
#########################
# English names of the target language
# supported at the moment: Italian, French, Spanish
# default language:
lang="Spanish";
#
# command line parsing
#
if(LANG!="") lang = LANG;
#
# language specific configuration
#
# configuration for es-en dictionary
#
if(lang=="Spanish") {
# iso code of the language
iso = "es";
# exclude entire current POS if regexp is matched
# this regexp typically contains headline-templates of non-lema (form of) entries
exclude_POS="\\{\\{es\\-verb\\-form\\||\\{\\{es-adj[^\\}]*\\|(m|masculine)\\=|\\{\\{head\\|es\\|(noun|adjective|verb) form|\\{\\{es\\-adj\\-form|\\{\\{head\\|es\\|(misspelling|obsolete)|\\{\\{misspelling of\\||\\{\\{es-past participle|\\{\\{es\\-pp\\|";
# exclude matched definition lines
# this regexp typically contains form of templates
exclude_defn="\\{\\{(es-verb form of|rfdef|defn)\\|";
# regexp matching head line of a masculine noun
m_noun="\\{\\{es\\-noun(\\|m|.*\\|g=m)[\\|\\}]";
# regexp matching head line of a feminine noun
f_noun="\\{\\{es\\-noun(\\|f|.*\\|g=f)[\\|\\}]";
# regexp matching head line of a both masculine  and feminine noun
mf_noun="\\{\\{es\\-noun(\\|mf|.*\\|g=mf)[\\|\\}]";
# regexp matching verb headline
verbhead="\\{\\{es\\-verb[\\|\\}]|\\{\\{head\\|es\\|verb[\\|\\}]";
# discard entries without head-line template:
no_head=0;
# languge specific templates to be removed from output lines
rmtemplate="\\{\\{(es\\-demonstrative\\-accent-usage|gloss\\-stub\\|(Spanish|es))[^}]*}}";
}
#
if(lang=="Italian") {
iso = "it";
exclude_POS="\\{head\\|it\\|[^\|]* form[s]*[\\|\\}]|\\{\\{(head\\|it\\|(misspelling|obsolete|plural)|it-pp)[\\|\\}]";
exclude_defn="Compound of|\\{\\{(present participle of|past participle of|rfdef|defn|misspelling of|conjugation of)\\|";
m_noun="\\{\\{it\\-noun\\|[^\\|]*(\\|m|.*\\|g=m)[\\|\\}]";
f_noun="\\{\\{it\\-noun\\|[^\\|]*(\\|f|.*\\|g=f)[\\|\\}]";
mf_noun="\\{\\{it\\-noun\\|[^\\|]*(\\|mf|.*\\|g=mf)[\\|\\}]";
verbhead="\\{\\{it\\-verb[\\|\\}]|\\{\\{head\\|it\\|verb[\\|\\}]";
no_head=1;
rmtemplate="\\{\\{gloss\\-stub\\|(Italian|it)[^}]*}}|\\{\\{jump\\|[^}]*}}";
}
#
if(lang=="French") {
iso = "fr";
exclude_POS="\\{\\{head\\|fr\\|[^\|]* form[s]*[\\|\\}]|\\{\\{head\\|fr\\|(misspelling|obsolete|plural|present participle)|\\{\\{(misspelling of|fr\\-pp|fr-verb[-]form|fr-verb form|fr-adj-form|fr-past participle)\\|";
exclude_defn="\\{\\{past participle of\\||Compound of|masculine plural past participle of|present participle of|feminine plural past participle of|masculine plural of|conjugation of|inflection of|plural of|feminine plural of|feminine past participle of|\\{\\{(rfdef|defn)\\|";
m_noun="\\{\\{fr\\-noun(\\|m|.*\\|g=m)[\\|\\}]";
f_noun="\\{\\{fr\\-noun(\\|f|.*\\|g=f)[\\|\\}]";
mf_noun="\\{\\{fr\\-noun(\\|mf|.*\\|g=mf)[\\|\\}]";
verbhead="\\{\\{fr\\-verb[\\|\\}]|\\{\\{head\\|fr\\|verb[\\|\\}]";
no_head=1;
rmtemplate="\\{\\{gloss\\-stub\\|French[^}]*}}|\\{\\{jump\\|[^}]*}}";
}
#
if(lang=="Finnish") {
iso = "fi";
exclude_POS="\\{\\{head\\|fi\\|(noun|adjective|verb|proper noun) form|\\{\\{head\\|fi\\|(misspelling|obsolete)|\\{\\{misspelling of\\||\\{\\{head\\|fi\\}\\}";
exclude_defn="\\{\\{(fi-form of|fi-participle of|infinitive of|inflected form of|agent noun of|fi-verb form of|defn|rfdef|nominative plural of|rftrans)\\|";
no_head=1;
rmtemplate="\\{\\{gloss\\-stub\\|Finnish[^}]*}}";
}
#
# initialisation of undefined lang-specific regexps
if(m_noun=="") m_noun="XXXXXX";
if(f_noun=="") f_noun="XXXXXX";
if(mf_noun=="") mf_noun="XXXXXX";
if(verbhead=="") verbhead="XXXXXX";
if(rmtemplate=="") rmtemplate="XXXXXX";
#
# initialization of variables used for parsing
#
# set to 0/1 if outside/inside language section
langsect=0;
# variable holding POS (part of speech) information
# pos=="-" means the current POS is a non-lema form to be excluded from the dictionary
pos= "";
# variable holding additional grammatical information as gender, plural/singular etc ({mfncps}})
gend="";
# variable holding page title
title = "";
# language dependent regular expressions
#
# command-line options
#
if(REMOVE_WIKILINKS == "y") remove_wikilinks = 1;
if(REMOVE_CONTEXT == "y") remove_context = 1;
if(REMOVE_SPACED == "y") remove_spaced = 1;
#
# regexp matching language section header
langhead="\\x3D\\x3D[\\x20]*"lang"[\\x20]*\\x3D\\x3D";
# regexp matching {{head|...|noun...
nounhead="\\{\\{head\\|"iso"\\|noun";
#
warnmissing="[[][[]Category:"lang" (nouns|adjectives|verbs)[]][]]";
}

function printout(outp) {
                        #print "przed", outp
# convert special xml formating like &lt; to html
                        gsub(/&lt;/,"<",outp);
                        gsub(/&gt;/,">",outp);
                        gsub(/&amp;/,"\\&",outp);
                        gsub(/&quot;/,"\"",outp);
                        gsub(/&nbsp;/, " ", outp);
                        gsub(/&hellip;/, "...", outp);
                        gsub(/&quot;/, "\"", outp);
                        gsub(/&[mn]dash;/, "-", outp);

# NOTE: these must be done after converting '&lt;' -> '<'  and '&gt;' -> '>'
# remove <ref ... \>
                        gsub(/<ref[^>]*\/>/,"",outp);

# remove <ref [name=....]> blbla </ref> OK?
                        gsub(/<ref[^>]*>.*<\/ref>/,"",outp);

# remove one-line <!-- commented text -->
                        gsub(/<!--[^!>]*-->/,"",outp);

# remove extra spaces
                        gsub(/[\ ]+/, " ", outp);

if(remove_wikilinks==1) {
                        outp = gensub(/([[][[])([^]|]*\|)([^]]*)([]][]])/ , "\\3", "g", outp);
                        outp = gensub(/([[][[])([^]]*)([]][]])/ , "\\2", "g", outp);
                        gsub(/[']{2,}/, "", outp);
                        }
if(remove_context==1)   {
                        gsub(/\{\{.*\}\} /, "", outp);
                        }
# {{}} --> {}
                        gsub(/\{\{/, "{", outp);
                        gsub(/\}\}/, "}", outp);
                        gsub(/\|/, ",", outp);

if (remove_spaced==1)   {
                        if(match(outp, "^.* .*\t") !=0) next;
                        }
                        print outp;
}

/\x3Ctitle/ {
gsub(/^[^\x3C]*/, ""); gsub(/[^\x3E]*$/, ""); gsub(/\x3Ctitle\x3E/, ""); gsub(/\x3C\/title\x3E/, "");
title=$0;
#print title;
langsect=0; pos= ""; gend = ""; gend2 = "";
}

# discard non-useful lines (speedup and false "trans-see" lines from comment lines)
/<comment>|<\/?page>|<timestamp>|<id>|<\/?contributor>|<\/?revision>|<username>|<minor \/>/  {next;}
/^$/ {next;}

{if(index(title,"Wiktionary:") != 0) {title=""; next;}}
{if(index(title,"Template:") != 0) {title=""; next;}}
{if(index(title,"Index:") != 0) {title=""; next;}}
{if(index(title,"Appendix:") != 0) {title=""; next;}}
{if(index(title,"User:") != 0) {title=""; next;}}
{if(index(title,"Help:") != 0) {title=""; next;}}


$0 ~ langhead {
langsect=1; pos= ""; gend = ""; gend2 = "";
#print lang, ": ", title;
next;}

/^\x3D\x3D[^\x3D]+/ { langsect=0; pos= ""; gend= ""; gend2= ""; next;}

# language and title detection done; skip all lines if not inside LANG section
{if(langsect==0) next;}

# determine POS
/\x3D\x3D\x3D/ { pos=""; gend=""; gend2=""; }
/\x3D\x3D\x3D[\x20]*Noun[\x20]*[1-9]*\x3D\x3D\x3D/ { pos="n"; next;}
#/\x3D\x3D\x3D[\x20]*Verb[\x20]*\x3D\x3D\x3D/ { pos="v"; next;}
/\x3D\x3D\x3D[\x20]*Verb/ { pos="v"; next;}
/\x3D\x3D\x3D[\x20]*Adjective[\x20]*\x3D\x3D\x3D/ { pos="adj"; next;}
/\x3D\x3D\x3D[\x20]*Adverb[\x20]*\x3D\x3D\x3D/ { pos="adv"; next;}
/\x3D\x3D\x3D[\x20]*Interjection[\x20]*\x3D\x3D\x3D/ { pos="interj"; next;}
/\x3D\x3D\x3D[\x20]*Article[\x20]*\x3D\x3D\x3D/ { pos="art"; next;}
/\x3D\x3D\x3D[\x20]*Proper\x20noun[\x20]*[1-9]*\x3D\x3D\x3D/ { pos="prop"; next;}
/\x3D\x3D\x3D[\x20]*Preposition[\x20]*\x3D\x3D\x3D/ { pos="prep"; next;}
/\x3D\x3D\x3D[\x20]*Postposition[\x20]*\x3D\x3D\x3D/ { pos="postp"; next;}
/\x3D\x3D\x3D[\x20]*\{\{initialism/ { pos="initialism"; next;}
/\x3D\x3D\x3D[\x20]*Numeral[\x20]*\x3D\x3D\x3D/ { pos="num"; next;}
/\x3D\x3D\x3D[\x20]*Cardinal number[\x20]*\x3D\x3D\x3D/ { pos="cardinal num"; next;}
/\x3D\x3D\x3D[\x20]*Ordinal number[\x20]*\x3D\x3D\x3D/ { pos="ordinal num"; next;}
/\x3D\x3D\x3D[\x20]*Number[\x20]*\x3D\x3D\x3D/ { pos="num"; next;}
/\x3D\x3D\x3D[\x20]*\{\{acronym/ { pos="acronym"; next;}
/\x3D\x3D\x3D[\x20]*Acronym/ { pos="acronym"; next;}
/\x3D\x3D\x3D[\x20]*\{\{abbreviation/ { pos="abbr"; next;}
/\x3D\x3D\x3D[\x20]*Determiner[\x20]*\x3D\x3D\x3D/ { pos="determiner"; next;}
/\x3D\x3D\x3D[\x20]*Phrase[\x20]*\x3D\x3D\x3D/ { pos="phrase"; next;}
/\x3D\x3D\x3D[\x20]*Suffix[\x20]*\x3D\x3D\x3D/ { pos="suffix"; next;}
/\x3D\x3D\x3D[\x20]*Pronoun[\x20]*\x3D\x3D\x3D/ { pos="pron"; next;}
/\x3D\x3D\x3D[\x20]*Conjunction[\x20]*\x3D\x3D\x3D/ { pos="conj"; next;}
/\x3D\x3D\x3D[\x20]*Proverb[\x20]*\x3D\x3D\x3D/ { pos="proverb"; next;}
/\x3D\x3D\x3D[\x20]*Contraction[\x20]*\x3D\x3D\x3D/ { pos="contraction"; next;}
/\x3D\x3D\x3D[\x20]*Particle[\x20]*\x3D\x3D\x3D/ { pos="particle"; next;}
/\x3D\x3D\x3D[\x20]*Symbol[\x20]*\x3D\x3D\x3D/ { pos="symbol"; next;}
/\x3D\x3D\x3D[\x20]*Prefix[\x20]*\x3D\x3D\x3D/ { pos="prefix"; next;}
/\x3D\x3D\x3D[\x20]*Letter[\x20]*\x3D\x3D\x3D/ { pos="letter"; next;}
/\x3D\x3D\x3D[\x20]*Abbreviation[\x20]*\x3D\x3D\x3D/ { pos="abbr"; next;}
/\x3D\x3D\x3D[\x20]*Initialism[\x20]*\x3D\x3D\x3D/ { pos="initialism"; next;}
/\x3D\x3D\x3D[\x20]*Idiom[\x20]*\x3D\x3D\x3D/ { pos="idiom"; next;}
/\x3D\x3D\x3D[\x20]*Affix[\x20]*\x3D\x3D\x3D/ { pos="affix"; next;}
/\x3D\x3D\x3D[\x20]*Adverbial phrase[\x20]*\x3D\x3D\x3D/ { pos="adv"; next;}
/\x3D\x3D\x3D[\x20]*Prepositional phrase[\x20]*\x3D\x3D\x3D/ { pos="prep"; next;}
#
# Usage notes dont contain definitions, skip
/\x3D\x3D\x3D[\x20]*Usage notes[\x20]*\x3D\x3D\x3D/ { pos="-"; next;}

# These are supposed to be examples: ommit BR:might be useful
/\x23\:|\x23\x23|\x23\*/ {next;}

# convert old {{infl| head line template call to new {{head| replacement
/\{\{infl\|/ {gsub(/\{\{infl\|/, "{{head|", $0);}

# form of headers, exclude current POS section
$0 ~ exclude_POS {pos="-";}

# discard entry without head-line
# use option "no_head=1" for languages with plain '''WORD''' rather than {{head|iso|... form|
# on the head line of non-lema entries
/^[']['][']/ {
if(no_head==1) {
if(index($0, "'''"title"'''") !=0)
        if((pos=="adj")||(pos=="n")||(pos=="v")) pos="-";
}}

# determine gender of nouns
$0 ~ m_noun {gend="m";}
$0 ~ f_noun {gend="f";}
$0 ~ mf_noun {gend="mf";}
$0 ~ nounhead  {
                                gend="";
# detetermine gender via g, g2, g3 parameters of head-template, e.g. {{head|blabla|g=m|g2=f}}
                                regexp="(\\{\\{head\\|"iso"\\|noun.*)(\\|g[=])([mfncps])(.*)";
                                temp=gensub(regexp, "\\3", "", $0);
                                if(temp != $0) gend = temp;
                                regexp="(\\{\\{head\\|"iso"\\|noun.*)(\\|g2[=])([mfncps])(.*)";
                                temp=gensub(regexp, "\\3", "", $0);
                                if(temp != $0) gend = (gend temp);
                                regexp="(\\{\\{head\\|"iso"\\|noun.*)(\\|g3[=])([mfncps])(.*)";
                                temp=gensub(regexp, "\\3", "", $0);
                                if(temp != $0) gend = (gend temp);
# detetermine gender via extra template called after head-template, e.g.: {{head|blabla}} {{m|f|blabla}}
                                regexp="(\\{\\{head\\|"iso"\\|.*\\{)([mfncps])([\\|\\}].*)";
                                temp=gensub(regexp, "\\2", "", $0);
                                if(temp != $0) gend = (gend temp);
                                regexp="(\\{\\{head\\|"iso"\\|.*\\{[mfncps]\\|)([mfncps])([\\|\\}].*)";
                                temp=gensub(regexp, "\\2", "", $0);
                                if(temp != $0) gend = (gend temp);
                                regexp="(\\{\\{head\\|"iso"\\|.*\\{[mfncps]\\|[mfncps]\\|)([mfncps])([\\|\\}].*)";
                                temp=gensub(regexp, "\\2", "", $0);
                                if(temp != $0) gend = (gend temp);
                        }

$0 ~ verbhead {
                gend="";
                if(match($0, "intransitive") != 0) gend = (gend "i");
                if(match($0, "[^n]transitive") != 0) gend = (gend "t");
                if(match($0, "reflexive") != 0) gend = (gend "r");
#               print "# VERBHEAD: "$0" on page: "title" gend: "gend;
                }

$0 ~ exclude_defn {next;}

# main section: format output lines
/^[\x20]*\x23/  {if((langsect==1)&&(pos != "-")&&(title!=""))
                        {
#remove some common template options
                gsub(/\|(lang|pos|sc|nodot|nocap|sort|diminutive|nocat|POS|gender|from|skey)=[^\|\}]*/, "", $0);

# remove {{rf* templates
                gsub(/\{\{(rfex|rfgloss|R\:|attention\||\,|rfv\-sense)[^}]*\}\}/, "", $0);

# remove languge specific templates
                gsub(rmtemplate, "", $0);

# discard all "form of" and "plural of" entries
                if(index($0, "{{plural of|") !=0) next;
                if(index($0, "{{form of|") !=0) next;
                if(index($0, "{{archaic form of|") !=0) next;
                if(index($0, "{{Latn-def|") !=0) next;

# convert {{term|...|lang=xx}} -> [[...]]
                $0=gensub(/(\{\{term\|)([^}\|]*)([^}]*)(\}\})/, "[[\\2]]", "g", $0);

# convert {{l|???|...}} -> [[...]]
                $0=gensub(/(\{\{l\|[^\|\}]*\|)([^\}]*)(\}\})/, "[[\\2]]", "g", $0);

# convert {{gloss|...}} -> (...)
                $0=gensub(/(\{\{(gloss)\|)([^}]*)(\}\})/, "(\\3)", "g", $0);

# convert {{non-gloss definition|...}} , {{n-g|, {{w|, {{spelink| {{&lit| {{pedlink| -> ...
                $0=gensub(/(\{\{(non-gloss definition|n-g|w|spelink|pedlink|[&]amp[;]lit)\|)([^}]*)(\}\})/, "\\3", "g", $0);

# convert {{sense|...}} -> (...)
                $0=gensub(/(\{\{sense\|)([^}]*)(\}\})/, "(\\2)", "g", $0);

# convert {{qualifier|...}} -> [...]
                $0=gensub(/(\{\{qualifier\|)([^}]*)(\}\})/, "[\\2]", "g", $0);

# convert {{italbrac|...}} -> (...)
                $0=gensub(/(\{\{italbrac\|)([^}]*)(\}\})/, "(\\2)", "g", $0);

# convert |_| -> " "
                gsub(/\|_\|/, " ", $0);

# convert {{apocopic form of|...}} etc.
# regexp not working?
                $0=gensub(/(\{\{(apocopic|obsolete) form of\|)([^}]*)(\}\})/, "\\2 form of \\3", "g", $0);

# convert {{feminine of|...}} etc.
                $0=gensub(/(\{\{(feminine|neuter|diminutive|superlative|comparative|augmentative) of\|)([^}]*)(\}\})/, "\\2 form of \\3", "g", $0);

# convert {{reflexive of|link|word}} -> reflexive form of [[word]]
                $0=gensub(/(\{\{(reflexive) of\|)([^}]*[|])([^}|]+)(\}\})/, "\\2 form of \\4", "g", $0);

# convert {{reflexive of|link}} -> reflexive form of [[link]]
                $0=gensub(/(\{\{(reflexive) of\|)([^}|]+)(\}\})/, "\\2 form of \\3", "g", $0);

# convert {{alternative spelling of|...}} etc.,
                $0=gensub(/(\{\{(contraction of|dated form of|alternative capitalization of|informal spelling of|nonstandard spelling of|alternative spelling of|obsolete spelling of|alternative form of|alternate form of|feminine plural of|abbreviation of|acronym of|rare spelling of|archaic spelling of|singular of|obsolete form of|eye dialect of|agent noun of|initialism of)\|)([^}]*)(\}\})/, "\\2 \\3", "g", $0);

# covert {{given name|male/female}}
                $0=gensub(/(\{\{given name\|)(male|female)(\}\})/, "\\2 given name", "g", $0);

# convert {{surname|
                replacement=lang" surname";
                $0=gensub(/\{\{surname[^}]*\}\}/, replacement, "g", $0);

# convert {{etyl|iso|iso2}} -> {{iso}}
# TODO: {{iso}} -> Language-name
                $0=gensub(/(\{\{etyl[|])([^|]*)([|][^}]*}})/, "{{\\2}}", "g", $0);

# verb: determine if transitive, intransitive, reflexive
                        if(pos=="v") {
                        gend2="";
                        if(match($0, "intransitive") != 0) gend2 = (gend2 "i");
                        if(match($0, "[^n]transitive") != 0) gend2 = (gend2 "t");
                        if(match($0, "reflexive") != 0) gend2 = (gend2 "r");
                        if(match($0, "pronominal") != 0) gend2 = (gend2 "p");
                        }

                        pos3=( pos gend );
                        pos3=( pos3 gend2 );
                        pos3=gensub(/(n)([mfncps])/, "\\2", "1", pos3);

                        LHS = sprintf("[[%s]] {%s}",title,pos3);

                        gsub(/^[\x20]*\x23[\x20]*/,"",$0);
                        gsub(/<\/text>/,"",$0);
                        gsub(/\.$/,"",$0);
                        regexp="\\|lang\\="iso;
                        gsub(regexp,"",$0);
                        $0 = gensub(/(\{\{|\|)((reflexive|intransitive|transitive|pronominal)\|)/,"\\1", "g", $0);
                        $0 = gensub(/(\|(reflexive|intransitive|transitive|pronominal))(\}\})/,"\\3", "g", $0);
                        $0 = gensub(/(\{\{(reflexive|intransitive|transitive|pronominal)\}\})/,"\\3", "g", $0);
                        gsub(/\{\{context\|/,"{{", $0);
                        gsub(/\{\{\}\}/,"", $0);

                        gsub(/\#English/,"",$0);
                        gsub(/\[\|/,"[",$0);

                        outp = LHS" :: "$0;
                        outp = sprintf("%s\t%s\t%s",title,pos3, $0);


# change :: {{...}} -> [...] ::
# templates at beginning of definition-lines are supposed to be context
                        #old=outp;
                        #for(i=0;i<10;i++)
                        #{
# move contexts to LHS
                        #if(match(old, /::[\x20]*\{\{(gloss|sense)[\|]/) != 0) break;
#                       #if(match(old, /::[\x20]*\{\{[^\}\|]*of[\|\}]/) != 0) break;
                        #outp=gensub(/(.*)([\x20]::[\x20])([\x20]*\{\{)([^\}]*)(\}\})(.*)/, "\\1 [\\4] \\2\\6", "g", old);
                        #if(outp==old) break;
                        #old=outp;
                        #}

# change [ | | ] -> [ , , ]
                        old=outp;
                        for(i=0;i<10;i++)
                        { outp=gensub(/([^\[]\[[^\]\[]*)(\|)([^\]]*])/, "\\1, \\3", "g", old);
                        if(outp==old) break;
                        old=outp;
                        }

# remove extra spaces
                        gsub(/[\ ]+/, " ", outp);

# convert {{plural}} -> {p}, {{m}} -> {m}, {{f}} -> {f}
                        outp=gensub(/(\{\{)([mfncsp])(lural\}\}|\}\})/, "{\\2}", "g", outp);

# rm #blabla from link inside square brackets
# first [[#bla|word]] -> [[title|word]] then other cases
                        outp=gensub(/(\[\[[#][^\|\]]*)(\|[^\]]*\]\])/, "[["title"\\2", "g", outp);
                        outp=gensub(/(\[\[[^\|\]]*[^ ])([ ]*[#][^\|\]]*)(\|[^\]]*\]\])/, "\\1\\3", "g", outp);

                        printout(outp);
                        #if (pos == "") print "#UNKNOWN POS on page ",title ; # unnecessary info?
                        }
                        }

$0 ~ warnmissing        {
                        if((pos=="-")&&(no_head==1))
                                print "missing head template on page [["title"]]" >"FIXME-"lang".txt";
                        }