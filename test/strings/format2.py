a = "normal {{ normal }} normal {10!r} normal {fo.__add__!s}".format(fo=1)




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
normal        : source.scenic, string.quoted.single.scenic
{{            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
 normal       : source.scenic, string.quoted.single.scenic
}}            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
 normal       : source.scenic, string.quoted.single.scenic
{10           : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
!r            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
 normal       : source.scenic, string.quoted.single.scenic
{fo.__add__   : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
!s            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
format        : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
fo            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
)             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
