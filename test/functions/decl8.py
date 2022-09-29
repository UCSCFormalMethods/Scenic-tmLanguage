def foo(a=1**1, *b:3*2=1*2, **a=1*2**3): pass



def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
**            : keyword.operator.arithmetic.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
*             : keyword.operator.unpacking.parameter.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
b             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
3             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
*             : keyword.operator.arithmetic.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
=             : keyword.operator.assignment.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
*             : keyword.operator.arithmetic.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
**            : keyword.operator.unpacking.parameter.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
*             : keyword.operator.arithmetic.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
**            : keyword.operator.arithmetic.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
3             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
