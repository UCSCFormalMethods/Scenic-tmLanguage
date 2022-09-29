a = """
multiline "unicode" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.multi.scenic
multiline "unicode" string  : source.scenic, string.quoted.multi.scenic
\             : constant.language.scenic, source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
\xf1          : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
\u1234        : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
aaaa          : source.scenic, string.quoted.multi.scenic
\U1234aaaa    : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
\N{BLACK SPADE SUIT} : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.multi.scenic
