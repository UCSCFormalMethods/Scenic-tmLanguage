a = r"bad string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass # doesn't break!



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
bad string    : source.scenic, string.regexp.quoted.single.scenic
              : invalid.illegal.newline.scenic, source.scenic, string.regexp.quoted.single.scenic
foo           : source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005" : invalid.illegal.line.continuation.scenic, source.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 doesn't break! : comment.line.number-sign.scenic, source.scenic
