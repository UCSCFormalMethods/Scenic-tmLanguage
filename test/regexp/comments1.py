a = r'''foo[abc] # comment'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
foo           : source.scenic, string.regexp.quoted.multi.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
a             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
b             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
c             : constant.character.set.regexp, meta.character.set.regexp, source.scenic, string.regexp.quoted.multi.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 comment      : comment.line.number-sign.scenic, source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
