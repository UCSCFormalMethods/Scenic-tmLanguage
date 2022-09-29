a = R"""
multiline "raw" string \

    \xf1 \u1234aaaa \U1234aaaa

    \N{BLACK SPADE SUIT}
"""



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
multiline "raw" string  : source.scenic, string.quoted.raw.multi.scenic
\             : source.scenic, string.quoted.raw.multi.scenic
              : source.scenic, string.quoted.raw.multi.scenic
    \xf1 \u1234aaaa \U1234aaaa : source.scenic, string.quoted.raw.multi.scenic
              : source.scenic, string.quoted.raw.multi.scenic
    \N        : source.scenic, string.quoted.raw.multi.scenic
{BLACK SPADE SUIT} : source.scenic, string.quoted.raw.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.multi.scenic
