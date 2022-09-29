a++
b--
++a
--b
a++c
c--b
a(--a)



a             : source.scenic
++            : invalid.illegal.operator.scenic, source.scenic
b             : source.scenic
--            : invalid.illegal.operator.scenic, source.scenic
++            : invalid.illegal.operator.scenic, source.scenic
a             : source.scenic
--            : invalid.illegal.operator.scenic, source.scenic
b             : source.scenic
a             : source.scenic
++            : invalid.illegal.operator.scenic, source.scenic
c             : source.scenic
c             : source.scenic
--            : invalid.illegal.operator.scenic, source.scenic
b             : source.scenic
a             : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
--            : invalid.illegal.operator.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
a             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
