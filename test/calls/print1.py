print "is", 2*2
print("is", 2*2)
print x,
print(x, end=" ")
print
print()
print >>sys.stderr, "er"
print("er", file=sys.stderr)
print (x, y)
print((x, y))




print         : source.scenic, support.function.builtin.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
is            : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
2             : constant.numeric.dec.scenic, source.scenic
*             : keyword.operator.arithmetic.scenic, source.scenic
2             : constant.numeric.dec.scenic, source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
is            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
*             : keyword.operator.arithmetic.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
print         : source.scenic, support.function.builtin.scenic
              : source.scenic
x             : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
end           : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
print         : source.scenic, support.function.builtin.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
print         : source.scenic, support.function.builtin.scenic
              : source.scenic
>>            : keyword.operator.bitwise.scenic, source.scenic
sys           : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
stderr        : meta.attribute.scenic, meta.member.access.scenic, source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
er            : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
er            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
file          : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
sys           : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
.             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
stderr        : meta.attribute.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
              : meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.parenthesis.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.element.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.parenthesis.end.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
