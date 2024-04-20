import pandas as pd
import plotly.express as px

df_pd= px.data.iris()
# print(df_pd)

l=['Country Name', 'Country Code']
fact_list=['literacy_rate_updated','pop_tot_updated','gdp_current_updated']
# fact_list=['gdp_current_updated']
i=0
df_final = pd.read_csv('income_cat.csv')
for fact in fact_list:
    df_fact = pd.read_csv('./Data_files/' + fact + '.csv')
    df_fact = df_fact.drop(['2023'], axis=1, errors='ignore')
    mask = df_fact['Country Name'] == 'World'
    df_fact = df_fact[~mask]
    mask = df_fact['Country Name'] == "High income"
    df_fact = df_fact[~mask]
    mask = df_fact['Country Name'] == 'Low income'
    df_fact = df_fact[~mask]
    mask = df_fact['Country Name'] == 'Lower middle income'
    df_fact = df_fact[~mask]
    mask = df_fact['Country Name'] == 'Upper middle income'
    df_fact = df_fact[~mask]
    header_list=['Country Name', 'Country Code',fact+" "+ 'Indicator Name', fact+" "+ 'Indicator Code', fact+" "+ '1960', fact+" "+ '1961', fact+" "+ '1962', fact+" "+ '1963', fact+" "+ '1964', fact+" "+ '1965', fact+" "+ '1966', fact+" "+ '1967', fact+" "+ '1968', fact+" "+ '1969', fact+" "+ '1970', fact+" "+ '1971', fact+" "+ '1972', fact+" "+ '1973', fact+" "+ '1974', fact+" "+ '1975', fact+" "+ '1976', fact+" "+ '1977', fact+" "+ '1978', fact+" "+ '1979', fact+" "+ '1980', fact+" "+ '1981', fact+" "+ '1982', fact+" "+ '1983', fact+" "+ '1984', fact+" "+ '1985', fact+" "+ '1986', fact+" "+ '1987', fact+" "+ '1988', fact+" "+ '1989', fact+" "+ '1990', fact+" "+ '1991', fact+" "+ '1992', fact+" "+ '1993', fact+" "+ '1994', fact+" "+ '1995', fact+" "+ '1996', fact+" "+ '1997', fact+" "+ '1998', fact+" "+ '1999', fact+" "+ '2000', fact+" "+ '2001', fact+" "+ '2002', fact+" "+ '2003', fact+" "+ '2004', fact+" "+ '2005', fact+" "+ '2006', fact+" "+ '2007', fact+" "+ '2008', fact+" "+ '2009', fact+" "+ '2010', fact+" "+ '2011', fact+" "+ '2012', fact+" "+ '2013', fact+" "+ '2014', fact+" "+ '2015', fact+" "+ '2016', fact+" "+ '2017', fact+" "+ '2018', fact+" "+ '2019', fact+" "+ '2020', fact+" "+ '2021', fact+" "+ '2022']
    df=df_fact.set_axis(header_list,axis=1)
    df_final = pd.merge(df_final, df, on=l)

# df_final.to_csv('test.csv')

fig = px.parallel_coordinates(df_final,color='Income Group',
                              dimensions=['literacy_rate_updated'+' 2018','pop_tot_updated'+' 2018','gdp_current_updated'+' 2018'],
                              color_continuous_scale=px.colors.diverging.Tealrose,
                              color_continuous_midpoint=2)

fig.show()