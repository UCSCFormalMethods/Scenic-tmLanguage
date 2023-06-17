while chunk := file.read(8192):
   process(chunk)
   y0 = (y1 := f(x))



while         : keyword.control.flow.scenic, source.scenic
              : source.scenic
chunk         : source.scenic
              : source.scenic
:=            : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
file          : source.scenic, variable.legacy.builtin.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
read          : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
8192          : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
)             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
process       : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
chunk         : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
y0            : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
y1            : source.scenic
              : source.scenic
:=            : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
f             : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
