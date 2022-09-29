@a.   b  .  \
   c.None.z(foo=BAR). \
       baz[1:2]
@foo.class.bar[]
@foo.ok '''
def foo(): pass




@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
a             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
b             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
\             : meta.function.decorator.scenic, punctuation.separator.continuation.line.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
c             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
None          : keyword.illegal.name.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
z             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
foo           : meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
BAR           : constant.other.caps.scenic, meta.function-call.arguments.scenic, meta.function.decorator.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
. \           : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : source.scenic
baz           : meta.indexed-name.scenic, meta.item-access.scenic, source.scenic
[             : meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic
:             : meta.item-access.arguments.scenic, meta.item-access.scenic, punctuation.separator.slice.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic
]             : meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
foo           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
class         : keyword.control.flow.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
[]            : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
foo           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
.             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.separator.period.scenic, source.scenic
ok            : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
'''           : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
