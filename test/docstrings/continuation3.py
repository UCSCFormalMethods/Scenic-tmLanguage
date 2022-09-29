# not a docstring
a = \
r'>>> print(42)a[wer]'

b = \
# docstring
r'>>> print()a[wer]'



#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 not a docstring : comment.line.number-sign.scenic, source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
>>> print     : source.scenic, string.regexp.quoted.single.scenic
(             : punctuation.parenthesis.begin.regexp, source.scenic, string.regexp.quoted.single.scenic, support.other.parenthesis.regexp
42            : source.scenic, string.regexp.quoted.single.scenic
)             : punctuation.parenthesis.end.regexp, source.scenic, string.regexp.quoted.single.scenic, support.other.parenthesis.regexp
a             : source.scenic, string.regexp.quoted.single.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.single.scenic
w             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
e             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
r             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 docstring    : comment.line.number-sign.scenic, source.scenic
r             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
>>> print()a[wer] : source.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
