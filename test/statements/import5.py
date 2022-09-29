from.foo import d
from.import a

foo.import

raise Exception from Foo

def bar():
    yield from baz




from          : keyword.control.import.scenic, source.scenic
.             : punctuation.separator.period.scenic, source.scenic
foo           : source.scenic
              : source.scenic
import        : keyword.control.import.scenic, source.scenic
              : source.scenic
d             : source.scenic
from          : keyword.control.import.scenic, source.scenic
.             : punctuation.separator.period.scenic, source.scenic
import        : keyword.control.import.scenic, source.scenic
              : source.scenic
a             : source.scenic
              : source.scenic
foo           : source.scenic
.             : meta.member.access.scenic, punctuation.separator.period.scenic, source.scenic
import        : keyword.control.import.scenic, meta.member.access.scenic, source.scenic
              : source.scenic
raise         : keyword.control.flow.scenic, source.scenic
              : source.scenic
Exception     : source.scenic, support.type.exception.scenic
              : source.scenic
from          : keyword.control.flow.scenic, source.scenic
              : source.scenic
Foo           : source.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
bar           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
yield from    : keyword.control.flow.scenic, source.scenic
              : source.scenic
baz           : source.scenic
