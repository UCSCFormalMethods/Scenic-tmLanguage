a = b'%b' % b'foo'



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
%b            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
              : source.scenic
%             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
foo           : source.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
