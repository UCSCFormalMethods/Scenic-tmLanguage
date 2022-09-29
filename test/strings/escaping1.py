a = "simple \\ string \
foo \' \" \a \b \c \f \n \r \t \v \5 \55 \555 \05 \005"



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
simple        : source.scenic, string.quoted.single.scenic
\\            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
 string       : source.scenic, string.quoted.single.scenic
\             : constant.language.scenic, source.scenic, string.quoted.single.scenic
foo           : source.scenic, string.quoted.single.scenic
\'            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\"            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\a            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\b            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
 \c           : source.scenic, string.quoted.single.scenic
\f            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\n            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\r            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\t            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\v            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\5            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\55           : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\555          : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\05           : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
\005          : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
