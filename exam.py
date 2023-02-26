# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.14.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# + [markdown] toc=true
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Programming-in-Python" data-toc-modified-id="Programming-in-Python-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Programming in Python</a></span><ul class="toc-item"><li><span><a href="#Exam:-February-22,-2023" data-toc-modified-id="Exam:-February-22,-2023-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Exam: February 22, 2023</a></span><ul class="toc-item"><li><span><a href="#Exercise-1-(max-4-points)" data-toc-modified-id="Exercise-1-(max-4-points)-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Exercise 1 (max 4 points)</a></span></li><li><span><a href="#Exercise-2-(max-2-points)" data-toc-modified-id="Exercise-2-(max-2-points)-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Exercise 2 (max 2 points)</a></span></li><li><span><a href="#Exercise-3-(max-7-points)" data-toc-modified-id="Exercise-3-(max-7-points)-1.1.3"><span class="toc-item-num">1.1.3&nbsp;&nbsp;</span>Exercise 3 (max 7 points)</a></span></li><li><span><a href="#Exercise-4-(max-4-points)" data-toc-modified-id="Exercise-4-(max-4-points)-1.1.4"><span class="toc-item-num">1.1.4&nbsp;&nbsp;</span>Exercise 4 (max 4 points)</a></span></li><li><span><a href="#Exercise-5-(max-2-points)" data-toc-modified-id="Exercise-5-(max-2-points)-1.1.5"><span class="toc-item-num">1.1.5&nbsp;&nbsp;</span>Exercise 5 (max 2 points)</a></span></li><li><span><a href="#Exercise-6-(max-3-points)" data-toc-modified-id="Exercise-6-(max-3-points)-1.1.6"><span class="toc-item-num">1.1.6&nbsp;&nbsp;</span>Exercise 6 (max 3 points)</a></span></li><li><span><a href="#Exercise-7-(max-5-points)" data-toc-modified-id="Exercise-7-(max-5-points)-1.1.7"><span class="toc-item-num">1.1.7&nbsp;&nbsp;</span>Exercise 7 (max 5 points)</a></span></li><li><span><a href="#Exercise-8-(max-6-points)" data-toc-modified-id="Exercise-8-(max-6-points)-1.1.8"><span class="toc-item-num">1.1.8&nbsp;&nbsp;</span>Exercise 8 (max 6 points)</a></span></li></ul></li></ul></li></ul></div>
# -

# # Programming in Python
# ## Exam: February 22, 2023
#
# You can solve the exercises below by using standard Python 3.10 libraries, NumPy, Matplotlib, Pandas, PyMC.
# You can browse the documentation: [Python](https://docs.python.org/3.10/), [NumPy](https://numpy.org/doc/stable/user/index.html), [Matplotlib](https://matplotlib.org/stable/users/index.html), [Pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html), [PyMC](https://docs.pymc.io).
# You can also look at the [slides of the course](https://homes.di.unimi.it/monga/lucidi2223/pyqb00.pdf) or your code on [GitHub](https://github.com).
#
# **It is forbidden to communicate with others.**
#
# To test examples in docstrings use
#
# ```python
# import doctest
# doctest.testmod()
# ```
#

import numpy as np
import pandas as pd  # type: ignore
import matplotlib.pyplot as plt # type: ignore
import pymc as pm   # type: ignore
import arviz as az   # type: ignore

# ### Exercise 1 (max 4 points)
#
# The file [prey_winter.csv](./prey_winter.csv) (Vogt, Kristina, Nagl, Daniela, Hackländer, Klaus, Ryser, Andreas, Zimmermann, Fridolin, Signer, Sven, Haller, Heinrich, Breitenmoser-Würsten, Christine, & Breitenmoser, Urs. (2023). Data for: Long-term changes in habitat selection and prey spectrum in a reintroduced Eurasian lynx (Lynx lynx) population in Switzerland [Data set]. https://doi.org/10.5061/dryad.sf7m0cg7v) contains:
#
# - project_period: NWA I (1983--1985, VHF telemetry data), NWA II (1997--2001, VHF telemetry data) and NWA III (2011--2017, GPS telemetry data)
# - animal_id: lynx name
# - species: ungulate prey species:  Ca-ca= Capreolus capreolus, Ru-ru= Rupicapra rupicapra
# - date: kill date in DD.MM.YYYY format
# - habitat_type: habitat type is defined as 1= forest, 2= open habitat, and 3= unsuitable habitat
# - elevation: m a.s.l. calculated from DEM with 25m grid cell size
# - slope: slope in degrees, calculated from DEM with 25m grid cell size
#
# Read the data in a pandas DataFrame. Be sure to use `id` as the index and that the column `date` has `pd.datetime64[ns]`.
#

prey = pd.read_csv('prey_winter.csv', sep=';', index_col='id', parse_dates=['date'], dayfirst=True)

assert prey.dtypes['date'] == 'datetime64[ns]' 

prey.head()

# ### Exercise 2 (max 2 points)
#
# Add a column period with the numbers 1, 2, 3 if, respectively, the row refers to `project_period` NWAI, NWAII, NWAIII.
#

prey['period'] = prey['project_period'].str.count('I')

prey.head()


# ### Exercise 3 (max 7 points)
#
# Define a function `date_check` that takes a `project_period` string and a date (as a `pd.datetime64[ns]`) and it checks if it falls in the correct time interval (see data description in Exercise 1). For example, `date_check` should return `True` for `'NWAIII'` and `pd.to_datetime('1.1.2015')` and `False` if the date is `pd.to_datetime('1.1.1989')`.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

def date_check(project_period: str, date: pd.Timestamp) -> bool:
    """Check if date falls in project_period.
    
    >>> date_check('NWAIII', pd.to_datetime('1.1.2015'))
    True
    
    >>> date_check('NWAIII', pd.to_datetime('1.1.1989'))
    False
    
    """
    
    if project_period == 'NWAI':
        min_d, max_d = 1983, 1985
    elif project_period == 'NWAII':
        min_d, max_d = 1997, 2001
    elif project_period == 'NWAIII':
        min_d, max_d = 2011, 2017
    else:
        assert False, 'Wrong project_period!'
    return min_d <= date.year <= max_d
    


import doctest
doctest.testmod()

# ### Exercise 4 (max 4 points)
#
# Use the function defined in Exercise 3 to assert that all the values in columns `date` are consistent with column `project_period`.

assert prey.apply(lambda row: date_check(row['project_period'], row['date']), axis=1).all()

# ### Exercise 5 (max 2 points)
#
# Print the median `elevation` for each species.

prey.groupby('species')['elevation'].median()

# ### Exercise 6 (max 3 points)
#
# Make a scatter plot of `elevation` vs. `slope`, using different color for each `habitat_type`.

_ = prey.plot.scatter('elevation', 'slope', c='habitat_type', colormap='Accent')

# ### Exercise 7 (max 5 points)
#
# Consider the animals with `habitat_type` 1 (forest). Consider them in ascending order of `elevation` and compute the  delta of elevation with respect the previous one (0, sea level, for the first). Draw these deltas vs. the elevation levels.

# +
forest = prey[prey['habitat_type'] == 1]
sorted_forest = forest.sort_values(by='elevation')

deltas = []
for i, val in enumerate(sorted_forest['elevation']):
    if i == 0:
        deltas.append(val)
    else:
        deltas.append(val - sorted_forest['elevation'].iloc[i-1])

# +
fig, ax = plt.subplots()

ax.scatter(sorted_forest['elevation'], deltas)
ax.set_xlabel('elevation')
_ = ax.set_ylabel('delta')
# -

# ### Exercise 8 (max 6 points)
#
# Consider this statistical model:
#
# - a parameter $\alpha$ is normally distributed with mean 0 and standard deviation 5
# - a parameter $\beta_e$ is normally distributed with mean 0 and standard deviation 5
# - a parameter $\beta_h$ is normally distributed with mean 0 and standard deviation 5
# - $\sigma$ is exponentially distributed with $\lambda = 1$
# - the observed `slope` is normally distributed with a standard deviation of $\sigma$ and a mean given by $\alpha + \beta_e\cdot E + \beta_h\cdot H$, where $E$ is the corresponding `elevation`, $H$ is the correspondig `habitat_type`.
#
# Code this model with pymc, sample the model, and plot the summary of the resulting estimation by using `az.plot_posterior`.
#
#
#
#

with pm.Model():
    
    a = pm.Normal('alpha', 0, 5)
    b_e = pm.Normal('beta_e', 0, 5)
    b_h = pm.Normal('beta_h', 0, 5)
    s = pm.Exponential('sigma', 1)
    
    pm.Normal('slope', sigma=s, mu=a + b_e*prey['elevation'] + b_h*prey['habitat_type'], observed=prey['slope'])
    
    idata = pm.sample()
    

_ = az.plot_posterior(idata)
