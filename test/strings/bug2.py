# issue 150
cmd = "git-clang-format --style=\"{{BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2, " \
 "AlignConsecutiveAssignments: true}}\" {COMMIT_SHA} -- ./**/*.proto > {OUTPUT}".format(




#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 issue 150    : comment.line.number-sign.scenic, source.scenic
cmd           : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
git-clang-format --style= : source.scenic, string.quoted.single.scenic
\"            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
{{            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
BasedOnStyle: Google, ColumnLimit: 100, IndentWidth: 2,  : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
\             : punctuation.separator.continuation.line.scenic, source.scenic
              : source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
AlignConsecutiveAssignments: true : source.scenic, string.quoted.single.scenic
}}            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
\"            : constant.character.escape.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic, string.quoted.single.scenic
{COMMIT_SHA}  : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
 -- ./**/*.proto >  : source.scenic, string.quoted.single.scenic
{OUTPUT}      : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
format        : meta.function-call.generic.scenic, meta.function-call.scenic, meta.member.access.scenic, source.scenic
(             : meta.function-call.scenic, meta.member.access.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
