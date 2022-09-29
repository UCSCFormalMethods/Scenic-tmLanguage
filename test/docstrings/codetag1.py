''' foo bar XXX baz '''

def foo():
    ''' foo FIXME baz '''



'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
 foo bar      : source.scenic, string.quoted.docstring.multi.scenic
XXX           : keyword.codetag.notation.scenic, source.scenic, string.quoted.docstring.multi.scenic
 baz          : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
 foo          : source.scenic, string.quoted.docstring.multi.scenic
FIXME         : keyword.codetag.notation.scenic, source.scenic, string.quoted.docstring.multi.scenic
 baz          : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
