some_number: int           # variable without initial value
some_list: List[int] = []  # variable with initial value




some_number   : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
int           : source.scenic, support.type.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 variable without initial value : comment.line.number-sign.scenic, source.scenic
some_list     : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
List          : meta.indexed-name.scenic, meta.item-access.scenic, source.scenic
[             : meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
int           : meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic, support.type.scenic
]             : meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 variable with initial value : comment.line.number-sign.scenic, source.scenic
