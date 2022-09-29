# testing annotations split over multiple lines
def __init__(self, a:('abc' 'def')=123, boo: 'abc'

                         'def' = foo(n(m=0), baz=
                            13)) -> 123 : 123



#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 testing annotations split over multiple lines : comment.line.number-sign.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
__init__      : meta.function.scenic, source.scenic, support.function.magic.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
self          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.self.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
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
=             : keyword.operator.assignment.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
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
=             : keyword.operator.assignment.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
foo           : meta.function-call.generic.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
(             : meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
n             : meta.function-call.arguments.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
m             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.end.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
baz           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
                             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
13            : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function-call.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.arguments.end.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
              : meta.function.scenic, source.scenic
->            : meta.function.scenic, punctuation.separator.annotation.result.scenic, source.scenic
              : meta.function.scenic, source.scenic
123           : constant.numeric.dec.scenic, meta.function.scenic, source.scenic
              : meta.function.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
123           : constant.numeric.dec.scenic, source.scenic
