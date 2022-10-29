import re


def get_field(key, data, repeat=True):
    found = None
    if repeat:
        found = []
    for row in data:
        if row.startswith(key):
            if repeat:
                found.append(row)
            else:
                return row
    if repeat and len(found) > 0:
        return found


def get_subfield(key, field, repeat=True):
    field_pattern = "\${0}([^$]*)".format(key)
    if repeat:
        return re.findall(field_pattern, field) or None
    found = re.search(field_pattern, field)
    if found:
        found = found.group()
        if found:
            return found.replace("${0}".format(key), "") or None
