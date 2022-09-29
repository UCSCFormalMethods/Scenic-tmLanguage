# testing annotations split over multiple lines
def some_func(a:
                 lambda x=None:
                    {key: val
                        for key, val in
                            (x if x is not None else [])
                    }=42):




#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 testing annotations split over multiple lines : comment.line.number-sign.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
some_func     : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
a             : meta.function.parameters.scenic, meta.function.scenic, source.scenic, variable.parameter.function.language.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.annotation.scenic, source.scenic
                  : meta.function.parameters.scenic, meta.function.scenic, source.scenic
lambda        : meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, source.scenic, storage.type.function.lambda.scenic
              : meta.function.lambda.parameters.scenic, meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, source.scenic
x             : meta.function.lambda.parameters.scenic, meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, source.scenic, variable.parameter.function.language.scenic
=             : keyword.operator.scenic, meta.function.lambda.parameters.scenic, meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, source.scenic
None          : constant.language.scenic, meta.function.lambda.parameters.scenic, meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, source.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, meta.lambda-function.scenic, punctuation.section.function.lambda.begin.scenic, source.scenic
                     : meta.function.parameters.scenic, meta.function.scenic, source.scenic
{             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.dict.begin.scenic, source.scenic
key           : meta.function.parameters.scenic, meta.function.scenic, source.scenic
:             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.dict.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
val           : meta.function.parameters.scenic, meta.function.scenic, source.scenic
                         : meta.function.parameters.scenic, meta.function.scenic, source.scenic
for           : keyword.control.flow.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
key           : meta.function.parameters.scenic, meta.function.scenic, source.scenic
,             : meta.function.parameters.scenic, meta.function.scenic, punctuation.separator.element.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
val           : meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
in            : keyword.control.flow.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
                             : meta.function.parameters.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.parenthesis.begin.scenic, source.scenic
x             : meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
if            : keyword.control.flow.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
x             : meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
is            : keyword.operator.logical.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
not           : keyword.operator.logical.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
None          : constant.language.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
else          : keyword.control.flow.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
              : meta.function.parameters.scenic, meta.function.scenic, source.scenic
[             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.list.begin.scenic, source.scenic
]             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.list.end.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.parenthesis.end.scenic, source.scenic
                     : meta.function.parameters.scenic, meta.function.scenic, source.scenic
}             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.dict.end.scenic, source.scenic
=             : keyword.operator.assignment.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.function.parameters.scenic, meta.function.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
