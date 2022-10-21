import re

from simplemma import simplemma


class Static:
    finds_r1 = ""
    finds_r2 = ""
    finds_r3 = ""


# R1
def R1_type(text):
    ret = ""
    finds_r1 = re.findall("\\b(\\w+)(?:\\W+\\1\\b)+", text)
    Static.finds_r1 = finds_r1
    for find in finds_r1:
        ret = ret + " R1"
    return ret


# R2
def R2_type(text):
    ret = ""
    text_n = re.sub("[aàeèéiíoòóuú]", "A", text)
    finds_r2 = re.findall("\\b(\\w+)\\s+\\1\\b", text_n)
    Static.finds_r2 = finds_r2
    if len(finds_r2) < len(Static.finds_r1):
        a = len(Static.finds_r1)
        b = len(finds_r2)
    else:
        a = len(finds_r2)
        b = len(Static.finds_r1)

    for find in range(int(a - b)):
        ret = ret + " R2"
    return ret


# R3
def R3_type(text):
    ret = ""
    finds_r3 = re.findall("\\b(\\w+)(\\W(\\w+)?(\\s\\w+\\s?)?\\s)+(\\1\\b)", text)
    Static.finds_r3 = finds_r3
    for find in finds_r3:
        ret = ret + " R3"
    return ret


# R4
def R4_type(text):
    ret = ""
    text_l = text.split(" ")
    text_l = filter(None, text_l)
    text_lem = ""
    for mot in text_l:
        lemma = simplemma.lemmatize(mot, lang='ca')
        text_lem = text_lem+" "+lemma
    finds_r4 = re.findall("\\b(\\w+)(?:\\W+\\1\\b)+", text)
    for find in finds_r4:
        ret = ret + " R4"
    return ret

# I1
def I1_type(text):
    ret = ""
    interjections = ["adéu", "adéu siau", "ah", "ai", "alerta", "alto", "al·leluia", "alça", "amén", "apa", "arri",
                     "arruix", "au", "bah", "bravo", "bufa", "ca", "caram", "carat", "caratxos", "cavall", "cordons",
                     "ec", "ecs", "eh", "ehem", "ei", "eia", "ela", "elis", "ell", "ep", "eureka", "fosca", "ha",
                     "hala", "hem", "hola", "hosanna", "hum", "hurra", "jas", "jau", "jesús", "malviatge", "manoi",
                     "mau", "moixoni", "nyiclis", "o", "oh", "oi", "oidà", "oixque", "ollaó", "redéu", "renoi", "salve",
                     "tafoi", "tat", "uf", "ui", "uix", "up", "vaja", "vatua", "visca", "xe", "xec", "àngela", "òndia"]
    for interjection in interjections:
        if re.findall("\\b" + interjection + "\\b", text):
            ret = ret + " I1"
    return ret


# I2
def I2_type(text):
    ret = ""
    interjections = []
    for interjection in interjections:
        if re.findall("\\b" + interjection + "\\b", text):
            ret = ret + " I2"
    return ret


# A

# ALL
def get_them_all(text):
    ret = ""
    ret = ret + R1_type(text)
    ret = ret + R2_type(text)
    ret = ret + R3_type(text)
    ret = ret + R4_type(text)
    ret = ret + I1_type(text)
    ret = ret + I2_type(text)
    #ret = ret + A_type(text)
    return ret

# # prova
# text = "ah en joanet camina qui més camina arriba i nyam nyam patim patum forçat forçat oh i llavors li diu ves camina qui caminaràs i pensa qui pensava"
# print(R1_type(text))
# print(R2_type(text))
# print(R3_type(text))
# print(R4_type(text))
#
# print(I1_type(text))
