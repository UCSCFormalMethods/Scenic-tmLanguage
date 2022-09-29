a = (from, a)
b = [from, b]
c = {from: {import: a}}



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
(             : punctuation.parenthesis.begin.scenic, source.scenic
from          : keyword.control.flow.scenic, source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
a             : source.scenic
)             : punctuation.parenthesis.end.scenic, source.scenic
b             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
[             : punctuation.definition.list.begin.scenic, source.scenic
from          : keyword.control.flow.scenic, source.scenic
,             : punctuation.separator.element.scenic, source.scenic
              : source.scenic
b             : source.scenic
]             : punctuation.definition.list.end.scenic, source.scenic
c             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
from          : keyword.control.flow.scenic, source.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
{             : punctuation.definition.dict.begin.scenic, source.scenic
import        : keyword.control.import.scenic, source.scenic
:             : punctuation.separator.dict.scenic, source.scenic
              : source.scenic
a             : source.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
}             : punctuation.definition.dict.end.scenic, source.scenic
