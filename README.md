# Explorer
Class defined in order to perform common and easy operations for performing an initial Exploratory Data Analysis on pandas DataFrame objects.

# Goal
Just collect common and repetitive operations on dataframes in a single object. Should be updated everytime a useful operation is found.

# Attributes
 - `dataframe`: original dataset of type: pandas.DataFrame.
 - `features`: list with dataframe columns.
 - `features_type_dict`: dictionary <feature_name> : <feature_type>
 - `dataframe_shape`: original dataframe shape.
 - `values_counter_dict`: dictionary with <feature_name> : <value_counts> maintains for each feature the number of elements that assume a certain value (for all possibile values).
 - `nulls_dataframe`: Dataframe with only null values (with the original dataframe index).

# Methods
 - `get_features()`: returns a *list* with original dataframe column names.
 - `get_features_type()`: returns a *dictionary* with column names as keys and `dataframe[<column_name>].dtype` as values.
 - `get_dataframe_shape()`: getting original dataframe shape. Returns tuple object type.
 - `get_values_counter_dict()`: returns a dictionary `values_counter_dict`.
 - `barplot_feat_counter(in_feature: str)`: barplots the content of `values_counter_dict` attribute.
 - `get_nulls()`: returns dataframe `nulls_dataframe` with observations of original dataframe that has null values.
 - `count_nulls(self)`: for each feature counts the number of of null values. Return a pandas Series object.

