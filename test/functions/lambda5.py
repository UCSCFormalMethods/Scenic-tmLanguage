anon = lambda -> qqq[None]: None
def f(): return 1 # this line should not break



anon          : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
lambda        : meta.lambda-function.scenic, source.scenic, storage.type.function.lambda.scenic
              : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
->            : invalid.illegal.annotation.scenic, meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
 qqq[None]    : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
:             : meta.lambda-function.scenic, punctuation.section.function.lambda.begin.scenic, source.scenic
              : source.scenic
None          : constant.language.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
f             : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
return        : keyword.control.flow.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 this line should not break : comment.line.number-sign.scenic, source.scenic
