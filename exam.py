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

pass

# ### Exercise 2 (max 2 points)
#
# Add a column period with the numbers 1, 2, 3 if, respectively, the row refers to `project_period` NWAI, NWAII, NWAIII.
#

pass

# ### Exercise 3 (max 7 points)
#
# Define a function `date_check` that takes a `project_period` string and a date (as a `pd.datetime64[ns]`) and it checks if it falls in the correct time interval (see data description in Exercise 1). For example, `date_check` should return `True` for `'NWAIII'` and `pd.to_datetime('1.1.2015')` and `False` if the date is `pd.to_datetime('1.1.1989')`.
#
# To get the full marks, you should declare correctly the type hints and add a test within a doctest string.

pass

# ### Exercise 4 (max 4 points)
#
# Use the function defined in Exercise 3 to assert that all the values in columns `date` are consistent with column `project_period`.

pass

# ### Exercise 5 (max 2 points)
#
# Print the median `elevation` for each species.

pass

# ### Exercise 6 (max 3 points)
#
# Make a scatter plot of `elevation` vs. `slope`, using different color for each `habitat_type`.



# ### Exercise 7 (max 5 points)
#
# Consider the animals with `habitat_type` 1 (forest). Consider them in ascending order of `elevation` and compute the  delta of elevation with respect the previous one (0, sea level, for the first). Draw these deltas vs. the elevation levels.

pass

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

pass
