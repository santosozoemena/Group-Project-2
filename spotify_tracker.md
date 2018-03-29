

```python
# Dependencies
import csv
import pandas as pd
import os
import numpy as np
```


```python
# Create empty lists to store the "track_name" and "region" for each number one song
position = []
url = []
region = []
```


```python
# Read csv
csvpath = os.path.join('Desktop', 'Project-2', 'spotify_data.csv')
import csv

spotify_df = pd.read_csv(csvpath, encoding="ISO-8859-1")
```


```python
# Add a blank column to flag number one hits
spotify_df['Number One']=np.nan
```


```python
spotify_df.count()
```




    Date                        145968
    Position                    145968
    Streams                     145968
    Track Name                  145900
    Artist                      145900
    Region                      145968
    URL                         145968
    RELEASE                     145968
    BPM                         145968
    ENERGY                      145968
    DANCE                       145968
    LOUD                        145968
    VALENCE                     145968
    LENGTH                      145968
    ACOUSTIC                    145968
    POP.                        145968
    Population                  145968
    Country Primary Language    145968
    Stream % of Pop             145968
    Number One                       0
    dtype: int64




```python
# Create a new dataframe for only number one songs
number_one_df = spotify_df.loc[spotify_df["Position"] == 1,:]
```


```python
number_one_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Position</th>
      <th>Streams</th>
      <th>Track Name</th>
      <th>Artist</th>
      <th>Region</th>
      <th>URL</th>
      <th>RELEASE</th>
      <th>BPM</th>
      <th>ENERGY</th>
      <th>DANCE</th>
      <th>LOUD</th>
      <th>VALENCE</th>
      <th>LENGTH</th>
      <th>ACOUSTIC</th>
      <th>POP.</th>
      <th>Population</th>
      <th>Country Primary Language</th>
      <th>Stream % of Pop</th>
      <th>Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>1</td>
      <td>19272</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1/2/2017</td>
      <td>1</td>
      <td>16672</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001023</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>50</th>
      <td>1/3/2017</td>
      <td>1</td>
      <td>17258</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001059</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>75</th>
      <td>1/4/2017</td>
      <td>1</td>
      <td>18146</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001114</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>100</th>
      <td>1/5/2017</td>
      <td>1</td>
      <td>17788</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001092</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
hits_df = number_one_df.drop_duplicates(subset=['URL','Region'], keep ='first')

```


```python
hits_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Position</th>
      <th>Streams</th>
      <th>Track Name</th>
      <th>Artist</th>
      <th>Region</th>
      <th>URL</th>
      <th>RELEASE</th>
      <th>BPM</th>
      <th>ENERGY</th>
      <th>DANCE</th>
      <th>LOUD</th>
      <th>VALENCE</th>
      <th>LENGTH</th>
      <th>ACOUSTIC</th>
      <th>POP.</th>
      <th>Population</th>
      <th>Country Primary Language</th>
      <th>Stream % of Pop</th>
      <th>Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>1</td>
      <td>19272</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>350</th>
      <td>1/15/2017</td>
      <td>1</td>
      <td>21318</td>
      <td>Despacito (Featuring Daddy Yankee)</td>
      <td>Luis Fonsi</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/4aWmUDTfIPGksMN...</td>
      <td>1/13/2017</td>
      <td>88</td>
      <td>79</td>
      <td>62</td>
      <td>-5</td>
      <td>87</td>
      <td>0.158333</td>
      <td>20</td>
      <td>78</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001309</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2475</th>
      <td>4/10/2017</td>
      <td>1</td>
      <td>19896</td>
      <td>Shape of You</td>
      <td>Ed Sheeran</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/7qiZfU4dY1lWllz...</td>
      <td>1/6/2017</td>
      <td>96</td>
      <td>65</td>
      <td>83</td>
      <td>-3</td>
      <td>93</td>
      <td>0.162500</td>
      <td>58</td>
      <td>86</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001221</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2650</th>
      <td>4/17/2017</td>
      <td>1</td>
      <td>21030</td>
      <td>Despacito - Remix</td>
      <td>Luis Fonsi</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5CtI0qwDJkDQGwX...</td>
      <td>4/17/2017</td>
      <td>88</td>
      <td>82</td>
      <td>63</td>
      <td>-4</td>
      <td>81</td>
      <td>0.159028</td>
      <td>22</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001291</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2850</th>
      <td>4/25/2017</td>
      <td>1</td>
      <td>20209</td>
      <td>Me RehÌ¼so</td>
      <td>Danny Ocean</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6De0lHrwBfPfrho...</td>
      <td>6/16/2017</td>
      <td>105</td>
      <td>80</td>
      <td>74</td>
      <td>-6</td>
      <td>43</td>
      <td>0.143056</td>
      <td>2</td>
      <td>90</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001241</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Create a new stripped-down dataframe for merging later.
hit_filter_df = hits_df[['URL', 'Region', 'Number One']]
```


```python
hit_filter_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>URL</th>
      <th>Region</th>
      <th>Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>350</th>
      <td>https://open.spotify.com/track/4aWmUDTfIPGksMN...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2475</th>
      <td>https://open.spotify.com/track/7qiZfU4dY1lWllz...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2650</th>
      <td>https://open.spotify.com/track/5CtI0qwDJkDQGwX...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2850</th>
      <td>https://open.spotify.com/track/6De0lHrwBfPfrho...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
hit_filter_df.count()
```




    URL           308
    Region        308
    Number One      0
    dtype: int64




```python
# Drop any rows that do not have at least 2 non-na values (Essentialy, Track name and region)
hit_filter_df.dropna(thresh=2)
hit_filter_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>URL</th>
      <th>Region</th>
      <th>Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>350</th>
      <td>https://open.spotify.com/track/4aWmUDTfIPGksMN...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2475</th>
      <td>https://open.spotify.com/track/7qiZfU4dY1lWllz...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2650</th>
      <td>https://open.spotify.com/track/5CtI0qwDJkDQGwX...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2850</th>
      <td>https://open.spotify.com/track/6De0lHrwBfPfrho...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
hit_filter_df.count()
```




    URL           308
    Region        308
    Number One      0
    dtype: int64




```python
# Export file as a csv, without the Pandas index, but with the header
hit_filter_df.to_csv("Desktop/Project-2/numberOneUnique.csv", index=False, header=True)
```


```python
# Read newly created csv and create a renamed df for merging
csvpath2 = os.path.join('Desktop', 'Project-2', 'numberOneUnique.csv')
import csv

numberOneUnique_df = pd.read_csv(csvpath2, encoding="ISO-8859-1")
```


```python
numberOneUnique_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>URL</th>
      <th>Region</th>
      <th>Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>https://open.spotify.com/track/4aWmUDTfIPGksMN...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>https://open.spotify.com/track/7qiZfU4dY1lWllz...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>https://open.spotify.com/track/5CtI0qwDJkDQGwX...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>https://open.spotify.com/track/6De0lHrwBfPfrho...</td>
      <td>Ecuador</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Fill the "Number One" Column with "Number One Hit" 
numberOneUnique_df['Number One'] = 'Number One Hit'
```


```python
# Consider Merging with a smaller version of the total dataframe without all the song dynamics?
```


```python
merge_table_df = pd.merge(spotify_df, numberOneUnique_df, on=['URL','Region'], how='left')
```


```python
merge_table_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Position</th>
      <th>Streams</th>
      <th>Track Name</th>
      <th>Artist</th>
      <th>Region</th>
      <th>URL</th>
      <th>RELEASE</th>
      <th>BPM</th>
      <th>ENERGY</th>
      <th>...</th>
      <th>LOUD</th>
      <th>VALENCE</th>
      <th>LENGTH</th>
      <th>ACOUSTIC</th>
      <th>POP.</th>
      <th>Population</th>
      <th>Country Primary Language</th>
      <th>Stream % of Pop</th>
      <th>Number One_x</th>
      <th>Number One_y</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>1</td>
      <td>19272</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>...</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>NaN</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2017</td>
      <td>2</td>
      <td>19270</td>
      <td>Chantaje</td>
      <td>Shakira</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6mICuAdrwEjh6Y6...</td>
      <td>5/26/2017</td>
      <td>102</td>
      <td>77</td>
      <td>...</td>
      <td>-3</td>
      <td>91</td>
      <td>0.136111</td>
      <td>19</td>
      <td>83</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/2017</td>
      <td>3</td>
      <td>15761</td>
      <td>Otra Vez (feat. J Balvin)</td>
      <td>Zion &amp; Lennox</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3QwBODjSEzelZyV...</td>
      <td>9/30/2016</td>
      <td>96</td>
      <td>77</td>
      <td>...</td>
      <td>-5</td>
      <td>70</td>
      <td>0.145139</td>
      <td>6</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000967</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/2017</td>
      <td>4</td>
      <td>14954</td>
      <td>Vente Pa' Ca</td>
      <td>Ricky Martin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/7DM4BPaS7uofFul...</td>
      <td>9/23/2016</td>
      <td>100</td>
      <td>92</td>
      <td>...</td>
      <td>-4</td>
      <td>53</td>
      <td>0.179861</td>
      <td>0</td>
      <td>80</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000918</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2017</td>
      <td>5</td>
      <td>14269</td>
      <td>Safari</td>
      <td>J Balvin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6rQSrBHf7HlZjtc...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000876</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>5</th>
      <td>1/1/2017</td>
      <td>6</td>
      <td>12843</td>
      <td>La Bicicleta</td>
      <td>Carlos Vives</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/0sXvAOmXgjR2QUq...</td>
      <td>5/26/2017</td>
      <td>180</td>
      <td>96</td>
      <td>...</td>
      <td>-2</td>
      <td>95</td>
      <td>0.158333</td>
      <td>20</td>
      <td>73</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000788</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>6</th>
      <td>1/1/2017</td>
      <td>7</td>
      <td>10986</td>
      <td>Ay Mi Dios</td>
      <td>IAmChino</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6stYbAJgTszHAHZ...</td>
      <td>2/22/2016</td>
      <td>92</td>
      <td>83</td>
      <td>...</td>
      <td>-3</td>
      <td>81</td>
      <td>0.175000</td>
      <td>17</td>
      <td>63</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000674</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>7</th>
      <td>1/1/2017</td>
      <td>8</td>
      <td>10653</td>
      <td>Andas En Mi Cabeza</td>
      <td>Chino &amp; Nacho</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5mey7CLLuFToM2P...</td>
      <td>2/19/2016</td>
      <td>104</td>
      <td>95</td>
      <td>...</td>
      <td>-2</td>
      <td>53</td>
      <td>0.171528</td>
      <td>3</td>
      <td>71</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000654</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>8</th>
      <td>1/1/2017</td>
      <td>9</td>
      <td>9807</td>
      <td>Traicionera</td>
      <td>Sebastian Yatra</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5J1c3M4EldCfNxX...</td>
      <td>6/24/2016</td>
      <td>91</td>
      <td>67</td>
      <td>...</td>
      <td>-5</td>
      <td>66</td>
      <td>0.158333</td>
      <td>14</td>
      <td>75</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000602</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>9</th>
      <td>1/1/2017</td>
      <td>10</td>
      <td>9612</td>
      <td>Shaky Shaky</td>
      <td>Daddy Yankee</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/58IL315gMSTD37D...</td>
      <td>4/8/2016</td>
      <td>88</td>
      <td>63</td>
      <td>...</td>
      <td>-4</td>
      <td>86</td>
      <td>0.162500</td>
      <td>6</td>
      <td>68</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000590</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>10</th>
      <td>1/1/2017</td>
      <td>11</td>
      <td>9611</td>
      <td>Vacaciones</td>
      <td>Wisin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3dQDid3IUNhZy1O...</td>
      <td>12/1/2017</td>
      <td>96</td>
      <td>91</td>
      <td>...</td>
      <td>-3</td>
      <td>70</td>
      <td>0.165972</td>
      <td>25</td>
      <td>78</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000590</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>11</th>
      <td>1/1/2017</td>
      <td>12</td>
      <td>8982</td>
      <td>Dile Que Tu Me Quieres</td>
      <td>Ozuna</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/20ZAJdsKB5IGbGj...</td>
      <td>6/6/2016</td>
      <td>176</td>
      <td>69</td>
      <td>...</td>
      <td>-7</td>
      <td>83</td>
      <td>0.156944</td>
      <td>10</td>
      <td>76</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000551</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>12</th>
      <td>1/1/2017</td>
      <td>13</td>
      <td>8834</td>
      <td>Let Me Love You</td>
      <td>DJ Snake</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/4pdPtRcBmOSQDlJ...</td>
      <td>8/5/2016</td>
      <td>100</td>
      <td>71</td>
      <td>...</td>
      <td>-5</td>
      <td>15</td>
      <td>0.143056</td>
      <td>8</td>
      <td>77</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000542</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>13</th>
      <td>1/1/2017</td>
      <td>14</td>
      <td>8309</td>
      <td>DUELE EL CORAZON</td>
      <td>Enrique Iglesias</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6YZdkObH88npeKr...</td>
      <td>4/18/2016</td>
      <td>91</td>
      <td>90</td>
      <td>...</td>
      <td>-3</td>
      <td>85</td>
      <td>0.139583</td>
      <td>8</td>
      <td>77</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000510</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>14</th>
      <td>1/1/2017</td>
      <td>15</td>
      <td>7822</td>
      <td>Chillax</td>
      <td>Farruko</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/1lxswgIpzV6HhEN...</td>
      <td>10/23/2015</td>
      <td>92</td>
      <td>65</td>
      <td>...</td>
      <td>-5</td>
      <td>51</td>
      <td>0.137500</td>
      <td>7</td>
      <td>75</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000480</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>15</th>
      <td>1/1/2017</td>
      <td>16</td>
      <td>7586</td>
      <td>Borro Cassette</td>
      <td>Maluma</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6DUdDIRgLqCGq1D...</td>
      <td>10/30/2015</td>
      <td>176</td>
      <td>70</td>
      <td>...</td>
      <td>-6</td>
      <td>79</td>
      <td>0.143750</td>
      <td>13</td>
      <td>79</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000466</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>16</th>
      <td>1/1/2017</td>
      <td>17</td>
      <td>7472</td>
      <td>One Dance</td>
      <td>Drake</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/1xznGGDReH1oQq0...</td>
      <td>5/13/2016</td>
      <td>104</td>
      <td>62</td>
      <td>...</td>
      <td>-6</td>
      <td>38</td>
      <td>0.120833</td>
      <td>1</td>
      <td>74</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000459</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>17</th>
      <td>1/1/2017</td>
      <td>18</td>
      <td>7416</td>
      <td>Closer</td>
      <td>The Chainsmokers</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/7BKLCZ1jbUBVqRi...</td>
      <td>7/5/1905</td>
      <td>137</td>
      <td>75</td>
      <td>...</td>
      <td>-8</td>
      <td>52</td>
      <td>0.145139</td>
      <td>0</td>
      <td>63</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000455</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>18</th>
      <td>1/1/2017</td>
      <td>19</td>
      <td>7006</td>
      <td>Starboy</td>
      <td>The Weeknd</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5aAx2yezTd8zXrk...</td>
      <td>9/22/2016</td>
      <td>186</td>
      <td>59</td>
      <td>...</td>
      <td>-7</td>
      <td>50</td>
      <td>0.159722</td>
      <td>17</td>
      <td>18</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000430</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>19</th>
      <td>1/1/2017</td>
      <td>20</td>
      <td>6779</td>
      <td>Desde Esa Noche</td>
      <td>ThalÌ?a</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/1pWYnQIlqxTh5bx...</td>
      <td>5/6/2016</td>
      <td>95</td>
      <td>93</td>
      <td>...</td>
      <td>-1</td>
      <td>84</td>
      <td>0.158333</td>
      <td>17</td>
      <td>75</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000416</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>20</th>
      <td>1/1/2017</td>
      <td>21</td>
      <td>6582</td>
      <td>Don't Wanna Know (feat. Kendrick Lamar)</td>
      <td>Maroon 5</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5MFzQMkrl1FOOng...</td>
      <td>11/3/2017</td>
      <td>100</td>
      <td>62</td>
      <td>...</td>
      <td>-6</td>
      <td>43</td>
      <td>0.148611</td>
      <td>34</td>
      <td>75</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000404</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>21</th>
      <td>1/1/2017</td>
      <td>22</td>
      <td>6521</td>
      <td>La Gozadera</td>
      <td>Gente De Zona</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/0OMRAvrtLWE2Tvc...</td>
      <td>4/22/2016</td>
      <td>95</td>
      <td>99</td>
      <td>...</td>
      <td>-2</td>
      <td>90</td>
      <td>0.140972</td>
      <td>17</td>
      <td>78</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000400</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>22</th>
      <td>1/1/2017</td>
      <td>23</td>
      <td>6261</td>
      <td>24K Magic</td>
      <td>Bruno Mars</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6b8Be6ljOzmkOmF...</td>
      <td>11/17/2016</td>
      <td>107</td>
      <td>80</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.156944</td>
      <td>3</td>
      <td>84</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000384</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>23</th>
      <td>1/1/2017</td>
      <td>24</td>
      <td>6237</td>
      <td>Me Llamas (feat. Maluma) - Remix</td>
      <td>Piso 21</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/5hEM0JchdVzQ5Pw...</td>
      <td>12/2/2016</td>
      <td>93</td>
      <td>84</td>
      <td>...</td>
      <td>-4</td>
      <td>75</td>
      <td>0.145833</td>
      <td>55</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000383</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>24</th>
      <td>1/1/2017</td>
      <td>25</td>
      <td>6028</td>
      <td>Cuatro Babys</td>
      <td>Maluma</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/0JoHqmlqE0W0i9p...</td>
      <td>10/7/2016</td>
      <td>130</td>
      <td>55</td>
      <td>...</td>
      <td>-6</td>
      <td>10</td>
      <td>0.193056</td>
      <td>10</td>
      <td>73</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000370</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1/2/2017</td>
      <td>1</td>
      <td>16672</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>...</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001023</td>
      <td>NaN</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>26</th>
      <td>1/2/2017</td>
      <td>2</td>
      <td>15594</td>
      <td>Chantaje</td>
      <td>Shakira</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6mICuAdrwEjh6Y6...</td>
      <td>5/26/2017</td>
      <td>102</td>
      <td>77</td>
      <td>...</td>
      <td>-3</td>
      <td>91</td>
      <td>0.136111</td>
      <td>19</td>
      <td>83</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000957</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>27</th>
      <td>1/2/2017</td>
      <td>3</td>
      <td>13507</td>
      <td>Otra Vez (feat. J Balvin)</td>
      <td>Zion &amp; Lennox</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3QwBODjSEzelZyV...</td>
      <td>9/30/2016</td>
      <td>96</td>
      <td>77</td>
      <td>...</td>
      <td>-5</td>
      <td>70</td>
      <td>0.145139</td>
      <td>6</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000829</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>28</th>
      <td>1/2/2017</td>
      <td>4</td>
      <td>11958</td>
      <td>Safari</td>
      <td>J Balvin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6rQSrBHf7HlZjtc...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000734</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>29</th>
      <td>1/2/2017</td>
      <td>5</td>
      <td>11590</td>
      <td>Vente Pa' Ca</td>
      <td>Ricky Martin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/7DM4BPaS7uofFul...</td>
      <td>9/23/2016</td>
      <td>100</td>
      <td>92</td>
      <td>...</td>
      <td>-4</td>
      <td>53</td>
      <td>0.179861</td>
      <td>0</td>
      <td>80</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000711</td>
      <td>NaN</td>
      <td>NaN</td>
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
      <th>145938</th>
      <td>3/18/2017</td>
      <td>21</td>
      <td>69908</td>
      <td>Cuatro Babys</td>
      <td>Maluma</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/0JoHqmlqE0W0i9p...</td>
      <td>10/7/2016</td>
      <td>130</td>
      <td>55</td>
      <td>...</td>
      <td>-6</td>
      <td>10</td>
      <td>0.193056</td>
      <td>10</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003930</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145939</th>
      <td>3/18/2017</td>
      <td>22</td>
      <td>63100</td>
      <td>Soy Peor</td>
      <td>Bad Bunny</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/5MT96Zz0ymUJNm8...</td>
      <td>11/3/2017</td>
      <td>140</td>
      <td>68</td>
      <td>...</td>
      <td>-6</td>
      <td>68</td>
      <td>0.206250</td>
      <td>42</td>
      <td>92</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003547</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145940</th>
      <td>3/18/2017</td>
      <td>23</td>
      <td>62332</td>
      <td>Amor Completo</td>
      <td>Mon Laferte</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/00kIWJu9IHiQ6i0...</td>
      <td>5/31/2017</td>
      <td>94</td>
      <td>71</td>
      <td>...</td>
      <td>-6</td>
      <td>52</td>
      <td>0.161111</td>
      <td>34</td>
      <td>69</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003504</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145941</th>
      <td>3/18/2017</td>
      <td>24</td>
      <td>59698</td>
      <td>Si Tu Novio Te Deja Sola</td>
      <td>J Balvin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/0RFFFGtPn6a58RH...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003356</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145942</th>
      <td>3/18/2017</td>
      <td>25</td>
      <td>58032</td>
      <td>Borro Cassette</td>
      <td>Maluma</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6DUdDIRgLqCGq1D...</td>
      <td>10/30/2015</td>
      <td>176</td>
      <td>70</td>
      <td>...</td>
      <td>-6</td>
      <td>79</td>
      <td>0.143750</td>
      <td>13</td>
      <td>79</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003262</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145943</th>
      <td>3/19/2017</td>
      <td>1</td>
      <td>185371</td>
      <td>Despacito (Featuring Daddy Yankee)</td>
      <td>Luis Fonsi</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/4aWmUDTfIPGksMN...</td>
      <td>1/13/2017</td>
      <td>88</td>
      <td>79</td>
      <td>...</td>
      <td>-5</td>
      <td>87</td>
      <td>0.158333</td>
      <td>20</td>
      <td>78</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.010420</td>
      <td>NaN</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>145944</th>
      <td>3/19/2017</td>
      <td>2</td>
      <td>124423</td>
      <td>Shape of You</td>
      <td>Ed Sheeran</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/7qiZfU4dY1lWllz...</td>
      <td>1/6/2017</td>
      <td>96</td>
      <td>65</td>
      <td>...</td>
      <td>-3</td>
      <td>93</td>
      <td>0.162500</td>
      <td>58</td>
      <td>86</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.006994</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145945</th>
      <td>3/19/2017</td>
      <td>3</td>
      <td>123936</td>
      <td>Me RehÌ¼so</td>
      <td>Danny Ocean</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6De0lHrwBfPfrho...</td>
      <td>6/16/2017</td>
      <td>105</td>
      <td>80</td>
      <td>...</td>
      <td>-6</td>
      <td>43</td>
      <td>0.143056</td>
      <td>2</td>
      <td>90</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.006967</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145946</th>
      <td>3/19/2017</td>
      <td>4</td>
      <td>120693</td>
      <td>El Amante</td>
      <td>Nicky Jam</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/3umS4y3uQDkqekN...</td>
      <td>1/20/2017</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-6</td>
      <td>73</td>
      <td>0.152778</td>
      <td>24</td>
      <td>81</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.006785</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145947</th>
      <td>3/19/2017</td>
      <td>5</td>
      <td>103403</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>...</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.005813</td>
      <td>NaN</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>145948</th>
      <td>3/19/2017</td>
      <td>6</td>
      <td>101767</td>
      <td>Sola (Remix) [feat. Daddy Yankee, Wisin, Farru...</td>
      <td>Anuel Aa</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/5q2JbCNi4Fcnglg...</td>
      <td>12/2/2016</td>
      <td>170</td>
      <td>87</td>
      <td>...</td>
      <td>-4</td>
      <td>77</td>
      <td>0.213889</td>
      <td>27</td>
      <td>82</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.005721</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145949</th>
      <td>3/19/2017</td>
      <td>7</td>
      <td>98079</td>
      <td>Otra Vez (feat. J Balvin)</td>
      <td>Zion &amp; Lennox</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/3QwBODjSEzelZyV...</td>
      <td>9/30/2016</td>
      <td>96</td>
      <td>77</td>
      <td>...</td>
      <td>-5</td>
      <td>70</td>
      <td>0.145139</td>
      <td>6</td>
      <td>81</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.005513</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145950</th>
      <td>3/19/2017</td>
      <td>8</td>
      <td>91594</td>
      <td>Chantaje</td>
      <td>Shakira</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6mICuAdrwEjh6Y6...</td>
      <td>5/26/2017</td>
      <td>102</td>
      <td>77</td>
      <td>...</td>
      <td>-3</td>
      <td>91</td>
      <td>0.136111</td>
      <td>19</td>
      <td>83</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.005149</td>
      <td>NaN</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>145951</th>
      <td>3/19/2017</td>
      <td>9</td>
      <td>90837</td>
      <td>La Rompe Corazones</td>
      <td>Daddy Yankee</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/4okba5wu9mMLXx7...</td>
      <td>1/13/2017</td>
      <td>176</td>
      <td>86</td>
      <td>...</td>
      <td>-3</td>
      <td>87</td>
      <td>0.142361</td>
      <td>11</td>
      <td>77</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.005106</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145952</th>
      <td>3/19/2017</td>
      <td>10</td>
      <td>83280</td>
      <td>Te Quiero Pa«Mi</td>
      <td>Don Omar</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/3BY2mafsbsoKGqS...</td>
      <td>11/11/2016</td>
      <td>89</td>
      <td>82</td>
      <td>...</td>
      <td>-4</td>
      <td>62</td>
      <td>0.147222</td>
      <td>13</td>
      <td>67</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004681</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145953</th>
      <td>3/19/2017</td>
      <td>11</td>
      <td>82421</td>
      <td>AmÌÁrrame</td>
      <td>Mon Laferte</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/0u13src3QcditRU...</td>
      <td>5/31/2017</td>
      <td>94</td>
      <td>71</td>
      <td>...</td>
      <td>-6</td>
      <td>52</td>
      <td>0.161111</td>
      <td>34</td>
      <td>69</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004633</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145954</th>
      <td>3/19/2017</td>
      <td>12</td>
      <td>81640</td>
      <td>SUBEME LA RADIO</td>
      <td>Enrique Iglesias</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/7nKBxz47S9SD79N...</td>
      <td>2/24/2017</td>
      <td>91</td>
      <td>82</td>
      <td>...</td>
      <td>-3</td>
      <td>65</td>
      <td>0.144444</td>
      <td>7</td>
      <td>81</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004589</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145955</th>
      <td>3/19/2017</td>
      <td>13</td>
      <td>75787</td>
      <td>Vacaciones</td>
      <td>Wisin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/3dQDid3IUNhZy1O...</td>
      <td>12/1/2017</td>
      <td>96</td>
      <td>91</td>
      <td>...</td>
      <td>-3</td>
      <td>70</td>
      <td>0.165972</td>
      <td>25</td>
      <td>78</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004260</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145956</th>
      <td>3/19/2017</td>
      <td>14</td>
      <td>75128</td>
      <td>Tu Falta De Querer</td>
      <td>Mon Laferte</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/4skuEIloXWuxxge...</td>
      <td>5/31/2017</td>
      <td>94</td>
      <td>71</td>
      <td>...</td>
      <td>-6</td>
      <td>52</td>
      <td>0.161111</td>
      <td>34</td>
      <td>69</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004223</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145957</th>
      <td>3/19/2017</td>
      <td>15</td>
      <td>74237</td>
      <td>Ay Mi Dios</td>
      <td>IAmChino</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6stYbAJgTszHAHZ...</td>
      <td>2/22/2016</td>
      <td>92</td>
      <td>83</td>
      <td>...</td>
      <td>-3</td>
      <td>81</td>
      <td>0.175000</td>
      <td>17</td>
      <td>63</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004173</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145958</th>
      <td>3/19/2017</td>
      <td>16</td>
      <td>73524</td>
      <td>Sigo ExtraÌ±ÌÁndote</td>
      <td>J Balvin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6qDF4wWL49CAVbg...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004133</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145959</th>
      <td>3/19/2017</td>
      <td>17</td>
      <td>73306</td>
      <td>Safari</td>
      <td>J Balvin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6rQSrBHf7HlZjtc...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.004121</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145960</th>
      <td>3/19/2017</td>
      <td>18</td>
      <td>70519</td>
      <td>Me Llamas (feat. Maluma) - Remix</td>
      <td>Piso 21</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/5hEM0JchdVzQ5Pw...</td>
      <td>12/2/2016</td>
      <td>93</td>
      <td>84</td>
      <td>...</td>
      <td>-4</td>
      <td>75</td>
      <td>0.145833</td>
      <td>55</td>
      <td>81</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003964</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145961</th>
      <td>3/19/2017</td>
      <td>19</td>
      <td>69442</td>
      <td>Vente Pa' Ca</td>
      <td>Ricky Martin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/7DM4BPaS7uofFul...</td>
      <td>9/23/2016</td>
      <td>100</td>
      <td>92</td>
      <td>...</td>
      <td>-4</td>
      <td>53</td>
      <td>0.179861</td>
      <td>0</td>
      <td>80</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003904</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145962</th>
      <td>3/19/2017</td>
      <td>20</td>
      <td>64546</td>
      <td>Caile (feat. Zion &amp; De La Ghetto)</td>
      <td>Revol</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/626rYyBfeAeleh1...</td>
      <td>5/31/2017</td>
      <td>94</td>
      <td>71</td>
      <td>...</td>
      <td>-6</td>
      <td>52</td>
      <td>0.161111</td>
      <td>34</td>
      <td>69</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003628</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145963</th>
      <td>3/19/2017</td>
      <td>21</td>
      <td>61646</td>
      <td>Cuatro Babys</td>
      <td>Maluma</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/0JoHqmlqE0W0i9p...</td>
      <td>10/7/2016</td>
      <td>130</td>
      <td>55</td>
      <td>...</td>
      <td>-6</td>
      <td>10</td>
      <td>0.193056</td>
      <td>10</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003465</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145964</th>
      <td>3/19/2017</td>
      <td>22</td>
      <td>57717</td>
      <td>Soy Peor</td>
      <td>Bad Bunny</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/5MT96Zz0ymUJNm8...</td>
      <td>11/3/2017</td>
      <td>140</td>
      <td>68</td>
      <td>...</td>
      <td>-6</td>
      <td>68</td>
      <td>0.206250</td>
      <td>42</td>
      <td>92</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003244</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145965</th>
      <td>3/19/2017</td>
      <td>23</td>
      <td>55471</td>
      <td>Amor Completo</td>
      <td>Mon Laferte</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/00kIWJu9IHiQ6i0...</td>
      <td>5/31/2017</td>
      <td>94</td>
      <td>71</td>
      <td>...</td>
      <td>-6</td>
      <td>52</td>
      <td>0.161111</td>
      <td>34</td>
      <td>69</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.003118</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145966</th>
      <td>3/19/2017</td>
      <td>24</td>
      <td>53086</td>
      <td>Si Tu Novio Te Deja Sola</td>
      <td>J Balvin</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/0RFFFGtPn6a58RH...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>...</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.002984</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>145967</th>
      <td>3/19/2017</td>
      <td>25</td>
      <td>52007</td>
      <td>Borro Cassette</td>
      <td>Maluma</td>
      <td>Chile</td>
      <td>https://open.spotify.com/track/6DUdDIRgLqCGq1D...</td>
      <td>10/30/2015</td>
      <td>176</td>
      <td>70</td>
      <td>...</td>
      <td>-6</td>
      <td>79</td>
      <td>0.143750</td>
      <td>13</td>
      <td>79</td>
      <td>17789267</td>
      <td>Spanish</td>
      <td>0.002924</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
<p>145968 rows × 21 columns</p>
</div>




```python
clean_merge_df = merge_table_df.drop(["Number One_x"], axis=1)
clean_merge_df.rename(columns={'Number One_y': 'Reached Number One'}, inplace=True)
```


```python
clean_merge_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Position</th>
      <th>Streams</th>
      <th>Track Name</th>
      <th>Artist</th>
      <th>Region</th>
      <th>URL</th>
      <th>RELEASE</th>
      <th>BPM</th>
      <th>ENERGY</th>
      <th>DANCE</th>
      <th>LOUD</th>
      <th>VALENCE</th>
      <th>LENGTH</th>
      <th>ACOUSTIC</th>
      <th>POP.</th>
      <th>Population</th>
      <th>Country Primary Language</th>
      <th>Stream % of Pop</th>
      <th>Reached Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>1</td>
      <td>19272</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1/1/2017</td>
      <td>2</td>
      <td>19270</td>
      <td>Chantaje</td>
      <td>Shakira</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6mICuAdrwEjh6Y6...</td>
      <td>5/26/2017</td>
      <td>102</td>
      <td>77</td>
      <td>85</td>
      <td>-3</td>
      <td>91</td>
      <td>0.136111</td>
      <td>19</td>
      <td>83</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1/1/2017</td>
      <td>3</td>
      <td>15761</td>
      <td>Otra Vez (feat. J Balvin)</td>
      <td>Zion &amp; Lennox</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3QwBODjSEzelZyV...</td>
      <td>9/30/2016</td>
      <td>96</td>
      <td>77</td>
      <td>83</td>
      <td>-5</td>
      <td>70</td>
      <td>0.145139</td>
      <td>6</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000967</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1/1/2017</td>
      <td>4</td>
      <td>14954</td>
      <td>Vente Pa' Ca</td>
      <td>Ricky Martin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/7DM4BPaS7uofFul...</td>
      <td>9/23/2016</td>
      <td>100</td>
      <td>92</td>
      <td>66</td>
      <td>-4</td>
      <td>53</td>
      <td>0.179861</td>
      <td>0</td>
      <td>80</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000918</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1/1/2017</td>
      <td>5</td>
      <td>14269</td>
      <td>Safari</td>
      <td>J Balvin</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/6rQSrBHf7HlZjtc...</td>
      <td>6/24/2016</td>
      <td>180</td>
      <td>69</td>
      <td>71</td>
      <td>-4</td>
      <td>63</td>
      <td>0.143056</td>
      <td>53</td>
      <td>73</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.000876</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
hit_tracker_df = clean_merge_df.loc[clean_merge_df["Reached Number One"] == "Number One Hit",:]
```


```python
hit_tracker_df.dtypes
```




    Date                         object
    Position                      int64
    Streams                       int64
    Track Name                   object
    Artist                       object
    Region                       object
    URL                          object
    RELEASE                      object
    BPM                           int64
    ENERGY                        int64
    DANCE                         int64
    LOUD                          int64
    VALENCE                       int64
    LENGTH                      float64
    ACOUSTIC                      int64
    POP.                          int64
    Population                    int64
    Country Primary Language     object
    Stream % of Pop             float64
    Reached Number One           object
    dtype: object




```python
hit_tracker_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Position</th>
      <th>Streams</th>
      <th>Track Name</th>
      <th>Artist</th>
      <th>Region</th>
      <th>URL</th>
      <th>RELEASE</th>
      <th>BPM</th>
      <th>ENERGY</th>
      <th>DANCE</th>
      <th>LOUD</th>
      <th>VALENCE</th>
      <th>LENGTH</th>
      <th>ACOUSTIC</th>
      <th>POP.</th>
      <th>Population</th>
      <th>Country Primary Language</th>
      <th>Stream % of Pop</th>
      <th>Reached Number One</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1/1/2017</td>
      <td>1</td>
      <td>19272</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001183</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>25</th>
      <td>1/2/2017</td>
      <td>1</td>
      <td>16672</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001023</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>50</th>
      <td>1/3/2017</td>
      <td>1</td>
      <td>17258</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001059</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>75</th>
      <td>1/4/2017</td>
      <td>1</td>
      <td>18146</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001114</td>
      <td>Number One Hit</td>
    </tr>
    <tr>
      <th>100</th>
      <td>1/5/2017</td>
      <td>1</td>
      <td>17788</td>
      <td>Reggaetn Lento (Bailemos)</td>
      <td>CNCO</td>
      <td>Ecuador</td>
      <td>https://open.spotify.com/track/3AEZUABDXNtecAO...</td>
      <td>8/26/2016</td>
      <td>94</td>
      <td>84</td>
      <td>76</td>
      <td>-3</td>
      <td>71</td>
      <td>0.154861</td>
      <td>40</td>
      <td>81</td>
      <td>16290913</td>
      <td>Spanish</td>
      <td>0.001092</td>
      <td>Number One Hit</td>
    </tr>
  </tbody>
</table>
</div>




```python
# Export file as a csv, without the Pandas index, but with the header
hit_tracker_df.to_csv("Desktop/Project-2/hit_songs_only.csv", index=False, header=True)
```


```python
# can join same song per country to add rows of relative positions. Need max counts to change to max lengths, though
# have a map for stuff like number one turnover. Or for individual songs a map / line combo for streams vs normalized
# per country, and chart history timeline(and maybe don't have to normalize)
# Or, volume per country = do calculationz to normalize and pick most extreme examples
```
