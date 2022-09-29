# testing comments in function definition
def foo(    # before args
    a=42,   # between
            # args
    b=      # in args
      24,
    d       # before '='
     =99,
    e
    )       # incomplete definition, missing COLON, you're probably typing it
    # pre docstring
    '''Docstring'''
    # post docstring

def bar(): return 1




#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 testing comments in function definition : comment.line.number-sign.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 before args  : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 between      : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 args         : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
b             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 in args      : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
24            : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
d             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 before '='   : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
99            : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
e             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
              : meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 incomplete definition, missing COLON, you're probably typing it : comment.line.number-sign.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 pre docstring : comment.line.number-sign.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.multi.scenic
Docstring     : source.scenic, string.quoted.docstring.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.multi.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 post docstring : comment.line.number-sign.scenic, source.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
bar           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
return        : keyword.control.flow.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
