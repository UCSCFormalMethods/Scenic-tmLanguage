rf'fo{2}'
rf"fo{2}"
rf'''fo{2}'''
rf"""fo{2}"""




rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{2}           : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
'             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
{2}           : source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.single.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
{2}           : source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
rf            : source.scenic, storage.type.string.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.begin.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
fo            : source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
{2}           : source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
"""           : punctuation.definition.string.end.scenic, source.scenic, string.interpolated.scenic, string.regexp.quoted.multi.scenic
