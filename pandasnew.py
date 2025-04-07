# import numpy as np
# import pandas as pd
# labels =['a','b','c']
# mydata=[10,20,30,40]
# arr=np.array(mydata)
# d={'a':10,'b':20,'c':30}
# print("labels",labels)
# print("mydata",mydata)
# print("array",arr)
# print("dictionary",d)

# print(pd.Series(data=mydata))
# print(pd.Series(data=mydata,index=labels))

# JSON
# import json
# d='{"name": "saad", "age": 23}'
# j=json.loads(d)
# print(j['name'])
# print(j['age'])

# d2={'a':10,'b':20,'c':30}
# j2=json.dumps(d2)

# print(j2)



import re


# pat=r"(/d+)-(/d+)"
# tx="event on 2025-04-05"
# match=re.search(pat,tx)
# if match:
#     print("matched")
# else:
#     print("not")

# s="s.saadbme@gmail.com"
# pat=r"a-zA-Z0-9%_+-"
# match=re.search(s,pat)
# if match:
#     print("yes",match.group())
# else:
#     print("no")

# s="the rain in spain"
# y=re.findall('ai',s)
# validate password and url

import logging
logging.basicConfig(
    level=logging.Debug,
    filemode='app.log'
    filename='a',
    format='@'
)
import pylint as p
