match (foo + bar):
    ... # cases
match [foo, bar]:
    ... # cases
match {foo, bar}:
    ... # cases




match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
foo           : source.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
bar           : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
foo           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
bar           : source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
foo           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
bar           : source.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic