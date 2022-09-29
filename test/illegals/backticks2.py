a = `\
123`
print a



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
`             : invalid.deprecated.backtick.scenic, source.scenic
\             : invalid.deprecated.backtick.scenic, punctuation.separator.continuation.line.scenic, source.scenic
              : invalid.deprecated.backtick.scenic, source.scenic
123           : constant.numeric.dec.scenic, invalid.deprecated.backtick.scenic, source.scenic
`             : invalid.deprecated.backtick.scenic, source.scenic
print         : source.scenic, support.function.builtin.scenic
              : source.scenic
a             : source.scenic
