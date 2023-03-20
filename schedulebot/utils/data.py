import os

import numpy as np
import pandas as pd


def reversed4(variable):
    res = ''.join(reversed(variable))
    return res


def parse_subject_name(x):
    qualification_types = ["professor", "assistant"]

    teachers_name = x
    qualification_type = ""
    if any(qualification_type in x for qualification_type in qualification_types):
        parts = x.split(" ", -1)
        teachers_name = parts[0] + " " + parts[1]
        qualification_type = parts[-1]

    return (teachers_name, qualification_type)


CURRENT_DPATH = os.path.dirname(os.path.abspath("__file__"))
DATA_DPATH = os.path.join(CURRENT_DPATH, "data")
data_version = '2023-02-26'
src_dpath = os.path.join(DATA_DPATH, data_version)
fpath = os.path.join(src_dpath, "Teachers+Lessons.csv")
bd = pd.read_csv(fpath, index_col=0)

parsed_teachers_name = bd['TEACHERS'].apply(parse_subject_name).tolist()
parsed_teachers_name = np.array(parsed_teachers_name).reshape(-1, 2)

bd['name'] = parsed_teachers_name[:, 0]
bd['qualification'] = parsed_teachers_name[:, 1]

print(bd.head())
