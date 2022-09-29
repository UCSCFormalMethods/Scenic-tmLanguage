a = r"foo#not a comment"
a = r"""
    (?x)        # multi-line regexp
        foo     # comment
"""
a = R"""
    (?x)        # not a
        foo     # comment
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
foo#not a comment : source.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 multi-line regexp : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
        foo      : source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 comment      : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
    (?x)        # not a : source.scenic, string.quoted.raw.multi.scenic
        foo     # comment : source.scenic, string.quoted.raw.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.multi.scenic
