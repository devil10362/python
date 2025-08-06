

import pandas as pd

x=pd.DataFrame({"name":["x","y"],"age":[20,30]},index=[1,2])
y=pd.DataFrame({"name":["a","b"],"age":[40,50]},index=[3,4])
print(pd.concat([x,y]))