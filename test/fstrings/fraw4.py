a = rf'fo{{{2}}}'
a = rf'fo{{{bar}}}'
a = rf'fo{{2}}'





a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
{{            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
}}            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
{{            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
bar           : meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
}}            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
{{            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
2             : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
}}            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
