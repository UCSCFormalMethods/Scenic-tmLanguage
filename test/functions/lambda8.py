anon = lambda a,
              d=1: None
def foo(): pass



anon          : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
lambda        : meta.lambda-function.scenic, source.scenic, storage.type.function.lambda.scenic
              : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic
a             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, source.scenic, variable.parameter.function.language.scenic
,             : meta.function.lambda.parameters.scenic, meta.lambda-function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.lambda-function.scenic, source.scenic
               : source.scenic
d             : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
1             : constant.numeric.dec.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
None          : constant.language.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
