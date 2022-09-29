a = r"""
    (?x)        # multi-XXXline XXX regexp
        foo     (?# comm TODOent TODO)
        foo     # type: int
        foo     (?# type: int)
"""



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
 multi-XXXline  : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
XXX           : comment.line.number-sign.scenic, keyword.codetag.notation.scenic, source.scenic, string.regexp.quoted.multi.scenic
 regexp       : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
        foo      : source.scenic, string.regexp.quoted.multi.scenic
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
 comm TODOent  : comment.regexp, source.scenic, string.regexp.quoted.multi.scenic
TODO          : comment.regexp, keyword.codetag.notation.scenic, source.scenic, string.regexp.quoted.multi.scenic
)             : comment.regexp, punctuation.comment.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
        foo      : source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 type: int    : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
        foo      : source.scenic, string.regexp.quoted.multi.scenic
(?#           : comment.regexp, punctuation.comment.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
 type: int    : comment.regexp, source.scenic, string.regexp.quoted.multi.scenic
)             : comment.regexp, punctuation.comment.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
