a = r'[a-z]'
a = R'[a-z]'



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.single.scenic
a             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
-             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
z             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.single.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
[a-z]         : source.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.single.scenic
