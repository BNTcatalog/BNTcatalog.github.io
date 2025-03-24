import pandas as pd
import numpy as np
import plotly
import plotly.express as px
import json

class StarDatabase:
    """
    Manages star data from CSV file
    """
    def __init__(self, csv_path):
        """
        Initialize the database from a CSV file

        Args:
            csv_path (str): Path to the CSV file containing star data
        """
        try:
            self.data = pd.read_csv(csv_path)
            self.columns = self.data.columns.tolist()
        except Exception as e:
            print(f"Error loading CSV: {e}")
            self.data = pd.DataFrame()
            self.columns = []
    def get_all_stars(self):
        """
        Retrieve all stars from the database

        Returns:
            pandas.DataFrame: All star data
        """
        return self.data

    def get_star_by_id(self, star_id):
        """
        Retrieve a specific star by ID
        
        Args:
            star_id (int/str): Unique identifier for the star
        
            pandas.Series: Details of the specified star
        """
        return self.data[self.data['id'] == star_id].iloc[0] if not self.data.empty else None
    

