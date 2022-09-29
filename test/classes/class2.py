@dec
# Bar.name=... is not legal, but the test is for highlighter not breaking badly
class Spam(Foo.Bar, Bar.name={'very': 'odd'}):
    pass




@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
dec           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 Bar.name=... is not legal, but the test is for highlighter not breaking badly : comment.line.number-sign.scenic, source.scenic
class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Spam          : entity.name.type.class.scenic, meta.class.scenic, source.scenic
(             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.begin.scenic, source.scenic
Foo           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
.             : meta.class.inheritance.scenic, meta.class.scenic, meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
Bar           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.member.access.scenic, source.scenic
,             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.inheritance.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
Bar           : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
.             : meta.class.inheritance.scenic, meta.class.scenic, meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
name          : entity.other.inherited-class.scenic, meta.class.inheritance.scenic, meta.class.scenic, meta.member.access.scenic, source.scenic
=             : keyword.operator.assignment.scenic, meta.class.inheritance.scenic, meta.class.scenic, source.scenic
{             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.dict.begin.scenic, source.scenic
'             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
very          : meta.class.inheritance.scenic, meta.class.scenic, source.scenic, string.quoted.single.scenic
'             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.separator.dict.scenic, source.scenic
              : meta.class.inheritance.scenic, meta.class.scenic, source.scenic
'             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
odd           : meta.class.inheritance.scenic, meta.class.scenic, source.scenic, string.quoted.single.scenic
'             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
}             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.dict.end.scenic, source.scenic
)             : meta.class.inheritance.scenic, meta.class.scenic, punctuation.definition.inheritance.end.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
