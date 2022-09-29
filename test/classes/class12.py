class F:
    @classmethod
    def meth(cls, a, b=1):
        cls.a = a
        cls.b = b
        print(cls)
        cls()
        cls + 1
        a.cls = 1
        a.cls.__name__
        cls[123]




class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
F             : entity.name.type.class.scenic, meta.class.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
classmethod   : meta.function.decorator.scenic, source.scenic, support.type.scenic
              : meta.function.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
meth          : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
cls           : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.cls.scenic
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
cls           : source.scenic, variable.language.special.cls.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
a             : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
cls           : source.scenic, variable.language.special.cls.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
b             : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
b             : source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
cls           : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.language.special.cls.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
cls           : meta.function-call.scenic, source.scenic, variable.language.special.cls.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
cls           : source.scenic, variable.language.special.cls.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
cls           : meta.attribute.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
              : source.scenic
a             : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
cls           : meta.attribute.scenic, meta.member.access.scenic, source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
__name__      : meta.member.access.scenic, source.scenic, support.variable.magic.scenic
              : source.scenic
cls           : meta.item-access.scenic, source.scenic, variable.language.special.cls.scenic
[             : meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
123           : constant.numeric.dec.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic
]             : meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
