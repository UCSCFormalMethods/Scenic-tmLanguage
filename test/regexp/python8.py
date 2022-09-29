# And now something fun!

CookiePattern = re.compile(r"""
    (?x)                           # This is a verbose pattern
    \s*                            # Optional whitespace at start of cookie
    (?P<key>                       # Start of group 'key'
    [""" + _LegalKeyChars + r"""]+?   # Any word of at least one letter
    )                              # End of group 'key'
    (                              # Optional group: there may not be a value.
    \s*=\s*                          # Equal Sign
    (?P<val>                         # Start of group 'val'
    "(?:[^\\"]|\\.)*"                  # Any doublequoted string
    |                                  # or
    \w{3},\s[\w\d\s-]{9,11}\s[\d:]{8}\sGMT  # Special case for "expires" attr
    |                                  # or
    [""" + _LegalValueChars + r"""]*      # Any word or empty string
    )                                # End of group 'val'
    )?                             # End of optional value group
    \s*                            # Any number of spaces.
    (\s+|;|$)                      # Ending either at space, semicolon, or EOS.
    """, re.ASCII)                 # May be removed if safe.




#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 And now something fun! : comment.line.number-sign.scenic, source.scenic
              : source.scenic
CookiePattern : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
re            : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
compile       : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
r             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
(?x)          : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
                            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 This is a verbose pattern : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
                             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Optional whitespace at start of cookie : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.parenthesis.named.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
?P<key>       : entity.name.tag.named.group.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
                        : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Start of group 'key' : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
_LegalKeyChars : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
r             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
]             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
+?            : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Any word of at least one letter : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
    )                               : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 End of group 'key' : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.parenthesis.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
                               : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Optional group: there may not be a value. : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
=             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
                           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Equal Sign   : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.parenthesis.named.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
?P<val>       : entity.name.tag.named.group.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
                          : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Start of group 'val' : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
    "         : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
(?:           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.parenthesis.non-capturing.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
[             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
^             : keyword.operator.negation.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\\            : constant.character.escape.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
"             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\\            : constant.character.escape.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
.             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.match.any.regexp
)             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.parenthesis.non-capturing.end.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
"                   : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Any doublequoted string : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
                                   : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 or           : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\w            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
{3}           : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
[             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
\w            : meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
\d            : meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
\s            : meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
-             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
{9,11}        : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
[             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
\d            : meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
:             : constant.character.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
]             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.end.regexp, source.scenic, string.regexp.quoted.multi.scenic
{8}           : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
GMT           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Special case for "expires" attr : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
                                   : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 or           : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, source.scenic, string.regexp.quoted.multi.scenic
[             : constant.other.set.regexp, meta.character.set.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, meta.named.regexp, punctuation.character.set.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
_LegalValueChars : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
+             : keyword.operator.arithmetic.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
r             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
]             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Any word or empty string : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
    )                                 : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 End of group 'val' : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
    )         : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
?             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
                              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 End of optional value group : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
*             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
                             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Any number of spaces. : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
(             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.parenthesis.begin.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
\s            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.escape.special.regexp
+             : keyword.operator.quantifier.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
;             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
|             : keyword.operator.disjunction.regexp, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
$             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic, support.other.match.end.regexp
)             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.parenthesis.end.regexp, source.scenic, string.regexp.quoted.multi.scenic, support.other.parenthesis.regexp
                       : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
#             : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.comment.scenic, source.scenic, string.regexp.quoted.multi.scenic
 Ending either at space, semicolon, or EOS. : comment.line.number-sign.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic, string.regexp.quoted.multi.scenic
"""           : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
,             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.separator.arguments.scenic, source.scenic
              : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
re            : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
.             : meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
ASCII         : constant.other.caps.scenic, meta.function-call.arguments.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
)             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.end.scenic, source.scenic
                  : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 May be removed if safe. : comment.line.number-sign.scenic, source.scenic
