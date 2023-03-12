import pandas as pd
import numpy as np

def date_format(df):
    df['MES/AÑO'] = pd.to_datetime(df['MES/AÑO'], format='%Y%m')
    return df['MES/AÑO']