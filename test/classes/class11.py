class F:
    def __init__(self, a, b=1):
        self.a = a
        self.b = b
        print(self)
        self()
        a.self = 1
        a.self.bar = 2
        self[123]




class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
F             : entity.name.type.class.scenic, meta.class.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : meta.function.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
__init__      : meta.function.scenic, source.scenic, support.function.magic.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
self          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.self.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
b             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
self          : source.scenic, variable.language.special.self.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
a             : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
self          : source.scenic, variable.language.special.self.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
b             : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
self          : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.language.special.self.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
self          : meta.function-call.scenic, source.scenic, variable.language.special.self.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
a             : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
self          : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
self          : meta.attribute.scenic, meta.member.access.scenic, source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
bar           : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
2             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
self          : meta.item-access.scenic, source.scenic, variable.language.special.self.scenic
[             : meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
123           : constant.numeric.dec.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic
]             : meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
