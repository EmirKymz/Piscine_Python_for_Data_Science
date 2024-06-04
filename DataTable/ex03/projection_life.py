import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.ticker as ticker
from load_csv import load

def convert_to_value(value, pos):
    """
    make the x-axis labels more readable
    """
    if value >= 1e6:
        return f'{value*1e-6:.0f}M'
    elif value >= 1e3:
        return f'{value*1e-3:.0f}k'
    else:
        return f'{value:.0f}'


def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.0fM' % (x * 1e-6)


def main():
    income_df = load('income_per_person_gdppercapita_ppp_inflation_adjusted.csv')
    life_expectancy_df = load('life_expectancy_years.csv')
    if income_df is None or life_expectancy_df is None:
        print('Data is not loaded. Exiting...')
        exit()

    plt.title('1900')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life expectancy')
    plt.scatter(income_df['1800'], life_expectancy_df['1800'])
    plt.xscale('log')
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(convert_to_value))
    plt.gca().set_xticks([300, 1000, 10000])

    #plt.show()
    plt.savefig('projection_life.png')

if __name__ == '__main__':
    main()
