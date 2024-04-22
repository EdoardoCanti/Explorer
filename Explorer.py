import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Explorer:
    
    def __init__(self, dataframe:pd.DataFrame):
        self.dataframe = dataframe # Original dataset
        self.features = list(self.dataframe.columns) # Dataset columns
        self.features_type_dict = {} # Dictionary <feature_name> : <feature_type>
        self.dataframe_shape = self.dataframe.shape # Original dataset shape
        self.values_counter_dict = {} # Dictionary with <feature_name> : <value_counts> maintains for each feature the number of elements that assume a certain value (for all possibile values)
        self.nulls_dataframe = self.dataframe.copy() # Dataframe with only null values (with the original dataframe index)
        
        for feat in self.features:
            self.values_counter_dict[feat] = self.dataframe[feat].value_counts()
        print("Explorer > Object initialized on Dataframe with shape: {}".format(self.dataframe_shape))

    def get_features(self) -> list:
        return self.features
    
    def get_features_type(self) -> dict:
        for feat in self.features:
            self.features_type_dict[feat] = self.dataframe[feat].dtype
            print("Found Type: {}".format(self.dataframe[feat].dtype))
        return self.features_type_dict
    
    def get_dataframe_shape(self):
        return self.dataframe_shape
    
    def get_values_counter_dict(self) -> dict:
        return self.values_counter_dict
    
    def barplot_feat_counter(self, in_feature: str):
        plt.figure(figsize=(8,6))
        plt.title("{} values count".format(in_feature))
        plt.bar(self.values_counter_dict[in_feature].keys(), self.values_counter_dict[in_feature].values)
        plt.xlabel("{} values".format(in_feature))
        plt.ylabel("{} values count".format(in_feature))
        plt.xticks(rotation=90)
        plt.xticks(rotation=90)
        plt.show()

    def get_nulls(self) -> pd.DataFrame:
        nulls_filter = self.dataframe.isnull().any(axis = 1)
        self.nulls_dataframe =  self.nulls_dataframe[nulls_filter]
        return self.nulls_dataframe
    
    def count_nulls(self) -> pd.core.series.Series:
        nulls_counter = self.dataframe.isna().sum()
        return nulls_counter
        