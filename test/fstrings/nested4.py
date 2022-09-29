f"""result: {value:{60}.{16!s:2}{'qwerty'
[2]}}"""
def foo(): pass




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
result:       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
value         : meta.fstring.scenic, source.scenic
:             : meta.fstring.scenic, source.scenic, storage.type.format.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
60            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
.             : meta.fstring.scenic, source.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
16            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
!s            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
:2            : meta.fstring.scenic, source.scenic, storage.type.format.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
qwerty        : meta.fstring.scenic, source.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
[             : meta.fstring.scenic, punctuation.definition.list.begin.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
]             : meta.fstring.scenic, punctuation.definition.list.end.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
