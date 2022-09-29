a = r'
    (?x)
        foo
'
# comment



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
              : invalid.illegal.newline.scenic, source.scenic, string.regexp.quoted.single.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
?             : invalid.illegal.operator.scenic, source.scenic
x             : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
              : source.scenic
foo           : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
              : invalid.illegal.newline.scenic, source.scenic, string.quoted.docstring.single.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 comment      : comment.line.number-sign.scenic, source.scenic
