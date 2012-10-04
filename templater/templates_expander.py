# -*- coding: utf-8 -*-

from collections import OrderedDict


def es_conj(args):
    r = result = OrderedDict()

    # use subjunctive present forms if no negative provided
    if len(args) == 62:
        for x in range(34, 39):
            args.append('no ' + args[x])

    grammar = [
     {'indicative':['present', 'imperfect', 'preterite', 'future', 'conditional']},
     {'subjunctive':['present', 'imperfect_ra', 'imperfect_se', 'future']},
     {'imperative':['affirmative', 'negative']}
     ]
    skip = ['1_imperative_affirmative', '1_imperative_negative']

    r['infinitive'] = args[0]
    r['gerund'] = args[1]
    r['past_participle'] = args[2]

    x = 3
    for mood_dic in grammar:
        mood = mood_dic.keys()[0]
        tenses = mood_dic[mood]
        # from ipdb import set_trace; set_trace()
        for tense in tenses:
            for person in range(1, 7):
                lhs = "%s_%s_%s" % (person, mood, tense)
                if lhs not in skip:
                    r[lhs] = args[x]
                    x += 1
    print r
    return r


def es_conj_ar_andar(stem, ref_stem=None):
    # To use with a reflexive verb add ''ref_stem=accented form of verb stem'' to the template call.
    if ref_stem:
        s = """{stem}arse
{stem}ándose
{stem}ado
me {stem}o
te {stem}as
se {stem}a
nos {stem}amos
os {stem}áis
se {stem}an

me {stem}aba
te {stem}abas
se {stem}aba
nos {stem}ábamos
os {stem}abais
se {stem}aban

me {stem}uve
te {stem}uviste
se {stem}uvo
nos {stem}uvimos
os {stem}uvisteis
se {stem}uvieron

me {stem}aré
te {stem}arás
se {stem}ará
nos {stem}aremos
os {stem}aréis
se {stem}arán

me {stem}aría
te {stem}arías
se {stem}aría
nos {stem}aríamos
os {stem}aríais
se {stem}arían

me {stem}e
te {stem}es
se {stem}e
nos {stem}emos
os {stem}éis
se {stem}en

me {stem}uviera
te {stem}uvieras
se {stem}uviera
nos {stem}uviéramos
os {stem}uvierais
se {stem}uvieran

me {stem}uviese
te {stem}uvieses
se {stem}uviese
nos {stem}uviésemos
os {stem}uvieseis
se {stem}uviesen

me {stem}uviere
te {stem}uvieres
se {stem}uviere
nos {stem}uviéremos
os {stem}uviereis
se {stem}uvieren

{ref_stem}ate
{ref_stem}ese
{stem}émonos
{stem}aos
{ref_stem}ense""".replace('\n\n', '\n').format(stem=stem, ref_stem=ref_stem)
    else:
        s = """{stem}ar
{stem}ando
{stem}ado

{stem}o
{stem}as
{stem}a
{stem}amos
{stem}áis
{stem}an

{stem}aba
{stem}abas
{stem}aba
{stem}ábamos
{stem}abais
{stem}aban

{stem}uve
{stem}uviste
{stem}uvo
{stem}uvimos
{stem}uvisteis
{stem}uvieron

{stem}aré
{stem}arás
{stem}ará
{stem}aremos
{stem}aréis
{stem}arán

{stem}aría
{stem}arías
{stem}aría
{stem}aríamos
{stem}aríais
{stem}arían

{stem}e
{stem}es
{stem}e
{stem}emos
{stem}éis
{stem}en

{stem}uviera
{stem}uvieras
{stem}uviera
{stem}uviéramos
{stem}uvierais
{stem}uvieran

{stem}uviese
{stem}uvieses
{stem}uviese
{stem}uviésemos
{stem}uvieseis
{stem}uviesen

{stem}uviere
{stem}uvieres
{stem}uviere
{stem}uviéremos
{stem}uviereis
{stem}uvieren

{stem}a
{stem}e
{stem}emos
{stem}ad
{stem}en""".replace('\n\n', '\n').format(stem=stem, ref_stem=ref_stem)

    # call= [

    # ]
    # print len(tuple(s.split("\n")))
    t = s.split("\n")
    es_conj(t)

es_conj_ar_andar('and')
