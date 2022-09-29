a = f"""
multiline "unicode" string
    \N{BLACK SPADE SUIT} {foo+2}
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
multiline "unicode" string : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\N{BLACK SPADE SUIT} : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
foo           : meta.fstring.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
