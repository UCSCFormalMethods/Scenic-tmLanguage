f'''
    prefix {
        foo(f"""
            inner prefix
            { bar["q"] + f'insane{42 + 9000}stuff{def aaa(): pass}111'}
            inner suffix
        """)
    } suffix
'''




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
    prefix    : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
foo           : meta.fstring.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
            inner prefix : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
bar           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.indexed-name.scenic, meta.item-access.scenic, source.scenic
[             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
q             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, source.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.arguments.scenic, meta.item-access.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
]             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.item-access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
f             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
insane        : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
42            : constant.numeric.dec.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
9000          : constant.numeric.dec.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
stuff         : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
def           : keyword.control.flow.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
aaa           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.generic.scenic, meta.function-call.scenic, source.scenic
(             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.separator.colon.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
pass          : keyword.control.flow.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
111           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
            inner suffix : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
"""           : meta.fstring.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
)             : meta.fstring.scenic, meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
 suffix       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
