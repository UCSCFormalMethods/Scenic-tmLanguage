a = '%i' % 42
a = "%(language)s has %(number)03d quote types."
a = b"%(language)s has %(number)03d quote types."
a = R"%(language)s has %(number)03d quote types."



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
%i            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
%             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
42            : constant.numeric.dec.scenic, source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
%(language)s  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
 has          : source.scenic, string.quoted.single.scenic
%(number)03d  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
 quote types. : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
%(language)s  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.binary.single.scenic
 has          : source.scenic, string.quoted.binary.single.scenic
%(number)03d  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.binary.single.scenic
 quote types. : source.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.single.scenic
%(language)s  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.raw.single.scenic
 has          : source.scenic, string.quoted.raw.single.scenic
%(number)03d  : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.raw.single.scenic
 quote types. : source.scenic, string.quoted.raw.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.single.scenic
