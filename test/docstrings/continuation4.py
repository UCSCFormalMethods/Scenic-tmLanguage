    # not a docstring
    a = \
    r'''
    >>> print(42)
    a[wer]
    '''

    b = \
    # docstring
    r'''
    >>> print()
    a[wer]
    '''



              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 not a docstring : comment.line.number-sign.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
    >>> print : source.scenic, string.regexp.quoted.multi.scenic
(             : punctuation.parenthesis.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
42            : source.scenic, string.regexp.quoted.multi.scenic
)             : punctuation.parenthesis.end.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
    a         : source.scenic, string.regexp.quoted.multi.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
w             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
e             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
r             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 docstring    : comment.line.number-sign.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.multi.scenic
              : source.scenic, string.quoted.docstring.raw.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.raw.multi.scenic
print()       : source.scenic, string.quoted.docstring.raw.multi.scenic
    a[wer]    : source.scenic, string.quoted.docstring.raw.multi.scenic
              : source.scenic, string.quoted.docstring.raw.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.multi.scenic
