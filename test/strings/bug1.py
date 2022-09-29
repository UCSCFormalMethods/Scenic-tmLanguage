# issue 150
myrecord = {
    "a": {k: str(v) for k, v in foo if ""}
}




#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 issue 150    : comment.line.number-sign.scenic, source.scenic
myrecord        : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
a             : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
k             : source.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
str           : meta.function-call.scenic, source.scenic, support.type.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
v             : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
for           : keyword.control.flow.scenic, source.scenic
              : source.scenic
k             : source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
v             : source.scenic
              : source.scenic
in            : keyword.control.flow.scenic, source.scenic
              : source.scenic
foo           : source.scenic
              : source.scenic
if            : keyword.control.flow.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
