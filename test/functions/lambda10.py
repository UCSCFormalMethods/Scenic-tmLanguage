showcase = lambda a, /, b, *, c: (a + b + c)




showcase      : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
lambda        : meta.lambda-function.scenic, source.scenic, storage.type.function.lambda.scenic
              : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
a             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic, variable.parameter.function.language.scenic
,             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
/             : keyword.operator.positional.parameter.scenic, meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
,             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
b             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic, variable.parameter.function.language.scenic
,             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
*             : keyword.operator.unpacking.parameter.scenic, meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
,             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
c             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.lambda-function.scenic, punctuation.section.function.lambda.begin.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
a             : source.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
c             : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
