class Foo(Bar, str, type=12, metaclass=FooMeta): pass



class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Foo           : entity.name.type.class.scenic, meta.class.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.begin.scenic, source.scenic
Bar           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
,             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.inheritance.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
str           : meta.class.inheritance.scenic, meta.class.scenic, source.scenic, support.type.scenic
,             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.inheritance.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
type          : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic, variable.parameter.class.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
12            : constant.numeric.dec.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
,             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.inheritance.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
metaclass     : meta.class.inheritance.scenic, meta.class.scenic, source.scenic, support.type.metaclass.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
FooMeta       : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.end.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
