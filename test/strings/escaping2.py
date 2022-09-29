replace = {'"' : R'\"',
           "'" : R'\'',
           '\\': R'\\'}



replace       : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
"             : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
\"            : source.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
'             : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
\'            : source.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
\\            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
\\            : source.scenic, string.quoted.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.single.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
