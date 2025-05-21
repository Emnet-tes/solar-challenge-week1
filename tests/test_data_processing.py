import pytest
import pandas as pd
import numpy as np
from src.data.data_processing import clean_data, calculate_solar_metrics

def test_clean_data():
    # Create sample data
    data = pd.DataFrame({
        'GHI': [1000, np.nan, 1200, -100, 1500],
        'DNI': [800, 900, np.nan, 1000, -50],
        'DHI': [200, 300, 400, np.nan, 500]
    })
    
    # Clean the data
    cleaned_data = clean_data(data)
    
    # Assertions
    assert not cleaned_data.isnull().any().any(), "Cleaned data should not contain null values"
    assert (cleaned_data >= 0).all().all(), "All values should be non-negative"
    assert len(cleaned_data) == 3, "Invalid values should be removed"

def test_calculate_solar_metrics():
    # Create sample data
    data = pd.DataFrame({
        'GHI': [1000, 1200, 1500],
        'DNI': [800, 900, 1000],
        'DHI': [200, 300, 400]
    })
    
    # Calculate metrics
    metrics = calculate_solar_metrics(data)
    
    # Assertions
    assert 'daily_average' in metrics, "Should calculate daily average"
    assert 'monthly_average' in metrics, "Should calculate monthly average"
    assert 'peak_hours' in metrics, "Should calculate peak hours"
    assert isinstance(metrics['daily_average'], float), "Daily average should be a float" 