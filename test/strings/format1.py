a = "{0[ ]:X>+10d}"
a = "{0[ ]!s:X>+10d}"
a = "{0[ ]:Xd>+10d}" #invalid



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
{0[ ]         : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
:X>+10d       : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
{0[ ]         : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
!s            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
:X>+10d       : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
{0[ ]         : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
:             : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, storage.type.format.scenic, string.quoted.single.scenic
Xd>+10d}      : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
invalid       : comment.line.number-sign.scenic, source.scenic
