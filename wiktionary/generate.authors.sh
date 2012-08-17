#!/bin/bash
# author: http://en.wiktionary.org/wiki/User:Matthias_Buchmeier
# source www: http://en.wiktionary.org/wiki/User:Matthias_Buchmeier/download
# generates a list of enwiktionary contributors, sorted by number of edits
# excludes contributors with less edits than EDITTHREASH:
EDITTHREASH=200
TEMPFILE=./users-unsorted.txt
TARGET=CREDITS
#APIFLAGS=\&redirects\&aulimit=500\&auexcludegroup=bot
# include all bots, as inactive bots will be included anyhow
APIFLAGS=\&redirects\&aulimit=500

wget "http://en.wiktionary.org/w/api.php?action=query&list=allusers&format=xmlfm&auprop=editcount&auwitheditsonly$APIFLAGS=" -O -\
|gawk -f userlistfilter.awk -v THREASH=$EDITTHREASH >$TEMPFILE
NEXT=`tail -n 1 $TEMPFILE|gawk 'BEGIN {FS="\t";} /^NEXT/ {print $2;}'`

while [ "$NEXT" != "THELASTUSERLIST" ]
do
wget "http://en.wiktionary.org/w/api.php?action=query&list=allusers&format=xmlfm&auprop=editcount&auwitheditsonly&aufrom=$NEXT$APIFLAGS" -O -\
|gawk -f userlistfilter.awk -v THREASH=$EDITTHREASH >>$TEMPFILE
NEXT=`tail -n 1 $TEMPFILE|gawk 'BEGIN {FS="\t";} /^NEXT/ {print $2;}'`
#echo "$NEXT"
done

sort -r $TEMPFILE|gawk 'BEGIN {FS="\t";} /^[0-9]/ {print $2;}' >$TARGET
rm $TEMPFILE