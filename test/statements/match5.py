match command.split() if command else ['default']:
    ... # Other cases
    case ["north"] | ["go", "north"]:
        ... # handle case
    case ["get", obj] | ["pick", "up", *other] | ["pick", obj, "up"]:
        ... # handle case




match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
command       : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
split         : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
if            : keyword.control.flow.scenic, source.scenic
              : source.scenic
command       : source.scenic
              : source.scenic
else          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
default       : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 Other cases  : comment.line.number-sign.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
north         : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
              : source.scenic
|             : keyword.operator.bitwise.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
go            : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
north         : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 handle case  : comment.line.number-sign.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
get           : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
obj           : source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
              : source.scenic
|             : keyword.operator.bitwise.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
pick          : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
up            : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
*             : keyword.operator.arithmetic.scenic, source.scenic
other         : source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
              : source.scenic
|             : keyword.operator.bitwise.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
pick          : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
obj           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
up            : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 handle case  : comment.line.number-sign.scenic, source.scenic
