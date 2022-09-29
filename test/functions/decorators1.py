@some_decorator # with comment
@some.class.decorator
@some_decorator(1)
@some.decorator   (1, 3)
@some_decorator(a=2, b={'q': 42}, **kwargs)
@classmethod
def decorated(a): pass



@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
some_decorator : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 with comment : comment.line.number-sign.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
some          : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
class         : keyword.control.flow.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
decorator     : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
some_decorator : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
some          : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
decorator     : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
3             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
some_decorator : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
a             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
b             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
{             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.definition.dict.begin.scenic, source.scenic
'             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
q             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.separator.dict.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
}             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.definition.dict.end.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function.decorator.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
**            : keyword.operator.unpacking.arguments.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
kwargs        : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
classmethod   : meta.function.decorator.scenic, source.scenic, support.type.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
decorated     : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
