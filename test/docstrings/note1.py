''' foo bar XXX baz '''

def foo():
    ''' foo FIXME baz '''


'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
 foo bar      : source.python, string.quoted.docstring.python
XXX           : source.python, string.quoted.docstring.note.python, string.quoted.docstring.python
 baz          : source.python, string.quoted.docstring.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python
              : source.python
def           : meta.function.python, source.python, storage.type.function.python
              : meta.function.python, source.python
foo           : entity.name.function.python, meta.function.python, source.python
(             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.begin.python, source.python
)             : meta.function.parameters.python, meta.function.python, punctuation.definition.parameters.end.python, source.python
:             : meta.function.python, punctuation.section.function.begin.python, source.python
              : source.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.docstring.python
 foo          : source.python, string.quoted.docstring.python
FIXME         : source.python, string.quoted.docstring.note.python, string.quoted.docstring.python
 baz          : source.python, string.quoted.docstring.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.docstring.python