a = '''blah {foo-bar %d
       blah {foo-bar %d}
       blah {foo-bar %d //insane {}}
       {}blah {foo-bar %d //insane {}}'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.multi.scenic
blah {foo-bar  : source.scenic, string.quoted.multi.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.multi.scenic
       blah   : source.scenic, string.quoted.multi.scenic
{foo-bar      : source.scenic, string.quoted.multi.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.multi.scenic
}             : source.scenic, string.quoted.multi.scenic
       blah {foo-bar  : source.scenic, string.quoted.multi.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.multi.scenic
 //insane {}} : source.scenic, string.quoted.multi.scenic
       {}blah {foo-bar  : source.scenic, string.quoted.multi.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.multi.scenic
 //insane {}} : source.scenic, string.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.multi.scenic
