from . . . foo import \
    (
        # XXX: legal comment inside import
        time as bar,
        # another comment
        baz,
        datetime as ham
    )
raise Exception('!') from None




from          : keyword.control.import.scenic, source.scenic
              : source.scenic
.             : punctuation.separator.period.scenic, source.scenic
              : source.scenic
.             : punctuation.separator.period.scenic, source.scenic
              : source.scenic
.             : punctuation.separator.period.scenic, source.scenic
              : source.scenic
foo           : source.scenic
              : source.scenic
import        : keyword.control.import.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
              : comment.line.number-sign.scenic, source.scenic
XXX           : comment.line.number-sign.scenic, keyword.codetag.notation.scenic, source.scenic
: legal comment inside import : comment.line.number-sign.scenic, source.scenic
              : source.scenic
time          : source.scenic
              : source.scenic
as            : keyword.control.import.scenic, source.scenic
              : source.scenic
bar           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 another comment : comment.line.number-sign.scenic, source.scenic
              : source.scenic
baz           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
datetime      : source.scenic
              : source.scenic
as            : keyword.control.import.scenic, source.scenic
              : source.scenic
ham           : source.scenic
              : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
raise         : keyword.control.flow.scenic, source.scenic
              : source.scenic
Exception     : meta.function-call.scenic, source.scenic, support.type.exception.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
!             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
from          : keyword.control.flow.scenic, source.scenic
              : source.scenic
None          : constant.language.scenic, source.scenic
