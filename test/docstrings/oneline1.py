'''>>> print("""docstring""")'''
async
""">>> print('''docstring''')"""
await
"""\n>>> print('''docstring''')"""
await
"""   >>> print('''docstring''')"""
await
""" 1  >>> print('''docstring''')"""
await



'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.multi.scenic
print("""docstring""") : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
async         : keyword.control.flow.scenic, source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.multi.scenic
print('''docstring''') : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
await         : keyword.control.flow.scenic, source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
\n            : constant.character.escape.scenic, source.scenic, string.quoted.docstring.multi.scenic
>>> print('''docstring''') : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
await         : keyword.control.flow.scenic, source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic, string.quoted.docstring.multi.scenic
>>>           : keyword.control.flow.scenic, source.scenic, string.quoted.docstring.multi.scenic
print('''docstring''') : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
await         : keyword.control.flow.scenic, source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
 1  >>> print('''docstring''') : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
await         : keyword.control.flow.scenic, source.scenic
