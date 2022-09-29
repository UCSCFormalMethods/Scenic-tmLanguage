a = rf'fo{{{2}}}'
a = rf'fo{{{bar}}}'
a = rf'fo{{2}}'





a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{{            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{2}           : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
}}            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{{            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{bar}         : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
}}            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{{2}}         : keyword.operator.quantifier.regexp, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
