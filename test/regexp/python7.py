a = r'('
1

a = r"(?="
1

a = r"""(?:
"""
1

a = r'''[
'''
1



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
(             : punctuation.parenthesis.begin.regexp, source.scenic, string.regexp.quoted.single.scenic, support.other.parenthesis.regexp
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
(             : keyword.operator.lookahead.regexp, punctuation.parenthesis.lookahead.begin.regexp, source.scenic, string.regexp.quoted.single.scenic
?=            : keyword.operator.lookahead.regexp, source.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
(?:           : punctuation.parenthesis.non-capturing.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
"""           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
1             : constant.numeric.dec.scenic, source.scenic
