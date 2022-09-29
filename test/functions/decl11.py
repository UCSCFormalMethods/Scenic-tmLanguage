# testing annotations split over multiple lines
def foo(a:('abc' 'def')==123, boo: 'abc'

                         'def' == foo(n(m=0)))



#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 testing annotations split over multiple lines : comment.line.number-sign.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.parenthesis.begin.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
abc           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
def           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.parenthesis.end.scenic, source.scenic
==            : keyword.operator.comparison.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
123           : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
boo           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
abc           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
                          : meta.function.parameters.scenic, meta.function.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
def           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
==            : keyword.operator.comparison.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
foo           : meta.function-call.generic.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
(             : meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
n             : meta.function-call.arguments.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
m             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.end.scenic, source.scenic
)             : meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.end.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
