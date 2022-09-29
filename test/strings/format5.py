a = 'qqq{0:{width}{base}}www'
a = 'qqq{0:$20}www'
a = 'qqq{0}www'




a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
qqq           : source.scenic, string.quoted.single.scenic
{0            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
:             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
{width}{base}} : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
www           : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
qqq           : source.scenic, string.quoted.single.scenic
{0            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
:             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
$20}          : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
www           : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
qqq           : source.scenic, string.quoted.single.scenic
{0}           : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
www           : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
