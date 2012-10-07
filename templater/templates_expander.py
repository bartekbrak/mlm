# -*- coding: utf-8 -*-

import re
from collections import OrderedDict
from templates import templates
from functools import partial


def template_string_to_list(template_string, *args, **kwargs):
    """ formats template string ready for last template processor"""
    return template_string.replace('\n\n', '\n').format(*args, **kwargs).split('\n')


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
        mood = list(mood_dic.keys())[0]
        tenses = mood_dic[mood]
        # from ipdb import set_trace; set_trace()
        for tense in tenses:
            for person in range(1, 7):
                lhs = "%s_%s_%s" % (person, mood, tense)
                if lhs not in skip:
                    r[lhs] = args[x]
                    x += 1
    return r

def pprint(output):
    for description, word in output.items():
        print("{description}: {word}".format(description=description, word=word))


def CHA(template, *args, **kwargs):
    """arbitrary name"""
    template = templates[template]
    template = resolve_ternaries(template, **kwargs)
    return es_conj(template_string_to_list(template, *args, **kwargs))

def resolve_ternaries_helper(match, **kwargs):
    if match.groups()[0] in kwargs:
        return match.groups()[1]
    else:
        return match.groups()[2]

def resolve_ternaries(template, **kwargs):
    """format: (pseudo_test?val_if_true:val_if_false)"""
    m = re.compile('\((.*)\?(.*):(.*)\)')
    # m = re.compile('\{\{#if: \{\{\{(.*)\|\}\}\}\|(.*)\|(.*)\}\}')
    return m.sub(partial(resolve_ternaries_helper, **kwargs), template)

# pprint(CHA('es-conj-ar (errar)', ''))
# pprint(CHA('es-conj-ar (andar)', 'and'))
# pprint(CHA('es-conj-ar (andar)', 'and', ref_stem='and'))  # fake verb, can't find a sample
pprint(CHA('es-conj-ar', 'abland', ref_stem='ablánd'))
# pprint(CHA('es-conj-ar', 'abacor'))
# pprint(CHA('es-conj-ar (e-ie)', 'ac', 'rt'))
# pprint(CHA('es-conj-ar (e-ie) ref_obj', 'AAA', 'BBB'))
# pprint(CHA('es-conj-ar ref_stem', 'ababill', ref_stem='ababíll'))
