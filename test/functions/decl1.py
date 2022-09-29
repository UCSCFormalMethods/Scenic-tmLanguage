def myfunc(self,            # gotta have self
           param1="value",  # values are cool
           param2=True,     # or False, whatever
           **kwargs):       # you never know
    pass



def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
myfunc        : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
self          : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic, variable.parameter.function.language.special.self.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 gotta have self : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
param1        : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
"             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
value         : meta.function.parameters.scenic, meta.function.scenic, source.scenic, string.quoted.single.scenic
"             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 values are cool : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
param2        : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
True          : constant.language.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.parameters.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
#             : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.comment.scenic, source.scenic
 or False, whatever : comment.line.number-sign.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
**            : keyword.operator.unpacking.parameter.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
kwargs        : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 you never know : comment.line.number-sign.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
