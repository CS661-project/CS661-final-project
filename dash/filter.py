import pandas as pd
import math
filename='./Data_files/percent_pop_in_services'
df = pd.read_csv(filename+".csv")
# col=df.shape[1]
# print(col)

countries=[
"Africa Eastern and Southern",
"Africa Western and Central",
"Arab World",
"Central Europe and the Baltics",
"Caribbean small states",
"East Asia & Pacific (excluding high income)",
"Early-demographic dividend",
"East Asia & Pacific",
"Europe & Central Asia (excluding high income)",
"Europe & Central Asia",
"Euro area",
"European Union",
"Fragile and conflict affected situations",
"High income",
"Heavily indebted poor countries (HIPC)",
"IBRD only",
"IDA & IBRD total",
"IDA total",
"IDA blend",
"IDA only",
"Latin America & Caribbean (excluding high income)",
"Latin America & Caribbean",
"Least developed countries: UN classification",
"Low income",
"Lower middle income",
"Low & middle income",
"Late-demographic dividend",
"Middle East & North Africa",
"Middle income",
"Middle East & North Africa (excluding high income)",
"North America",
"OECD members",
"Other small states",
"Pre-demographic dividend",
"Pacific island small states",
"Post-demographic dividend",
"South Asia",
"Sub-Saharan Africa (excluding high income)",
"Sub-Saharan Africa",
"Small states",
"East Asia & Pacific (IDA & IBRD)",
"Europe & Central Asia (IDA & IBRD)",
"Latin America & Caribbean (IDA & IBRD)",
"Middle East & North Africa (IDA & IBRD)",
"South Asia (IDA & IBRD)",
"Sub-Saharan Africa (IDA & IBRD)",
"Upper middle income",
# "World",
"Sub-Saharan Africa (IDA & IBRD countries)",
"East Asia & Pacific (IDA & IBRD countries)",
"Europe & Central Asia (IDA & IBRD countries)",
"Latin America & the Caribbean (IDA & IBRD countries)",
"Middle East & North Africa (IDA & IBRD countries)",
"Not classified",
]

for row in df.iterrows():
    if row[1]['Country Name'] in countries:
        df=df.drop(row[0])

for iter in range(2):
    if(iter==1):
        df= pd.read_csv(filename+"_updated.csv")
    for index,row in df.iterrows():
        # print(df.at[index,'2020'])
        b_yr=1960
        f_yr=-1
        count=0
        delta=0
        delta_f=0
        # print(row[str("1960")])
        for i in range(1960,2023):
            # print(row[str(i)],'\n')
            #no value read till now
            if(count==0 and pd.isna(row[str(i)])):
                delta=0
                f_yr=-1
                # print("in1")
                continue
            #value read but not first
            elif(pd.isna(row[str(i)])!=True and count!=0):
                delta=0
                f_yr=-1
                b_yr=i
                # print("in2")

            # first value read
            elif(pd.isna(row[str(i)])!=True and count==0):
                delta=0
                f_yr=-1
                b_yr=i
                count=1
                # print(index,i,"in3")
            elif(pd.isna(row[str(i)]) and count!=0):
                # print(index,i,"in4")
                if(f_yr!=-1):
                    df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                    # print(row[str(b_yr)]+delta*(i-b_yr))
                    # print()
                else:
                    for j in range(b_yr+1,2023):
                        if(pd.isna(row[str(j)])):
                            continue
                        else:
                            f_yr=j
                            delta=(row[str(j)]-row[str(b_yr)])/(j-b_yr)
                            break
                    if(f_yr!=-1):
                        df.at[index,str(i)]=row[str(b_yr)]+delta*(i-b_yr)
                        # print(row[str(b_yr)]+delta*(i-b_yr))
                        # print()
                    else:
                        if(iter==1):
                            print("in final case")
                            # df.to_csv(filename+"_updated.csv")
                            # df = pd.read_csv(filename+"_updated.csv")
                            for k in range(5):
                                delta_f=delta_f+(row[str(b_yr-k)]-row[str(b_yr-k-1)])/row[str(b_yr-k-1)]
                            delta_f=delta_f/5
                            for j in range(b_yr+1,2023):
                                df.at[index,str(j)]=row[str(b_yr)]*(pow((1+delta_f),(j-b_yr)))
                                print(index,row[str(b_yr)]*(pow((1+delta_f),(j-b_yr))))
                            break

    # print(df)
    df.to_csv(filename+"_updated.csv")