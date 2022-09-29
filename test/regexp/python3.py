a = r'''
    (?x)
        foo
'''
a = br'''
    (?x)
        foo
'''
a = rb'''
    (?x)
        foo
'''
a = Br'''
    (?x)
        foo
'''
a = rB'''
    (?x)
        foo
'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
        foo   : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
br            : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
        foo   : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rb            : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
        foo   : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
Br            : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
        foo   : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
rB            : source.scenic, storage.type.string.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.regexp.quoted.multi.scenic
              : source.scenic, string.regexp.quoted.multi.scenic
(?x)          : source.scenic, storage.modifier.flag.regexp, string.regexp.quoted.multi.scenic
        foo   : source.scenic, string.regexp.quoted.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.regexp.quoted.multi.scenic
