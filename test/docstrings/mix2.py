'TEST'

class Foo:
    # comment
    R'TEST'

    def foo(self, a:'TEST') -> 'TEST': #ok
        r'TEST'
        with bar:
            pass

    def bar(self, a:'TEST') -> 'TEST': pass
        'TEST' # additional docstring
        with bar:
            pass



'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
TEST          : source.scenic, string.quoted.docstring.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
class         : meta.class.scenic, source.scenic, storage.type.class.scenic
              : meta.class.scenic, source.scenic
Foo           : entity.name.type.class.scenic, meta.class.scenic, source.scenic
:             : meta.class.scenic, punctuation.section.class.begin.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 comment      : comment.line.number-sign.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
TEST          : source.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
              : source.scenic
              : meta.function.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
self          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.self.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
              : meta.function.scenic, source.scenic
->            : meta.function.scenic, punctuation.separator.annotation.result.scenic, source.scenic
              : meta.function.scenic, source.scenic
'             : meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
ok            : comment.line.number-sign.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
TEST          : source.scenic, string.quoted.docstring.raw.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
              : source.scenic
with          : keyword.control.flow.scenic, source.scenic
              : source.scenic
bar           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
              : source.scenic
              : meta.function.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
bar           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
self          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.self.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
              : meta.function.scenic, source.scenic
->            : meta.function.scenic, punctuation.separator.annotation.result.scenic, source.scenic
              : meta.function.scenic, source.scenic
'             : meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : meta.function.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
TEST          : source.scenic, string.quoted.docstring.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 additional docstring : comment.line.number-sign.scenic, source.scenic
              : source.scenic
with          : keyword.control.flow.scenic, source.scenic
              : source.scenic
bar           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
