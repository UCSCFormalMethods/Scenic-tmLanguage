from ... import foo as bar
raise Exception('done') from exc
yield from foo




from          : keyword.control.import.scenic, source.scenic
              : source.scenic
...           : punctuation.separator.period.scenic, source.scenic
              : source.scenic
import        : keyword.control.import.scenic, source.scenic
              : source.scenic
foo           : source.scenic
              : source.scenic
as            : keyword.control.import.scenic, source.scenic
              : source.scenic
bar           : source.scenic
raise         : keyword.control.flow.scenic, source.scenic
              : source.scenic
Exception     : meta.function-call.scenic, source.scenic, support.type.exception.scenic
(             : meta.function-call.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
done          : meta.function-call.arguments.scenic, meta.function-call.scenic, source.scenic, string.quoted.single.scenic
'             : meta.function-call.arguments.scenic, meta.function-call.scenic, punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
)             : meta.function-call.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
from          : keyword.control.flow.scenic, source.scenic
              : source.scenic
exc           : source.scenic
yield from    : keyword.control.flow.scenic, source.scenic
              : source.scenic
foo           : source.scenic
