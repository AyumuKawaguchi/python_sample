#coding:utf-8 
import re
 
# 検索対象
regdate = 'これは以下案件情報です以上これは'
# 検索条件
pattern = "(以下.*以上)"
# 
d = re.search(pattern, regdate)
print(d.group(1))