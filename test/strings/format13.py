a = '''\n
{% for item in seq %}
    \n {{ item }} \n \N{BLACK SPADE SUIT}
{% endfor %}
'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.multi.scenic
\n            : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
{% for item in seq %} : source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
\n            : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
 {{ item }}   : source.scenic, string.quoted.multi.scenic
\n            : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
              : source.scenic, string.quoted.multi.scenic
\N{BLACK SPADE SUIT} : constant.character.escape.scenic, source.scenic, string.quoted.multi.scenic
{% endfor %}  : source.scenic, string.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.multi.scenic
