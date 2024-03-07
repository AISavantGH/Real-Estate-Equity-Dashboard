# Real Estate Equity Dashboard

The Real Estate Equity Dashboard is an interactive web application designed to provide insights into home equity trends, financial stability metrics, and interest in selling or upgrading properties. Built with Taipy GUI, this application leverages Python's powerful data manipulation libraries to process and visualize real estate data effectively. Users can interact with the dashboard to filter information based on property size or interest level, making it an invaluable tool for real estate analysts, investors, and homeowners alike.

Features
Data Visualization: Interactive charts and tables showcasing property details, home equity trends, and financial stability metrics.
Interactive Filters: Dynamically filter data based on property size and interest levels to tailor the information display.
Data Handling: Robust data loading and cleaning processes ensure accuracy and reliability of the displayed information.
Responsive Design: Crafted to provide a seamless user experience across various devices and screen sizes.

How to Run
Ensure you have Python installed on your system.
Clone this repository to your local machine.
Install the required dependencies using pip install -r requirements.txt.
Run app.py to launch the dashboard in your web browser.

Generating Test Data
To generate 200 records of test data for this application, run the generate_test_data.py script. This script creates a CSV file named home_equity_data.csv in the project directory, overwriting any existing file.


script
import pandas as pd
import numpy as np
# Generate 200 records of dummy data
np.random.seed(0)  # For reproducibility
data = pd.DataFrame({
    'Property ID': np.arange(1, 201),
    'Location': np.random.choice(['Location A', 'Location B', 'Location C', 'Location D'], 200),
    'Size': np.random.choice([100, 200, 300, 400], 200),
    'Home Equity': np.random.randint(100000, 500000, 200),
    'Financial Stability': np.random.randint(1, 100, 200),
    'Interest Level': np.random.choice(['High', 'Medium', 'Low'], 200),
})

# Save to CSV, overwriting any existing file
data.to_csv('home_equity_data.csv', index=False)

Dependencies
Taipy
Pandas
NumPy

Contribution
Contributions to the Real Estate Equity Dashboard are welcome! Whether it's feature enhancements, bug fixes, or documentation improvements, feel free to fork this repository and submit your pull requests.

License
This project is open-sourced under the MIT License. See the LICENSE file for more details.
