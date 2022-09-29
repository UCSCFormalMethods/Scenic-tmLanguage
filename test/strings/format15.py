a = '''
{{ before detection }}
{# jinja comment #}
{{ after detection }}
'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.multi.scenic
{{            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.multi.scenic
 before detection  : source.scenic, string.quoted.multi.scenic
}}            : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.multi.scenic
{# jinja comment #} : source.scenic, string.quoted.multi.scenic
{{ after detection }} : source.scenic, string.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.multi.scenic
