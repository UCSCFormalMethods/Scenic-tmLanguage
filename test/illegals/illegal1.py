->
def f(): pass
$
?
a=$('.class').fuuuu(baz=1)
# we recover just fine
b = !some_ruby?
# hey ;)




->            : invalid.illegal.annotation.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
f             : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
$             : invalid.illegal.operator.scenic, source.scenic
?             : invalid.illegal.operator.scenic, source.scenic
a             : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
$             : invalid.illegal.operator.scenic, source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
.class        : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
fuuuu         : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
baz           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
)             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 we recover just fine : comment.line.number-sign.scenic, source.scenic
b             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
!             : invalid.illegal.operator.scenic, source.scenic
some_ruby     : source.scenic
?             : invalid.illegal.operator.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 hey ;)       : comment.line.number-sign.scenic, source.scenic
