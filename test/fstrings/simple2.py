a = f"normal {{ normal }} normal } {10!r} normal {fo.__add__!s}"




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
normal        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{{            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
 normal       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
}}            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
 normal       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
}             : invalid.illegal.brace.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
10            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
!r            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
 normal       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
fo            : meta.fstring.scenic, source.scenic
.             : meta.fstring.scenic, meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
__add__       : meta.fstring.scenic, meta.member.access.scenic, source.scenic, support.function.magic.scenic
!s            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
"             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
