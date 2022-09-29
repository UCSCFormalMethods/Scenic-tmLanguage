def foo():
    "TE\"ST"

def foo():
    r"TE\"ST"

def foo():
    R"TE\"ST"

def foo():
    u"TEST"

def foo():
    U"TEST"

def foo():
    b"TEST"

def foo():
    B"TEST"



def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.single.scenic
TE            : source.scenic, string.quoted.docstring.single.scenic
\"            : constant.character.escape.scenic, source.scenic, string.quoted.docstring.single.scenic
ST            : source.scenic, string.quoted.docstring.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
r             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
TE            : source.scenic, string.quoted.docstring.raw.single.scenic
\"            : source.scenic, string.quoted.docstring.raw.single.scenic
ST            : source.scenic, string.quoted.docstring.raw.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.docstring.raw.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
TE            : source.scenic, string.quoted.docstring.raw.single.scenic
\"            : source.scenic, string.quoted.docstring.raw.single.scenic
ST            : source.scenic, string.quoted.docstring.raw.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.docstring.raw.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
u             : source.scenic, storage.type.string.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
U             : source.scenic, storage.type.string.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.single.scenic
TEST          : source.scenic, string.quoted.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
b             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
TEST          : source.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
foo           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
B             : source.scenic, storage.type.string.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.binary.single.scenic
TEST          : source.scenic, string.quoted.binary.single.scenic
"             : punctuation.definition.string.end.scenic, source.scenic, string.quoted.binary.single.scenic
