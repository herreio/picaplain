from . import translations


def translate(code, db):
    if isinstance(code, str) \
            and isinstance(db, dict) \
            and code in db:
        return db[code]


def translate_ilns_system_flag(flag):
    return translate(flag, translations.ILN_SYSTEM_FLAG)


def translate_collection_code(code):
    return translate(code, translations.COLLECTION_CODE)


def translate_url_producer_type(code):
    return translate(code, translations.URL_PRODUCER_TYPE)


def translate_url_license_code(code):
    return translate(code, translations.URL_LICENSE_CODE)


def translate_url_origin_code(code):
    return translate(code, translations.URL_ORIGIN_CODE)


def translate_lending_indicator_gbv(indicator):
    return translate(indicator, translations.LENDING_INDICATOR_GBV)


def translate_lending_indicator_swb(indicator):
    return translate(indicator, translations.LENDING_INDICATOR_SWB)


def translate_interlibrary_loan_indicator_pos1(indicator):
    return translate(indicator, translations.INTERLIBRARY_LOAN_INDICATOR_POS1_SWB)


def translate_interlibrary_loan_indicator_pos2(indicator):
    return translate(indicator, translations.INTERLIBRARY_LOAN_INDICATOR_POS2_SWB)
