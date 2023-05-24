#!/usr/bin/env python
# coding: utf-8
"""
Licensing

Copyright 2020 Esri

Licensed under the Apache License, Version 2.0 (the "License"); You
may not use this file except in compliance with the License. You may
obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied. See the License for the specific language governing
permissions and limitations under the License.

A copy of the license is available in the repository's
LICENSE file.
"""
from typing import List

from arcgis.features import GeoAccessor
from arcgis.gis import GIS
import cenpy
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

from . import config


def add_percent_column(percent_column_name: str, numerator_variables: List[str],
                       denominator_variable: str) -> pd.DataFrame:
    """
    Helper function to calculate the percent columns and report the description of the variables being used.

    .. note::

        This function modifies the data frame in place, so the original data frame will have the newly added column.

    Args:
        percent_column_name: column name to be added to the data frame
        numerator_variables: list of column names to be summed together for calculating the percentage
        denominator_variable: column name to be used as the denominator for calculating the percentage

    Returns:
        Pointer to the updated data frame.
    """
    # check to ensure the expected columns are present
    missing_num_cols = [c for c in numerator_variables if c not in df.columns]
    if len(missing_num_cols):
        raise ValueError(f'Cannot locate columns needed for calculating percent column - {missing_num_cols}')

    if denominator_variable not in df.columns:
        raise ValueError(f'Cannot locate column needed for calculating percent column - {denominator_variable}')

    # calculate and add the percent column to the dataframe
    df[percent_column_name] = df[numerator_variables].sum(axis=1) / df[denominator_variable]

    return df


# Create `APIConnection` Object Instance
api_conn = cenpy.remote.APIConnection(config.api_database)

# Add `E` to Designate Estimate Variables
req_vars = [f'{var}E' for var in config.api_variables]

# Get Explanation for Variables
label_df = api_conn.variables[api_conn.variables.index.isin(req_vars)]
label_series = label_df['label'].str.replace('!!', ' ') + ' / ' + label_df['concept']

# Make Request to Get Data
req_cols = ['NAME', 'GEO_ID'] + req_vars
df = api_conn.query(
    cols=req_cols, 
    geo_unit='county', 
    geo_filter={'state': '*'}
)

# Convert Values to Scalar (Integers)
df[req_vars] = df[req_vars].astype('int')

# calculate percent columns
for col_nm, _, numerator_vars, denominator_vars, _ in config.percent_variable_lst:
    df = add_percent_column(col_nm, numerator_vars, denominator_vars)

# Data Cleanup
df = df.drop(columns=req_vars)
df['FIPS'] = df['state'] + df['county']

# Use Min-Max Scaler to rescale the data
quant_cols = [c['name'] for c in config.percent_variable_lst]
qual_cols = [c for c in df.columns if c not in quant_cols]

# create an instance of the min-max scaler
min_max_trs = MinMaxScaler(feature_range=(0, 1))

# transform the data - since it returns a numpy array, convert back into data frame
df_scaled = pd.DataFrame(min_max_trs.fit_transform(df[quant_cols]), columns=quant_cols)

# combine the non-scalar columns back onto the data frame again
df_scaled = pd.merge(df[qual_cols], df_scaled, left_index=True, right_index=True)

# apply weighting coefficients
for var in config.percent_variable_lst:
    df_scaled[var['name']] = df_scaled[var['name']] * var['coefficient']

# Create Composite Index
df['composite_index'] = df_scaled[quant_cols].sum(axis=1) / len(quant_cols)

# Connect Using a `GIS` Object Instance
gis = GIS(profile=config.gis_profile)

# Access the County Boundaries `Item`
itm = gis.content.get('9859918e235f47ce90deff19bed75010')

# Create a Layer Object Instance
lyr = itm.layers[2]

# Retrieve Data Using a Query
lyr_df = lyr.query(out_fields=['FIPS'], out_sr=4326).sdf

# Combine Geometry and Custom Data
df_geo = df.join(lyr_df[['FIPS', 'SHAPE']].set_index('FIPS'), on='FIPS', how='right')
df_geo.spatial.set_geometry('SHAPE')

# ## Share for Mapping
fl = df_geo.spatial.to_featurelayer('Economic_Index', gis)
