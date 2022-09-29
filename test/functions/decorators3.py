@ f . bar (baz = 1)
def foo(): pass



@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
f             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
baz           : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic, variable.parameter.function-call.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
