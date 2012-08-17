BEGIN {
Count_Threash=1;
if(THREASH!="") Count_Threash=THREASH;
}

/[&]lt[;]u userid[=][&]quot[;]/ {
ID=gensub(/(^.*name[=][&]quot[;])(.*)([&]quot[;] editcount.*$)/, "\\2", $0);
COUNT=gensub(/(^.*editcount[=][&]quot[;])([0-9]*)([&]quot[;]).*$/, "\\2", $0);
if(1.0*COUNT>=Count_Threash) {printf "%08d\t", COUNT; print ID;}
}

/[&]lt[;]allusers aufrom[=][&]quot[;]/ {
NEXT=gensub(/(^.*[&]lt[;]allusers aufrom[=][&]quot[;])(.*)([&]quot[;] [\/][&]gt[;].*$)/, "\\2", $0);
}

END {
if(NEXT=="") { print "NEXT\tTHELASTUSERLIST"; exit;}
print "NEXT\t"NEXT;
}