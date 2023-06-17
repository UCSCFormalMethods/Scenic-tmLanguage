match point:
    case Point(x, y) if x == y:
        print(f"The point is located on the diagonal Y=X.")
    case Point(x, y):
        print(f"Point is not on the diagonal.")




match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
point         : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
if            : keyword.control.flow.scenic, source.scenic
              : source.scenic
x             : source.scenic
              : source.scenic
==            : keyword.operator.comparison.scenic, source.scenic
              : source.scenic
y             : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
The point is located on the diagonal Y=X. : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
Point is not on the diagonal. : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
