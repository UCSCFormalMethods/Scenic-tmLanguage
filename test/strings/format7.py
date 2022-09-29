# XXX we have to highlight '% o' here, as it is a valid python
# format spec. Otherwise, it would be hard to spot an error in
# the code below.
a = '12% of %s' % ('name',)



#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
              : comment.line.number-sign.scenic, source.scenic
XXX           : comment.line.number-sign.scenic, keyword.codetag.notation.scenic, source.scenic
 we have to highlight '% o' here, as it is a valid python : comment.line.number-sign.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 format spec. Otherwise, it would be hard to spot an error in : comment.line.number-sign.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 the code below. : comment.line.number-sign.scenic, source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
12            : source.scenic, string.quoted.single.scenic
% o           : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
f             : source.scenic, string.quoted.single.scenic
%s            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
%             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
name          : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
