import csv
import re

import get_expressives


def parse_data(file):
    results = file
    data = list()
    with open(results, 'r+', encoding='utf-8') as csvfile:  # obre el document de resultats
        cap = csvfile.readline()
        data.append(cap.split(";"))  # desa la capçalera a la llista "data"
        reader = csv.reader(csvfile, delimiter=";")  # llegeix cada fila del csv
        for row in reader:  # per a cada fila fes el següent:
            rows = list(row)  # converteix cada fila a una llista
            data.append(rows)  # afegeix la fila-llista a la llista general
            text = rows[2]  # selecciona el text brut
            text_net = re.sub("[\.\[,:;\-—!\?¿'\"«»’]", "", text).lower()  # neteja'l
            word_n = len(text_net.split(" "))  # compta quantes paraules té
            rows.insert(3, text_net)  # desa el número de paraules
            rows.insert(11, word_n)  # mira la durada del segment
            srate = int(word_n) / float(
                rows[10].replace(',', '.'))  # calcula l'speech rate nombre de paraules / durada del segment
            rows.insert(12, str(srate).replace('.', ','))  # desa'l
        csvfile.close()  # tanca el doc original
    return data


def collect_data(data):
    for row in data:
        if row[3] != "":
            expressive = get_expressives.get_them_all(row[3])
            row.append(expressive)
        else:
            pass
    return (data)


def write_data(data, results_py):
    with open(results_py, "w", encoding="utf-8") as csvfile_py:  # crea un nou csv
        write = csv.writer(csvfile_py, delimiter=";", lineterminator="\n")  # formata'l
        write.writerows(data)  # escriu-hi els resultats
        csvfile_py.close()  # tanca'l
