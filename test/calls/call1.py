some_call(A, b, c[1], *args, FOO=lambda:{'q': 42}, **kwargs)




some_call     : meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
A             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
b             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
c             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.indexed-name.scenic, meta.item-access.scenic, source.scenic
[             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
1             : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic
]             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
*             : keyword.operator.unpacking.arguments.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
args          : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
FOO           : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, variable.parameter.function-call.scenic
=             : keyword.operator.assignment.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
lambda        : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.lambda-function.scenic, source.scenic, storage.type.function.lambda.scenic
:             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.lambda-function.scenic, punctuation.section.function.lambda.begin.scenic, source.scenic
{             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.dict.begin.scenic, source.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
q             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.dict.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
}             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.dict.end.scenic, source.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
**            : keyword.operator.unpacking.arguments.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
kwargs        : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
