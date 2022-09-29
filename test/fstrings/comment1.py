f'prefix{10 # comment, making the string technically illegal
def foo(): pass




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
prefix        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
10            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
 #            : meta.fstring.scenic, source.scenic
comment       : meta.fstring.scenic, source.scenic
,             : meta.fstring.scenic, punctuation.separator.element.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
making        : meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
the           : meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
string        : meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
technically   : meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
illegal       : meta.fstring.scenic, source.scenic
              : invalid.illegal.newline.scenic, meta.fstring.scenic, source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
