#  gawk script to extract translations from the database dump of en.wiktionary.org
#
# (c) 2011-2012 by Matthias Buchmeier
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
# TODO: resolve {{unsupported|...}} esp. from glosses
# TODO: remove trans-see links without target
# TODO: inclusion of English "alternative forms/spellings"
# TODO: include blacklist of pages to be excluded, e.g Taumatawhakatangihangakoauauotamateaturipukakapikimaungahoronukupokaiwhenuakitanatahu
#
BEGIN {
# target language configuration
# to configure the target language edit the following lines
# or configure the target language on the command-line with the following options:
#
# Command-line options:
#######################
#  required gawk command-line switches:
#
#    name of the language to be extracted, or bar-separated list of languages:
#    -v LANG=language
#
#    iso-code of the language to be extracted, or bar-separated list of iso-codes:
#    -v ISO=iso-code
#
#    name of the language family as specified on the headline of a nested section:
#    (required only if LANG contains multiple languages)
#    -v GENERIC_LANG=language_family
#
#  optional gawk command-line switches:
#
#    this option has to be used for languages written in non-latin script, e.g. Cyrillic, Greek, etc.:
#    -v LATIN=n
#
#    remove wiki-links and wiki-style bolding, italicizing:
#    -v REMOVE_WIKILINKS=y --re-interval
#
#    don't include trans-see links:
#    -v TRANS_SEE=n
#
#    bar-separated list of languages to be excluded (the default is to include all nested lines):
#    -v EXCLUDE_LANG="language1|language2|langguage3"
#
#    bar-separated list of qualifiers to be added (specified in the same order as the ISO-list):
#    -v ISO_QUALIFIER="qualifier1|qualifier3"
#
#    bar-separated list of qualifiers to be added (specified in the same order as the LANG-list):
#    -v LANG_QUALIFIER="qualifier1||qualifier3"
#
#########################
# User defined variables:
#########################
# English names of the target language as specified on beginning of translation line,
# multiple names have to separated by "|":
# this list should include the both the language family name and the nested section language names
# lang="Spanish";
#
# iso codes of the target language as used in t-template,
# multiple codes have to separated by "|":
# iso = "es";
#
# unique language family name, as used in nesting headline
#generic_lang = "Spanish";
generic_lang = "";
#
# language headwords of nested sections to be excluded from the dictionary
# multiple languages have to separated by "|":
exclude_lang = "";
#
# set to 0/1  for latin/non-latin script
latin = 1;
#
# set to 0 if you want to remove [[]]-wikilinks and wiki-syntax bolding and italicizing
remove_wikilinks=0;
#
# set to 1 if transliterations might contain wikilinks
links_inside_tr=0;
#
# show trans-see links
enable_trans_see=1;
#
# show ttbc sections
enable_ttbc=1;
#
# enable English IPA
enable_ipa=0;
#
# parsing of commandline switches
#
if(LANG!="") lang = LANG;
#
# default excluded languages (uncomment if you want to specify them on the command line)
if(EXCLUDE_LANG=="")
{
if(lang=="French") exclude_lang = "French Creole|Old French|Middle French";
if(lang=="Spanish") exclude_lang = "Old Spanish|Aragonese";
if(lang=="German") exclude_lang = "Low German|Middle High German|Old High German|Alemannic|Alemannic German|Kölsch|Bavarian|Alsatian|Badisch|Berliner|Bernese|Camelottisch|Frankonian|Lichtensteinisch|Luxembourgeois|Moselfraenkisch|Plattdeutsch|Rhoihessisch|Ruhrisch|Saarlaendisch|Saxon|Swabian|Viennese|Alsace|Palatinate German|Swiss German|Kölsch";
if(lang=="Italian") exclude_lang = "Sicilian";
}
#
# predefined language options (uncomment if you want to configure on the command line)
if(lang == "Norwegian")
{
iso="no|nn|nb";
lang="Norwegian|Nynorsk|Norwegian Nynorsk|Bokmål|Norwegian Bokmål|Norwegian Høgnorsk";
iso_qualifier="|Nynorsk|Bokmål";
lang_qualifier="|Nynorsk|Nynorsk|Bokmål|Bokmål|Høgnorsk";
exclude_lang = "Old Norse|Old Norwegian"
}
#
if(lang == "Dutch")
{
iso="nl|vls";
lang="Dutch|Flemish|West Flemish|Brabantish";
iso_qualifier="|Flemish";
lang_qualifier="|Flemish|Flemish|Brabantish";
exclude_lang = "Dutch Low Saxon|Old Dutch|Drents|Gronings|Twents";
}
#
if(lang == "Japanese")
{
iso="ja";
links_inside_tr=1;
latin=0;
}
#
if(lang == "Standard_Arabic")
{
generic_lang="Arabic";
lang="Arabic|MSA|Standard Arabic";
iso="ar|arb";
latin=0;
enable_trans_see=0;
exclude_lang = "Algerian|Andalusian|Bahrani|Chadian|Egyptian|Egyptian Arabic|Gulf|Gulf Arabic|Hassānīya|Iraqi|Iraqi Arabic|Lebanese|Lebanese/Syrian|Levantine|Levantine Arabic|Libyan|Moroccan|Moroccan Arabic|Morocco|North Levantine Arabic|Palestinian|Palestinian Arabic|South Levantine Arabic|Syrian|Sudanese|Tunisian Arabic|UAE"
}
#
#
if(lang == "Mandarin")
{
generic_lang="Chinese";
lang="Mandarin|Central Mandarin|Jianghuai Mandarin|Northern Mandarin|West Mandarin|Wuhan|Xi[']an|Liuzhou|Chengdu|Xuzhou|Yangzhou|Ürümqi|Harbin|Simplified|Traditional|Chinese [(]Mandarin[)]|Chinese traditional[/]simplified|Chinese|Pinyin|Chinese [(]Traditional[)]|Chinese [(]Simplified[)]";
lang_qualifier="|Central China|Jianghuai|Northern China|West China|Wuhan|Xi[']an|Liuzhou|Chengdu|Xuzhou|Yangzhou|Ürümqi|Harbin|"
iso="zh|lzh|zho|chi|cmn|zh-tw|zh-cn|zhx-zho";
iso_qualifier="|Literary Chinese|";
latin=0;
enable_trans_see=0;
exclude_lang = "Amoy|Bai|Cantonese|Changsha|Chaozhou|Dungan|Eastern Hokkien|Eastern Min|Fuzhou|Gan|Guangzhou|Haikou|Hainanese|Hakka|Hangzhou|Hokkien|Hui|Jian[']ou|Jin|Jixi|Meixian|Min Bei|Min Dong|Min-nan|Min nan|Min Nan|Min-Nan|Nanchang|Nanning|Northern Hokkien|Northern Min|Northern Wu|Old Chinese|Pinghua|Shanghai|Shanghainese|Sichuanese|Southern Min|Southern Wu|Suzhou|Taiyuan|Taiwan|Taiwanese|Teochew|Tuhua Dong[']an|Wenzhou|Wu|Xiang|Xiamen|Yangzhou|Yue"
}
#
if(lang == "Mandarin_nonested")
{
lang="Mandarin";
generic_lang="Mandarin";
enable_trans_see=0;
enable_ttbc=0;
latin=0;
iso="zh|cmn"
}
#
#
if(lang=="Persian")
{
iso="fa";
exclude_lang="Old Persian";
latin=0;
enable_trans_see=0;
}
#
if(lang=="Kurdish")
{
iso="ku|kmr|kur";
exclude_lang="Sorani|Soranî";
lang="Kurmanji|Kurmancî|Kurdish";
generic_lang="Kurdish";
enable_trans_see=0;
latin=0;
}
#
# Modern Greek
if(lang=="Greek")
{
iso="el";
exclude_lang="Ancient Greek|Ancient|Hebrew|Modern Romanization|Ancient Romanization|Mycenaean|Classical|Katharevousa|Katharevoussa|Pontic Greek|Koine|Pontic Greek|Roman";
lang="Modern Greek|Modern|Greek";
generic_lang="Greek";
latin=0;
}
#
if(lang=="Indonesian")
{
iso="id";
generic_lang="Indonesian";
lang=="Indonesian|Standard Indonesian|Stabdard"
exclude_lang="Acehnese|Balinese|Banjar|Banjarese|Buginese|Javanese|Kaili|Madurese|Makasar|Mandar|Minangkabau|Nias|Sasak|Sunda|Sundanese|Indonesian Bajau";
enable_trans_see=0;
}
#
if(lang=="Malay")
{
iso="ms";
generic_lang="Malay";
lang=="Rumi|Malay"
exclude_lang="Malayalam|Malaysian Sign Language|Jawi";
enable_trans_see=0;
}
#
# END of user defined section
#############################
#
if(LATIN == "n") latin = 0;
if(REMOVE_WIKILINKS == "y") remove_wikilinks = 1;
if((ISO!="")&&(iso=="")) iso = ISO;
if(GENERIC_LANG!="") generic_lang = GENERIC_LANG;
if((LANG!="")&&(GENERIC_LANG=="")&&(generic_lang=="")) generic_lang = LANG;
if(ISO_QUALIFIER!="")  iso_qualifier = ISO_QUALIFIER;
if(LANG_QUALIFIER!="")  lang_qualifier = LANG_QUALIFIER;
if(TRANS_SEE=="n") enable_trans_see = 0;
if(EXCLUDE_LANG!="") exclude_lang = EXCLUDE_LANG;
if(ENABLE_IPA=="y") enable_ipa = 1;
#
#print "lang="lang";iso="iso";generic_lang="generic_lang";exclude_lang="exclude_lang;
#
# save iso- and lang-qualifiers into array
n_iso=split(iso,iso_array,"|");
split(iso_qualifier,iso_qualifier_array,"|");
for(i=1;i<=n_iso;i++) {
if(iso_qualifier_array[i] == "") qualifier[iso_array[i]] = "";
else   qualifier[iso_array[i]] = " ["iso_qualifier_array[i]"] ";
#print iso_array[i]" "qualifier[iso_array[i]];
}

n_lang=split(lang,lang_array,"|");
split(lang_qualifier,lang_qualifier_array,"|");
for(i=1;i<=n_lang;i++) {
if(lang_qualifier_array[i] == "") qualifier[lang_array[i]] = "";
else   qualifier[lang_array[i]] = " ["lang_qualifier_array[i]"] ";
#print lang_array[i]" "qualifier[lang_array[i]];
}

#
# initialization of variables used for parsing
#
# english = 0/1 outside/inside English section
english = 0;
# trans = 0/1 outside/inside Translations section
trans = 0;
# gloss = gloss-string or empty
gloss = "";
# pos = part of speech
pos = "";
# title = pagetitle
title = "";
# inside nested section? 0/1
nestsect = 0;
# inside Pronunciation section ?
pron = 0;
# default IPA pronunciation
ipa1 = "";
# default IPA regexp
defipa="\\{\\{a\\|(US|GenAm).*\\{\\{IPA\\|";
# alternative IPA pronunciation
ipa2 = "";
# alternative IPA regexp
altipa = "\\{\\{IPA\\|";
#
oldLHS = ""; oldRHS = "";
# regexp matching translation line
#transline = "^[*:]*[\\x20]*[[]*("lang")[]]*[\\x20]*[:]|^[*:]*[\\x20]*\\{\\{qualifier\\||\\{\\{ttbc\\|("lang")\\}\\}|\\{\\{ttbc\\|("iso")\\}\\}";
# regexp matching start of nested section
if(enable_ttbc==1)
neststart = "^\\*[\\x20]*([[]*("generic_lang")|\\{\\{ttbc\\|("generic_lang")\\}\\}|\\{\\{ttbc\\|("iso")\\}\\}|\\{\\{trreq\\|("iso")\\}\\})";
if(enable_ttbc==0)
neststart = "^\\*[\\x20]*[[]*("generic_lang")";
# regexp matching translation lines to be excluded
exclude = "^$";
if(exclude_lang != "")
#exclude = "^[*:]*[\\x20]*[[]*("exclude_lang")[]]*[\\x20]*[:]";
exclude = "^[*:]*[\\x20]*[[]*("exclude_lang")";
}

function printout(outp) {

# convert special xml formating like &lt; to html
                        gsub(/&lt;/,"<",outp);
                        gsub(/&gt;/,">",outp);
                        gsub(/&amp;/,"\\&",outp);
                        gsub(/&quot;/,"\"",outp);
                        gsub(/&nbsp;/, " ", outp);
                        gsub(/&hellip;/, "...", outp);
                        gsub(/&quot;/, "\"", outp);
                        gsub(/&[mn]dash;/, "-", outp);
                        gsub(/&thinsp;/, "", outp);

# NOTE: these must be done after converting '&lt;' -> '<'  and '&gt;' -> '>'
# remove <ref ... \>
                        gsub(/<ref[^>]*\/>/,"",outp);

# remove <ref [name=....]> blabla </ref> OK?
                        gsub(/<ref[^>]*>.*<\/ref>/,"",outp);

# remove one-line <!-- commented text -->
                        gsub(/<!--[^>]*-->/,"",outp);

# remove extra spaces
                        gsub(/[\ ]+/, " ", outp);

# remove remaining "<!--" (will prevent display of wikifile)
                        gsub(/<!--/,"", outp);

if(remove_LHS-term==1) {
# remove LHS {{term|...}}
                        gsub(/\|sc=[^\|\}]*/, "", outp);
                        gsub(/\|lang=[^\|\}]*/, "", outp);
                        gsub(/\{\{term\|/, "", outp);
                        gsub(/\}\}/, "", outp);
                        }

if(remove_wikilinks==1) {
                        outp = gensub(/([[][[])([^]|]*\|)([^]]*)([]][]])/ , "\\3", "g", outp);
                        outp = gensub(/([[][[])([^]]*)([]][]])/ , "\\2", "g", outp);
                        gsub(/[']{2,}/, "", outp);
                        }

# force LR-switch for some characters
if((generic_lang=="Arabic")&&(remove_wikilinks==0)) {
                        gsub(/[]][ ]*[/]3/, "] {{LR}}/3", outp);
                        }

                        print outp;
}

# determine page title
/\x3Ctitle/ {
gsub(/^[^\x3C]*/, ""); gsub(/[^\x3E]*$/, ""); gsub(/\x3Ctitle\x3E/, ""); gsub(/\x3C\/title\x3E/, "");
title=$0;
english=0;
trans=0; gloss=""; pos=""; nestsect=0;
if(index(title,"Wiktionary:") != 0) title="";
if(index(title,"Template:") != 0) title="";
if(index(title,"Appendix:") != 0) title="";
if(index(title,"User:") != 0) title="";
if(index(title,"Help:") != 0) title="";
}

# discard non-useful lines (speedup and false "trans-see" lines from comment lines)
/<comment>|<\/?page>|<timestamp>|<id>|<\/?contributor>|<\/?revision>|<username>|<minor \/>/  {next;}
/^$/ {next;}
/^[#\[]/ {next;}

# discard Wiktionary, Template and Appendix namespaces
{if(title=="") next;}

# detect English language section
/\x3D\x3D[\x20]*English[\x20]*\x3D\x3D/ {
english=1;
trans=0; gloss = ""; pos= ""; nestsect = 0;
pron=0; ipa1=""; ipa2="";
next;}

# detect non-English language section
/^\x3D\x3D[^\x3D]+/ {
english=0;
trans=0; gloss = ""; pos= ""; nestsect = 0;
next;}

# language and title detection done; skip all lines if not inside English section
{if(english==0) next;}

# determine pronunciation section
/\x3D\x3D\x3D[\x20]*Pronunciation/ {pron=1; ipa1=""; ipa2="";}
#determine ipa1 and ipa2
$0 ~ defipa {
if((pron==1)&&(ipa1=="")){      gsub(/\|lang\=en/, "", $0);
                                ipa1=gensub(/(.*\{\{IPA\|[\/\[]*)([^}\|\/]*)([\/\]]*.*)/, "\\2", "g", $0);
# print "def "title" "ipa1 >>"IPA.txt";
next;
}}
$0 ~ altipa {
if((pron==1)&&(ipa2=="")) {     gsub(/\|lang\=en/, "", $0);
                                ipa2=gensub(/(.*\{\{IPA\|[\/\[]*)([^}\|\/]*)([\/\]]*.*)/, "\\2", "g", $0);
# print "alt "title" "ipa2 >>"IPA.txt";
next;
}}

# determine part of speech (POS)
/\x3D\x3D\x3D[\x20]*Noun/ { pos="n"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Verb/ { pos="v"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Adjective/ { pos="adj"; trans=0;gloss = "";  next;}
/\x3D\x3D\x3D[\x20]*Adverb[\x20]*\x3D\x3D\x3D/ { pos="adv"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Interjection[\x20]*\x3D\x3D\x3D/ { pos="interj"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Article[\x20]*\x3D\x3D\x3D/ { pos="art"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Proper\x20noun[\x20]*\x3D\x3D\x3D/ { pos="prop"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Preposition[\x20]*\x3D\x3D\x3D/ { pos="prep"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*\{\{initialism/ { pos="initialism"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Initialism[\x20]*\x3D\x3D\x3D/ { pos="initialism"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Numeral[\x20]*\x3D\x3D\x3D/ { pos="num"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Cardinal num(ber|eral)[\x20]*\x3D\x3D\x3D/ { pos="cardinal num"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Ordinal number[\x20]*\x3D\x3D\x3D/ { pos="ordinal num"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Number[\x20]*\x3D\x3D\x3D/ { pos="num"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*\{\{acronym/ { pos="acronym"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Acronym/ { pos="acronym"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*\{\{abbreviation/ { pos="abbr"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Abbreviation[\x20]*\x3D\x3D\x3D/ { pos="abbr"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Determiner[\x20]*\x3D\x3D\x3D/ { pos="determiner"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Phrase[\x20]*\x3D\x3D\x3D/ { pos="phrase"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Suffix[\x20]*\x3D\x3D\x3D/ { pos="suffix"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Pronoun[\x20]*\x3D\x3D\x3D/ { pos="pron"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Conjunction[\x20]*\x3D\x3D\x3D/ { pos="conj"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Proverb[\x20]*\x3D\x3D\x3D/ { pos="proverb"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Contraction[\x20]*\x3D\x3D\x3D/ { pos="contraction"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Particle[\x20]*\x3D\x3D\x3D/ { pos="particle"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Symbol[\x20]*\x3D\x3D\x3D/ { pos="symbol"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Prefix[\x20]*\x3D\x3D\x3D/ { pos="prefix"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Possessive[\x20]adjective[\x20]*\x3D\x3D\x3D/ { pos="adj"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*(Adverb|Adverbial)[\x20]phrase[\x20]*\x3D\x3D\x3D/ { pos="adv"; trans=0; gloss = ""; next;}
/\x3D\x3D\x3D[\x20]*Prepositional[\x20]phrase[\x20]*\x3D\x3D\x3D/ { pos="prep"; trans=0; gloss = ""; next;}

# detect end of Translations section
/^\x3D\x3D|^\[\[/ {trans=0; nestsect=0;}

# detect start of Translations section
/\x3D\x3D\x3D\x3D[\x20]*Translations[\x20]*\x3D\x3D\x3D\x3D/ {
if(english==1) {trans=1; gloss=""; nestsect=0;}
next;}

# detect start of Checktrans section
/\{\{checktrans/ {gloss=""; nestsect=0;}

# determine gloss
/\{\{trans\-top\|/ {
gloss=gensub(/(\{\{trans\-top\|)(.*)(\}\})/, "\\2", "g", $0);
gsub(/\{\{jump[^\}]*\}\}/, "", gloss);
gsub(/\([1-9]\)/, "", gloss);
nestsect=0;
}

# handle {{trans-see||}} links
/\{\{trans\-see\|/ {

# remove <\/text>, (might be there at the end of page (XML-code)
                gsub(/<\/text>/,"",$0);

                gloss=gensub(/(\{\{trans-see\|)([^\}\|]*)(\}\}.*)/, "\\2", "g", $0);
                link=gloss;
                if(gloss==$0)  {
                gloss=gensub(/(\{\{trans-see\|)([^\|]+)(\|)([^\}]+)(\}\}.*)/, "\\2", "g", $0);
                link=gensub(/(\{\{trans-see\|)([^\|]+)(\|)([^\}]+)(\}\}.*)/, "\\4", "g", $0);
                }
#               print "TRANS-SEE: "$0" :: "gloss" :: "link;

                gsub(/\[\[/,"",gloss);
                gsub(/\]\]/,"",gloss);

                LHS = sprintf("[[%s]] ", title);
                        if(pos != "") LHS = (LHS sprintf("{%s} ", pos));
                if(enable_ipa==1) {
                        if(ipa1!="") { LHS = (LHS sprintf("/%s/ ", ipa1)); ipa1=""; ipa2="";}
                        if(ipa2!="") { LHS = (LHS sprintf("/%s/ ", ipa2)); ipa1=""; ipa2="";}
                        }
                        if (gloss != "") LHS = (LHS sprintf("(%s) ", gloss));

                if(index(link,"[[")==0)
                        outp = (LHS " SEE: [["link"]] ::");

                if(index(link,"[[")!=0)
                        outp = (LHS " SEE: "link" ::");

if(enable_trans_see==1)
                        printout(outp);
                        gloss=""; nestsect = 0;
}

# determine nested section
/^[*][^*:]|\{\{ttbc|\{\{trans\-|\{\{trreq|^[[]/ {nestsect = 0;}
#/^\*[\x20]*[[]*[A-Z]|\{\{ttbc|\{\{trans\-|\{\{trreq/ {nestsect = 0;}
$0 ~ neststart {nestsect = 1;}

# skip lines matching exclude
$0 ~ exclude {next;}

# skip {{trreq| ... lines
/\{\{trreq\|/  {next;}

# determine translations
#$0 ~ transline {
{if(trans==0) next;}
/^[*]/ {
# print "transline:"$0";trans="trans";nestsect="nestsect;
        if((trans==1)&&(nestsect==1)) {

# set LHS
                LHS = sprintf("[[%s]] ", title);
                # if(pos != "") LHS = (LHS sprintf("{%s} ", pos));
                # if(enable_ipa==1) {
                #         if(ipa1!="") { LHS = (LHS sprintf("/%s/ ", ipa1)); ipa1=""; ipa2="";}
                #         if(ipa2!="") { LHS = (LHS sprintf("/%s/ ", ipa2)); ipa1=""; ipa2="";}
                #         }
                # if (gloss != "") LHS = (LHS sprintf("(%s) ", gloss));

# conversion of obsolete/redirected/equivalent templates
#
gsub(/\{\{(i|italbrac|ib|qual)\|/, "{{qualifier|", $0);
gsub(/\{\{(t-simple|apdx-t|t-SOP|t[+]|t[-]|tø)\|/, "{{t|", $0);

regexp="^\\*[\\x20]*[[]*"generic_lang"[\\x20]*[]]*[:]";
if($0 ~ regexp) {

for(i=1;i<=n_iso;i++) {
regexp="\\{\\{t\\|"iso_array[i]"\\|"
repl=qualifier[iso_array[i]]"&";
#print regexp"; "repl;
gsub(regexp, repl);
} }

for(i=1;i<=n_lang;i++) {
regexp="^[*:]*[\\x20]*[[]*"lang_array[i]"[]]*[\\x20:]*|^[*:]*[\\x20]*\\{\\{ttbc\\|"lang_array[i]"\\}\\}[\\x20:]*";
gsub(regexp, qualifier[lang_array[i]]);
}

for(i=1;i<=n_iso;i++) {
regexp="^[*:]*[\\x20]*\\{\\{ttbc\\|"iso_array[i]"\\}\\}[\\x20:]*";
gsub(regexp, qualifier[iso_array[i]]);
}

# remove remaining "^** " from qualifier nested sections
                        sub(/^[*:]*[\x20]*/, "" ,$0);

# remove xs parameter from t-templates:
                        gsub(/\|xs=[^\|\}]*/, "", $0);

# remove sc script-type parameter from t-templates:
                        gsub(/\|sc=[^\|\}]*/, "", $0);

                        TR=$0;

# remove script templates Cyrl, Arab, fa-Arab, Thai, IPA, IPAchar, unicode, Jpan, Latinx, Hani, Hans, Hant, Tfng, Deva, Hebr, Kore, Hang:
                        TR=gensub(/(\{\{(Arab|Cyrl|fa-Arab|IPA|IPAchar|Thai|unicode|Jpan|Latinx|Hani|Hans|Hant|Tfng|ku-Arab|Deva|Hebr|Kore|Hang)\|)([^}]*)(\}\})/, "\\3", "g", TR);

# language family related templates
        if(generic_lang=="Arabic") {
                        gsub(/\{\{LR\}\}/,"",TR);
                        gsub(/\{\{dual\}\}/,"{dual}",TR);
        }

        if((generic_lang=="Chinese")||(generic_lang=="Mandarin")) {
# first version without wikilinks inside
                        TR=gensub(/(\{\{zh\-ts\|)([^\|\[]*)(\|)([^\|\[]*)(\}\})/, "[[\\2]], [[\\4]]", "g", TR);
                        TR=gensub(/(\{\{zh\-zh\-p\|)([^\|\[]*)(\|)([^\|]*)(\}\})/, "[[\\2]] /\\4/", "g", TR);
                        TR=gensub(/(\{\{zh\-tsp\|)([^\|\[]*)(\|)([^\|\[]*)(\|)([^\|]*)(\}\})/, "[[\\2]], [[\\4]] /\\6/", "g", TR);
# next allow wikilinks but don't link additionally
                        TR=gensub(/(\{\{zh\-ts\|)([^\|]*)(\|)([^\|]*)(\}\})/, "\\2, \\4", "g", TR);
                        TR=gensub(/(\{\{zh\-zh\-p\|)([^\|]*)(\|)([^\|]*)(\}\})/, "\\2 /\\4/", "g", TR);
                        TR=gensub(/(\{\{zh\-tsp\|)([^\|]*)(\|)([^\|]*)(\|)([^\|]*)(\}\})/, "\\2, \\4 /\\6/", "g", TR);
        }

# rm rfr rfscript
                        gsub(/\{\{(rfr|rfscript)\|[^}]*\}\}/, "", TR);

# convert {{term|...|lang=xx}} -> [[...]]
                        TR=gensub(/(\{\{term\|)([^}\|]*)([^}]*)(\}\})/, "[[\\2]]", "g", TR);

# convert {{l|iso|...|...|tr=...|g=...}} -> [[...|...]] /TR/
        if(latin == 0)  {
                        regexp = "(\\{\\{l[^}]*)(\\|tr=)([^|}]*)([^}]*\\}\\})";
                        TR=gensub(regexp, "\\1\\4 /\\3/", "g", TR);
                        }
                        regexp = "(\\{\\{l[^}]*)(\\|)(g=|g2=|gloss=)([^|}]*)([^}]*\\}\\})"
                        TR=gensub(regexp, "\\1\\5", "g", TR);

                        TR=gensub(/(\{\{l\|)([^}\|]*\|)([^}]*)(\}\})/, "[[\\3]]", "g", TR);
#                       TR=gensub(/(\{\{l\|)([^}\|]*\|)([^}\|]*)(\|[^}]*\}\})/, "[[\\3]]", "g", TR);

# convert {{t|...}} -> [[...]] and determine gender and singular/plural:
############################################################################
# move Transliteration (tr= arguments) -> /.../
        if(latin == 0)  {
                        regexp = "(\\{\\{[^}]*)(\\|tr=)([^|}]*)([^}]*\\}\\})";
                        TR=gensub(regexp, "\\1\\4 /\\3/", "g", TR);
                        }

#                       regexp = "({{(t|t[+]|t[-]|tø)\\|("iso")\\|[^\\|}]*)(\\|)([mfnspc])([^}]*}})";

                        regexp = "(\\{\\{t\\|("iso")\\|[^}]*)(\\|)([mfnspc]\\|[mfnspc])(\\}\\}|\\|[^}]*}})";
                        TR=gensub(regexp, "\\1\\5 {{\\4}}", "g", TR);
                        regexp = "(\\{\\{t\\|("iso")\\|[^}]*)(\\|)([mfnspc])(\\}\\}|\\|[^}]*\\}\\})";
                        TR=gensub(regexp, "\\1\\5 {\\4}", "g", TR);
                        TR=gensub(regexp, "\\1\\5 {\\4}", "g", TR);
                        regexp = "(\\{\\{t\\|("iso")\\|)([^}\\]\\[]*)(\\}\\})";
                        TR=gensub(regexp, "[[\\3]]", "g", TR);
                        regexp = "(\\{\\{t\\|("iso")\\|)([^}]*)(\\}\\})";
                        TR=gensub(regexp, "\\3", "g", TR);
                        gsub(/\|alt\=/, "|", TR);
                        TR=gensub(/([[][[])(alt\=)([^|]*)(\|)([^]]*)([]][]])/, "[[\\5|\\3]]", "g", TR);

# convert {{m}}, {{m|f}}, {{m|f|n}}, {{m|f|n|p}}
                        TR=gensub(/(\{\{)([mfncsp])(\}\})/, "{\\2}", "g", TR);
                        TR=gensub(/(\{\{)([mfncsp])(\|)([mfncsp])(\}\})/, "{\\2} {\\4}", "g", TR);
                        TR=gensub(/(\{\{)([mfncsp])(\|)([mfncsp])(\|)([mfncsp])(\}\})/, "{\\2} {\\4} {\\6}", "g", TR);
                        TR=gensub(/(\{\{)([mfncsp])(\|)([mfncsp])(\|)([mfncsp])(\|)([mfncsp])(\}\})/, "{\\2} {\\4} {\\6} {\\8}", "g", TR);

                        regexp = "\\[\\[\\#("lang")\\|";
                        gsub(regexp, "[[", TR);
                        regexp = "#("lang")\\|";
                        gsub(regexp, "|", TR);

# convert common gender "{c}" to "{m} {f}" for languages de, es, fr, it, pt
if((iso=="de")||(iso=="es")||(iso=="fr")||(iso=="it")||(iso=="pt")) {
                        gsub(/\{\{c\}\}/,"{m} {f}",TR);
                        gsub(/\{c\}/,"{m} {f}",TR);
                        }

# convert obsolete {{plural}} to {p}
                        gsub(/\{\{plural\}\}/,"{p}",TR);

# convert {{pf.}}, {{impf}}
                        gsub(/\{\{impf\}\}/,"{impf}",TR); gsub(/\{\{pf[.]*\}\}/,"{pf}",TR);

# convert {{indeclinable}} {{indecl}}
                        gsub(/\{\{(indecl|indeclinable)\}\}/,"{indecl}",TR);

# remove {{g|}}, {{attention|}} tags, {{rfc-tbot}}, {{inv}}
                        gsub(/\{\{g\|[^\}]*\}\}|\{\{attention\|[^\}]*\}\}|\{\{rfc-tbot\}\}|\{\{inv\}\}/,"",TR);

# convert {{not used|iso}} -> Not used in LANG
                        regexp = "(\\{\\{not used\\|("iso")\\}\\})";
                        repl = "Not used in "generic_lang;
                        gsub(regexp, repl, TR);

# convert "qualifier" templates -> [...]:
                        TR=gensub(/(\{\{qualifier\|)([^}]*)(\}\})/, "[\\2]", "g", TR);

# remove (1) and thelike
                        gsub(/\([0-9\x20,;-]*\)/, "", TR);

# convert Transliteration in brackets (...) -> /.../
                if(latin == 0) {
                        if(links_inside_tr==1) TR=gensub(/([^'])(\()([^'][^){]*)(\))/ ,"\\1/\\3/", "g", TR);
                        if(links_inside_tr==0) TR=gensub(/([^'])(\()([^'][^)[{\+\"]*)(\))/ ,"\\1/\\3/", "g", TR);
# rm empty transliteration "//" (due to empty tr argument)
                        gsub(/[/][/]/, "", TR);
                        }
# rm empty wikilinks
                        gsub(/\[\[[ ]*\]\]/, "", TR);

# convert {{gloss|...}},  {{sense|...}} -> (...)
                        TR=gensub(/(\{\{(gloss|sense)\|)([^}]*)(\}\})/, "(\\3)", "g", TR);

# bartek
                        # if (gloss != "") TR = (sprintf("(%s) ", gloss) TR);
                        TR=gensub(/(\{)([mfncsp])(\})/, "", "g", TR);
                        if(enable_ipa==1) {
                                if(ipa1!="") { TR = (sprintf("/%s/ ", ipa1) TR); ipa1=""; ipa2="";}
                                if(ipa2!="") { TR = (sprintf("/%s/ ", ipa2) TR); ipa1=""; ipa2="";}
                                }
                        if(pos != "") TR = (sprintf("{%s} ", pos) TR);
# remove <\/text>, (might be there at the end of page (XML-code)
                        gsub(/<\/text>/,"",TR);

# change [ | | ] -> [ , , ]
                        old=TR;
                        for(i=0;i<20;i++)
                        {TR=gensub(/((^|[^\[])\[[^\]\[]*)(\|)([^\]]*])/, "\\1, \\4", "g", old);
                        if(TR==old) break;
                        old=TR;}

if(LHS == oldLHS) {
if(TR != "") {if(oldRHS != "") oldRHS = oldRHS"; "TR;
                if(oldRHS == "") oldRHS = TR; }
}

if(LHS != oldLHS) {
if(oldRHS != "")  {outp = (oldLHS sprintf(":: %s",oldRHS));
                        printout(outp);}
oldLHS = LHS;
oldRHS = TR;
}

# print a comment if POS is unknown
                        if (pos == "") print "#WARNING: unknown POS on page:\""title"\"";
# end trans=1
}
next;
# end determine translations
}

# prevent flooding of dict with Warnings on nested lines starting with "** {{qualifier|"
/^[*:]*[\x20]*\{\{qualifier\|/ {next;}
/^[*][*:]/ {if((trans==1)&&(nestsect == 1)) print "#WARNING: unknown nested section headword on page:\""title"\", :",$0;}

END {
if(oldRHS != "")        {outp = (oldLHS sprintf(":: %s",oldRHS));
                printout(outp);}
}