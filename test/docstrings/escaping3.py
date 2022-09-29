r'''Module docstring

    (?x)                # not a regexp
        foo[20]{42}     # not a comment
'''



r             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.multi.scenic
Module docstring : source.scenic, string.quoted.docstring.raw.multi.scenic
              : source.scenic, string.quoted.docstring.raw.multi.scenic
    (?x)                # not a regexp : source.scenic, string.quoted.docstring.raw.multi.scenic
        foo[20]{42}     # not a comment : source.scenic, string.quoted.docstring.raw.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.multi.scenic
