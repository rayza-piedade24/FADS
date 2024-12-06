```python
import numpy as np
```


```python
import pandas as pd
```


```python
import seaborn as sns
```


```python
from matplotlib import pyplot as plt
```


```python

%matplotlib inline


```


```python
datcensus_df = pd.read_csv("data_agric_census_freg.csv")
```


```python
census_df = datcensus_df
```


```python
census_df.shape
```




    (3068, 16)




```python
census_df.info()
```

    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 3068 entries, 0 to 3067
    Data columns (total 16 columns):
     #   Column         Non-Null Count  Dtype  
    ---  ------         --------------  -----  
     0   freguesia      3068 non-null   object 
     1   municipality   3068 non-null   object 
     2   NUTS2          3068 non-null   object 
     3   e_none         3068 non-null   int64  
     4   e_basic        3068 non-null   int64  
     5   e_secondary    3068 non-null   int64  
     6   e_superior     3068 non-null   int64  
     7   l_family       3068 non-null   int64  
     8   l_holder       3068 non-null   int64  
     9   l_spouse       3068 non-null   int64  
     10  l_other_fam    3068 non-null   int64  
     11  l_regular      3068 non-null   int64  
     12  l_non_regular  3068 non-null   int64  
     13  l_non_hired    3068 non-null   int64  
     14  value_eur      3068 non-null   int64  
     15  area_ha        3068 non-null   float64
    dtypes: float64(1), int64(12), object(3)
    memory usage: 383.6+ KB
    


```python
census_df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>freguesia</th>
      <th>municipality</th>
      <th>NUTS2</th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aboim das Choças</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>15</td>
      <td>61</td>
      <td>11</td>
      <td>7</td>
      <td>34</td>
      <td>15</td>
      <td>13</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>101072</td>
      <td>1921.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aguiã</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>24</td>
      <td>68</td>
      <td>5</td>
      <td>2</td>
      <td>70</td>
      <td>38</td>
      <td>27</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>156561</td>
      <td>1642.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ázere</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>3</td>
      <td>48</td>
      <td>12</td>
      <td>5</td>
      <td>18</td>
      <td>11</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>140132</td>
      <td>2428.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cabana Maior</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>24</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
      <td>25</td>
      <td>15</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>189450</td>
      <td>152.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabreiro</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>66</td>
      <td>107</td>
      <td>23</td>
      <td>8</td>
      <td>114</td>
      <td>71</td>
      <td>32</td>
      <td>11</td>
      <td>6</td>
      <td>3</td>
      <td>0</td>
      <td>612235</td>
      <td>221.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.set(style='white',font_scale=1.3, rc={'figure.figsize':(20,20)})
ax=census_df.hist(bins=20,color='red' )

```


    
![png](output_10_0.png)
    



```python
g = sns.PairGrid(census_df, hue="NUTS2")
g.map(sns.scatterplot)
g.add_legend()
```




    <seaborn.axisgrid.PairGrid at 0x20b1a09c1a0>




    
![png](output_11_1.png)
    



```python
values = ['Norte','Centro','Área Metropolitana de Lisboa', 'Alentejo', 'Algarve']
```


```python
df1 = census_df.loc[census_df['NUTS2'].isin(values)].copy()
```


```python
df1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>freguesia</th>
      <th>municipality</th>
      <th>NUTS2</th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Aboim das Choças</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>15</td>
      <td>61</td>
      <td>11</td>
      <td>7</td>
      <td>34</td>
      <td>15</td>
      <td>13</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>101072</td>
      <td>1921.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Aguiã</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>24</td>
      <td>68</td>
      <td>5</td>
      <td>2</td>
      <td>70</td>
      <td>38</td>
      <td>27</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>156561</td>
      <td>1642.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Ázere</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>3</td>
      <td>48</td>
      <td>12</td>
      <td>5</td>
      <td>18</td>
      <td>11</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>140132</td>
      <td>2428.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Cabana Maior</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>24</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
      <td>25</td>
      <td>15</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>189450</td>
      <td>152.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Cabreiro</td>
      <td>Arcos de Valdevez</td>
      <td>Norte</td>
      <td>66</td>
      <td>107</td>
      <td>23</td>
      <td>8</td>
      <td>114</td>
      <td>71</td>
      <td>32</td>
      <td>11</td>
      <td>6</td>
      <td>3</td>
      <td>0</td>
      <td>612235</td>
      <td>221.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
sns.lmplot( x="value_eur", y="area_ha", data=df1, fit_reg=False, hue='NUTS2', legend=True)
```




    <seaborn.axisgrid.FacetGrid at 0x20b1a09cec0>




    
![png](output_15_1.png)
    



```python
sns.lmplot( x="value_eur", y="l_family", data=df1, fit_reg=False, hue='NUTS2', legend=True)
```




    <seaborn.axisgrid.FacetGrid at 0x20b257156d0>




    
![png](output_16_1.png)
    



```python
sns.lmplot( x="value_eur", y="l_regular", data=df1, fit_reg=False, hue='NUTS2', legend=True)
```




    <seaborn.axisgrid.FacetGrid at 0x20b25799bd0>




    
![png](output_17_1.png)
    



```python
df1.drop(['municipality', 'freguesia', 'NUTS2'], axis = 1, inplace = True)
```


```python
df1.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>61</td>
      <td>11</td>
      <td>7</td>
      <td>34</td>
      <td>15</td>
      <td>13</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>101072</td>
      <td>1921.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>68</td>
      <td>5</td>
      <td>2</td>
      <td>70</td>
      <td>38</td>
      <td>27</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>156561</td>
      <td>1642.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>48</td>
      <td>12</td>
      <td>5</td>
      <td>18</td>
      <td>11</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>140132</td>
      <td>2428.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
      <td>25</td>
      <td>15</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>189450</td>
      <td>152.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>66</td>
      <td>107</td>
      <td>23</td>
      <td>8</td>
      <td>114</td>
      <td>71</td>
      <td>32</td>
      <td>11</td>
      <td>6</td>
      <td>3</td>
      <td>0</td>
      <td>612235</td>
      <td>221.4</td>
    </tr>
  </tbody>
</table>
</div>




```python
df1.describe(include='all')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2858.000000</td>
      <td>2.858000e+03</td>
      <td>2858.000000</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>24.181246</td>
      <td>131.563331</td>
      <td>29.861092</td>
      <td>24.155353</td>
      <td>68.982855</td>
      <td>38.526242</td>
      <td>20.178446</td>
      <td>10.386984</td>
      <td>20.017145</td>
      <td>10.136459</td>
      <td>3.486704</td>
      <td>2.178883e+06</td>
      <td>3961.614836</td>
    </tr>
    <tr>
      <th>std</th>
      <td>23.915059</td>
      <td>115.296087</td>
      <td>28.110898</td>
      <td>25.185215</td>
      <td>60.683535</td>
      <td>33.733408</td>
      <td>19.496991</td>
      <td>10.401193</td>
      <td>68.855675</td>
      <td>25.875951</td>
      <td>20.248958</td>
      <td>5.092582e+06</td>
      <td>7374.743620</td>
    </tr>
    <tr>
      <th>min</th>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>0.000000</td>
      <td>1.103000e+03</td>
      <td>0.000000</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>8.000000</td>
      <td>54.000000</td>
      <td>11.000000</td>
      <td>8.000000</td>
      <td>28.000000</td>
      <td>16.000000</td>
      <td>7.000000</td>
      <td>4.000000</td>
      <td>1.000000</td>
      <td>1.000000</td>
      <td>0.000000</td>
      <td>3.399678e+05</td>
      <td>1012.775000</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>18.000000</td>
      <td>101.500000</td>
      <td>22.000000</td>
      <td>17.000000</td>
      <td>54.000000</td>
      <td>30.000000</td>
      <td>15.000000</td>
      <td>7.000000</td>
      <td>5.000000</td>
      <td>3.000000</td>
      <td>0.000000</td>
      <td>7.599300e+05</td>
      <td>2198.950000</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>32.000000</td>
      <td>178.000000</td>
      <td>39.000000</td>
      <td>32.000000</td>
      <td>90.000000</td>
      <td>51.000000</td>
      <td>27.000000</td>
      <td>14.000000</td>
      <td>17.000000</td>
      <td>9.000000</td>
      <td>1.000000</td>
      <td>1.851618e+06</td>
      <td>4332.025000</td>
    </tr>
    <tr>
      <th>max</th>
      <td>211.000000</td>
      <td>1102.000000</td>
      <td>289.000000</td>
      <td>212.000000</td>
      <td>822.000000</td>
      <td>401.000000</td>
      <td>278.000000</td>
      <td>144.000000</td>
      <td>2646.000000</td>
      <td>601.000000</td>
      <td>751.000000</td>
      <td>1.023541e+08</td>
      <td>171049.600000</td>
    </tr>
  </tbody>
</table>
</div>




```python
fig, axes = plt.subplots(nrows=3, ncols=5,figsize=(12,18))
fig.suptitle('Outliers\n', size = 25)

sns.boxplot(ax=axes[0, 0], data=df1['e_none'], palette='Spectral').set_title("education none")
sns.boxplot(ax=axes[0, 1], data=df1['e_basic'], palette='Spectral').set_title("education basic")
sns.boxplot(ax=axes[0, 2], data=df1['e_secondary'], palette='Spectral').set_title("education secondary")
sns.boxplot(ax=axes[0, 3], data=df1['e_superior'], palette='Spectral').set_title("education superior")
sns.boxplot(ax=axes[0, 4], data=df1['l_family'], palette='Spectral').set_title("labour family")
sns.boxplot(ax=axes[1, 0], data=df1['l_holder'], palette='Spectral').set_title("labour holder")
sns.boxplot(ax=axes[1, 1], data=df1['l_spouse'], palette='Spectral').set_title("labour spouse")
sns.boxplot(ax=axes[1, 2], data=df1['l_other_fam'], palette='Spectral').set_title("labour other family")
sns.boxplot(ax=axes[1, 3], data=df1['l_regular'], palette='Spectral').set_title("labour regular")
sns.boxplot(ax=axes[1, 4], data=df1['l_non_regular'], palette='Spectral').set_title("labour non regular")
sns.boxplot(ax=axes[2, 0], data=df1['l_non_hired'], palette='Spectral').set_title("labour non hired")
sns.boxplot(ax=axes[2, 1], data=df1['value_eur'], palette='Spectral').set_title("production value")
sns.boxplot(ax=axes[2, 2], data=df1['area_ha'], palette='Spectral').set_title("production area")

plt.tight_layout()
```

    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:4: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[0, 0], data=df1['e_none'], palette='Spectral').set_title("education none")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:5: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[0, 1], data=df1['e_basic'], palette='Spectral').set_title("education basic")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:6: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[0, 2], data=df1['e_secondary'], palette='Spectral').set_title("education secondary")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:7: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[0, 3], data=df1['e_superior'], palette='Spectral').set_title("education superior")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:8: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[0, 4], data=df1['l_family'], palette='Spectral').set_title("labour family")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:9: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[1, 0], data=df1['l_holder'], palette='Spectral').set_title("labour holder")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:10: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[1, 1], data=df1['l_spouse'], palette='Spectral').set_title("labour spouse")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:11: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[1, 2], data=df1['l_other_fam'], palette='Spectral').set_title("labour other family")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:12: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[1, 3], data=df1['l_regular'], palette='Spectral').set_title("labour regular")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:13: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[1, 4], data=df1['l_non_regular'], palette='Spectral').set_title("labour non regular")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:14: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[2, 0], data=df1['l_non_hired'], palette='Spectral').set_title("labour non hired")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:15: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[2, 1], data=df1['value_eur'], palette='Spectral').set_title("production value")
    C:\Users\Rayza\AppData\Local\Temp\ipykernel_13332\1237962810.py:16: FutureWarning: 
    
    Passing `palette` without assigning `hue` is deprecated and will be removed in v0.14.0. Assign the `x` variable to `hue` and set `legend=False` for the same effect.
    
      sns.boxplot(ax=axes[2, 2], data=df1['area_ha'], palette='Spectral').set_title("production area")
    


    
![png](output_21_1.png)
    



```python
df2 = df1.copy()
```


```python
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
df3=scaler.fit_transform(df2)
```


```python
df3
```




    array([[-0.38397783, -0.61212554, -0.67107044, ..., -0.17222191,
            -0.40807876, -0.27662952],
           [-0.00758005, -0.55140166, -0.88454814, ..., -0.17222191,
            -0.39718081, -0.31448152],
           [-0.88584153, -0.72489845, -0.63549082, ..., -0.17222191,
            -0.40040744, -0.20791002],
           ...,
           [-0.96948548, -1.1152662 , -1.06244623, ..., -0.17222191,
            -0.42605354, -0.21104288],
           [ 2.45991648,  0.64572612,  0.82327352, ...,  1.06262558,
             1.14214756,  0.06873105],
           [-0.96948548, -0.97646878, -0.95570738, ..., -0.17222191,
            -0.38717863, -0.12767625]])




```python
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(df3)
    wcss.append(kmeans.inertia_)
    
plt.subplots(nrows=1, ncols=1,figsize=(10,10))
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
```


    
![png](output_25_0.png)
    



```python
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot
pyplot.figure(figsize=(12, 5))
dendrogram = sch.dendrogram(sch.linkage(df3, method = 'ward'))
plt.title('Dendrogram')
plt.ylabel('Euclidean distances')
plt.show()
```


    
![png](output_26_0.png)
    



```python
df_kmeans = df2.copy()
```


```python
kmeans = KMeans(n_clusters = 5, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(df_kmeans)
```


```python
df_kmeans
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>61</td>
      <td>11</td>
      <td>7</td>
      <td>34</td>
      <td>15</td>
      <td>13</td>
      <td>6</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>101072</td>
      <td>1921.9</td>
    </tr>
    <tr>
      <th>1</th>
      <td>24</td>
      <td>68</td>
      <td>5</td>
      <td>2</td>
      <td>70</td>
      <td>38</td>
      <td>27</td>
      <td>5</td>
      <td>0</td>
      <td>2</td>
      <td>0</td>
      <td>156561</td>
      <td>1642.8</td>
    </tr>
    <tr>
      <th>2</th>
      <td>3</td>
      <td>48</td>
      <td>12</td>
      <td>5</td>
      <td>18</td>
      <td>11</td>
      <td>5</td>
      <td>2</td>
      <td>0</td>
      <td>1</td>
      <td>0</td>
      <td>140132</td>
      <td>2428.6</td>
    </tr>
    <tr>
      <th>3</th>
      <td>24</td>
      <td>34</td>
      <td>5</td>
      <td>0</td>
      <td>25</td>
      <td>15</td>
      <td>9</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>189450</td>
      <td>152.7</td>
    </tr>
    <tr>
      <th>4</th>
      <td>66</td>
      <td>107</td>
      <td>23</td>
      <td>8</td>
      <td>114</td>
      <td>71</td>
      <td>32</td>
      <td>11</td>
      <td>6</td>
      <td>3</td>
      <td>0</td>
      <td>612235</td>
      <td>221.4</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2853</th>
      <td>7</td>
      <td>20</td>
      <td>9</td>
      <td>1</td>
      <td>10</td>
      <td>6</td>
      <td>1</td>
      <td>2</td>
      <td>1</td>
      <td>0</td>
      <td>0</td>
      <td>477153</td>
      <td>565.2</td>
    </tr>
    <tr>
      <th>2854</th>
      <td>34</td>
      <td>108</td>
      <td>36</td>
      <td>22</td>
      <td>55</td>
      <td>38</td>
      <td>9</td>
      <td>8</td>
      <td>9</td>
      <td>1</td>
      <td>2</td>
      <td>2025760</td>
      <td>525.2</td>
    </tr>
    <tr>
      <th>2855</th>
      <td>1</td>
      <td>3</td>
      <td>0</td>
      <td>2</td>
      <td>3</td>
      <td>1</td>
      <td>2</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>0</td>
      <td>9550</td>
      <td>2405.5</td>
    </tr>
    <tr>
      <th>2856</th>
      <td>83</td>
      <td>206</td>
      <td>53</td>
      <td>52</td>
      <td>90</td>
      <td>48</td>
      <td>22</td>
      <td>20</td>
      <td>208</td>
      <td>23</td>
      <td>25</td>
      <td>7994345</td>
      <td>4468.4</td>
    </tr>
    <tr>
      <th>2857</th>
      <td>1</td>
      <td>19</td>
      <td>3</td>
      <td>2</td>
      <td>8</td>
      <td>5</td>
      <td>2</td>
      <td>1</td>
      <td>1</td>
      <td>1</td>
      <td>0</td>
      <td>207489</td>
      <td>3020.2</td>
    </tr>
  </tbody>
</table>
<p>2858 rows × 13 columns</p>
</div>




```python
df_kmeans = df1.copy()
```


```python
df_kmeans['Cluster'] = y_kmeans
```


```python
df_kmeans['Cluster'].value_counts()
```




    Cluster
    0    2431
    2     303
    4      95
    1      25
    3       4
    Name: count, dtype: int64




```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_kmeans, x='e_secondary', y='value_eur', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='e_secondary', ylabel='value_eur'>




    
![png](output_33_1.png)
    



```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_kmeans, x='e_superior', y='value_eur', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='e_superior', ylabel='value_eur'>




    
![png](output_34_1.png)
    



```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_kmeans, x='l_family', y='value_eur', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='l_family', ylabel='value_eur'>




    
![png](output_35_1.png)
    



```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_kmeans, x='l_non_hired', y='value_eur', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='l_non_hired', ylabel='value_eur'>




    
![png](output_36_1.png)
    



```python
df_AgglomerativeC = df3.copy()
```


```python
from sklearn.cluster import AgglomerativeClustering
```


```python
AgglomerativeC = AgglomerativeClustering(n_clusters=4, metric = 'euclidean', linkage = 'ward')
y_AgglomerativeC = AgglomerativeC.fit_predict(df_AgglomerativeC)
```


```python
df_AgglomerativeC = df2.copy()
```


```python
df_AgglomerativeC['Cluster'] = y_AgglomerativeC
df_AgglomerativeC['Cluster'].value_counts()
```




    Cluster
    1    2134
    0     685
    3      38
    2       1
    Name: count, dtype: int64




```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_AgglomerativeC, x='e_secondary', y='value_eur', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='e_secondary', ylabel='value_eur'>




    
![png](output_42_1.png)
    



```python
from sklearn.preprocessing import StandardScaler

std_scaler = StandardScaler()
data_cluster=df1.copy()
data_cluster[data_cluster.columns]=std_scaler.fit_transform(data_cluster)

```


```python
data_cluster.describe()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>e_none</th>
      <th>e_basic</th>
      <th>e_secondary</th>
      <th>e_superior</th>
      <th>l_family</th>
      <th>l_holder</th>
      <th>l_spouse</th>
      <th>l_other_fam</th>
      <th>l_regular</th>
      <th>l_non_regular</th>
      <th>l_non_hired</th>
      <th>value_eur</th>
      <th>area_ha</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>count</th>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2.858000e+03</td>
      <td>2858.000000</td>
      <td>2.858000e+03</td>
    </tr>
    <tr>
      <th>mean</th>
      <td>6.464000e-17</td>
      <td>9.944615e-17</td>
      <td>-1.988923e-17</td>
      <td>-9.944615e-18</td>
      <td>4.475077e-17</td>
      <td>1.988923e-17</td>
      <td>-4.972307e-17</td>
      <td>7.707077e-17</td>
      <td>9.944615e-18</td>
      <td>-3.480615e-17</td>
      <td>-1.988923e-17</td>
      <td>0.000000</td>
      <td>-9.944615e-18</td>
    </tr>
    <tr>
      <th>std</th>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175e+00</td>
      <td>1.000175</td>
      <td>1.000175e+00</td>
    </tr>
    <tr>
      <th>min</th>
      <td>-1.011307e+00</td>
      <td>-1.141291e+00</td>
      <td>-1.062446e+00</td>
      <td>-9.592763e-01</td>
      <td>-1.136963e+00</td>
      <td>-1.142280e+00</td>
      <td>-1.035133e+00</td>
      <td>-9.988087e-01</td>
      <td>-2.907625e-01</td>
      <td>-3.918014e-01</td>
      <td>-1.722219e-01</td>
      <td>-0.427713</td>
      <td>-5.372808e-01</td>
    </tr>
    <tr>
      <th>25%</th>
      <td>-6.767317e-01</td>
      <td>-6.728494e-01</td>
      <td>-6.710704e-01</td>
      <td>-6.415740e-01</td>
      <td>-6.754720e-01</td>
      <td>-6.678894e-01</td>
      <td>-6.760404e-01</td>
      <td>-6.141701e-01</td>
      <td>-2.762368e-01</td>
      <td>-3.531487e-01</td>
      <td>-1.722219e-01</td>
      <td>-0.361160</td>
      <td>-3.999266e-01</td>
    </tr>
    <tr>
      <th>50%</th>
      <td>-2.585119e-01</td>
      <td>-2.607946e-01</td>
      <td>-2.796946e-01</td>
      <td>-2.841590e-01</td>
      <td>-2.469447e-01</td>
      <td>-2.527979e-01</td>
      <td>-2.656488e-01</td>
      <td>-3.256912e-01</td>
      <td>-2.181341e-01</td>
      <td>-2.758433e-01</td>
      <td>-1.722219e-01</td>
      <td>-0.278680</td>
      <td>-2.390555e-01</td>
    </tr>
    <tr>
      <th>75%</th>
      <td>3.269958e-01</td>
      <td>4.028306e-01</td>
      <td>3.251589e-01</td>
      <td>3.115327e-01</td>
      <td>3.464008e-01</td>
      <td>3.698393e-01</td>
      <td>3.499385e-01</td>
      <td>3.474263e-01</td>
      <td>-4.382606e-02</td>
      <td>-4.392719e-02</td>
      <td>-1.228280e-01</td>
      <td>-0.064274</td>
      <td>5.023564e-02</td>
    </tr>
    <tr>
      <th>max</th>
      <td>7.813129e+00</td>
      <td>8.418382e+00</td>
      <td>9.220063e+00</td>
      <td>7.459834e+00</td>
      <td>1.241109e+01</td>
      <td>1.074713e+01</td>
      <td>1.322597e+01</td>
      <td>1.284818e+01</td>
      <td>3.814417e+01</td>
      <td>2.283846e+01</td>
      <td>3.692260e+01</td>
      <td>19.674262</td>
      <td>2.266075e+01</td>
    </tr>
  </tbody>
</table>
</div>




```python
from sklearn.decomposition import PCA
pca_2 = PCA(2)
pca_2_result = pca_2.fit_transform(data_cluster)

print ('Cumulative variance explained by 2 principal components: {:.2%}'.format(np.sum(pca_2.explained_variance_ratio_)))
```

    Cumulative variance explained by 2 principal components: 71.55%
    


```python
sns.set(style='white', rc={'figure.figsize':(9,6)},font_scale=1.1)

plt.scatter(x=pca_2_result[:, 0], y=pca_2_result[:, 1], color='red',lw=0.1)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Data represented by the 2 strongest principal components',fontweight='bold')
plt.show()
```


    
![png](output_46_0.png)
    



```python
from sklearn.ensemble import IsolationForest
df2 = df1.copy()
```


```python
model=IsolationForest(n_estimators=150, max_samples='auto', contamination=float(0.1), max_features=1.0)
model.fit(df2)
```




<style>#sk-container-id-1 {
  /* Definition of color scheme common for light and dark mode */
  --sklearn-color-text: black;
  --sklearn-color-line: gray;
  /* Definition of color scheme for unfitted estimators */
  --sklearn-color-unfitted-level-0: #fff5e6;
  --sklearn-color-unfitted-level-1: #f6e4d2;
  --sklearn-color-unfitted-level-2: #ffe0b3;
  --sklearn-color-unfitted-level-3: chocolate;
  /* Definition of color scheme for fitted estimators */
  --sklearn-color-fitted-level-0: #f0f8ff;
  --sklearn-color-fitted-level-1: #d4ebff;
  --sklearn-color-fitted-level-2: #b3dbfd;
  --sklearn-color-fitted-level-3: cornflowerblue;

  /* Specific color for light theme */
  --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, white)));
  --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, black)));
  --sklearn-color-icon: #696969;

  @media (prefers-color-scheme: dark) {
    /* Redefinition of color scheme for dark theme */
    --sklearn-color-text-on-default-background: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-background: var(--sg-background-color, var(--theme-background, var(--jp-layout-color0, #111)));
    --sklearn-color-border-box: var(--sg-text-color, var(--theme-code-foreground, var(--jp-content-font-color1, white)));
    --sklearn-color-icon: #878787;
  }
}

#sk-container-id-1 {
  color: var(--sklearn-color-text);
}

#sk-container-id-1 pre {
  padding: 0;
}

#sk-container-id-1 input.sk-hidden--visually {
  border: 0;
  clip: rect(1px 1px 1px 1px);
  clip: rect(1px, 1px, 1px, 1px);
  height: 1px;
  margin: -1px;
  overflow: hidden;
  padding: 0;
  position: absolute;
  width: 1px;
}

#sk-container-id-1 div.sk-dashed-wrapped {
  border: 1px dashed var(--sklearn-color-line);
  margin: 0 0.4em 0.5em 0.4em;
  box-sizing: border-box;
  padding-bottom: 0.4em;
  background-color: var(--sklearn-color-background);
}

#sk-container-id-1 div.sk-container {
  /* jupyter's `normalize.less` sets `[hidden] { display: none; }`
     but bootstrap.min.css set `[hidden] { display: none !important; }`
     so we also need the `!important` here to be able to override the
     default hidden behavior on the sphinx rendered scikit-learn.org.
     See: https://github.com/scikit-learn/scikit-learn/issues/21755 */
  display: inline-block !important;
  position: relative;
}

#sk-container-id-1 div.sk-text-repr-fallback {
  display: none;
}

div.sk-parallel-item,
div.sk-serial,
div.sk-item {
  /* draw centered vertical line to link estimators */
  background-image: linear-gradient(var(--sklearn-color-text-on-default-background), var(--sklearn-color-text-on-default-background));
  background-size: 2px 100%;
  background-repeat: no-repeat;
  background-position: center center;
}

/* Parallel-specific style estimator block */

#sk-container-id-1 div.sk-parallel-item::after {
  content: "";
  width: 100%;
  border-bottom: 2px solid var(--sklearn-color-text-on-default-background);
  flex-grow: 1;
}

#sk-container-id-1 div.sk-parallel {
  display: flex;
  align-items: stretch;
  justify-content: center;
  background-color: var(--sklearn-color-background);
  position: relative;
}

#sk-container-id-1 div.sk-parallel-item {
  display: flex;
  flex-direction: column;
}

#sk-container-id-1 div.sk-parallel-item:first-child::after {
  align-self: flex-end;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:last-child::after {
  align-self: flex-start;
  width: 50%;
}

#sk-container-id-1 div.sk-parallel-item:only-child::after {
  width: 0;
}

/* Serial-specific style estimator block */

#sk-container-id-1 div.sk-serial {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: var(--sklearn-color-background);
  padding-right: 1em;
  padding-left: 1em;
}


/* Toggleable style: style used for estimator/Pipeline/ColumnTransformer box that is
clickable and can be expanded/collapsed.
- Pipeline and ColumnTransformer use this feature and define the default style
- Estimators will overwrite some part of the style using the `sk-estimator` class
*/

/* Pipeline and ColumnTransformer style (default) */

#sk-container-id-1 div.sk-toggleable {
  /* Default theme specific background. It is overwritten whether we have a
  specific estimator or a Pipeline/ColumnTransformer */
  background-color: var(--sklearn-color-background);
}

/* Toggleable label */
#sk-container-id-1 label.sk-toggleable__label {
  cursor: pointer;
  display: block;
  width: 100%;
  margin-bottom: 0;
  padding: 0.5em;
  box-sizing: border-box;
  text-align: center;
}

#sk-container-id-1 label.sk-toggleable__label-arrow:before {
  /* Arrow on the left of the label */
  content: "▸";
  float: left;
  margin-right: 0.25em;
  color: var(--sklearn-color-icon);
}

#sk-container-id-1 label.sk-toggleable__label-arrow:hover:before {
  color: var(--sklearn-color-text);
}

/* Toggleable content - dropdown */

#sk-container-id-1 div.sk-toggleable__content {
  max-height: 0;
  max-width: 0;
  overflow: hidden;
  text-align: left;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content pre {
  margin: 0.2em;
  border-radius: 0.25em;
  color: var(--sklearn-color-text);
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-toggleable__content.fitted pre {
  /* unfitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

#sk-container-id-1 input.sk-toggleable__control:checked~div.sk-toggleable__content {
  /* Expand drop-down */
  max-height: 200px;
  max-width: 100%;
  overflow: auto;
}

#sk-container-id-1 input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {
  content: "▾";
}

/* Pipeline/ColumnTransformer-specific style */

#sk-container-id-1 div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-label.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator-specific style */

/* Colorize estimator box */
#sk-container-id-1 div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted input.sk-toggleable__control:checked~label.sk-toggleable__label {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

#sk-container-id-1 div.sk-label label.sk-toggleable__label,
#sk-container-id-1 div.sk-label label {
  /* The background is the default theme color */
  color: var(--sklearn-color-text-on-default-background);
}

/* On hover, darken the color of the background */
#sk-container-id-1 div.sk-label:hover label.sk-toggleable__label {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-unfitted-level-2);
}

/* Label box, darken color on hover, fitted */
#sk-container-id-1 div.sk-label.fitted:hover label.sk-toggleable__label.fitted {
  color: var(--sklearn-color-text);
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Estimator label */

#sk-container-id-1 div.sk-label label {
  font-family: monospace;
  font-weight: bold;
  display: inline-block;
  line-height: 1.2em;
}

#sk-container-id-1 div.sk-label-container {
  text-align: center;
}

/* Estimator-specific */
#sk-container-id-1 div.sk-estimator {
  font-family: monospace;
  border: 1px dotted var(--sklearn-color-border-box);
  border-radius: 0.25em;
  box-sizing: border-box;
  margin-bottom: 0.5em;
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-0);
}

#sk-container-id-1 div.sk-estimator.fitted {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-0);
}

/* on hover */
#sk-container-id-1 div.sk-estimator:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-2);
}

#sk-container-id-1 div.sk-estimator.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-2);
}

/* Specification for estimator info (e.g. "i" and "?") */

/* Common style for "i" and "?" */

.sk-estimator-doc-link,
a:link.sk-estimator-doc-link,
a:visited.sk-estimator-doc-link {
  float: right;
  font-size: smaller;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1em;
  height: 1em;
  width: 1em;
  text-decoration: none !important;
  margin-left: 1ex;
  /* unfitted */
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
  color: var(--sklearn-color-unfitted-level-1);
}

.sk-estimator-doc-link.fitted,
a:link.sk-estimator-doc-link.fitted,
a:visited.sk-estimator-doc-link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
div.sk-estimator:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover,
div.sk-label-container:hover .sk-estimator-doc-link:hover,
.sk-estimator-doc-link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

div.sk-estimator.fitted:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover,
div.sk-label-container:hover .sk-estimator-doc-link.fitted:hover,
.sk-estimator-doc-link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

/* Span, style for the box shown on hovering the info icon */
.sk-estimator-doc-link span {
  display: none;
  z-index: 9999;
  position: relative;
  font-weight: normal;
  right: .2ex;
  padding: .5ex;
  margin: .5ex;
  width: min-content;
  min-width: 20ex;
  max-width: 50ex;
  color: var(--sklearn-color-text);
  box-shadow: 2pt 2pt 4pt #999;
  /* unfitted */
  background: var(--sklearn-color-unfitted-level-0);
  border: .5pt solid var(--sklearn-color-unfitted-level-3);
}

.sk-estimator-doc-link.fitted span {
  /* fitted */
  background: var(--sklearn-color-fitted-level-0);
  border: var(--sklearn-color-fitted-level-3);
}

.sk-estimator-doc-link:hover span {
  display: block;
}

/* "?"-specific style due to the `<a>` HTML tag */

#sk-container-id-1 a.estimator_doc_link {
  float: right;
  font-size: 1rem;
  line-height: 1em;
  font-family: monospace;
  background-color: var(--sklearn-color-background);
  border-radius: 1rem;
  height: 1rem;
  width: 1rem;
  text-decoration: none;
  /* unfitted */
  color: var(--sklearn-color-unfitted-level-1);
  border: var(--sklearn-color-unfitted-level-1) 1pt solid;
}

#sk-container-id-1 a.estimator_doc_link.fitted {
  /* fitted */
  border: var(--sklearn-color-fitted-level-1) 1pt solid;
  color: var(--sklearn-color-fitted-level-1);
}

/* On hover */
#sk-container-id-1 a.estimator_doc_link:hover {
  /* unfitted */
  background-color: var(--sklearn-color-unfitted-level-3);
  color: var(--sklearn-color-background);
  text-decoration: none;
}

#sk-container-id-1 a.estimator_doc_link.fitted:hover {
  /* fitted */
  background-color: var(--sklearn-color-fitted-level-3);
}
</style><div id="sk-container-id-1" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>IsolationForest(contamination=0.1, n_estimators=150)</pre><b>In a Jupyter environment, please rerun this cell to show the HTML representation or trust the notebook. <br />On GitHub, the HTML representation is unable to render, please try loading this page with nbviewer.org.</b></div><div class="sk-container" hidden><div class="sk-item"><div class="sk-estimator fitted sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="sk-estimator-id-1" type="checkbox" checked><label for="sk-estimator-id-1" class="sk-toggleable__label fitted sk-toggleable__label-arrow fitted">&nbsp;&nbsp;IsolationForest<a class="sk-estimator-doc-link fitted" rel="noreferrer" target="_blank" href="https://scikit-learn.org/1.5/modules/generated/sklearn.ensemble.IsolationForest.html">?<span>Documentation for IsolationForest</span></a><span class="sk-estimator-doc-link fitted">i<span>Fitted</span></span></label><div class="sk-toggleable__content fitted"><pre>IsolationForest(contamination=0.1, n_estimators=150)</pre></div> </div></div></div></div>




```python
scores=model.decision_function(df2)
```


```python
anomaly=model.predict(df2)
```


```python
df2['scores']=scores
df2['anomaly']=anomaly
```


```python
anomaly = df2.loc[df2['anomaly']==-1]
anomaly_index = list(anomaly.index)
print('Total number of outliers is:', len(anomaly))
```

    Total number of outliers is: 286
    


```python
df2 = df2.drop(anomaly_index, axis = 0).reset_index(drop=True)
```


```python
sns.set(style='white',font_scale=1.3, rc={'figure.figsize':(20,20)})
ax=df2.hist(bins=20,color='red' )
```


    
![png](output_54_0.png)
    



```python
df2.plot( kind = 'box', subplots = True, layout = (4,4), sharex = False, sharey = False,color='black')
plt.show()
```


    
![png](output_55_0.png)
    



```python
df2.drop(['scores', 'anomaly'], axis = 1, inplace =True)
```


```python
from sklearn.preprocessing import StandardScaler

std_scaler = StandardScaler()
data_cluster=df2.copy()
data_cluster[data_cluster.columns]=std_scaler.fit_transform(data_cluster)
```


```python
from sklearn.decomposition import PCA
pca_2 = PCA(2)
pca_2_result = pca_2.fit_transform(data_cluster)

print ('Cumulative variance explained by 2 principal components: {:.2%}'.format(np.sum(pca_2.explained_variance_ratio_)))
```

    Cumulative variance explained by 2 principal components: 65.30%
    


```python
sns.set(style='white', rc={'figure.figsize':(9,6)},font_scale=1.1)

plt.scatter(x=pca_2_result[:, 0], y=pca_2_result[:, 1], color='red',lw=0.1)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('Data represented by the 2 strongest principal components',fontweight='bold')
plt.show()
```


    
![png](output_59_0.png)
    



```python
pca_2_result = pd.DataFrame(pca_2_result, columns=["PC1","PC2"])
```


```python
from sklearn.cluster import KMeans
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', random_state = 42)
    kmeans.fit(pca_2_result)
    wcss.append(kmeans.inertia_)
plt.plot(range(1, 11), wcss)
plt.title('The Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')
plt.show()
```


    
![png](output_61_0.png)
    



```python
import scipy.cluster.hierarchy as sch
from matplotlib import pyplot
pyplot.figure(figsize=(12, 5))
dendrogram = sch.dendrogram(sch.linkage(pca_2_result, method = 'ward'))
plt.title('Dendrogram')
plt.ylabel('Euclidean distances')
plt.show()
```


    
![png](output_62_0.png)
    



```python
df_kmeans = pca_2_result.copy()
```


```python
kmeans = KMeans(n_clusters = 4, init = 'k-means++', random_state = 42)
y_kmeans = kmeans.fit_predict(df_kmeans)
```


```python
df_kmeans
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>PC1</th>
      <th>PC2</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>-1.809439</td>
      <td>-0.749231</td>
    </tr>
    <tr>
      <th>1</th>
      <td>-0.771581</td>
      <td>-1.276252</td>
    </tr>
    <tr>
      <th>2</th>
      <td>-2.671718</td>
      <td>-0.344625</td>
    </tr>
    <tr>
      <th>3</th>
      <td>-2.394671</td>
      <td>-0.712554</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2.025919</td>
      <td>-1.796732</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2567</th>
      <td>-2.474934</td>
      <td>-0.188110</td>
    </tr>
    <tr>
      <th>2568</th>
      <td>-3.086162</td>
      <td>-0.227259</td>
    </tr>
    <tr>
      <th>2569</th>
      <td>0.342698</td>
      <td>0.047330</td>
    </tr>
    <tr>
      <th>2570</th>
      <td>-3.684036</td>
      <td>-0.197483</td>
    </tr>
    <tr>
      <th>2571</th>
      <td>-3.362171</td>
      <td>-0.129452</td>
    </tr>
  </tbody>
</table>
<p>2572 rows × 2 columns</p>
</div>




```python
df_kmeans = pca_2_result.copy()
```


```python
df_kmeans['Cluster'] = y_kmeans
df_kmeans['Cluster'].value_counts()
```




    Cluster
    0    1127
    2     849
    1     397
    3     199
    Name: count, dtype: int64




```python
sns.scatterplot(data=df_kmeans, x='PC1', y='PC2', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='PC1', ylabel='PC2'>




    
![png](output_68_1.png)
    



```python
df_AgglomerativeC = pca_2_result.copy()
```


```python
from sklearn.cluster import AgglomerativeClustering


AgglomerativeC = AgglomerativeClustering(n_clusters=4, metric = 'euclidean', linkage = 'ward')
y_AgglomerativeC = AgglomerativeC.fit_predict(df_AgglomerativeC)
```


```python
df_AgglomerativeC = pca_2_result.copy()
```


```python
df_AgglomerativeC['Cluster'] = y_AgglomerativeC
df_AgglomerativeC['Cluster'].value_counts()
```




    Cluster
    0    1390
    3     543
    1     492
    2     147
    Name: count, dtype: int64




```python
plt.figure(figsize=(15,7))
sns.scatterplot(data=df_AgglomerativeC, x='PC1', y='PC2', hue = 'Cluster', s=15, palette="tab10")
```




    <Axes: xlabel='PC1', ylabel='PC2'>




    
![png](output_73_1.png)
    

