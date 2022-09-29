if isinstance(t1, TypeVar): # type: ignore
    continue



if            : keyword.control.flow.scenic, source.scenic
              : source.scenic
isinstance    : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
t1            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
TypeVar       : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, meta.typehint.comment.scenic, source.scenic
type:         : comment.line.number-sign.scenic, comment.typehint.directive.notation.scenic, meta.typehint.comment.scenic, source.scenic
              : comment.line.number-sign.scenic, meta.typehint.comment.scenic, source.scenic
ignore        : comment.line.number-sign.scenic, comment.typehint.ignore.notation.scenic, meta.typehint.comment.scenic, source.scenic
              : source.scenic
continue      : keyword.control.flow.scenic, source.scenic
