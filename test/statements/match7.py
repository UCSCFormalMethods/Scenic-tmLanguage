match 'prefix' + foo:
    ... # cases
match "prefix" + foo:
    ... # cases
match f'prefix{foo}':
    ... # cases
match f"prefix{foo}":
    ... # cases
match -foo:
    ... # cases
match not foo:
    ... # cases




match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
prefix        : source.scenic, string.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
foo           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
prefix        : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
+             : keyword.operator.arithmetic.scenic, source.scenic
              : source.scenic
foo           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
'             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
prefix        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
foo           : meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
'             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
f             : meta.fstring.scenic, source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.quoted.single.scenic
"             : meta.fstring.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
prefix        : meta.fstring.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
{             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
foo           : meta.fstring.scenic, source.scenic
}             : constant.character.format.placeholder.other.scenic, meta.fstring.scenic, source.scenic
"             : meta.fstring.scenic, punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.quoted.single.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
-             : keyword.operator.arithmetic.scenic, source.scenic
foo           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic
match         : keyword.control.flow.scenic, source.scenic
              : source.scenic
not           : keyword.operator.logical.scenic, source.scenic
              : source.scenic
foo           : source.scenic
:             : punctuation.separator.colon.scenic, source.scenic
              : source.scenic
...           : constant.other.ellipsis.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 cases        : comment.line.number-sign.scenic, source.scenic