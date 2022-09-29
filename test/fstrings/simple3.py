a = f'hello { foo("bar")/23 !r:f} times'




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
hello         : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
foo           : meta.fstring.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
bar           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
/             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, source.scenic
23            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
!r            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
:f            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
 times        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
