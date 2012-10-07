# -*- coding: utf-8 -*-

templates = {
    'es-conj-ar (errar)':
"""{0}errar
{0}errando
{0}errado

{0}yerro, {0}erro
{0}yerras, {0}erras
{0}yerra, {0}erra
{0}erramos
{0}erráis
{0}yerran, {0}erran

{0}erraba
{0}errabas
{0}erraba
{0}errábamos
{0}errabais
{0}erraban

{0}erré
{0}erraste
{0}erró
{0}erramos
{0}errasteis
{0}erraron

{0}erraré
{0}errarás
{0}errará
{0}erraremos
{0}erraréis
{0}errarán

{0}erraría
{0}errarías
{0}erraría
{0}erraríamos
{0}erraríais
{0}errarían

{0}yerre, {0}erre
{0}yerres, {0}erres
{0}yerre, {0}erre
{0}erremos
{0}erréis
{0}yerren, {0}erren

{0}errara
{0}erraras
{0}errara
{0}erráramos
{0}errarais
{0}erraran

{0}errase
{0}errases
{0}errase
{0}errásemos
{0}erraseis
{0}errasen

{0}errare
{0}errares
{0}errare
{0}erráremos
{0}errareis
{0}erraren

{0}yerra, {0}erra
{0}yerre, {0}erre
{0}erremos
{0}errad
{0}yerren, {0}erren""",
    'es-conj-ar (andar)':
"""{0}ar(ref_stem?se:)
{0}(ref_stem?ándose:ando)
{0}ado

(ref_stem?me :){0}o
(ref_stem?te :){0}as
(ref_stem?se :){0}a
(ref_stem?nos :){0}amos
(ref_stem?os :){0}áis
(ref_stem?me :){0}an

(ref_stem?me :){0}aba
(ref_stem?te :){0}abas
(ref_stem?se :){0}aba
(ref_stem?nos :){0}ábamos
(ref_stem?os :){0}abais
(ref_stem?me :){0}aban

(ref_stem?me :){0}uve
(ref_stem?te :){0}uviste
(ref_stem?se :){0}uvo
(ref_stem?nos :){0}uvimos
(ref_stem?os :){0}uvisteis
(ref_stem?me :){0}uvieron

(ref_stem?me :){0}aré
(ref_stem?te :){0}arás
(ref_stem?se :){0}ará
(ref_stem?nos :){0}aremos
(ref_stem?os :){0}aréis
(ref_stem?me :){0}arán

(ref_stem?me :){0}aría
(ref_stem?te :){0}arías
(ref_stem?se :){0}aría
(ref_stem?nos :){0}aríamos
(ref_stem?os :){0}aríais
(ref_stem?me :){0}arían

(ref_stem?me :){0}e
(ref_stem?te :){0}es
(ref_stem?se :){0}e
(ref_stem?nos :){0}emos
(ref_stem?os :){0}éis
(ref_stem?me :){0}en

(ref_stem?me :){0}uviera
(ref_stem?te :){0}uvieras
(ref_stem?se :){0}uviera
(ref_stem?nos :){0}uviéramos
(ref_stem?os :){0}uvierais
(ref_stem?me :){0}uvieran

(ref_stem?me :){0}uviese
(ref_stem?te :){0}uvieses
(ref_stem?se :){0}uviese
(ref_stem?nos :){0}uviésemos
(ref_stem?os :){0}uvieseis
(ref_stem?me :){0}uviesen

(ref_stem?me :){0}uviere
(ref_stem?te :){0}uvieres
(ref_stem?se :){0}uviere
(ref_stem?nos :){0}uviéremos
(ref_stem?os :){0}uviereis
(ref_stem?me :){0}uvieren

(ref_stem?{ref_stem}ate:{0}a)
(ref_stem?{ref_stem}ese:{0}e)
{0}(ref_stem?émonos:emos)
{0}(ref_stem?aos:ad)
(ref_stem?{ref_stem}ense:{0}en)""",
    'es-conj-ar':
"""{0}ar
{0}ando
{0}ado

{0}o
{0}as
{0}a
{0}amos
{0}áis
{0}an

{0}aba
{0}abas
{0}aba
{0}ábamos
{0}abais
{0}aban

{0}é
{0}aste
{0}ó
{0}amos
{0}asteis
{0}aron

{0}aré
{0}arás
{0}ará
{0}aremos
{0}aréis
{0}arán

{0}aría
{0}arías
{0}aría
{0}aríamos
{0}aríais
{0}arían

{0}e
{0}es
{0}e
{0}emos
{0}éis
{0}en

{0}ara
{0}aras
{0}ara
{0}áramos
{0}arais
{0}aran

{0}ase
{0}ases
{0}ase
{0}ásemos
{0}aseis
{0}asen

{0}are
{0}ares
{0}are
{0}áremos
{0}areis
{0}aren

{0}a
{0}e
{0}emos
{0}ad
{0}en

no {0}es
no {0}e
no {0}emos
no {0}éis
no {0}en""",
    'es-conj-ar ref_stem':
"""{0}arse
{0}ándose
{0}ado

me {0}o
te {0}as
se {0}a
nos {0}amos
os {0}áis
se {0}an

me {0}aba
te {0}abas
se {0}aba
nos {0}ábamos
os {0}abais
se {0}aban

me {0}é
te {0}aste
se {0}ó
nos {0}amos
os {0}asteis
se {0}aron

me {0}aré
te {0}arás
se {0}ará
nos {0}aremos
os {0}aréis
se {0}arán

me {0}aría
te {0}arías
se {0}aría
nos {0}aríamos
os {0}aríais
se {0}arían

me {0}e
te {0}es
se {0}e
nos {0}emos
os {0}éis
se {0}en

me {0}ara
te {0}aras
se {0}ara
nos {0}áramos
os {0}arais
se {0}aran

me {0}ase
te {0}ases
se {0}ase
nos {0}ásemos
os {0}aseis
se {0}asen

me {0}are
te {0}ares
se {0}are
nos {0}áremos
os {0}areis
se {0}aren

{ref_stem}ate
{ref_stem}ese
{0}émonos
{0}aos
{ref_stem}ense

no te {0}es
no se {0}e
no nos {0}emos
no os {0}éis
no se {0}en""",
    'es-conj-ar (e-ie)':
"""{0}e{1}ar
{0}e{1}ando
{0}e{1}ado

{0}ie{1}o
{0}ie{1}as
{0}ie{1}a
{0}e{1}amos
{0}e{1}áis
{0}ie{1}an

{0}e{1}aba
{0}e{1}abas
{0}e{1}aba
{0}e{1}ábamos
{0}e{1}abais
{0}e{1}aban

{0}e{1}é
{0}e{1}aste
{0}e{1}ó
{0}e{1}amos
{0}e{1}asteis
{0}e{1}aron

{0}e{1}aré
{0}e{1}arás
{0}e{1}ará
{0}e{1}aremos
{0}e{1}aréis
{0}e{1}arán

{0}e{1}aría
{0}e{1}arías
{0}e{1}aría
{0}e{1}aríamos
{0}e{1}aríais
{0}e{1}arían

{0}ie{1}e
{0}ie{1}es
{0}ie{1}e
{0}e{1}emos
{0}e{1}éis
{0}ie{1}en

{0}e{1}ara
{0}e{1}aras
{0}e{1}ara
{0}e{1}áramos
{0}e{1}arais
{0}e{1}aran

{0}e{1}ase
{0}e{1}ases
{0}e{1}ase
{0}e{1}ásemos
{0}e{1}aseis
{0}e{1}asen

{0}e{1}are
{0}e{1}ares
{0}e{1}are
{0}e{1}áremos
{0}e{1}areis
{0}e{1}aren

{0}ie{1}a
{0}ie{1}e
{0}e{1}emos
{0}e{1}ad
{0}ie{1}en

no {0}ie{1}es
no {0}ie{1}e
no {0}e{1}emos
no {0}e{1}éis
no {0}ie{1}en""",
    'es-conj-ar (e-ie) ref_obj':
"""{0}e{1}arse
{0}e{1}ándose
{0}e{1}ado

me {0}ie{1}o
te {0}ie{1}as
se {0}ie{1}a
nos {0}e{1}amos
os {0}e{1}áis
se {0}ie{1}an

me {0}e{1}aba
te {0}e{1}abas
se {0}e{1}aba
nos {0}e{1}ábamos
os {0}e{1}abais
se {0}e{1}aban

me {0}e{1}é
te {0}e{1}aste
se {0}e{1}ó
nos {0}e{1}amos
os {0}e{1}asteis
se {0}e{1}aron

me {0}e{1}aré
te {0}e{1}arás
se {0}e{1}ará
nos {0}e{1}aremos
os {0}e{1}aréis
se {0}e{1}arán

me {0}e{1}aría
te {0}e{1}arías
se {0}e{1}aría
nos {0}e{1}aríamos
os {0}e{1}aríais
se {0}e{1}arían

me {0}ie{1}e
te {0}ie{1}es
se {0}ie{1}e
nos {0}e{1}emos
os {0}e{1}éis
se {0}ie{1}en

me {0}e{1}ara
te {0}e{1}aras
se {0}e{1}ara
nos {0}e{1}áramos
os {0}e{1}arais
se {0}e{1}aran

me {0}e{1}ase
me {0}e{1}ases
se {0}e{1}ase
nos {0}e{1}ásemos
os {0}e{1}aseis
se {0}e{1}asen

me {0}e{1}are
me {0}e{1}ares
os {0}e{1}are
nos {0}e{1}áremos
os {0}e{1}areis
os {0}e{1}aren

{0}ié{1}ate
{0}ié{1}ese
{0}e{1}émonos
{0}e{1}aos
{0}ié{1}ense

no te {0}ie{1}es
no se {0}ie{1}e
no nos {0}e{1}emos
no os {0}e{1}éis
no se {0}ie{1}en""",
    'es-conj-ar-imp':
"""{0}ar
{0}ando
{0}ado
*{0}o
*{0}as
{0}a
*{0}amos
*{0}áis
*{0}an
*{0}aba
*{0}abas
{0}aba
*{0}ábamos
*{0}abais
*{0}aban
*{0}é
*{0}aste
{0}ó
*{0}amos
*{0}asteis
*{0}aron
*{0}aré
*{0}arás
{0}ará
*{0}aremos
*{0}aréis
*{0}arán
*{0}aría
*{0}arías
{0}aría
*{0}aríamos
*{0}aríais
*{0}arían
*{0}e
*{0}es
{0}e
*{0}emos
*{0}éis
*{0}en
*{0}ara
*{0}aras
{0}ara
*{0}áramos
*{0}arais
*{0}aran
*{0}ase
*{0}ases
{0}ase
*{0}ásemos
*{0}aseis
*{0}asen
*{0}are
*{0}ares
{0}are
*{0}áremos
*{0}areis
*{0}aren
*{0}a
{0}e
*{0}emos
*{0}ad
*{0}en
*no {0}es
no {0}e
*no {0}emos
*no {0}éis
*no {0}en""",
    'es-conj-ar (e-ie)':
"""{0}e{1}ar
{0}e{1}ando
{0}e{1}ado
{0}ie{1}o
{0}ie{1}as
{0}ie{1}a
{0}e{1}amos
{0}e{1}áis
{0}ie{1}an
{0}e{1}aba
{0}e{1}abas
{0}e{1}aba
{0}e{1}ábamos
{0}e{1}abais
{0}e{1}aban
{0}e{1}é
{0}e{1}aste
{0}e{1}ó
{0}e{1}amos
{0}e{1}asteis
{0}e{1}aron
{0}e{1}aré
{0}e{1}arás
{0}e{1}ará
{0}e{1}aremos
{0}e{1}aréis
{0}e{1}arán
{0}e{1}aría
{0}e{1}arías
{0}e{1}aría
{0}e{1}aríamos
{0}e{1}aríais
{0}e{1}arían
{0}ie{1}e
{0}ie{1}es
{0}ie{1}e
{0}e{1}emos
{0}e{1}éis
{0}ie{1}en
{0}e{1}ara
{0}e{1}aras
{0}e{1}ara
{0}e{1}áramos
{0}e{1}arais
{0}e{1}aran
{0}e{1}ase
{0}e{1}ases
{0}e{1}ase
{0}e{1}ásemos
{0}e{1}aseis
{0}e{1}asen
{0}e{1}are
{0}e{1}ares
{0}e{1}are
{0}e{1}áremos
{0}e{1}areis
{0}e{1}aren
{0}ie{1}a
{0}ie{1}e
{0}e{1}emos
{0}e{1}ad
{0}ie{1}en
no {0}ie{1}es
no {0}ie{1}e
no {0}e{1}emos
no {0}e{1}éis
no {0}ie{1}en""",
    'es-conj-ar (go-güe)':
"""{0}o{1}ar
{0}o{1}ando
{0}o{1}ado
{0}üe{1}o
{0}üe{1}as
{0}üe{1}a
{0}o{1}amos
{0}o{1}áis
{0}üe{1}an
{0}o{1}aba
{0}o{1}abas
{0}o{1}aba
{0}o{1}ábamos
{0}o{1}abais
{0}o{1}aban
{0}o{1}é
{0}o{1}aste
{0}o{1}ó
{0}o{1}amos
{0}o{1}asteis
{0}o{1}aron
{0}o{1}aré
{0}o{1}arás
{0}o{1}ará
{0}o{1}aremos
{0}o{1}aréis
{0}o{1}arán
{0}o{1}aría
{0}o{1}arías
{0}o{1}aría
{0}o{1}aríamos
{0}o{1}aríais
{0}o{1}arían
{0}üe{1}e
{0}üe{1}es
{0}üe{1}e
{0}o{1}emos
{0}o{1}éis
{0}üe{1}en
{0}o{1}ara
{0}o{1}aras
{0}o{1}ara
{0}o{1}áramos
{0}o{1}arais
{0}o{1}aran
{0}o{1}ase
{0}o{1}ases
{0}o{1}ase
{0}o{1}ásemos
{0}o{1}aseis
{0}o{1}asen
{0}o{1}are
{0}o{1}ares
{0}o{1}are
{0}o{1}áremos
{0}o{1}areis
{0}o{1}aren
{0}üe{1}a
{0}üe{1}e
{0}o{1}emos
{0}o{1}ad
{0}üe{1}en
no {0}üe{1}es
no {0}üe{1}e
no {0}o{1}emos
no {0}o{1}éis
no {0}üe{1}en""",
    'es-conj-ar (o-hue)':
"""{0}o{1}ar
{0}o{1}ando
{0}o{1}ado
{0}hue{1}o
{0}hue{1}as
{0}hue{1}a
{0}o{1}amos
{0}o{1}áis
{0}hue{1}an
{0}o{1}aba
{0}o{1}abas
{0}o{1}aba
{0}o{1}ábamos
{0}o{1}abais
{0}o{1}aban
{0}o{1}é
{0}o{1}aste
{0}o{1}ó
{0}o{1}amos
{0}o{1}asteis
{0}o{1}aron
{0}o{1}aré
{0}o{1}arás
{0}o{1}ará
{0}o{1}aremos
{0}o{1}aréis
{0}o{1}arán
{0}o{1}aría
{0}o{1}arías
{0}o{1}aría
{0}o{1}aríamos
{0}o{1}aríais
{0}o{1}arían
{0}hue{1}e
{0}hue{1}es
{0}hue{1}e
{0}o{1}emos
{0}o{1}éis
{0}hue{1}en
{0}o{1}ara
{0}o{1}aras
{0}o{1}ara
{0}o{1}áramos
{0}o{1}arais
{0}o{1}aran
{0}o{1}ase
{0}o{1}ases
{0}o{1}ase
{0}o{1}ásemos
{0}o{1}aseis
{0}o{1}asen
{0}o{1}are
{0}o{1}ares
{0}o{1}are
{0}o{1}áremos
{0}o{1}areis
{0}o{1}aren
{0}hue{1}a
{0}hue{1}e
{0}o{1}emos
{0}o{1}ad
{0}hue{1}en
no {0}hue{1}es
no {0}hue{1}e
no {0}o{1}emos
no {0}o{1}éis
no {0}hue{1}en""",
    'es-conj-ar (o-ue)':
"""{0}o{1}ar
{0}o{1}ando
{0}o{1}ado
{0}ue{1}o
{0}ue{1}as
{0}ue{1}a
{0}o{1}amos
{0}o{1}áis
{0}ue{1}an
{0}o{1}aba
{0}o{1}abas
{0}o{1}aba
{0}o{1}ábamos
{0}o{1}abais
{0}o{1}aban
{0}o{1}é
{0}o{1}aste
{0}o{1}ó
{0}o{1}amos
{0}o{1}asteis
{0}o{1}aron
{0}o{1}aré
{0}o{1}arás
{0}o{1}ará
{0}o{1}aremos
{0}o{1}aréis
{0}o{1}arán
{0}o{1}aría
{0}o{1}arías
{0}o{1}aría
{0}o{1}aríamos
{0}o{1}aríais
{0}o{1}arían
{0}ue{1}e
{0}ue{1}es
{0}ue{1}e
{0}o{1}emos
{0}o{1}éis
{0}ue{1}en
{0}o{1}ara
{0}o{1}aras
{0}o{1}ara
{0}o{1}áramos
{0}o{1}arais
{0}o{1}aran
{0}o{1}ase
{0}o{1}ases
{0}o{1}ase
{0}o{1}ásemos
{0}o{1}aseis
{0}o{1}asen
{0}o{1}are
{0}o{1}ares
{0}o{1}are
{0}o{1}áremos
{0}o{1}areis
{0}o{1}aren
{0}ue{1}a
{0}ue{1}e
{0}o{1}emos
{0}o{1}ad
{0}ue{1}en
no {0}ue{1}es
no {0}ue{1}e
no {0}o{1}emos
no {0}o{1}éis
no {0}ue{1}en""",
    'es-conj-car':
"""{0}car
{0}cando
{0}cado
{0}co
{0}cas
{0}ca
{0}camos
{0}cáis
{0}can
{0}caba
{0}cabas
{0}caba
{0}cábamos
{0}cabais
{0}caban
{0}qué
{0}caste
{0}có
{0}camos
{0}casteis
{0}caron
{0}caré
{0}carás
{0}cará
{0}caremos
{0}caréis
{0}carán
{0}caría
{0}carías
{0}caría
{0}caríamos
{0}caríais
{0}carían
{0}que
{0}ques
{0}que
{0}quemos
{0}quéis
{0}quen
{0}cara
{0}caras
{0}cara
{0}cáramos
{0}carais
{0}caran
{0}case
{0}cases
{0}case
{0}cásemos
{0}caseis
{0}casen
{0}care
{0}cares
{0}care
{0}cáremos
{0}careis
{0}caren
{0}ca
{0}que
{0}quemos
{0}cad
{0}quen
no {0}ques
no {0}que
no {0}quemos
no {0}quéis
no {0}quen""",
    'es-conj-cer':
"""{0}cer
{0}ciendo
{0}cido
{0}zo
{0}ces
{0}ce
{0}cemos
{0}céis
{0}cen
{0}cía
{0}cías
{0}cía
{0}cíamos
{0}cíais
{0}cían
{0}cí
{0}ciste
{0}ció
{0}cimos
{0}cisteis
{0}cieron
{0}ceré
{0}cerás
{0}cerá
{0}ceremos
{0}ceréis
{0}cerán
{0}cería
{0}cerías
{0}cería
{0}ceríamos
{0}ceríais
{0}cerían
{0}za
{0}zas
{0}za
{0}zamos
{0}záis
{0}zan
{0}ciera
{0}cieras
{0}ciera
{0}ciéramos
{0}cierais
{0}cieran
{0}ciese
{0}cieses
{0}ciese
{0}ciésemos
{0}cieseis
{0}ciesen
{0}ciere
{0}cieres
{0}ciere
{0}ciéremos
{0}ciereis
{0}cieren
{0}ce
{0}za
{0}zamos
{0}ced
{0}zan
no {0}zas
no {0}za
no {0}zamos
no {0}záis
no {0}zan""",
    'es-conj-cer (o-ue)':
"""{0}o{1}cer
{0}o{1}ciendo
{0}o{1}cido
{0}ue{1}zo
{0}ue{1}ces
{0}ue{1}ce
{0}o{1}cemos
{0}o{1}céis
{0}ue{1}cen
{0}o{1}cía
{0}o{1}cías
{0}o{1}cía
{0}o{1}cíamos
{0}o{1}cíais
{0}o{1}cían
{0}o{1}cí
{0}o{1}ciste
{0}o{1}ció
{0}o{1}cimos
{0}o{1}cisteis
{0}o{1}cieron
{0}o{1}ceré
{0}o{1}cerás
{0}o{1}cerá
{0}o{1}ceremos
{0}o{1}ceréis
{0}o{1}cerán
{0}o{1}cería
{0}o{1}cerías
{0}o{1}cería
{0}o{1}ceríamos
{0}o{1}ceríais
{0}o{1}cerían
{0}ue{1}za
{0}ue{1}zas
{0}ue{1}za
{0}o{1}zamos
{0}o{1}záis
{0}ue{1}zan
{0}o{1}ciera
{0}o{1}cieras
{0}o{1}ciera
{0}o{1}ciéramos
{0}o{1}cierais
{0}o{1}cieran
{0}o{1}ciese
{0}o{1}cieses
{0}o{1}ciese
{0}o{1}ciésemos
{0}o{1}cieseis
{0}o{1}ciesen
{0}o{1}ciere
{0}o{1}cieres
{0}o{1}ciere
{0}o{1}ciéremos
{0}o{1}ciereis
{0}o{1}cieren
{0}ue{1}ce
{0}ue{1}za
{0}o{1}zamos
{0}o{1}ced
{0}ue{1}zan
no {0}ue{1}zas
no {0}ue{1}za
no {0}o{1}zamos
no {0}o{1}záis
no {0}ue{1}zan""",
    'es-conj-cir':
"""{0}cir
{0}ciendo
{0}cido
{0}zo
{0}ces
{0}ce
{0}cimos
{0}cís
{0}cen
{0}cía
{0}cías
{0}cía
{0}cíamos
{0}cíais
{0}cían
{0}cí
{0}ciste
{0}ció
{0}cimos
{0}cisteis
{0}cieron
{0}ciré
{0}cirás
{0}cirá
{0}ciremos
{0}ciréis
{0}cirán
{0}ciría
{0}cirías
{0}ciría
{0}ciríamos
{0}ciríais
{0}cirían
{0}za
{0}zas
{0}za
{0}zamos
{0}záis
{0}zan
{0}ciera
{0}cieras
{0}ciera
{0}ciéramos
{0}cierais
{0}cieran
{0}ciese
{0}cieses
{0}ciese
{0}ciésemos
{0}cieseis
{0}ciesen
{0}ciere
{0}cieres
{0}ciere
{0}ciéremos
{0}ciereis
{0}cieren
{0}ce
{0}za
{0}zamos
{0}cid
{0}zan
no {0}zas
no {0}za
no {0}zamos
no {0}záis
no {0}zan""",
    'es-conj-ar (dar)':
"""{0}ar
{0}ando
{0}ado
{0}oy
{0}as
{0}a
{0}amos
{0}ais
{0}an
{0}aba
{0}abas
{0}aba
{0}ábamos
{0}abais
{0}aban
{0}i
{0}iste
{0}io
{0}imos
{0}isteis
{0}ieron
{0}aré
{0}arás
{0}ará
{0}aremos
{0}aréis
{0}arán
{0}aría
{0}arías
{0}aría
{0}aríamos
{0}aríais
{0}arían
{0}é
{0}es
{0}é
{0}emos
{0}eis
{0}en
{1}ra
{1}ras
{1}ra
{1}ramos
{1}rais
{1}ran
{1}se
{1}ses
{1}se
{1}semos
{1}seis
{1}sen
{1}re
{1}res
{1}re
{1}remos
{1}reis
{1}ren
{0}a
{0}é
{0}emos
{0}ad
{0}en
no {0}es
no {0}é
no {0}emos
no {0}eis
no {0}en""",
    'es-conj-ducir':
"""{0}ducir
{0}duciendo
{0}ducido
{0}duzco
{0}duces
{0}duce
{0}ducimos
{0}ducís
{0}ducen
{0}ducía
{0}ducías
{0}ducía
{0}ducíamos
{0}ducíais
{0}ducían
{0}duje
{0}dujiste
{0}dujo
{0}dujimos
{0}dujisteis
{0}dujeron
{0}duciré
{0}ducirás
{0}ducirá
{0}duciremos
{0}duciréis
{0}ducirán
{0}duciría
{0}ducirías
{0}duciría
{0}duciríamos
{0}duciríais
{0}ducirían
{0}duzca
{0}duzcas
{0}duzca
{0}duzcamos
{0}duzcáis
{0}duzcan
{0}dujera
{0}dujeras
{0}dujera
{0}dujéramos
{0}dujerais
{0}dujeran
{0}dujese
{0}dujeses
{0}dujese
{0}dujésemos
{0}dujeseis
{0}dujesen
{0}dujere
{0}dujeres
{0}dujere
{0}dujéremos
{0}dujereis
{0}dujeren
{0}duce
{0}duzca
{0}duzcamos
{0}ducid
{0}duzcan
no {0}duzcas
no {0}duzca
no {0}duzcamos
no {0}duzcáis
no {0}duzcan""",
    'es-conj-eer':
"""{0}eer
{0}eyendo
{0}eído
{0}eo
{0}ees
{0}ee
{0}eemos
{0}eéis
{0}een
{0}eía
{0}eías
{0}eía
{0}eíamos
{0}eíais
{0}eían
{0}eí
{0}eíste
{0}eyó
{0}eímos
{0}eísteis
{0}eyeron
{0}eeré
{0}eerás
{0}eerá
{0}eeremos
{0}eeréis
{0}eerán
{0}eería
{0}eerías
{0}eería
{0}eeríamos
{0}eeríais
{0}eerían
{0}ea
{0}eas
{0}ea
{0}eamos
{0}eáis
{0}ean
{0}eyera
{0}eyeras
{0}eyera
{0}eyéramos
{0}eyerais
{0}eyeran
{0}eyese
{0}eyeses
{0}eyese
{0}eyésemos
{0}eyeseis
{0}eyesen
{0}eyere
{0}eyeres
{0}eyere
{0}eyéremos
{0}eyereis
{0}eyeren
{0}ee
{0}ea
{0}eamos
{0}eed
{0}ean
no {0}eas
no {0}ea
no {0}eamos
no {0}eáis
no {0}ean""",
    'es-conj-er':
"""{0}er
{0}iendo
{0}ido
{0}o
{0}es
{0}e
{0}emos
{0}éis
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ió
{0}imos
{0}isteis
{0}ieron
{0}eré
{0}erás
{0}erá
{0}eremos
{0}eréis
{0}erán
{0}ería
{0}erías
{0}ería
{0}eríamos
{0}eríais
{0}erían
{0}a
{0}as
{0}a
{0}amos
{0}áis
{0}an
{0}iera
{0}ieras
{0}iera
{0}iéramos
{0}ierais
{0}ieran
{0}iese
{0}ieses
{0}iese
{0}iésemos
{0}ieseis
{0}iesen
{0}iere
{0}ieres
{0}iere
{0}iéremos
{0}iereis
{0}ieren
{0}e
{0}a
{0}amos
{0}ed
{0}an
no {0}as
no {0}a
no {0}amos
no {0}áis
no {0}an""",
    'es-conj-er (atardecer)':
"""{0}cer
{0}ciendo
{0}cido
*{0}zco
*{0}ces
{0}ce
*{0}cemos
*{0}céis
*{0}cen
*{0}cía
*{0}cías
{0}cía
*{0}cíamos
*{0}cíais
*{0}cían
*{0}cí
*{0}ciste
{0}ció
*{0}cimos
*{0}cisteis
*{0}cieron
*{0}ceré
*{0}cerás
{0}cerá
*{0}ceremos
*{0}ceréis
*{0}cerán
*{0}cería
*{0}cerías
{0}cería
*{0}ceríamos
*{0}ceríais
*{0}cerían
*{0}zca
*{0}zcas
{0}zca
*{0}zcamos
*{0}zcáis
*{0}zcan
*{0}ciera
*{0}cieras
{0}ciera
*{0}ciéramos
*{0}cierais
*{0}cieran
*{0}ciese
*{0}cieses
{0}ciese
*{0}ciésemos
*{0}cieseis
*{0}ciesen
*{0}ciere
*{0}cieres
{0}ciere
*{0}ciéremos
*{0}ciereis
*{0}cieren
*{0}ce
{0}zca
*{0}zcamos
*{0}ced
*{0}zcan
*{0}zcas
no {0}zca
*{0}zcamos
*{0}zcáis
*{0}zcan""",
    'es-conj-er (c-zc)':
"""{0}cer
{0}ciendo
{0}cido
{0}zco
{0}ces
{0}ce
{0}cemos
{0}céis
{0}cen
{0}cía
{0}cías
{0}cía
{0}cíamos
{0}cíais
{0}cían
{0}cí
{0}ciste
{0}ció
{0}cimos
{0}cisteis
{0}cieron
{0}ceré
{0}cerás
{0}cerá
{0}ceremos
{0}ceréis
{0}cerán
{0}cería
{0}cerías
{0}cería
{0}ceríamos
{0}ceríais
{0}cerían
{0}zca
{0}zcas
{0}zca
{0}zcamos
{0}zcáis
{0}zcan
{0}ciera
{0}cieras
{0}ciera
{0}ciéramos
{0}cierais
{0}cieran
{0}ciese
{0}cieses
{0}ciese
{0}ciésemos
{0}cieseis
{0}ciesen
{0}ciere
{0}cieres
{0}ciere
{0}ciéremos
{0}ciereis
{0}cieren
{0}ce
{0}zca
{0}zcamos
{0}ced
{0}zcan
no {0}zcas
no {0}zca
no {0}zcamos
no {0}zcáis
no {0}zcan""",
    'es-conj-er (e-ie)':
"""{0}e{1}er
{0}e{1}iendo
{0}e{1}ido
{0}ie{1}o
{0}ie{1}es
{0}ie{1}e
{0}e{1}emos
{0}e{1}éis
{0}ie{1}en
{0}e{1}ía
{0}e{1}ías
{0}e{1}ía
{0}e{1}íamos
{0}e{1}íais
{0}e{1}ían
{0}e{1}í
{0}e{1}iste
{0}e{1}ió
{0}e{1}imos
{0}e{1}isteis
{0}e{1}ieron
{0}e{1}eré
{0}e{1}erás
{0}e{1}erá
{0}e{1}eremos
{0}e{1}eréis
{0}e{1}erán
{0}e{1}ería
{0}e{1}erías
{0}e{1}ería
{0}e{1}eríamos
{0}e{1}eríais
{0}e{1}erían
{0}ie{1}a
{0}ie{1}as
{0}ie{1}a
{0}e{1}amos
{0}e{1}áis
{0}ie{1}an
{0}e{1}iera
{0}e{1}ieras
{0}e{1}iera
{0}e{1}iéramos
{0}e{1}ierais
{0}e{1}ieran
{0}e{1}iese
{0}e{1}ieses
{0}e{1}iese
{0}e{1}iésemos
{0}e{1}ieseis
{0}e{1}iesen
{0}e{1}iere
{0}e{1}ieres
{0}e{1}iere
{0}e{1}iéremos
{0}e{1}iereis
{0}e{1}ieren
{0}ie{1}e
{0}ie{1}a
{0}e{1}amos
{0}e{1}ed
{0}ie{1}an
no {0}ie{1}as
no {0}ie{1}a
no {0}e{1}amos
no {0}e{1}áis
no {0}ie{1}an""",
    'es-conj-er (o-hue)':
"""{0}o{1}er
{0}o{1}iendo
{0}o{1}ido
{0}hue{1}o
{0}hue{1}es
{0}hue{1}e
{0}o{1}emos
{0}o{1}éis
{0}hue{1}en
{0}o{1}ía
{0}o{1}ías
{0}o{1}ía
{0}o{1}íamos
{0}o{1}íais
{0}o{1}ían
{0}o{1}í
{0}o{1}iste
{0}o{1}ió
{0}o{1}imos
{0}o{1}isteis
{0}o{1}ieron
{0}o{1}eré
{0}o{1}erás
{0}o{1}erá
{0}o{1}eremos
{0}o{1}eréis
{0}o{1}erán
{0}o{1}ería
{0}o{1}erías
{0}o{1}ería
{0}o{1}eríamos
{0}o{1}eríais
{0}o{1}erían
{0}hue{1}a
{0}hue{1}as
{0}hue{1}a
{0}o{1}amos
{0}o{1}áis
{0}hue{1}an
{0}o{1}iera
{0}o{1}ieras
{0}o{1}iera
{0}o{1}iéramos
{0}o{1}ierais
{0}o{1}ieran
{0}o{1}iese
{0}o{1}ieses
{0}o{1}iese
{0}o{1}iésemos
{0}o{1}ieseis
{0}o{1}iesen
{0}o{1}iere
{0}o{1}ieres
{0}o{1}iere
{0}o{1}iéremos
{0}o{1}iereis
{0}o{1}ieren
{0}hue{1}e
{0}hue{1}a
{0}o{1}amos
{0}o{1}ed
{0}hue{1}an
no {0}hue{1}as
no {0}hue{1}a
no {0}o{1}amos
no {0}o{1}áis
no {0}hue{1}an""",
    'es-conj-er (o-ue)':
"""{0}o{1}er
{0}o{1}iendo
{0}o{1}ido
{0}ue{1}o
{0}ue{1}es
{0}ue{1}e
{0}o{1}emos
{0}o{1}éis
{0}ue{1}en
{0}o{1}ía
{0}o{1}ías
{0}o{1}ía
{0}o{1}íamos
{0}o{1}íais
{0}o{1}ían
{0}o{1}í
{0}o{1}iste
{0}o{1}ió
{0}o{1}imos
{0}o{1}isteis
{0}o{1}ieron
{0}o{1}eré
{0}o{1}erás
{0}o{1}erá
{0}o{1}eremos
{0}o{1}eréis
{0}o{1}erán
{0}o{1}ería
{0}o{1}erías
{0}o{1}ería
{0}o{1}eríamos
{0}o{1}eríais
{0}o{1}erían
{0}ue{1}a
{0}ue{1}as
{0}ue{1}a
{0}o{1}amos
{0}o{1}áis
{0}ue{1}an
{0}o{1}iera
{0}o{1}ieras
{0}o{1}iera
{0}o{1}iéramos
{0}o{1}ierais
{0}o{1}ieran
{0}o{1}iese
{0}o{1}ieses
{0}o{1}iese
{0}o{1}iésemos
{0}o{1}ieseis
{0}o{1}iesen
{0}o{1}iere
{0}o{1}ieres
{0}o{1}iere
{0}o{1}iéremos
{0}o{1}iereis
{0}o{1}ieren
{0}ue{1}e
{0}ue{1}a
{0}o{1}amos
{0}o{1}ed
{0}ue{1}an
no {0}ue{1}as
no {0}ue{1}a
no {0}o{1}amos
no {0}o{1}éis
no {0}ue{1}an""",
    'es-conj-ar (errar)':
"""{0}errar
{0}errando
{0}errado
{0}yerro, {0}erro
{0}yerras, {0}erras
{0}yerra, {0}erra
{0}erramos
{0}erráis
{0}yerran, {0}erran
{0}erraba
{0}errabas
{0}erraba
{0}errábamos
{0}errabais
{0}erraban
{0}erré
{0}erraste
{0}erró
{0}erramos
{0}errasteis
{0}erraron
{0}erraré
{0}errarás
{0}errará
{0}erraremos
{0}erraréis
{0}errarán
{0}erraría
{0}errarías
{0}erraría
{0}erraríamos
{0}erraríais
{0}errarían
{0}yerre, {0}erre
{0}yerres, {0}erres
{0}yerre, {0}erre
{0}erremos
{0}erréis
{0}yerren, {0}erren
{0}errara
{0}erraras
{0}errara
{0}erráramos
{0}errarais
{0}erraran
{0}errase
{0}errases
{0}errase
{0}errásemos
{0}erraseis
{0}errasen
{0}errare
{0}errares
{0}errare
{0}erráremos
{0}errareis
{0}erraren
{0}yerra, {0}erra
{0}yerre, {0}erre
{0}erremos
{0}errad
{0}yerren, {0}erren
no {0}yerres, {0}erres
no {0}yerre, {0}erre
no {0}erremos
no {0}erréis
no {0}yerren, {0}erren""",
    'es-conj-ar (estar)':
"""estar
estando
estado
estoy
estás
está
estamos
estáis
están
estaba
estabas
estaba
estábamos
estabais
estaban
estuve
estuviste
estuvo
estuvimos
estuvisteis
estuvieron
estaré
estarás
estará
estaremos
estaréis
estarán
estaría
estarías
estaría
estaríamos
estaríais
estarían
esté
estés
esté
estemos
estéis
estén
estuviera
estuvieras
estuviera
estuviéramos
estuvierais
estuvieran
estuviese
estuvieses
estuviese
estuviésemos
estuvieseis
estuviesen
estuviere
estuvieres
estuviere
estuviéremos
estuviereis
estuvieren
está
esté
estemos
estad
estén
no estés
no esté
no estemos
no estéis
no estén""",
    'es-conj-ar (i-í)':
"""{0}i{1}ar
{0}i{1}ando
{0}i{1}ado
{0}í{1}o
{0}í{1}as
{0}í{1}a
{0}i{1}amos
{0}i{1}áis
{0}í{1}an
{0}i{1}aba
{0}i{1}abas
{0}i{1}aba
{0}i{1}ábamos
{0}i{1}abais
{0}i{1}aban
{0}i{1}é
{0}i{1}aste
{0}i{1}ó
{0}i{1}amos
{0}i{1}asteis
{0}i{1}aron
{0}i{1}aré
{0}i{1}arás
{0}i{1}ará
{0}i{1}aremos
{0}i{1}aréis
{0}i{1}arán
{0}i{1}aría
{0}i{1}arías
{0}i{1}aría
{0}i{1}aríamos
{0}i{1}aríais
{0}i{1}arían
{0}í{1}e
{0}í{1}es
{0}í{1}e
{0}i{1}emos
{0}i{1}éis
{0}í{1}en
{0}i{1}ara
{0}i{1}aras
{0}i{1}ara
{0}i{1}áramos
{0}i{1}arais
{0}i{1}aran
{0}i{1}ase
{0}i{1}ases
{0}i{1}ase
{0}i{1}ásemos
{0}i{1}aseis
{0}i{1}asen
{0}i{1}are
{0}i{1}ares
{0}i{1}are
{0}i{1}áremos
{0}i{1}areis
{0}i{1}aren
{0}í{1}a
{0}í{1}e
{0}i{1}emos
{0}i{1}ad
{0}í{1}en
no {0}í{1}es
no {0}í{1}e
no {0}i{1}emos
no {0}i{1}éis
no {0}í{1}en""",
    'es-conj-ar (u-ú)':
"""{0}u{1}ar
{0}u{1}ando
{0}u{1}ado
{0}ú{1}o
{0}ú{1}as
{0}ú{1}a
{0}u{1}amos
{0}u{1}áis
{0}ú{1}an
{0}u{1}aba
{0}u{1}abas
{0}u{1}aba
{0}u{1}ábamos
{0}u{1}abais
{0}u{1}aban
{0}u{1}é
{0}u{1}aste
{0}u{1}ó
{0}u{1}amos
{0}u{1}asteis
{0}u{1}aron
{0}u{1}aré
{0}u{1}arás
{0}u{1}ará
{0}u{1}aremos
{0}u{1}aréis
{0}u{1}arán
{0}u{1}aría
{0}u{1}arías
{0}u{1}aría
{0}u{1}aríamos
{0}u{1}aríais
{0}u{1}arían
{0}ú{1}e
{0}ú{1}es
{0}ú{1}e
{0}u{1}emos
{0}u{1}éis
{0}ú{1}en
{0}u{1}ara
{0}u{1}aras
{0}u{1}ara
{0}u{1}áramos
{0}u{1}arais
{0}u{1}aran
{0}u{1}ase
{0}u{1}ases
{0}u{1}ase
{0}u{1}ásemos
{0}u{1}aseis
{0}u{1}asen
{0}u{1}are
{0}u{1}ares
{0}u{1}are
{0}u{1}áremos
{0}u{1}areis
{0}u{1}aren
{0}ú{1}a
{0}ú{1}e
{0}u{1}emos
{0}u{1}ad
{0}ú{1}en
no {0}ú{1}es
no {0}ú{1}e
no {0}u{1}emos
no {0}u{1}éis
no {0}ú{1}en""",
    'es-conj-car (o-ue)':
"""{0}o{1}car
{0}o{1}cando
{0}o{1}cado
{0}ue{1}co
{0}ue{1}cas
{0}ue{1}ca
{0}o{1}camos
{0}o{1}cáis
{0}ue{1}can
{0}o{1}caba
{0}o{1}cabas
{0}o{1}caba
{0}o{1}cábamos
{0}o{1}cabais
{0}o{1}caban
{0}o{1}qué
{0}o{1}caste
{0}o{1}có
{0}o{1}camos
{0}o{1}casteis
{0}o{1}caron
{0}o{1}caré
{0}o{1}carás
{0}o{1}cará
{0}o{1}caremos
{0}o{1}caréis
{0}o{1}carán
{0}o{1}caría
{0}o{1}carías
{0}o{1}caría
{0}o{1}caríamos
{0}o{1}caríais
{0}o{1}carían
{0}ue{1}que
{0}ue{1}ques
{0}ue{1}que
{0}o{1}quemos
{0}o{1}quéis
{0}ue{1}quen
{0}o{1}cara
{0}o{1}caras
{0}o{1}cara
{0}o{1}cáramos
{0}o{1}carais
{0}o{1}caran
{0}o{1}case
{0}o{1}cases
{0}o{1}case
{0}o{1}cásemos
{0}o{1}caseis
{0}o{1}casen
{0}o{1}care
{0}o{1}cares
{0}o{1}care
{0}o{1}cáremos
{0}o{1}careis
{0}o{1}caren
{0}ue{1}ca
{0}ue{1}que
{0}o{1}quemos
{0}o{1}cad
{0}ue{1}quen
no {0}ue{1}ques
no {0}ue{1}que
no {0}o{1}quemos
no {0}o{1}quéis
no {0}ue{1}quen""",
    'es-conj-egir':
"""{0}egir
{0}igiendo
{0}egido, {0}ecto
{0}ijo
{0}iges
{0}ige
{0}egimos
{0}egís
{0}igen
{0}egía
{0}egías
{0}egía
{0}egíamos
{0}egíais
{0}egían
{0}egí
{0}egiste
{0}igió
{0}egimos
{0}egisteis
{0}igieron
{0}egiré
{0}egirás
{0}egirá
{0}egiremos
{0}egiréis
{0}egirán
{0}egiría
{0}egirías
{0}egiría
{0}egiríamos
{0}egiríais
{0}egirían
{0}ija
{0}ijas
{0}ija
{0}ijamos
{0}ijáis
{0}ijan
{0}igiera
{0}igieras
{0}igiera
{0}igiéramos
{0}igierais
{0}igieran
{0}igiese
{0}igieses
{0}igiese
{0}igiésemos
{0}igieseis
{0}igiesen
{0}igiere
{0}igieres
{0}igiere
{0}igiéremos
{0}igiereis
{0}igieren
{0}ige
{0}ija
{0}ijamos
{0}egid
{0}ijan
no {0}ijas
no {0}ija
no {0}ijamos
no {0}ijáis
no {0}ijan""",
    'es-conj-er (atañer)':
"""{0}er
{0}endo
{0}ido
*{0}o
*{0}es
{0}e
*{0}emos
*{0}éis
{0}en
*{0}ía
*{0}ías
{0}ía
*{0}íamos
*{0}íais
{0}ían
*{0}í
*{0}iste
{0}ó
*{0}imos
*{0}isteis
{0}eron
*{0}eré
*{0}erás
{0}erá
*{0}eremos
*{0}eréis
{0}erán
*{0}ería
*{0}erías
{0}ería
*{0}eríamos
*{0}eríais
{0}erían
*{0}a
*{0}as
{0}a
*{0}amos
*{0}áis
{0}an
*{0}era
*{0}eras
{0}era
*{0}éramos
*{0}erais
{0}eran
*{0}ese
*{0}eses
{0}ese
*{0}ésemos
*{0}eseis
{0}esen
*{0}ere
*{0}eres
{0}ere
*{0}éremos
*{0}ereis
{0}eren
*{0}e
*{0}a
*{0}amos
*{0}ed
*{0}an
*no {0}as
*no {0}a
*no {0}amos
*no {0}áis
*no {0}an""",
    'es-conj-er (caber)':
"""caber
cabiendo
cabido
quepo
cabes
cabe
cabemos
cabéis
caben
cabía
cabías
cabía
cabíamos
cabíais
cabían
cupe
cupiste
cupo
cupimos
cupisteis
cupieron
cabré
cabrás
cabrá
cabremos
cabréis
cabrán
cabría
cabrías
cabría
cabríamos
cabríais
cabrían
quepa
quepas
quepa
quepamos
quepáis
quepan
cupiera
cupieras
cupiera
cupiéramos
cupierais
cupieran
cupiese
cupieses
cupiese
cupiésemos
cupieseis
cupiesen
cupiere
cupieres
cupiere
cupiéremos
cupiereis
cupieren
cabe
quepa
quepamos
cabed
quepan
no quepas
no quepa
no quepamos
no quepáis
no quepan""",
    'es-conj-er (caer)':
"""{0}caer
{0}cayendo
{0}caído
{0}caigo
{0}caes
{0}cae
{0}caemos
{0}caéis
{0}caen
{0}caía
{0}caías
{0}caía
{0}caíamos
{0}caíais
{0}caían
{0}caí
{0}caíste
{0}cayó
{0}caímos
{0}caísteis
{0}cayeron
{0}caeré
{0}caerás
{0}caerá
{0}caeremos
{0}caeréis
{0}caerán
{0}caería
{0}caerías
{0}caería
{0}caeríamos
{0}caeríais
{0}caerían
{0}caiga
{0}caigas
{0}caiga
{0}caigamos
{0}caigáis
{0}caigan
{0}cayera
{0}cayeras
{0}cayera
{0}cayéramos
{0}cayerais
{0}cayeran
{0}cayese
{0}cayeses
{0}cayese
{0}cayésemos
{0}cayeseis
{0}cayesen
{0}cayere
{0}cayeres
{0}cayere
{0}cayéremos
{0}cayereis
{0}cayeren
{0}cae
{0}caiga
{0}caigamos
{0}caed
{0}caigan
no {0}caigas
no {0}caiga
no {0}caigamos
no {0}caigáis
no {0}caigan""",
    'es-conj-er (haber)':
"""haber
habiendo
habido
he
has
ha, hay
hemos
habéis
han, hay
había
habías
había
habíamos
habíais
habían
hube
hubiste
hubo
hubimos
hubisteis
hubieron
habré
habrás
habrá
habremos
habréis
habrán
habría
habrías
habría
habríamos
habríais
habrían
haya
hayas
haya
hayamos
hayáis
hayan
hubiera
hubieras
hubiera
hubiéramos
hubierais
hubieran
hubiese
hubieses
hubiese
hubiésemos
hubieseis
hubiesen
hubiere
hubieres
hubiere
hubiéremos
hubiereis
hubieren
habe, hé0
haya
hayamos
habed0
hayan
no hayas
no haya
no hayamos
no hayáis
no hayan""",
    'es-conj-er (hacer)':
"""{0}acer
{0}aciendo
{0}echo
{0}ago
{0}aces
{0}ace
{0}acemos
{0}acéis
{0}acen
{0}acía
{0}acías
{0}acía
{0}acíamos
{0}acíais
{0}acían
{0}ice
{0}iciste
{0}izo
{0}icimos
{0}icisteis
{0}icieron
{0}aré
{0}arás
{0}ará
{0}aremos
{0}aréis
{0}arán
{0}aría
{0}arías
{0}aría
{0}aríamos
{0}aríais
{0}arían
{0}aga
{0}agas
{0}aga
{0}agamos
{0}agáis
{0}agan
{0}iciera
{0}icieras
{0}iciera
{0}iciéramos
{0}icierais
{0}icieran
{0}iciese
{0}icieses
{0}iciese
{0}iciésemos
{0}icieseis
{0}iciesen
{0}iciere
{0}icieres
{0}iciere
{0}iciéremos
{0}iciereis
{0}icieren
{0}az
{0}aga
{0}agamos
{0}aced
{0}agan
no {0}agas
no {0}aga
no {0}agamos
no {0}agáis
no {0}agan""",
    'es-conj-er (placer)':
"""{0}placer
{0}placiendo
{0}placido
{0}plazco
{0}places
{0}place
{0}placemos
{0}placéis
{0}placen
{0}placía
{0}placías
{0}placía
{0}placíamos
{0}placíais
{0}placían
{0}plací
{0}placiste
{0}plació or {0}plugo
{0}placimos
{0}placisteis
{0}placieron or {0}pluguieron
{0}placeré
{0}placerás
{0}placerá
{0}placeremos
{0}placeréis
{0}placerán
{0}placería
{0}placerías
{0}placería
{0}placeríamos
{0}placeríais
{0}placerían
{0}plazca
{0}plazcas
{0}plazca, {0}plega, or {0}plegue
{0}plazcamos
{0}plazcáis
{0}plazcan
{0}placiera
{0}placieras
{0}placiera or {0}pluguiera
{0}placiéramos
{0}placierais
{0}placieran or {0}pluguieran
{0}placiese
{0}placieses
{0}placiese or {0}pluguiese
{0}placiésemos
{0}placieseis
{0}placiesen or {0}pluguiesen
{0}placiere
{0}placieres
{0}placiere or {0}pluguiere
{0}placiéremos
{0}placiereis
{0}placieren or {0}pluguieren
{0}place
{0}plazca
{0}plazcamos
{0}placed
{0}plazcan
no {0}plazcas
no {0}plazca, {0}plega, or {0}plegue
no {0}plazcamos
no {0}plazcáis
no {0}plazcan""",
    'es-conj-er (poder)':
"""poder
pudiendo
podido
puedo
puedes
puede
podemos
podéis
pueden
podía
podías
podía
podíamos
podíais
podían
pude
pudiste
pudo
pudimos
pudisteis
pudieron
podré
podrás
podrá
podremos
podréis
podrán
podría
podrías
podría
podríamos
podríais
podrían
pueda
puedas
pueda
podamos
podáis
puedan
pudiera
pudieras
pudiera
pudiéramos
pudierais
pudieran
pudiese
pudieses
pudiese
pudiésemos
pudieseis
pudiesen
pudiere
pudieres
pudiere
pudiéremos
pudiereis
pudieren
puede
pueda
podamos
poded
puedan
no puedas
no pueda
no podamos
no podáis
no puedan""",
    'es-conj-er (poner)':
"""{0}poner
{0}poniendo
{0}puesto
{0}pongo
{0}pones
{0}pone
{0}ponemos
{0}ponéis
{0}ponen
{0}ponía
{0}ponías
{0}ponía
{0}poníamos
{0}poníais
{0}ponían
{0}puse
{0}pusiste
{0}puso
{0}pusimos
{0}pusisteis
{0}pusieron
{0}pondré
{0}pondrás
{0}pondrá
{0}pondremos
{0}pondréis
{0}pondrán
{0}pondría
{0}pondrías
{0}pondría
{0}pondríamos
{0}pondríais
{0}pondrían
{0}ponga
{0}pongas
{0}ponga
{0}pongamos
{0}pongáis
{0}pongan
{0}pusiera
{0}pusieras
{0}pusiera
{0}pusiéramos
{0}pusierais
{0}pusieran
{0}pusiese
{0}pusieses
{0}pusiese
{0}pusiésemos
{0}pusieseis
{0}pusiesen
{0}pusiere
{0}pusieres
{0}pusiere
{0}pusiéremos
{0}pusiereis
{0}pusieren
pón
{0}ponga
{0}pongamos
{0}poned
{0}pongan
no {0}pongas
no {0}ponga
no {0}pongamos
no {0}pongáis
no {0}pongan""",
    'es-conj-er (querer)':
"""querer
queriendo
querido
quiero
quieres
quiere
queremos
queréis
quieren
quería
querías
quería
queríamos
queríais
querían
quise
quisiste
quiso
quisimos
quisisteis
quisieron
querré
querrás
querrá
querremos
querréis
querrán
querría
querrías
querría
querríamos
querríais
querrían
quiera
quieras
quiera
queramos
queráis
quieran
quisiera
quisieras
quisiera
quisiéramos
quisierais
quisieran
quisiese
quisieses
quisiese
quisiésemos
quisieseis
quisiesen
quisiere
quisieres
quisiere
quisiéremos
quisiereis
quisieren
quiere
quiera
queramos
quered
quieran
no quieras
no quiera
no queramos
no queráis
no quieran""",
    'es-conj-er (raer)':
"""raer
rayendo
raído
rao, raigo, or rayo
raes
rae
raemos
raéis
raen
raía
raías
raía
raíamos
raíais
raían
raí
raíste
rayó
raímos
raísteis
rayeron
raeré
raerás
raerá
raeremos
raeréis
raerán
raería
raerías
raería
raeríamos
raeríais
raerían
raiga or raya
raigas or rayas
raiga or raya
raigamos or rayamos
raigáis or rayáis
raigan or rayan
rayera
rayeras
rayera
rayéramos
rayerais
rayeran
rayese
rayeses
rayese
rayésemos
rayeseis
rayesen
rayere
rayeres
rayere
rayéremos
rayereis
rayeren
rae
raiga or raya
raigamos or rayamos
raed
raigan or rayan
no raigas or no rayas
no raiga or no raya
no raigamos or no rayamos
no raigáis or no rayáis
no raigan or no rayan""",
    'es-conj-er (rehacer)':
"""rehacer
rehaciendo
rehecho
rehago
rehaces
rehace
rehacemos
rehacéis
rehacen
rehacía
rehacías
rehacía
rehacíamos
rehacíais
rehacían
rehíce
rehiciste
rehízo
rehicimos
rehicisteis
rehicieron
reharé
reharás
rehará
reharemos
reharéis
reharán
reharía
reharías
reharía
reharíamos
reharíais
reharían
rehaga
rehagas
rehaga
rehagamos
rehagáis
rehagan
rehiciera
rehicieras
rehiciera
rehiciéramos
rehicierais
rehicieran
rehiciese
rehicieses
rehiciese
rehiciésemos
rehicieseis
rehiciesen
rehiciere
rehicieres
rehiciere
rehiciéremos
rehiciereis
rehicieren
rehaz
rehaga
rehagamos
rehaced
rehagan
no rehagas
no rehaga
no rehagamos
no rehagáis
no rehagan""",
    'es-conj-er (roer)':
"""{0}roer
{0}royendo
{0}roído
{0}roo, {0}roigo, or {0}royo
{0}roes
{0}roe
{0}roemos
{0}roéis
{0}roen
{0}roía
{0}roías
{0}roía
{0}roíamos
{0}roíais
{0}roían
{0}roí
{0}roíste
{0}royó
{0}roímos
{0}roísteis
{0}royeron
{0}roeré
{0}roerás
{0}roerá
{0}roeremos
{0}roeréis
{0}roerán
{0}roería
{0}roerías
{0}roería
{0}roeríamos
{0}roeríais
{0}roerían
{0}roa, {0}roiga, or {0}roya
{0}roas, {0}roigas, or {0}royas
{0}roa or {0}roiga
{0}roamos or {0}roigamos
{0}roáis, {0}roigáis, or {0}royáis
{0}roan, {0}roigan, or {0}royan
{0}royera
{0}royeras
{0}royera
{0}royéramos
{0}royerais
{0}royeran
{0}royese
{0}royeses
{0}royese
{0}royésemos
{0}royeseis
{0}royesen
{0}royere
{0}royeres
{0}royere
{0}royéremos
{0}royereis
{0}royeren
{0}roe
{0}roa or {0}roiga
{0}roamos or {0}roigamos
{0}roed
{0}roan or {0}roigan
no {0}roas, no {0}roigas, or no {0}royas
no {0}roa or no {0}roiga
no {0}roamos or no {0}roigamos
no {0}roáis, no {0}roigáis, or no {0}royáis
no {0}roan, no {0}roigan, or no {0}royan""",
    'es-conj-er (saber)':
"""{0}saber
{0}sabiendo
{0}sabido
{0}sé
{0}sabes
{0}sabe
{0}sabemos
{0}sabéis
{0}saben
{0}sabía
{0}sabías
{0}sabía
{0}sabíamos
{0}sabíais
{0}sabían
{0}supe
{0}supiste
{0}supo
{0}supimos
{0}supisteis
{0}supieron
{0}sabré
{0}sabrás
{0}sabrá
{0}sabremos
{0}sabréis
{0}sabrán
{0}sabría
{0}sabrías
{0}sabría
{0}sabríamos
{0}sabríais
{0}sabrían
{0}sepa
{0}sepas
{0}sepa
{0}sepamos
{0}sepáis
{0}sepan
{0}supiera
{0}supieras
{0}supiera
{0}supiéramos
{0}supierais
{0}supieran
{0}supiese
{0}supieses
{0}supiese
{0}supiésemos
{0}supieseis
{0}supiesen
{0}supiere
{0}supieres
{0}supiere
{0}supiéremos
{0}supiereis
{0}supieren
{0}sabe
{0}sepa
{0}sepamos
{0}sabed
{0}sepan
no {0}sepas
no {0}sepa
no {0}sepamos
no {0}sepáis
no {0}sepan""",
    'es-conj-er (ser)':
"""ser
siendo
sido
soy
eres
es
somos
sois
son
era
eras
era
éramos
erais
eran
fui
fuiste
fue
fuimos
fuisteis
fueron
seré
serás
será
seremos
seréis
serán
sería
serías
sería
seríamos
seríais
serían
sea
seas
sea
seamos
seáis
sean
fuera
fueras
fuera
fuéramos
fuerais
fueran
fuese
fueses
fuese
fuésemos
fueseis
fuesen
fuere
fueres
fuere
fuéremos
fuereis
fueren
sé
sea
seamos
sed
sean
no seas
no sea
no seamos
no seáis
no sean""",
    'es-conj-er (soler)':
"""soler
soliendo
*solido
suelo
sueles
suele
solemos
soléis
suelen
solía
solías
solía
solíamos
solíais
solían
*solí
*soliste
*solió
*solimos
*solisteis
*solieron
*soleré
*solerás
*solerá
*soleremos
*soleréis
*solerán
*solería
*solerías
*solería
*soleríamos
*soleríais
*solerían
suela
suelas
suela
solamos
soláis
suelan
soliera
solieras
soliera
soliéramos
solierais
solieran
soliese
solieses
soliese
soliésemos
solieseis
soliesen
*soliere
*solieres
*soliere
*soliéremos
*soliereis
*solieren
*suele
*suela
*solamos
*soled
*suelan
*no suelas
*no suela
*no solamos
*no soláis
*no suelan""",
    'es-conj-er (tener)':
"""{0}tener
{0}teniendo
{0}tenido
{0}tengo
{0}tienes
{0}tiene
{0}tenemos
{0}tenéis
{0}tienen
{0}tenía
{0}tenías
{0}tenía
{0}teníamos
{0}teníais
{0}tenían
{0}tuve
{0}tuviste
{0}tuvo
{0}tuvimos
{0}tuvisteis
{0}tuvieron
{0}tendré
{0}tendrás
{0}tendrá
{0}tendremos
{0}tendréis
{0}tendrán
{0}tendría
{0}tendrías
{0}tendría
{0}tendríamos
{0}tendríais
{0}tendrían
{0}tenga
{0}tengas
{0}tenga
{0}tengamos
{0}tengáis
{0}tengan
{0}tuviera
{0}tuvieras
{0}tuviera
{0}tuviéramos
{0}tuvierais
{0}tuvieran
{0}tuviese
{0}tuvieses
{0}tuviese
{0}tuviésemos
{0}tuvieseis
{0}tuviesen
{0}tuviere
{0}tuvieres
{0}tuviere
{0}tuviéremos
{0}tuviereis
{0}tuvieren
{0}tén
{0}tenga
{0}tengamos
{0}tened
{0}tengan
no {0}tengas
no {0}tenga
no {0}tengamos
no {0}tengáis
no {0}tengan""",
    'es-conj-er (traer)':
"""{0}er
{0}yendo
{0}ído
{0}igo
{0}es
{0}e
{0}emos
{0}éis
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}je
{0}jiste
{0}jo
{0}jimos
{0}jisteis
{0}jeron
{0}eré
{0}erás
{0}erá
{0}eremos
{0}eréis
{0}erán
{0}ería
{0}erías
{0}ería
{0}eríamos
{0}eríais
{0}erían
{0}iga
{0}igas
{0}iga
{0}igamos
{0}igáis
{0}igan
{0}jera
{0}jeras
{0}jera
{0}jéramos
{0}jerais
{0}jeran
{0}jese
{0}jeses
{0}jese
{0}jésemos
{0}jeseis
{0}jesen
{0}jere
{0}jeres
{0}jere
{0}jéremos
{0}jereis
{0}jeren
{0}e
{0}iga
{0}igamos
{0}ed
{0}igan
no {0}igas
no {0}iga
no {0}igamos
no {0}igáis
no {0}igan""",
    'es-conj-er (valer)':
"""{0}valer
{0}valiendo
{0}valido
{0}valgo
{0}vales
{0}vale
{0}valemos
{0}valéis
{0}valen
{0}valía
{0}valías
{0}valía
{0}valíamos
{0}valíais
{0}valían
{0}valí
{0}valiste
{0}valió
{0}valimos
{0}valisteis
{0}valieron
{0}valdré
{0}valdrás
{0}valdrá
{0}valdremos
{0}valdréis
{0}valdrán
{0}valdría
{0}valdrías
{0}valdría
{0}valdríamos
{0}valdríais
{0}valdrían
{0}valga
{0}valgas
{0}valga
{0}valgamos
{0}valgáis
{0}valgan
{0}valiera
{0}valieras
{0}valiera
{0}valiéramos
{0}valierais
{0}valieran
{0}valiese
{0}valieses
{0}valiese
{0}valiésemos
{0}valieseis
{0}valiesen
{0}valiere
{0}valieres
{0}valiere
{0}valiéremos
{0}valiereis
{0}valieren
{0}vale
{0}valga
{0}valgamos
{0}valed
{0}valgan
no {0}valgas
no {0}valga
no {0}valgamos
no {0}valgáis
no {0}valgan""",
    'es-conj-er (ver)':
"""{0}ver
{0}viendo
visto
{0}veo
ves
ve
{0}vemos
veis
ven
veía
veías
veía
veíamos
veíais
veían
vi
viste
vio
vimos
visteis
vieron
veré
verás
verá
veremos
veréis
verán
vería
verías
vería
veríamos
veríais
verían
vea
veas
vea
veamos
veáis
vean
viera
vieras
viera
viéramos
vierais
vieran
viese
vieses
viese
viésemos
vieseis
viesen
viere
vieres
viere
viéremos
viereis
vieren
{0}ve
{0}vea
{0}veamos
{0}ved
{0}vean
no veas
no vea
no veamos
no veáis
no vean""",
    'es-conj-er (yacer)':
"""{0}yacer
{0}yaciendo
{0}yacido
{0}yazco, {0}yazgo, or {0}yago
{0}yaces
{0}yace
{0}yacemos
{0}yacéis
{0}yacen
{0}yacía
{0}yacías
{0}yacía
{0}yacíamos
{0}yacíais
{0}yacían
{0}yací
{0}yaciste
{0}yació
{0}yacimos
{0}yacisteis
{0}yacieron
{0}yaceré
{0}yacerás
{0}yacerá
{0}yaceremos
{0}yaceréis
{0}yacerán
{0}yacería
{0}yacerías
{0}yacería
{0}yaceríamos
{0}yaceríais
{0}yacerían
{0}yazca, {0}yazga, or {0}yaga
{0}yazcas, {0}yazgas, or {0}yagas
{0}yazca, {0}yazga, or {0}yaga
{0}yazcamos, {0}yazgamos, or {0}yagamos
{0}yazcáis, {0}yazgáis, or {0}yagáis
{0}yazcan, {0}yazgan, or {0}yagan
{0}yaciera
{0}yacieras
{0}yaciera
{0}yaciéramos
{0}yacierais
{0}yacieran
{0}yaciese
{0}yacieses
{0}yaciese
{0}yaciésemos
{0}yacieseis
{0}yaciesen
{0}yaciere
{0}yacieres
{0}yaciere
{0}yaciéremos
{0}yaciereis
{0}yacieren
{0}yace or {0}yaz
{0}yazca, {0}yazga, or {0}yaga
{0}yazcamos, {0}yazgamos, or {0}yagamos
{0}yaced
{0}yazcan, {0}yazgan, or {0}yagan
no {0}yazcas
no {0}yazca, no {0}yazga, or no {0}yaga
no {0}yazcamos, no {0}yazgamos, or no {0}yagamos
no {0}yazcáis, no {0}yazgáis, or no {0}yagáis
no {0}yazcan, no {0}yazgan, or no {0}yagan""",
    'es-conj-eír':
"""{0}eír
{0}iendo
{0}eído
{0}ío
{0}íes
{0}íe
{0}eímos
{0}eís
{0}íen
{0}eía
{0}eías
{0}eía
{0}eíamos
{0}eíais
{0}eían
{0}eí
{0}eíste
{0}ió
{0}eímos
{0}eísteis
{0}ieron
{0}eiré
{0}eirás
{0}eirá
{0}eiremos
{0}eiréis
{0}eirán
{0}eiría
{0}eirías
{0}eiría
{0}eiríamos
{0}eiríais
{0}eirían
{0}ía
{0}ías
{0}ía
{0}iamos
{0}iáis
{0}ían
{0}iera
{0}ieras
{0}iera
{0}iéramos
{0}ierais
{0}ieran
{0}iese
{0}ieses
{0}iese
{0}iésemos
{0}ieseis
{0}iesen
{0}iere
{0}ieres
{0}iere
{0}iéremos
{0}iereis
{0}ieren
{0}íe
{0}ía
{0}iamos
{0}eíd
{0}ían
no {0}ías
no {0}ía
no {0}iamos
no {0}iáis
no {0}ían""",
    'es-conj-gar (u-ue)':
"""jugar
jugando
jugado
juego
juegas
juega
jugamos
jugáis
juegan
jugaba
jugabas
jugaba
jugábamos
jugabais
jugaban
jugué
jugaste
jugó
jugamos
jugasteis
jugaron
jugaré
jugarás
jugará
jugaremos
jugaréis
jugarán
jugaría
jugarías
jugaría
jugaríamos
jugaríais
jugarían
juegue
juegues
juegue
juguemos
juguéis
jueguen
jugara
jugaras
jugara
jugáramos
jugarais
jugaran
jugase
jugases
jugase
jugásemos
jugaseis
jugasen
jugare
jugares
jugare
jugáremos
jugareis
jugaren
juega
juegue
juguemos
jugad
jueguen
no juegues
no juegue
no juguemos
no juguéis
no jueguen""",
    'es-conj-guar':
"""{0}guar
{0}guando
{0}guado
{0}guo
{0}guas
{0}gua
{0}guamos
{0}guáis
{0}guan
{0}guaba
{0}guabas
{0}guaba
{0}guábamos
{0}guabais
{0}guaban
{0}güé
{0}guaste
{0}guó
{0}guamos
{0}guasteis
{0}guaron
{0}guaré
{0}guarás
{0}guará
{0}guaremos
{0}guaréis
{0}guarán
{0}guaría
{0}guarías
{0}guaría
{0}guaríamos
{0}guaríais
{0}guarían
{0}güe
{0}gües
{0}güe
{0}güemos
{0}güéis
{0}güen
{0}guara
{0}guaras
{0}guara
{0}guáramos
{0}guarais
{0}guaran
{0}guase
{0}guases
{0}guase
{0}guásemos
{0}guaseis
{0}guasen
{0}guare
{0}guares
{0}guare
{0}guáremos
{0}guareis
{0}guaren
{0}gua
{0}güe
{0}güemos
{0}guad
{0}güen
no {0}gües
no {0}güe
no {0}güemos
no {0}güéis
no {0}güen""",
    'es-conj-ir (abolir)':
"""{0}o{1}ir
{0}o{1}iendo
{0}o{1}ido
{0}o{1}o
{0}o{1}es
{0}o{1}e
{0}o{1}imos
{0}o{1}ís
{0}o{1}en
{0}o{1}ía
{0}o{1}ías
{0}o{1}ía
{0}o{1}íamos
{0}o{1}íais
{0}o{1}ían
{0}o{1}í
{0}o{1}iste
{0}o{1}ió
{0}o{1}imos
{0}o{1}isteis
{0}o{1}ieron
{0}o{1}iré
{0}o{1}irás
{0}o{1}irá
{0}o{1}iremos
{0}o{1}iréis
{0}o{1}irán
{0}o{1}iría
{0}o{1}irías
{0}o{1}iría
{0}o{1}iríamos
{0}o{1}iríais
{0}o{1}irían
{0}o{1}a
{0}o{1}as
{0}o{1}a
{0}o{1}amos
{0}o{1}áis
{0}o{1}an
{0}o{1}iera
{0}o{1}ieras
{0}o{1}iera
{0}o{1}iéramos
{0}o{1}ierais
{0}o{1}ieran
{0}o{1}iese
{0}o{1}ieses
{0}o{1}iese
{0}o{1}iésemos
{0}o{1}ieseis
{0}o{1}iesen
{0}o{1}iere
{0}o{1}ieres
{0}o{1}iere
{0}o{1}iéremos
{0}o{1}iereis
{0}o{1}ieren
{0}o{1}e
{0}o{1}a
{0}o{1}amos
{0}o{1}id
{0}o{1}an
no {0}o{1}as
no {0}o{1}a
no {0}o{1}amos
no {0}o{1}áis
no {0}o{1}an""",
    'es-conj-ir (asir)':
"""{0}ir
{0}iendo
{0}ido
{0}go
{0}es
{0}e
{0}imos
{0}ís
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ió
{0}imos
{0}isteis
{0}ieron
{0}iré
{0}irás
{0}irá
{0}iremos
{0}iréis
{0}irán
{0}iría
{0}irías
{0}iría
{0}iríamos
{0}iríais
{0}irían
{0}ga
{0}gas
{0}ga
{0}gamos
{0}gáis
{0}gan
{0}iera
{0}ieras
{0}iera
{0}iéramos
{0}ierais
{0}ieran
{0}iese
{0}ieses
{0}iese
{0}iésemos
{0}ieseis
{0}iesen
{0}iere
{0}ieres
{0}iere
{0}iéremos
{0}iereis
{0}ieren
{0}e
{0}ga
{0}gamos
{0}id
{0}gan
no {0}gas
no {0}ga
no {0}gamos
no {0}gáis
no {0}gan""",
    'es-conj-ir (aterir)':
"""{0}ir
{0}iendo
{0}ido
*{0}o
*{0}es
*{0}e
 {0}imos
 {0}ís
*{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ió
{0}imos
{0}isteis
{0}ieron
{0}iré
{0}irás
{0}irá
{0}iremos
{0}iréis
{0}irán
{0}iría
{0}irías
{0}iría
{0}iríamos
{0}iríais
{0}irían
*{0}a
*{0}as
*{0}a
*{0}amos
*{0}áis
*{0}an
{0}iera
{0}ieras
{0}iera
{0}iéramos
{0}ierais
{0}ieran
{0}iese
{0}ieses
{0}iese
{0}iésemos
{0}ieseis
{0}iesen
{0}iere
{0}ieres
{0}iere
{0}iéremos
{0}iereis
{0}ieren
*{0}e
*{0}a
*{0}amos
{0}id
*{0}an
*no {0}as
*no {0}a
*no {0}amos
*no {0}áis
*no {0}an""",
    'es-conj-ir (decir)':
"""{0}decir
{0}diciendo
{0}dicho
{0}digo
{0}dices
{0}dice
{0}decimos
{0}decís
{0}dicen
{0}decía
{0}decías
{0}decía
{0}decíamos
{0}decíais
{0}decían
{0}dije
{0}dijiste
{0}dijo
{0}dijimos
{0}dijisteis
{0}dijeron
{0}diré
{0}dirás
{0}dirá
{0}diremos
{0}diréis
{0}dirán
{0}diría
{0}dirías
{0}diría
{0}diríamos
{0}diríais
{0}dirían
{0}diga
{0}digas
{0}diga
{0}digamos
{0}digáis
{0}digan
{0}dijera
{0}dijeras
{0}dijera
{0}dijéramos
{0}dijerais
{0}dijeran
{0}dijese
{0}dijeses
{0}dijese
{0}dijésemos
{0}dijeseis
{0}dijesen
{0}dijere
{0}dijeres
{0}dijere
{0}dijéremos
{0}dijereis
{0}dijeren
di
{0}diga
{0}digamos
{0}decid
{0}digan
no {0}digas
no {0}diga
no {0}digamos
no {0}digáis
no {0}digan""",
    'es-conj-ir (e-ie)':
"""{0}e{1}ir
{0}e{1}iendo
{0}e{1}ido
{0}ie{1}o
{0}ie{1}es
{0}ie{1}e
{0}e{1}imos
{0}e{1}ís
{0}ie{1}en
{0}e{1}ía
{0}e{1}ías
{0}e{1}ía
{0}e{1}íamos
{0}e{1}íais
{0}e{1}ían
{0}e{1}í
{0}e{1}iste
{0}e{1}ió
{0}e{1}imos
{0}e{1}isteis
{0}e{1}ieron
{0}e{1}iré
{0}e{1}irás
{0}e{1}irá
{0}e{1}iremos
{0}e{1}iréis
{0}e{1}irán
{0}e{1}iría
{0}e{1}irías
{0}e{1}iría
{0}e{1}iríamos
{0}e{1}iríais
{0}e{1}irían
{0}ie{1}a
{0}ie{1}as
{0}ie{1}a
{0}e{1}amos
{0}e{1}áis
{0}ie{1}an
{0}e{1}iera
{0}e{1}ieras
{0}e{1}iera
{0}e{1}iéramos
{0}e{1}ierais
{0}e{1}ieran
{0}e{1}iese
{0}e{1}ieses
{0}e{1}iese
{0}e{1}iésemos
{0}e{1}ieseis
{0}e{1}iesen
{0}e{1}iere
{0}e{1}ieres
{0}e{1}iere
{0}e{1}iéremos
{0}e{1}iereis
{0}e{1}ieren
{0}ie{1}e
{0}ie{1}a
{0}e{1}amos
{0}e{1}id
{0}ie{1}an
no {0}ie{1}as
no {0}ie{1}a
no {0}e{1}amos
no {0}e{1}áis
no {0}ie{1}an""",
    'es-conj-ir (embaír)':
"""{0}aír
{0}ayendo
{0}aído
—
—
—
{0}aímos
{0}aís
—
{0}aía
{0}aías
{0}aía
{0}aíamos
{0}aíais
{0}aían
{0}aí
{0}aíste
{0}ayó
{0}aímos
{0}aísteis
{0}ayeron
{0}airé
{0}airás
{0}airá
{0}airemos
{0}airéis
{0}airán
{0}airía
{0}airías
{0}airía
{0}airíamos
{0}airíais
{0}airían
—
—
—
—
—
—
{0}ayera
{0}ayeras
{0}ayera
{0}ayéramos
{0}ayerais
{0}ayeran
{0}ayese
{0}ayeses
{0}ayese
{0}ayésemos
{0}ayeseis
{0}ayesen
{0}ayere
{0}ayeres
{0}ayere
{0}ayéremos
{0}ayereis
{0}ayeren
—
—
—
{0}aíd
—
—
—
—
—
—""",
    'es-conj-ir (erguir)':
"""erguir
irguiendo
erguido
irgo, yergo
irgues, yergues
irgue, yergue
erguimos
erguís
irguen, yerguen
erguía
erguías
erguía
erguíamos
erguíais
erguían
erguí
erguiste
irguió
erguimos
erguisteis
irguieron
erguiré
erguirás
erguirá
erguiremos
erguiréis
erguirán
erguiría
erguirías
erguiría
erguiríamos
erguiríais
erguirían
irga, yerga
irgas, yergas
irga, yerga
irgamos, yergamos
irgáis, yergáis
irgan, yergan
irguiera
irguieras
irguiera
irguiéramos
irguierais
irguieran
irguiese
irguieses
irguiese
irguiésemos
irguieseis
irguiesen
irguiere
irguieres
irguiere
irguiéremos
irguiereis
irguieren
irgue, yergue
irga, yerga
irgamos, yergamos
erguid
irgan, yergan
no irgas, no yergas
no irga, no yerga
no irgamos, no yergamos
no irgáis, no yergáis
no irgan, no yergan""",
    'es-conj-ir (i-ie)':
"""{0}i{1}ir
{0}i{1}iendo
{0}i{1}ido
{0}ie{1}o
{0}ie{1}es
{0}ie{1}e
{0}i{1}imos
{0}i{1}ís
{0}ie{1}en
{0}i{1}ía
{0}i{1}ías
{0}i{1}ía
{0}i{1}íamos
{0}i{1}íais
{0}i{1}ían
{0}i{1}í
{0}i{1}iste
{0}i{1}ió
{0}i{1}imos
{0}i{1}isteis
{0}i{1}ieron
{0}i{1}iré
{0}i{1}irás
{0}i{1}irá
{0}i{1}iremos
{0}i{1}iréis
{0}i{1}irán
{0}i{1}iría
{0}i{1}irías
{0}i{1}iría
{0}i{1}iríamos
{0}i{1}iríais
{0}i{1}irían
{0}ie{1}a
{0}ie{1}as
{0}ie{1}a
{0}i{1}amos
{0}i{1}áis
{0}ie{1}an
{0}i{1}iera
{0}i{1}ieras
{0}i{1}iera
{0}i{1}iéramos
{0}i{1}ierais
{0}i{1}ieran
{0}i{1}iese
{0}i{1}ieses
{0}i{1}iese
{0}i{1}iésemos
{0}i{1}ieseis
{0}i{1}iesen
{0}i{1}iere
{0}i{1}ieres
{0}i{1}iere
{0}i{1}iéremos
{0}i{1}iereis
{0}i{1}ieren
{0}ie{1}e
{0}ie{1}a
{0}i{1}amos
{0}i{1}id
{0}ie{1}an
no {0}ie{1}as
no {0}ie{1}a
no {0}i{1}amos
no {0}i{1}áis
no {0}ie{1}an""",
    'es-conj-ir (ir)':
"""ir
yendo
ido
voy
vas
va
vamos
vais
van
iba
ibas
iba
íbamos
ibais
iban
fui
fuiste
fue
fuimos
fuisteis
fueron
iré
irás
irá
iremos
iréis
irán
iría
irías
iría
iríamos
iríais
irían
vaya
vayas
vaya
vayamos
vayáis
vayan
fuera
fueras
fuera
fuéramos
fuerais
fueran
fuese
fueses
fuese
fuésemos
fueseis
fuesen
fuere
fueres
fuere
fuéremos
fuereis
fueren
ve
vaya
vamos, or vayamos
id
vayan
no vayas
no vaya
no vamos, or no vayamos
no vayáis
no vayan""",
    'es-conj-ir (o-ue)':
"""{0}o{1}ir
{0}u{1}iendo
{0}o{1}ido
{0}ue{1}o
{0}ue{1}es
{0}ue{1}e
{0}o{1}imos
{0}o{1}ís
{0}ue{1}en
{0}o{1}ía
{0}o{1}ías
{0}o{1}ía
{0}o{1}íamos
{0}o{1}íais
{0}o{1}ían
{0}o{1}í
{0}o{1}iste
{0}u{1}ió
{0}o{1}imos
{0}o{1}isteis
{0}u{1}ieron
{0}o{1}iré
{0}o{1}irás
{0}o{1}irá
{0}o{1}iremos
{0}o{1}iréis
{0}o{1}irán
{0}o{1}iría
{0}o{1}irías
{0}o{1}iría
{0}o{1}iríamos
{0}o{1}iríais
{0}o{1}irían
{0}ue{1}a
{0}ue{1}as
{0}ue{1}a
{0}u{1}amos
{0}u{1}áis
{0}ue{1}an
{0}u{1}iera
{0}u{1}ieras
{0}u{1}iera
{0}u{1}iéramos
{0}u{1}ierais
{0}u{1}ieran
{0}u{1}iese
{0}u{1}ieses
{0}u{1}iese
{0}u{1}iésemos
{0}u{1}ieseis
{0}u{1}iesen
{0}u{1}iere
{0}u{1}ieres
{0}u{1}iere
{0}u{1}iéremos
{0}u{1}iereis
{0}u{1}ieren
{0}ue{1}e
{0}ue{1}a
{0}u{1}amos
{0}o{1}id
{0}ue{1}an
no {0}ue{1}as
no {0}ue{1}a
no {0}u{1}amos
no {0}u{1}áis
no {0}ue{1}an""",
    'es-conj-ir (oír)':
"""{0}ír
{0}yendo
{0}ído
{0}igo
{0}yes
{0}ye
{0}ímos
{0}ís
{0}yen
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}íste
{0}yó
{0}ímos
{0}ísteis
{0}yeron
{0}iré
{0}irás
{0}irá
{0}iremos
{0}iréis
{0}irán
{0}iría
{0}irías
{0}iría
{0}iríamos
{0}iríais
{0}irían
{0}iga
{0}igas
{0}iga
{0}igamos
{0}igáis
{0}igan
{0}yera
{0}yeras
{0}yera
{0}yéramos
{0}yerais
{0}yeran
{0}yese
{0}yeses
{0}yese
{0}yésemos
{0}yeseis
{0}yesen
{0}yere
{0}yeres
{0}yere
{0}yéremos
{0}yereis
{0}yeren
{0}ye
{0}iga
{0}igamos
{0}íd
{0}igan
no {0}igas
no {0}iga
no {0}igamos
no {0}igáis
no {0}igan""",
    'es-conj-ir (rehuir)':
"""rehuir
rehuyendo
rehuido
rehúyo
rehúyes
rehúye
rehuimos
rehuís
rehúyen
rehuía
rehuías
rehuía
rehuíamos
rehuíais
rehuían
rehuí
rehuiste
rehuyó
rehuimos
rehuisteis
rehuyeron
rehuiré
rehuirás
rehuirá
rehuiremos
rehuiréis
rehuirán
rehuiría
rehuirías
rehuiría
rehuiríamos
rehuiríais
rehuirían
rehúya
rehúyas
rehúya
rehuyamos
rehuyáis
rehúyan
rehuyera
rehuyeras
rehuyera
rehuyéramos
rehuyerais
rehuyeran
rehuyese
rehuyeses
rehuyese
rehuyésemos
rehuyeseis
rehuyesen
rehuyere
rehuyeres
rehuyere
rehuyéremos
rehuyereis
rehuyeren
rehúye
rehúya
rehuyamos
rehuid
rehúyan
no rehúyas
no rehúya
no rehuyamos
no rehuyáis
no rehúyan""",
    'es-conj-ir (salir)':
"""{0}salir
{0}saliendo
{0}salido
{0}salgo
{0}sales
{0}sale
{0}salimos
{0}salís
{0}salen
{0}salía
{0}salías
{0}salía
{0}salíamos
{0}salíais
{0}salían
{0}salí
{0}saliste
{0}salió
{0}salimos
{0}salisteis
{0}salieron
{0}saldré
{0}saldrás
{0}saldrá
{0}saldremos
{0}saldréis
{0}saldrán
{0}saldría
{0}saldrías
{0}saldría
{0}saldríamos
{0}saldríais
{0}saldrían
{0}salga
{0}salgas
{0}salga
{0}salgamos
{0}salgáis
{0}salgan
{0}saliera
{0}salieras
{0}saliera
{0}saliéramos
{0}salierais
{0}salieran
{0}saliese
{0}salieses
{0}saliese
{0}saliésemos
{0}salieseis
{0}saliesen
{0}saliere
{0}salieres
{0}saliere
{0}saliéremos
{0}saliereis
{0}salieren
{0}sal
{0}salga
{0}salgamos
{0}salid
{0}salgan
no {0}salgas
no {0}salga
no {0}salgamos
no {0}salgáis
no {0}salgan""",
    'es-conj-ir (venir)':
"""venir
viniendo
venido
vengo
vienes
viene
venimos
venís
vienen
venía
venías
venía
veníamos
veníais
venían
vine
viniste
vino
vinimos
vinisteis
vinieron
vendré
vendrás
vendrá
vendremos
vendréis
vendrán
vendría
vendrías
vendría
vendríamos
vendríais
vendrían
venga
vengas
venga
vengamos
vengáis
vengan
viniera
vinieras
viniera
viniéramos
vinierais
vinieran
viniese
vinieses
viniese
viniésemos
vinieseis
viniesen
viniere
vinieres
viniere
viniéremos
viniereis
vinieren
{0}vén
venga
vengamos
venid
vengan
no vengas
no venga
no vengamos
no vengáis
no vengan""",
    'es-conj-izar':
"""{0}izar
{0}izando
{0}izado
{0}ízo
{0}ízas
{0}íza
{0}izamos
{0}izáis
{0}ízan
{0}izaba
{0}izabas
{0}izaba
{0}izábamos
{0}izabais
{0}izaban
{0}icé
{0}izaste
{0}izó
{0}izamos
{0}izasteis
{0}izaron
{0}izaré
{0}izarás
{0}izará
{0}izaremos
{0}izaréis
{0}izarán
{0}izaría
{0}izarías
{0}izaría
{0}izaríamos
{0}izaríais
{0}izarían
{0}íce
{0}íces
{0}íce
{0}icemos
{0}icéis
{0}ícen
{0}izara
{0}izaras
{0}izara
{0}izáramos
{0}izarais
{0}izaran
{0}izase
{0}izases
{0}izase
{0}izásemos
{0}izaseis
{0}izasen
{0}izare
{0}izares
{0}izare
{0}izáremos
{0}izareis
{0}izaren
{0}íza
{0}íce
{0}icemos
{0}izad
{0}ícen
no {0}íces
no {0}íce
no {0}icemos
no {0}icéis
no {0}ícen""",
    'es-conj-ñer':
"""{0}er
{0}endo
{0}ido
{0}o
{0}es
{0}e
{0}emos
{0}éis
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ó
{0}imos
{0}isteis
{0}eron
{0}eré
{0}erás
{0}erá
{0}eremos
{0}eréis
{0}erán
{0}ería
{0}erías
{0}ería
{0}eríamos
{0}eríais
{0}erían
{0}a
{0}as
{0}a
{0}amos
{0}áis
{0}an
{0}era
{0}eras
{0}era
{0}éramos
{0}erais
{0}eran
{0}ese
{0}eses
{0}ese
{0}ésemos
{0}eseis
{0}esen
{0}ere
{0}eres
{0}ere
{0}éremos
{0}ereis
{0}eren
{0}e
{0}a
{0}amos
{0}ed
{0}an
no {0}as
no {0}a
no {0}amos
no {0}áis
no {0}an""",
    'es-conj-gar':
"""{0}gar
{0}gando
{0}gado
{0}go
{0}gas
{0}ga
{0}gamos
{0}gáis
{0}gan
{0}gaba
{0}gabas
{0}gaba
{0}gábamos
{0}gabais
{0}gaban
{0}gué
{0}gaste
{0}gó
{0}gamos
{0}gasteis
{0}garon
{0}garé
{0}garás
{0}gará
{0}garemos
{0}garéis
{0}garán
{0}garía
{0}garías
{0}garía
{0}garíamos
{0}garíais
{0}garían
{0}gue
{0}gues
{0}gue
{0}guemos
{0}guéis
{0}guen
{0}gara
{0}garas
{0}gara
{0}gáramos
{0}garais
{0}garan
{0}gase
{0}gases
{0}gase
{0}gásemos
{0}gaseis
{0}gasen
{0}gare
{0}gares
{0}gare
{0}gáremos
{0}gareis
{0}garen
{0}ga
{0}gue
{0}guemos
{0}gad
{0}guen
no {0}gues
no {0}gue
no {0}guemos
no {0}guéis
no {0}guen""",
    'es-conj-gar (e-ie)':
"""{0}e{1}gar
{0}e{1}gando
{0}e{1}gado
{0}ie{1}go
{0}ie{1}gas
{0}ie{1}ga
{0}e{1}gamos
{0}e{1}gáis
{0}ie{1}gan
{0}e{1}gaba
{0}e{1}gabas
{0}e{1}gaba
{0}e{1}gábamos
{0}e{1}gabais
{0}e{1}gaban
{0}e{1}gué
{0}e{1}gaste
{0}e{1}gó
{0}e{1}gamos
{0}e{1}gasteis
{0}e{1}garon
{0}e{1}garé
{0}e{1}garás
{0}e{1}gará
{0}e{1}garemos
{0}e{1}garéis
{0}e{1}garán
{0}e{1}garía
{0}e{1}garías
{0}e{1}garía
{0}e{1}garíamos
{0}e{1}garíais
{0}e{1}garían
{0}ie{1}gue
{0}ie{1}gues
{0}ie{1}gue
{0}e{1}guemos
{0}e{1}guéis
{0}ie{1}guen
{0}e{1}gara
{0}e{1}garas
{0}e{1}gara
{0}e{1}gáramos
{0}e{1}garais
{0}e{1}garan
{0}e{1}gase
{0}e{1}gases
{0}e{1}gase
{0}e{1}gásemos
{0}e{1}gaseis
{0}e{1}gasen
{0}e{1}gare
{0}e{1}gares
{0}e{1}gare
{0}e{1}gáremos
{0}e{1}gareis
{0}e{1}garen
{0}ie{1}ga
{0}ie{1}gue
{0}e{1}guemos
{0}e{1}gad
{0}ie{1}guen
no {0}ie{1}gues
no {0}ie{1}gue
no {0}e{1}guemos
no {0}e{1}guéis
no {0}ie{1}guen""",
    'es-conj-gar (o-ue)':
"""{0}o{1}gar
{0}o{1}gando
{0}o{1}gado
{0}ue{1}go
{0}ue{1}gas
{0}ue{1}ga
{0}o{1}gamos
{0}o{1}gáis
{0}ue{1}gan
{0}o{1}gaba
{0}o{1}gabas
{0}o{1}gaba
{0}o{1}gábamos
{0}o{1}gabais
{0}o{1}gaban
{0}o{1}gué
{0}o{1}gaste
{0}o{1}gó
{0}o{1}gamos
{0}o{1}gasteis
{0}o{1}garon
{0}o{1}garé
{0}o{1}garás
{0}o{1}gará
{0}o{1}garemos
{0}o{1}garéis
{0}o{1}garán
{0}o{1}garía
{0}o{1}garías
{0}o{1}garía
{0}o{1}garíamos
{0}o{1}garíais
{0}o{1}garían
{0}ue{1}gue
{0}ue{1}gues
{0}ue{1}gue
{0}o{1}guemos
{0}o{1}guéis
{0}ue{1}guen
{0}o{1}gara
{0}o{1}garas
{0}o{1}gara
{0}o{1}gáramos
{0}o{1}garais
{0}o{1}garan
{0}o{1}gase
{0}o{1}gases
{0}o{1}gase
{0}o{1}gásemos
{0}o{1}gaseis
{0}o{1}gasen
{0}o{1}gare
{0}o{1}gares
{0}o{1}gare
{0}o{1}gáremos
{0}o{1}gareis
{0}o{1}garen
{0}ue{1}ga
{0}ue{1}gue
{0}o{1}guemos
{0}o{1}gad
{0}ue{1}guen
no {0}ue{1}gues
no {0}ue{1}gue
no {0}o{1}guemos
no {0}o{1}guéis
no {0}ue{1}guen""",
    'es-conj-ger':
"""{0}ger
{0}giendo
{0}gido
{0}jo
{0}ges
{0}ge
{0}gemos
{0}géis
{0}gen
{0}gía
{0}gías
{0}gía
{0}gíamos
{0}gíais
{0}gían
{0}gí
{0}giste
{0}gió
{0}gimos
{0}gisteis
{0}gieron
{0}geré
{0}gerás
{0}gerá
{0}geremos
{0}geréis
{0}gerán
{0}gería
{0}gerías
{0}gería
{0}geríamos
{0}geríais
{0}gerían
{0}ja
{0}jas
{0}ja
{0}jamos
{0}jáis
{0}jan
{0}giera
{0}gieras
{0}giera
{0}giéramos
{0}gierais
{0}gieran
{0}giese
{0}gieses
{0}giese
{0}giésemos
{0}gieseis
{0}giesen
{0}giere
{0}gieres
{0}giere
{0}giéremos
{0}giereis
{0}gieren
{0}ge
{0}ja
{0}jamos
{0}ged
{0}jan
no {0}jas
no {0}ja
no {0}jamos
no {0}jáis
no {0}jan""",
    'es-conj-gir':
"""{0}gir
{0}giendo
{0}gido
{0}jo
{0}ges
{0}ge
{0}gimos
{0}gís
{0}gen
{0}gía
{0}gías
{0}gía
{0}gíamos
{0}gíais
{0}gían
{0}gí
{0}giste
{0}gió
{0}gimos
{0}gisteis
{0}gieron
{0}giré
{0}girás
{0}girá
{0}giremos
{0}giréis
{0}girán
{0}giría
{0}girías
{0}giría
{0}giríamos
{0}giríais
{0}girían
{0}ja
{0}jas
{0}ja
{0}jamos
{0}jáis
{0}jan
{0}giera
{0}gieras
{0}giera
{0}giéramos
{0}gierais
{0}gieran
{0}giese
{0}gieses
{0}giese
{0}giésemos
{0}gieseis
{0}giesen
{0}giere
{0}gieres
{0}giere
{0}giéremos
{0}giereis
{0}gieren
{0}ge
{0}ja
{0}jamos
{0}gid
{0}jan
no {0}jas
no {0}ja
no {0}jamos
no {0}jáis
no {0}jan""",
    'es-conj-guir':
"""{0}guir
{0}guiendo
{0}guido
{0}go
{0}gues
{0}gue
{0}guimos
{0}guís
{0}guen
{0}guía
{0}guías
{0}guía
{0}guíamos
{0}guíais
{0}guían
{0}guí
{0}guiste
{0}guió
{0}guimos
{0}guisteis
{0}guieron
{0}guiré
{0}guirás
{0}guirá
{0}guiremos
{0}guiréis
{0}guirán
{0}guiría
{0}guirías
{0}guiría
{0}guiríamos
{0}guiríais
{0}guirían
{0}ga
{0}gas
{0}ga
{0}gamos
{0}gáis
{0}gan
{0}guiera
{0}guieras
{0}guiera
{0}guiéramos
{0}guierais
{0}guieran
{0}guiese
{0}guieses
{0}guiese
{0}guiésemos
{0}guieseis
{0}guiesen
{0}guiere
{0}guieres
{0}guiere
{0}guiéremos
{0}guiereis
{0}guieren
{0}gue
{0}ga
{0}gamos
{0}guid
{0}gan
no {0}gas
no {0}ga
no {0}gamos
no {0}gáis
no {0}gan""",
    'es-conj-guir (e-i)':
"""{0}e{1}guir
{0}i{1}guiendo
{0}e{1}guido
{0}i{1}go
{0}i{1}gues
{0}i{1}gue
{0}e{1}guimos
{0}e{1}guís
{0}i{1}guen
{0}e{1}guía
{0}e{1}guías
{0}e{1}guía
{0}e{1}guíamos
{0}e{1}guíais
{0}e{1}guían
{0}e{1}guí
{0}e{1}guiste
{0}i{1}guió
{0}e{1}guimos
{0}e{1}guisteis
{0}i{1}guieron
{0}e{1}guiré
{0}e{1}guirás
{0}e{1}guirá
{0}e{1}guiremos
{0}e{1}guiréis
{0}e{1}guirán
{0}e{1}guiría
{0}e{1}guirías
{0}e{1}guiría
{0}e{1}guiríamos
{0}e{1}guiríais
{0}e{1}guirían
{0}i{1}ga
{0}i{1}gas
{0}i{1}ga
{0}i{1}gamos
{0}i{1}gáis
{0}i{1}gan
{0}i{1}guiera
{0}i{1}guieras
{0}i{1}guiera
{0}i{1}guiéramos
{0}i{1}guierais
{0}i{1}guieran
{0}i{1}guiese
{0}i{1}guieses
{0}i{1}guiese
{0}i{1}guiésemos
{0}i{1}guieseis
{0}i{1}guiesen
{0}i{1}guiere
{0}i{1}guieres
{0}i{1}guiere
{0}i{1}guiéremos
{0}i{1}guiereis
{0}i{1}guieren
{0}i{1}gue
{0}i{1}ga
{0}i{1}gamos
{0}e{1}guid
{0}i{1}gan
no {0}i{1}gas
no {0}i{1}ga
no {0}i{1}gamos
no {0}i{1}gáis
no {0}i{1}gan""",
    'es-conj-güir':
"""{0}güir
{0}guyendo
{0}güido
{0}guyo
{0}guyes
{0}guye
{0}güimos
{0}güís
{0}guyen
{0}güía
{0}güías
{0}güía
{0}güíamos
{0}güíais
{0}güían
{0}güí
{0}güiste
{0}guyó
{0}güimos
{0}güisteis
{0}guyeron
{0}güiré
{0}güirás
{0}güirá
{0}güiremos
{0}güiréis
{0}güirán
{0}güiría
{0}güirías
{0}güiría
{0}güiríamos
{0}güiríais
{0}güirían
{0}guya
{0}guyas
{0}guya
{0}guyamos
{0}guyáis
{0}guyan
{0}guyera
{0}guyeras
{0}guyera
{0}guyéramos
{0}guyerais
{0}guyeran
{0}guyese
{0}guyeses
{0}guyese
{0}guyésemos
{0}guyeseis
{0}guyesen
{0}guyere
{0}guyeres
{0}guyere
{0}guyéremos
{0}guyereis
{0}guyeren
{0}guye
{0}guya
{0}guyamos
{0}güid
{0}guyan
no {0}guyas
no {0}guya
no {0}guyamos
no {0}guyáis
no {0}guyan""",
    'es-conj-car (i-í)':
"""{0}i{1}car
{0}i{1}cando
{0}i{1}cado
{0}í{1}co
{0}í{1}cas
{0}í{1}ca
{0}i{1}camos
{0}i{1}cáis
{0}í{1}can
{0}i{1}caba
{0}i{1}cabas
{0}i{1}caba
{0}i{1}cábamos
{0}i{1}cabais
{0}i{1}caban
{0}i{1}qué
{0}i{1}caste
{0}i{1}có
{0}i{1}camos
{0}i{1}casteis
{0}i{1}caron
{0}i{1}caré
{0}i{1}carás
{0}i{1}cará
{0}i{1}caremos
{0}i{1}caréis
{0}i{1}carán
{0}i{1}caría
{0}i{1}carías
{0}i{1}caría
{0}i{1}caríamos
{0}i{1}caríais
{0}i{1}carían
{0}í{1}que
{0}í{1}ques
{0}í{1}que
{0}i{1}quemos
{0}i{1}quéis
{0}í{1}quen
{0}i{1}cara
{0}i{1}caras
{0}i{1}cara
{0}i{1}cáramos
{0}i{1}carais
{0}i{1}caran
{0}i{1}case
{0}i{1}cases
{0}i{1}case
{0}i{1}cásemos
{0}i{1}caseis
{0}i{1}casen
{0}i{1}care
{0}i{1}cares
{0}i{1}care
{0}i{1}cáremos
{0}i{1}careis
{0}i{1}caren
{0}í{1}ca
{0}í{1}que
{0}i{1}quemos
{0}i{1}cad
{0}í{1}quen
no {0}í{1}ques
no {0}í{1}que
no {0}i{1}quemos
no {0}i{1}quéis
no {0}í{1}quen""",
    'es-conj-gar (i-í)':
"""{0}i{1}gar
{0}i{1}gando
{0}i{1}gado
{0}í{1}go
{0}í{1}gas
{0}í{1}ga
{0}i{1}gamos
{0}i{1}gáis
{0}í{1}gan
{0}i{1}gaba
{0}i{1}gabas
{0}i{1}gaba
{0}i{1}gábamos
{0}i{1}gabais
{0}i{1}gaban
{0}i{1}gué
{0}i{1}gaste
{0}i{1}gó
{0}i{1}gamos
{0}i{1}gasteis
{0}i{1}garon
{0}i{1}garé
{0}i{1}garás
{0}i{1}gará
{0}i{1}garemos
{0}i{1}garéis
{0}i{1}garán
{0}i{1}garía
{0}i{1}garías
{0}i{1}garía
{0}i{1}garíamos
{0}i{1}garíais
{0}i{1}garían
{0}í{1}gue
{0}í{1}gues
{0}í{1}gue
{0}i{1}guemos
{0}i{1}guéis
{0}í{1}guen
{0}i{1}gara
{0}i{1}garas
{0}i{1}gara
{0}i{1}gáramos
{0}i{1}garais
{0}i{1}garan
{0}i{1}gase
{0}i{1}gases
{0}i{1}gase
{0}i{1}gásemos
{0}i{1}gaseis
{0}i{1}gasen
{0}i{1}gare
{0}i{1}gares
{0}i{1}gare
{0}i{1}gáremos
{0}i{1}gareis
{0}i{1}garen
{0}í{1}ga
{0}í{1}gue
{0}i{1}guemos
{0}i{1}gad
{0}í{1}guen
no {0}í{1}gues
no {0}í{1}gue
no {0}i{1}guemos
no {0}i{1}guéis
no {0}í{1}guen""",
    'es-conj-iar-ar':
"""{0}iar
{0}iando
{0}iado
{0}ío or {0}io
{0}ías or {0}ias
{0}ía or {0}ia
{0}iamos
{0}iáis
{0}ían or {0}ian
{0}iaba
{0}iabas
{0}iaba
{0}iábamos
{0}iabais
{0}iaban
{0}ié
{0}iaste
{0}ió
{0}iamos
{0}iasteis
{0}iaron
{0}iaré
{0}iarás
{0}iará
{0}iaremos
{0}iaréis
{0}iarán
{0}iaría
{0}iarías
{0}iaría
{0}iaríamos
{0}iaríais
{0}iarían
{0}íe or {0}ie
{0}íes or {0}ies
{0}íe or {0}ie
{0}iemos
{0}iéis
{0}íen or {0}ien
{0}iara
{0}iaras
{0}iara
{0}iáramos
{0}iarais
{0}iaran
{0}iase
{0}iases
{0}iase
{0}iásemos
{0}iaseis
{0}iasen
{0}iare
{0}iares
{0}iare
{0}iáremos
{0}iareis
{0}iaren
{0}ía or {0}ia
{0}íe or {0}ie
{0}iemos
{0}iad
{0}íen or {0}ien
no {0}íes or no {0}ies
no {0}íe or no {0}ie
no {0}iemos
no {0}iéis
no {0}íen or no {0}ien""",
    'es-conj-ir':
"""{0}ir
{0}iendo
{0}ido
{0}o
{0}es
{0}e
{0}imos
{0}ís
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ió
{0}imos
{0}isteis
{0}ieron
{0}iré
{0}irás
{0}irá
{0}iremos
{0}iréis
{0}irán
{0}iría
{0}irías
{0}iría
{0}iríamos
{0}iríais
{0}irían
{0}a
{0}as
{0}a
{0}amos
{0}áis
{0}an
{0}iera
{0}ieras
{0}iera
{0}iéramos
{0}ierais
{0}ieran
{0}iese
{0}ieses
{0}iese
{0}iésemos
{0}ieseis
{0}iesen
{0}iere
{0}ieres
{0}iere
{0}iéremos
{0}iereis
{0}ieren
{0}e
{0}a
{0}amos
{0}id
{0}an
no {0}as
no {0}a
no {0}amos
no {0}áis
no {0}an""",
    'es-conj-ir (c-zc)':
"""{0}cir
{0}ciendo
{0}cido
{0}zco
{0}ces
{0}ce
{0}cimos
{0}cís
{0}cen
{0}cía
{0}cías
{0}cía
{0}cíamos
{0}cíais
{0}cían
{0}cí
{0}ciste
{0}ció
{0}cimos
{0}cisteis
{0}cieron
{0}ciré
{0}cirás
{0}cirá
{0}ciremos
{0}ciréis
{0}cirán
{0}ciría
{0}cirías
{0}ciría
{0}ciríamos
{0}ciríais
{0}cirían
{0}zca
{0}zcas
{0}zca
{0}zcamos
{0}zcáis
{0}zcan
{0}ciera
{0}cieras
{0}ciera
{0}ciéramos
{0}cierais
{0}cieran
{0}ciese
{0}cieses
{0}ciese
{0}ciésemos
{0}cieseis
{0}ciesen
{0}ciere
{0}cieres
{0}ciere
{0}ciéremos
{0}ciereis
{0}cieren
{0}ce
{0}zca
{0}zcamos
{0}cid
{0}zcan
no {0}zcas
no {0}zca
no {0}zcamos
no {0}zcáis
no {0}zcan""",
    'es-conj-ir (e-i)':
"""{0}e{1}ir
{0}i{1}iendo
{0}e{1}ido
{0}i{1}o
{0}i{1}es
{0}i{1}e
{0}e{1}imos
{0}e{1}ís
{0}i{1}en
{0}e{1}ía
{0}e{1}ías
{0}e{1}ía
{0}e{1}íamos
{0}e{1}íais
{0}e{1}ían
{0}e{1}í
{0}e{1}iste
{0}i{1}ió
{0}e{1}imos
{0}e{1}isteis
{0}i{1}ieron
{0}e{1}iré
{0}e{1}irás
{0}e{1}irá
{0}e{1}iremos
{0}e{1}iréis
{0}e{1}irán
{0}e{1}iría
{0}e{1}irías
{0}e{1}iría
{0}e{1}iríamos
{0}e{1}iríais
{0}e{1}irían
{0}i{1}a
{0}i{1}as
{0}i{1}a
{0}i{1}amos
{0}i{1}áis
{0}i{1}an
{0}i{1}iera
{0}i{1}ieras
{0}i{1}iera
{0}i{1}iéramos
{0}i{1}ierais
{0}i{1}ieran
{0}i{1}iese
{0}i{1}ieses
{0}i{1}iese
{0}i{1}iésemos
{0}i{1}ieseis
{0}i{1}iesen
{0}i{1}iere
{0}i{1}ieres
{0}i{1}iere
{0}i{1}iéremos
{0}i{1}iereis
{0}i{1}ieren
{0}i{1}e
{0}i{1}a
{0}i{1}amos
{0}e{1}id
{0}i{1}an
no {0}i{1}as
no {0}i{1}a
no {0}i{1}amos
no {0}i{1}áis
no {0}i{1}an""",
    'es-conj-ir (e-ie-i)':
"""{0}e{1}ir
{0}i{1}iendo
{0}e{1}ido
{0}ie{1}o
{0}ie{1}es
{0}ie{1}e
{0}e{1}imos
{0}e{1}ís
{0}ie{1}en
{0}e{1}ía
{0}e{1}ías
{0}e{1}ía
{0}e{1}íamos
{0}e{1}íais
{0}e{1}ían
{0}e{1}í
{0}e{1}iste
{0}i{1}ió
{0}e{1}imos
{0}e{1}isteis
{0}i{1}ieron
{0}e{1}iré
{0}e{1}irás
{0}e{1}irá
{0}e{1}iremos
{0}e{1}iréis
{0}e{1}irán
{0}e{1}iría
{0}e{1}irías
{0}e{1}iría
{0}e{1}iríamos
{0}e{1}iríais
{0}e{1}irían
{0}ie{1}a
{0}ie{1}as
{0}ie{1}a
{0}i{1}amos
{0}i{1}áis
{0}ie{1}an
{0}i{1}iera
{0}i{1}ieras
{0}i{1}iera
{0}i{1}iéramos
{0}i{1}ierais
{0}i{1}ieran
{0}i{1}iese
{0}i{1}ieses
{0}i{1}iese
{0}i{1}iésemos
{0}i{1}ieseis
{0}i{1}iesen
{0}i{1}iere
{0}i{1}ieres
{0}i{1}iere
{0}i{1}iéremos
{0}i{1}iereis
{0}i{1}ieren
{0}ie{1}e
{0}ie{1}a
{0}i{1}amos
{0}e{1}id
{0}ie{1}an
no {0}ie{1}as
no {0}ie{1}a
no {0}i{1}amos
no {0}i{1}áis
no {0}ie{1}an""",
    'es-conj-ir (i-í)':
"""{0}i{1}ir
{0}i{1}iendo
{0}i{1}ido
{0}í{1}o
{0}í{1}es
{0}í{1}e
{0}i{1}imos
{0}i{1}ís
{0}í{1}en
{0}i{1}ía
{0}i{1}ías
{0}i{1}ía
{0}i{1}íamos
{0}i{1}íais
{0}i{1}ían
{0}i{1}í
{0}i{1}iste
{0}i{1}ió
{0}i{1}imos
{0}i{1}isteis
{0}i{1}ieron
{0}i{1}iré
{0}i{1}irás
{0}i{1}irá
{0}i{1}iremos
{0}i{1}iréis
{0}i{1}irán
{0}i{1}iría
{0}i{1}irías
{0}i{1}iría
{0}i{1}iríamos
{0}i{1}iríais
{0}i{1}irían
{0}í{1}a
{0}í{1}as
{0}í{1}a
{0}i{1}amos
{0}i{1}áis
{0}í{1}an
{0}i{1}iera
{0}i{1}ieras
{0}i{1}iera
{0}i{1}iéramos
{0}i{1}ierais
{0}i{1}ieran
{0}i{1}iese
{0}i{1}ieses
{0}i{1}iese
{0}i{1}iésemos
{0}i{1}ieseis
{0}i{1}iesen
{0}i{1}iere
{0}i{1}ieres
{0}i{1}iere
{0}i{1}iéremos
{0}i{1}iereis
{0}i{1}ieren
{0}í{1}e
{0}í{1}a
{0}i{1}amos
{0}i{1}id
{0}í{1}an
no {0}í{1}as
no {0}í{1}a
no {0}i{1}amos
no {0}i{1}áis
no {0}í{1}an""",
    'es-conj-ir (u-ú)':
"""{0}u{1}ir
{0}u{1}iendo
{0}u{1}ido
{0}ú{1}o
{0}ú{1}es
{0}ú{1}e
{0}u{1}imos
{0}u{1}ís
{0}ú{1}en
{0}u{1}ía
{0}u{1}ías
{0}u{1}ía
{0}u{1}íamos
{0}u{1}íais
{0}u{1}ían
{0}u{1}í
{0}u{1}iste
{0}u{1}ió
{0}u{1}imos
{0}u{1}isteis
{0}u{1}ieron
{0}u{1}iré
{0}u{1}irás
{0}u{1}irá
{0}u{1}iremos
{0}u{1}iréis
{0}u{1}irán
{0}u{1}iría
{0}u{1}irías
{0}u{1}iría
{0}u{1}iríamos
{0}u{1}iríais
{0}u{1}irían
{0}ú{1}a
{0}ú{1}as
{0}ú{1}a
{0}u{1}amos
{0}u{1}áis
{0}ú{1}an
{0}u{1}iera
{0}u{1}ieras
{0}u{1}iera
{0}u{1}iéramos
{0}u{1}ierais
{0}u{1}ieran
{0}u{1}iese
{0}u{1}ieses
{0}u{1}iese
{0}u{1}iésemos
{0}u{1}ieseis
{0}u{1}iesen
{0}u{1}iere
{0}u{1}ieres
{0}u{1}iere
{0}u{1}iéremos
{0}u{1}iereis
{0}u{1}ieren
{0}ú{1}e
{0}ú{1}a
{0}u{1}amos
{0}u{1}id
{0}ú{1}an
no {0}ú{1}as
no {0}ú{1}a
no {0}u{1}amos
no {0}u{1}áis
no {0}ú{1}an""",
    'es-conj-quir':
"""{0}quir
{0}quiendo
{0}quido
{0}co
{0}ques
{0}que
{0}quimos
{0}quís
{0}quen
{0}quía
{0}quías
{0}quía
{0}quíamos
{0}quíais
{0}quían
{0}quí
{0}quiste
{0}quió
{0}quimos
{0}quisteis
{0}quieron
{0}quiré
{0}quirás
{0}quirá
{0}quiremos
{0}quiréis
{0}quirán
{0}quiría
{0}quirías
{0}quiría
{0}quiríamos
{0}quiríais
{0}quirían
{0}ca
{0}cas
{0}ca
{0}camos
{0}cáis
{0}can
{0}quiera
{0}quieras
{0}quiera
{0}quiéramos
{0}quierais
{0}quieran
{0}quiese
{0}quieses
{0}quiese
{0}quiésemos
{0}quieseis
{0}quiesen
{0}quiere
{0}quieres
{0}quiere
{0}quiéremos
{0}quiereis
{0}quieren
{0}que
{0}ca
{0}camos
{0}quid
{0}can
no {0}cas
no {0}ca
no {0}camos
no {0}cáis
no {0}can""",
    'es-conj-uir':
"""{0}uir
{0}uyendo
{0}uido
{0}uyo
{0}uyes
{0}uye
{0}uimos
{0}uís
{0}uyen
{0}uía
{0}uías
{0}uía
{0}uíamos
{0}uíais
{0}uían
{0}uí
{0}uiste
{0}uyó
{0}uimos
{0}uisteis
{0}uyeron
{0}uiré
{0}uirás
{0}uirá
{0}uiremos
{0}uiréis
{0}uirán
{0}uiría
{0}uirías
{0}uiría
{0}uiríamos
{0}uiríais
{0}uirían
{0}uya
{0}uyas
{0}uya
{0}uyamos
{0}uyáis
{0}uyan
{0}uyera
{0}uyeras
{0}uyera
{0}uyéramos
{0}uyerais
{0}uyeran
{0}uyese
{0}uyeses
{0}uyese
{0}uyésemos
{0}uyeseis
{0}uyesen
{0}uyere
{0}uyeres
{0}uyere
{0}uyéremos
{0}uyereis
{0}uyeren
{0}uye
{0}uya
{0}uyamos
{0}uid
{0}uyan
no {0}uyas
no {0}uya
no {0}uyamos
no {0}uyáis
no {0}uyan""",
    'es-conj-zar':
"""{0}zar
{0}zando
{0}zado
{0}zo
{0}zas
{0}za
{0}zamos
{0}záis
{0}zan
{0}zaba
{0}zabas
{0}zaba
{0}zábamos
{0}zabais
{0}zaban
{0}cé
{0}zaste
{0}zó
{0}zamos
{0}zasteis
{0}zaron
{0}zaré
{0}zarás
{0}zará
{0}zaremos
{0}zaréis
{0}zarán
{0}zaría
{0}zarías
{0}zaría
{0}zaríamos
{0}zaríais
{0}zarían
{0}ce
{0}ces
{0}ce
{0}cemos
{0}céis
{0}cen
{0}zara
{0}zaras
{0}zara
{0}záramos
{0}zarais
{0}zaran
{0}zase
{0}zases
{0}zase
{0}zásemos
{0}zaseis
{0}zasen
{0}zare
{0}zares
{0}zare
{0}záremos
{0}zareis
{0}zaren
{0}za
{0}ce
{0}cemos
{0}zad
{0}cen
no {0}ces
no {0}ce
no {0}cemos
no {0}céis
no {0}cen""",
    'es-conj-zar (e-ie)':
"""{0}e{1}zar
{0}e{1}zando
{0}e{1}zado
{0}ie{1}zo
{0}ie{1}zas
{0}ie{1}za
{0}e{1}zamos
{0}e{1}záis
{0}ie{1}zan
{0}e{1}zaba
{0}e{1}zabas
{0}e{1}zaba
{0}e{1}zábamos
{0}e{1}zabais
{0}e{1}zaban
{0}e{1}cé
{0}e{1}zaste
{0}e{1}zó
{0}e{1}zamos
{0}e{1}zasteis
{0}e{1}zaron
{0}e{1}zaré
{0}e{1}zarás
{0}e{1}zará
{0}e{1}zaremos
{0}e{1}zaréis
{0}e{1}zarán
{0}e{1}zaría
{0}e{1}zarías
{0}e{1}zaría
{0}e{1}zaríamos
{0}e{1}zaríais
{0}e{1}zarían
{0}ie{1}ce
{0}ie{1}ces
{0}ie{1}ce
{0}e{1}cemos
{0}e{1}céis
{0}ie{1}cen
{0}e{1}zara
{0}e{1}zaras
{0}e{1}zara
{0}e{1}záramos
{0}e{1}zarais
{0}e{1}zaran
{0}e{1}zase
{0}e{1}zases
{0}e{1}zase
{0}e{1}zásemos
{0}e{1}zaseis
{0}e{1}zasen
{0}e{1}zare
{0}e{1}zares
{0}e{1}zare
{0}e{1}záremos
{0}e{1}zareis
{0}e{1}zaren
{0}ie{1}za
{0}ie{1}ce
{0}e{1}cemos
{0}e{1}zad
{0}ie{1}cen
no {0}ie{1}ces
no {0}ie{1}ce
no {0}e{1}cemos
no {0}e{1}céis
no {0}ie{1}cen""",
    'es-conj-zar (go-güe)':
"""{0}go{1}zar
{0}go{1}zando
{0}go{1}zado
{0}güe{1}zo
{0}güe{1}zas
{0}güe{1}za
{0}go{1}zamos
{0}go{1}záis
{0}güe{1}zan
{0}go{1}zaba
{0}go{1}zabas
{0}go{1}zaba
{0}go{1}zábamos
{0}go{1}zabais
{0}go{1}zaban
{0}go{1}cé
{0}go{1}zaste
{0}go{1}zó
{0}go{1}zamos
{0}go{1}zasteis
{0}go{1}zaron
{0}go{1}zaré
{0}go{1}zarás
{0}go{1}zará
{0}go{1}zaremos
{0}go{1}zaréis
{0}go{1}zarán
{0}go{1}zaría
{0}go{1}zarías
{0}go{1}zaría
{0}go{1}zaríamos
{0}go{1}zaríais
{0}go{1}zarían
{0}güe{1}ce
{0}güe{1}ces
{0}güe{1}ce
{0}go{1}cemos
{0}go{1}céis
{0}güe{1}cen
{0}go{1}zara
{0}go{1}zaras
{0}go{1}zara
{0}go{1}záramos
{0}go{1}zarais
{0}go{1}zaran
{0}go{1}zase
{0}go{1}zases
{0}go{1}zase
{0}go{1}zásemos
{0}go{1}zaseis
{0}go{1}zasen
{0}go{1}zare
{0}go{1}zares
{0}go{1}zare
{0}go{1}záremos
{0}go{1}zareis
{0}go{1}zaren
{0}güe{1}za
{0}güe{1}ce
{0}go{1}cemos
{0}go{1}zad
{0}güe{1}cen
no {0}güe{1}ces
no {0}güe{1}ce
no {0}go{1}cemos
no {0}go{1}céis
no {0}güe{1}cen""",
    'es-conj-zar (o-ue)':
"""{0}o{1}zar
{0}o{1}zando
{0}o{1}zado
{0}ue{1}zo
{0}ue{1}zas
{0}ue{1}za
{0}o{1}zamos
{0}o{1}záis
{0}ue{1}zan
{0}o{1}zaba
{0}o{1}zabas
{0}o{1}zaba
{0}o{1}zábamos
{0}o{1}zabais
{0}o{1}zaban
{0}o{1}cé
{0}o{1}zaste
{0}o{1}zó
{0}o{1}zamos
{0}o{1}zasteis
{0}o{1}zaron
{0}o{1}zaré
{0}o{1}zarás
{0}o{1}zará
{0}o{1}zaremos
{0}o{1}zaréis
{0}o{1}zarán
{0}o{1}zaría
{0}o{1}zarías
{0}o{1}zaría
{0}o{1}zaríamos
{0}o{1}zaríais
{0}o{1}zarían
{0}ue{1}ce
{0}ue{1}ces
{0}ue{1}ce
{0}o{1}cemos
{0}o{1}céis
{0}ue{1}cen
{0}o{1}zara
{0}o{1}zaras
{0}o{1}zara
{0}o{1}záramos
{0}o{1}zarais
{0}o{1}zaran
{0}o{1}zase
{0}o{1}zases
{0}o{1}zase
{0}o{1}zásemos
{0}o{1}zaseis
{0}o{1}zasen
{0}o{1}zare
{0}o{1}zares
{0}o{1}zare
{0}o{1}záremos
{0}o{1}zareis
{0}o{1}zaren
{0}ue{1}za
{0}ue{1}ce
{0}o{1}cemos
{0}o{1}zad
{0}ue{1}cen
no {0}ue{1}ces
no {0}ue{1}ce
no {0}o{1}cemos
no {0}o{1}céis
no {0}ue{1}cen""",
    'es-conj-ñir':
"""{0}ir
{0}endo
{0}ido
{0}o
{0}es
{0}e
{0}imos
{0}ís
{0}en
{0}ía
{0}ías
{0}ía
{0}íamos
{0}íais
{0}ían
{0}í
{0}iste
{0}ó
{0}imos
{0}isteis
{0}eron
{0}iré
{0}irás
{0}irá
{0}iremos
{0}iréis
{0}irán
{0}iría
{0}irías
{0}iría
{0}iríamos
{0}iríais
{0}irían
{0}a
{0}as
{0}a
{0}amos
{0}áis
{0}an
{0}era
{0}eras
{0}era
{0}éramos
{0}erais
{0}eran
{0}ese
{0}eses
{0}ese
{0}ésemos
{0}eseis
{0}esen
{0}ere
{0}eres
{0}ere
{0}éremos
{0}ereis
{0}eren
{0}e
{0}a
{0}amos
{0}id
{0}an
no {0}as
no {0}a
no {0}amos
no {0}áis
no {0}an""",
    'es-conj-ñir (e-i)':
"""{0}e{1}ñir
{0}i{1}ñendo
{0}e{1}ñido
{0}i{1}ño
{0}i{1}ñes
{0}i{1}ñe
{0}e{1}ñimos
{0}e{1}ñís
{0}i{1}ñen
{0}e{1}ñía
{0}e{1}ñías
{0}e{1}ñía
{0}e{1}ñíamos
{0}e{1}ñíais
{0}e{1}ñían
{0}e{1}ñí
{0}e{1}ñiste
{0}i{1}ñó
{0}e{1}ñimos
{0}e{1}ñisteis
{0}i{1}ñeron
{0}e{1}ñiré
{0}e{1}ñirás
{0}e{1}ñirá
{0}e{1}ñiremos
{0}e{1}ñiréis
{0}e{1}ñirán
{0}e{1}ñiría
{0}e{1}ñirías
{0}e{1}ñiría
{0}e{1}ñiríamos
{0}e{1}ñiríais
{0}e{1}ñirían
{0}i{1}ña
{0}i{1}ñas
{0}i{1}ña
{0}i{1}ñamos
{0}i{1}ñáis
{0}i{1}ñan
{0}i{1}ñera
{0}i{1}ñeras
{0}i{1}ñera
{0}i{1}ñéramos
{0}i{1}ñerais
{0}i{1}ñeran
{0}i{1}ñese
{0}i{1}ñeses
{0}i{1}ñese
{0}i{1}ñésemos
{0}i{1}ñeseis
{0}i{1}ñesen
{0}i{1}ñere
{0}i{1}ñeres
{0}i{1}ñere
{0}i{1}ñéremos
{0}i{1}ñereis
{0}i{1}ñeren
{0}i{1}ñe
{0}i{1}ña
{0}i{1}ñamos
{0}e{1}ñid
{0}i{1}ñan
no {0}i{1}ñas
no {0}i{1}ña
no {0}i{1}ñamos
no {0}i{1}ñáis
no {0}i{1}ñan"""

}


if __name__ == "__main__":
# a little test to check if all templates have same amount of elements, which is key

    for template, string in templates.items():
        print(len(string.replace('\n\n','\n').split('\n')), template)
