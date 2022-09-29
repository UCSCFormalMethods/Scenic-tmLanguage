try:
    1/0
except AbcError as ex:
    pass
except (ZeroDivisionError, GhiError) as ex:
    print(ex)
else:
    1
finally:
    2



try           : keyword.control.flow.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
/             : keyword.operator.arithmetic.scenic, source.scenic
0             : constant.numeric.dec.scenic, source.scenic
except        : keyword.control.flow.scenic, source.scenic
              : source.scenic
AbcError      : source.scenic
              : source.scenic
as            : keyword.control.flow.scenic, source.scenic
              : source.scenic
ex            : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
except        : keyword.control.flow.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
ZeroDivisionError : source.scenic, support.type.exception.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
GhiError      : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
              : source.scenic
as            : keyword.control.flow.scenic, source.scenic
              : source.scenic
ex            : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
print         : meta.function-call.scenic, source.scenic, support.function.builtin.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
ex            : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
else          : keyword.control.flow.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
1             : constant.numeric.dec.scenic, source.scenic
finally       : keyword.control.flow.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
2             : constant.numeric.dec.scenic, source.scenic
