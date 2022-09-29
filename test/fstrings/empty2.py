rf"{} {  }"
rf"""{}
{  }
"""





rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
              : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
              : invalid.illegal.brace.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
}             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
              : invalid.illegal.brace.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
}             : constant.character.format.placeholder.other.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
