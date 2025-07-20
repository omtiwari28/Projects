import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('Projects\Freecodecamp_projects\Sea_level_prediction\dataser.csv')

    # Create scatter plot
    plt.figure(figsize = (12,6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'] , color = 'blue' , label = 'data points')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Create first line of best fit
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    years_extended = pd.Series(range(1880, 2051))
    line_fit = slope * years_extended + intercept
    plt.plot(years_extended, line_fit, color='red', label='best fit line 1')
    plt.legend()

    # Create second line of best fit
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']
    slope_recent, intercept_recent, r_value_recent, p_value_recent, std_err_recent = linregress(x_recent, y_recent)
    years_extended_recent = pd.Series(range(2000, 2051))
    line_fit_recent = slope_recent * years_extended_recent + intercept_recent
    plt.plot(years_extended_recent, line_fit_recent, color='green', label='best fit line 2')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()