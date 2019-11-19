## Description
This package contains 2 functions,`plot_geo_time_value()` and `plot_gif_geo_time_value()`, used to draw input data on a map of France.

## Usage
#### `plot_geo_time_value(x, y, year, value, proj='mercator',  axs=None, name=[], hue='', **kwargs)`

Draws input data values on a series of maps of France (Matplotlib subplots), 1 per year.
Saves output to `output.pdf`

Parameter  | Description
------------- | -------------
x  | longitude (list)
y  | latitudes (list)
year | years to draw (list)
value  | values to draw (dataframe or numpy array)
proj  | projection methods (string)
axs  | matplotilb axes returned by the `matplotlib.subplot()` function
name  | names of the places to draw (vector)
hue  | meaning of the values (string)


#### `plot_gif_geo_time_value(x, y, year, value, proj='mercator', method='gif', fig=None, ax=None, name=[], hue='', **kwargs)`

Makes a video of the evolution of input data values of the years on a map of France (matplotlib Axe object).
Saves output to `output.'method'`

Parameter  | Description
------------- | -------------
x  | longitude (list)
y  | latitudes (list)
year | years to draw (list)
value  | values to draw (dataframe or numpy array)
proj  | projection methods (string)
method | file output format (string)
fig | matplotilb figure to draw on
axs  | matplotilb axes returned by the `matplotlib.subplot()` function
name  | names of the places to draw (vector)
hue  | meaning of the values (string)


## Example of usage
Example of project using this package : https://github.com/gabsens/Python-for-Data-Scientists-ENSAE/blob/master/Devoir/IREP%20et%20devoir.ipynb


```
fig, axs = plt.subplots(2, 2, figsize=(20,20), subplot_kw={'projection': ccrs.Mercator()})

# data longiture/latitude
x, y = data['LLX'], data['LLY']

years = range(2004, 2008)
years_str = [str(year) for year in years]

values = data[[colname for colname in data.columns.values if colname[-4:] in years_str]].astype('float')

plot_geo_time_value(x, y, year=years, value=values, proj='mercator', axs=axs, hue='produits dangereux')`
```
![output1](https://user-images.githubusercontent.com/13206388/68499846-9185d200-025a-11ea-8419-082070991b13.png)
```
fig, ax = plt.subplots(figsize=(10,10), subplot_kw={'projection': ccrs.Mercator()})

# data longiture/latitude
x, y = data['LLX'], data['LLY']

years = range(2003, 2018)
years_str = [str(year) for year in years]

values = data[[colname for colname in data.columns.values if colname[-4:] in years_str]].astype('float')

plot_gif_geo_time_value(x, y, value=values, year=years, fig=fig, ax=ax, proj='mercator', method='gif', hue='produits dangereux')
```
![output2](https://user-images.githubusercontent.com/13206388/68499628-ed039000-0259-11ea-947c-edaeab32aeed.gif)
