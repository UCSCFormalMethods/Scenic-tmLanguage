match points:
    case []:
        print("No points in the list.")
    case [Point(0, 0)]:
        print("The origin is the only point in the list.")
    case [Point(x, y)]:
        print(f"A single point is in the list.")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two points on the Y axis are in the list.")
    case _:
        print("Something else is found in the list.")



match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
points        : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
No points in the list. : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
The origin is the only point in the list. : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
x             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
A single point is in the list. : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y1            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
Point         : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
0             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
y2            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
Two points on the Y axis are in the list. : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
_             : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
Something else is found in the list. : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
