a = b"""
multiline "binary" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.multi.scenic
multiline "binary" string  : source.scenic, string.quoted.binary.multi.scenic
\             : constant.language.scenic, source.scenic, string.quoted.binary.multi.scenic
              : source.scenic, string.quoted.binary.multi.scenic
              : source.scenic, string.quoted.binary.multi.scenic
\xf1          : constant.character.escape.scenic, source.scenic, string.quoted.binary.multi.scenic
 \u1234aaaa \U1234aaaa : source.scenic, string.quoted.binary.multi.scenic
              : source.scenic, string.quoted.binary.multi.scenic
    \N{BLACK SPADE SUIT} : source.scenic, string.quoted.binary.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.multi.scenic
