# this is testing trailing whitespace after the decorator
# DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE
@foo    
@foo()    
@bar	
@bar()	
@bar() illegal # legal
@bar():   
def baz(): pass





#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 this is testing trailing whitespace after the decorator : comment.line.number-sign.scenic, source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 DO NOT DELETE TRAILING WHITESTAPCE IN THIS FILE : comment.line.number-sign.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
foo           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : meta.function.decorator.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
foo           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
              : source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
	             : meta.function.decorator.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
	             : source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
 illegal      : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : source.scenic
#             : comment.line.number-sign.scenic, punctuation.definition.comment.scenic, source.scenic
 legal        : comment.line.number-sign.scenic, source.scenic
@             : entity.name.function.decorator.scenic, meta.function.decorator.scenic, punctuation.definition.decorator.scenic, source.scenic
bar           : entity.name.function.decorator.scenic, meta.function.decorator.scenic, source.scenic
(             : meta.function.decorator.scenic, punctuation.definition.arguments.begin.scenic, source.scenic
)             : meta.function.decorator.scenic, punctuation.definition.arguments.end.scenic, source.scenic
:             : invalid.illegal.decorator.scenic, meta.function.decorator.scenic, source.scenic
              : source.scenic
def           : meta.function.scenic, source.scenic, storage.type.function.scenic
              : meta.function.scenic, source.scenic
baz           : entity.name.function.scenic, meta.function.scenic, source.scenic
(             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.begin.scenic, source.scenic
)             : meta.function.parameters.scenic, meta.function.scenic, punctuation.definition.parameters.end.scenic, source.scenic
:             : meta.function.scenic, punctuation.section.function.begin.scenic, source.scenic
              : source.scenic
pass          : keyword.control.flow.scenic, source.scenic
