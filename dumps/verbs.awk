# cat enwiktionary-20120821-pages-articles.xml | gawk -f verbs.awk
# wylistuje templatey, wlczayc do wiekszego skryptu
BEGIN {
    lang="German";
    langhead="\\x3D\\x3D[\\x20]*"lang"[\\x20]*\\x3D\\x3D";
    flush="";
    code="de"
    verbhead="\\{\\{"code"-";
}
/\x3Ctitle/ {
    #print flush
    gsub(/^[^\x3C]*/, ""); gsub(/[^\x3E]*$/, ""); gsub(/\x3Ctitle\x3E/, ""); gsub(/\x3C\/title\x3E/, "");
    title=$0; langsect=0;
    #flush=title;
}

$0 ~ langhead {
    langsect=1;
}

$0 ~ verbhead && !/form of/ {
    if(langsect==1) print title, $0;

}