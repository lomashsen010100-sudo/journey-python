import pandas as pd 

df1=pd.DataFrame({
    "name" : ["AMAN", "RIYA", "POOJA"],
    "marks" : [80, 70, 90]
})

df2=pd.DataFrame({
    "name" : ["RAHUL", "ROSHAN", "RAM"],
    "marks" : [90, 80, 70]
})

result=pd.concat([df1, df2])
print(result)