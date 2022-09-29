f'foo {{{bar}}}'




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
foo           : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{{            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
bar           : meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
}}            : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
