a = R'''\fr{still_ok}ac{m_{j \rightarrow i}(\mathrm{good})}
        {not_ok} %d
'''



a             : source.scenic
              : source.scenic
=             : keyword.operator.assignment.scenic, source.scenic
              : source.scenic
R             : source.scenic, storage.type.string.scenic, string.quoted.raw.multi.scenic
'''           : punctuation.definition.string.begin.scenic, source.scenic, string.quoted.raw.multi.scenic
\fr           : source.scenic, string.quoted.raw.multi.scenic
{still_ok}    : constant.character.format.placeholder.other.scenic, meta.format.brace.scenic, source.scenic, string.quoted.raw.multi.scenic
ac            : source.scenic, string.quoted.raw.multi.scenic
{m_{j \rightarrow i}(\mathrm{good})} : source.scenic, string.quoted.raw.multi.scenic
        {not_ok}  : source.scenic, string.quoted.raw.multi.scenic
%d            : constant.character.format.placeholder.other.scenic, meta.format.percent.scenic, source.scenic, string.quoted.raw.multi.scenic
'''           : punctuation.definition.string.end.scenic, source.scenic, string.quoted.raw.multi.scenic
