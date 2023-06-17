rf'fo{2}'
rf"fo{2}"
rf'''fo{2}'''
rf"""fo{2}"""




rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
"             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
"             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.single.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
rf            : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
fo            : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.raw.multi.scenic
