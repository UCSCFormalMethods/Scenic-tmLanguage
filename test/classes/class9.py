class Foo:
    __slots__ = ()
    __match_args__ = ('key', 'name')



class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Foo           : entity.name.type.class.scenic, meta.class.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
__slots__     : source.scenic, support.variable.magic.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
              : source.scenic
__match_args__ : source.scenic, support.variable.magic.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
key           : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
name          : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
