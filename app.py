from taipy.gui import Gui
import pandas as pd

def load_and_clean_data(filepath):
    try:
        data = pd.read_csv(filepath)
        expected_columns = ['Home Equity', 'Property ID', 'Location', 'Size', 'Financial Stability', 'Interest Level']
        
        # Check for missing columns
        missing_columns = [col for col in expected_columns if col not in data.columns]
        if missing_columns:
            raise ValueError(f"Missing columns in the DataFrame: {missing_columns}")
        
        # Convert 'Home Equity' to numeric, filling NaNs with 0
        data['Home Equity'] = pd.to_numeric(data['Home Equity'], errors='coerce').fillna(0)
        
        # Further cleaning steps could be added here as needed

        return data
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        return pd.DataFrame()
    except ValueError as e:
        print(e)
        return pd.DataFrame()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return pd.DataFrame()

# Load and clean data
data = load_and_clean_data('home_equity_data.csv')

# Initialize GUI
gui = Gui()

# Prepare dynamic content based on data availability
property_details_available = not data.empty and all(col in data.columns for col in ['Property ID', 'Location', 'Size', 'Home Equity'])
financial_stability_available = not data.empty and 'Financial Stability' in data.columns
interest_level_available = not data.empty and 'Interest Level' in data.columns

# Dynamic page content
dashboard_content = f"""
# Home Equity Monitoring Dashboard

## Property Details Overview
{'<|table|data={data.to_dict("records") if property_details_available else []}|columns=["Property ID", "Location", "Size", "Home Equity"]|title="Property Details Overview"|>' if property_details_available else '**Data for Property Details Overview is not available.**'}

## Financial Stability Metrics
{'<|chart|type="pie"|data={data.to_dict("records") if financial_stability_available else []}|values="Financial Stability"|title="Financial Stability Metrics"|>' if financial_stability_available else '**Data for Financial Stability Metrics is not available.**'}

## Interest in Selling/Upgrading
{'<|selector|bind=interest_level|data={data["Interest Level"].unique().tolist() if interest_level_available else []}|title="Filter by Interest Level"|>' if interest_level_available else '**Data for Interest in Selling/Upgrading is not available.**'}
"""

# Add the page to the GUI
gui.add_page(name="home_equity_dashboard", page=dashboard_content)

# Run the GUI
gui.run()
