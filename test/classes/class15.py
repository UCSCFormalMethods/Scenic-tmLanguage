class Spam(Foo, from==12):
    pass



class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Spam          : entity.name.type.class.scenic, meta.class.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.begin.scenic, source.scenic
Foo           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
,             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.inheritance.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
from          : keyword.control.flow.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
==            : keyword.operator.comparison.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
12            : constant.numeric.dec.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.end.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
