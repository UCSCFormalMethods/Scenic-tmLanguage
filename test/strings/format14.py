a = R'''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
\n            : source.scenic, string.quoted.raw.multi.scenic
{% for item in seq %} : source.scenic, string.quoted.raw.multi.scenic
    \n {{ item }} \n \N{BLACK SPADE SUIT} : source.scenic, string.quoted.raw.multi.scenic
{% endfor %}  : source.scenic, string.quoted.raw.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.multi.scenic
