a = 'blah {foo-bar %d'
a = 'blah {foo-bar %d}'
a = 'blah {foo-bar %d //insane {}}'
a = '{}blah {foo-bar %d //insane {}}'



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
blah {foo-bar  : source.scenic, string.quoted.single.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
blah          : source.scenic, string.quoted.single.scenic
{foo-bar      : source.scenic, string.quoted.single.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
}             : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
blah          : source.scenic, string.quoted.single.scenic
{foo-bar      : source.scenic, string.quoted.single.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
 //insane {}} : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
{}            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
blah          : source.scenic, string.quoted.single.scenic
{foo-bar      : source.scenic, string.quoted.single.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
 //insane {}} : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
