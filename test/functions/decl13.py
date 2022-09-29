def foo()
    -> notOK:
    pass



def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
              : source.scenic
->            : invalid.illegal.annotation.scenic, source.scenic
              : source.scenic
notOK         : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
