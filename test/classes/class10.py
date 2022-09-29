class Foo(Bar(q=1) (w=2) (e=3)): pass



class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Foo           : entity.name.type.class.scenic, meta.class.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.begin.scenic, source.scenic
Bar           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
q             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
w             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
2             : constant.numeric.dec.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
e             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
3             : constant.numeric.dec.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.end.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
