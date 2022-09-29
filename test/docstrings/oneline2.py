def foo():
    '''>>> print("""docstring""")'''
def foo():
    """>>> print('''docstring''')"""



def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.multi.scenic
print("""docstring""") : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.multi.scenic
print('''docstring''') : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
