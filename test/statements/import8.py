try:
    import \
                    time as ham, \
                    datetime \
            # XXX: comment at the end of import
except Exception as exc:
    pass




try           : keyword.control.flow.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
import        : keyword.control.import.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
                     : source.scenic
time          : source.scenic
              : source.scenic
as            : keyword.control.import.scenic, source.scenic
              : source.scenic
ham           : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
                     : source.scenic
datetime      : source.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
              : comment.line.number-sign.scenic, source.scenic
XXX           : comment.line.number-sign.scenic, keyword.codetag.notation.scenic, source.scenic
: comment at the end of import : comment.line.number-sign.scenic, source.scenic
except        : keyword.control.flow.scenic, source.scenic
              : source.scenic
Exception     : source.scenic, support.type.exception.scenic
              : source.scenic
as            : keyword.control.flow.scenic, source.scenic
              : source.scenic
exc           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
