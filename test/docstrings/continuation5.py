'implicit ' "concatenation"

'''implicit
''' 'concatenation'

'''implicit
''' """
concatenation
"""

'implicit' '''
concatenation
'''



'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
implicit      : source.scenic, string.quoted.docstring.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
concatenation : source.scenic, string.quoted.docstring.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
implicit      : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
concatenation : source.scenic, string.quoted.docstring.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
implicit      : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
concatenation : source.scenic, string.quoted.docstring.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
implicit      : source.scenic, string.quoted.docstring.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
concatenation : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
