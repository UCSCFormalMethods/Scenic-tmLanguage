f'''
    prefix{10
    + 32} suffix'''




f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.multi.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
              : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
    prefix    : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
10            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.fstring.scenic, source.scenic
              : meta.fstring.scenic, source.scenic
32            : constant.numeric.dec.scenic, meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
 suffix       : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
'''           : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.multi.scenic
