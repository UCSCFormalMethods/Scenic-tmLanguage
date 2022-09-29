@foo
async def foo():
    a = 1
    async for a, b, c in b:
        async with b as d, c:
            await func(a, b=1)



@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
foo           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
async         : meta.function.scenic, source.scenic, storage.type.function.async.scenic
              : meta.function.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
async         : keyword.control.flow.scenic, source.scenic
              : source.scenic
for           : keyword.control.flow.scenic, source.scenic
              : source.scenic
a             : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
b             : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
c             : source.scenic
              : source.scenic
in            : keyword.control.flow.scenic, source.scenic
              : source.scenic
b             : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
async         : keyword.control.flow.scenic, source.scenic
              : source.scenic
with          : keyword.control.flow.scenic, source.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
as            : keyword.control.flow.scenic, source.scenic
              : source.scenic
d             : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
c             : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
await         : keyword.control.flow.scenic, source.scenic
              : source.scenic
func          : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
a             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
b             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
