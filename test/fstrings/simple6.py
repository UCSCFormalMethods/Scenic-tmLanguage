f'insane{42 + 9000}stuff{def aaa(): pass}'
# def aaa() must not be parsed as a valid declaration




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
insane        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
9000          : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
stuff         : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
def           : keyword.control.flow.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
aaa           : meta.fstring.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : meta.fstring.scenic, punctuation.separator.colon.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
pass          : keyword.control.flow.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 def aaa() must not be parsed as a valid declaration : comment.line.number-sign.scenic, source.scenic
