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
