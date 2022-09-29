a = r'foo[^]'
a = r'foo[]'


a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
foo           : source.scenic, string.regexp.quoted.single.scenic
[^]           : source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
foo           : source.scenic, string.regexp.quoted.single.scenic
[]            : source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
