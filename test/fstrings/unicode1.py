a = f"""
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
multiline "unicode" string  : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\             : constant.language.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\xf1          : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\u1234        : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
aaaa          : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\U1234aaaa    : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
\N{BLACK SPADE SUIT} : constant.character.escape.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
