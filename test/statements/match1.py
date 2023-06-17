def foo(status):
    match status:
        case 404:
            return "Not found"
        case 401 | 403:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"




def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
status        : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
status        : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
404           : constant.numeric.dec.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
return        : keyword.control.flow.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
Not found     : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
401           : constant.numeric.dec.scenic, source.scenic
              : source.scenic
|             : keyword.operator.bitwise.scenic, source.scenic
              : source.scenic
403           : constant.numeric.dec.scenic, source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
return        : keyword.control.flow.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
Not allowed   : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
case          : keyword.control.flow.scenic, source.scenic
              : source.scenic
_             : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
return        : keyword.control.flow.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
Something's wrong with the internet : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
