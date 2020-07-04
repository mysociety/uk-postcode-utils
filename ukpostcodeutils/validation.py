from functools import partial
import re

PARTS = {
    'fst': 'ABCDEFGHIJKLMNOPRSTUWYZ',
    'sec': 'ABCDEFGHKLMNOPQRSTUVWXY',
    'thd': 'ABCDEFGHJKPSTUW',
    'fth': 'ABEHMNPRVWXY',
    'inward': 'ABDEFGHJLNPQRSTUWXYZ',
}

FULL_MATCH_REGEX = re.compile('|'.join([r.format(**PARTS) for r in (
    r'^[{fst}][1-9]\d[{inward}][{inward}]$',
    r'^[{fst}][1-9]\d\d[{inward}][{inward}]$',
    r'^[{fst}][{sec}]\d\d[{inward}][{inward}]$',
    r'^[{fst}][{sec}][1-9]\d\d[{inward}][{inward}]$',
    r'^[{fst}][1-9][{thd}]\d[{inward}][{inward}]$',
    r'^[{fst}][{sec}][1-9][{fth}]\d[{inward}][{inward}]$',
)]))

PARTIAL_MATCH_REGEX = re.compile('|'.join([r.format(**PARTS) for r in (
    r'^[{fst}][1-9]$',
    r'^[{fst}][1-9]\d$',
    r'^[{fst}][{sec}]\d$',
    r'^[{fst}][{sec}][1-9]\d$',
    r'^[{fst}][1-9][{thd}]$',
    r'^[{fst}][{sec}][1-9][{fth}]$',
)]))

del PARTS


def _match_postcode(regex, pc, extra_postcodes=()):
    if pc in extra_postcodes:
        return True
    return regex.match(pc) is not None


is_valid_postcode = partial(_match_postcode, FULL_MATCH_REGEX)
is_valid_partial_postcode = partial(_match_postcode, PARTIAL_MATCH_REGEX)
