a = 'XXX FIXME NB TODO'
a = r'XXX FIXME NB TODO'
a = b'XXX FIXME NB TODO'



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
XXX FIXME NB TODO : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.single.scenic
XXX FIXME NB TODO : source.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
XXX FIXME NB TODO : source.scenic, string.quoted.binary.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
