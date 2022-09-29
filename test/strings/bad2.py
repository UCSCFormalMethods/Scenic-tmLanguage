a = b"bad \\ string
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"

def foo(a=1): pass




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
bad           : source.scenic, string.quoted.binary.single.scenic
\\            : constant.character.escape.scenic, source.scenic, string.quoted.binary.single.scenic
 string       : source.scenic, string.quoted.binary.single.scenic
              : invalid.illegal.newline.scenic, source.scenic, string.quoted.binary.single.scenic
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
