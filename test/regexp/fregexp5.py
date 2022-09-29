a = rf'{{foo}}'
a = r'\{foo\}'




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{{            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
foo           : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
}}            : constant.character.escape.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
\{            : constant.character.escape.regexp, source.scenic, string.regexp.quoted.single.scenic
foo           : source.scenic, string.regexp.quoted.single.scenic
\}            : constant.character.escape.regexp, source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
