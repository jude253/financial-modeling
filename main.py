import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint

def get_change_over_time_list(rand_change_40):
    """
    This function gets the cumulative percentage change over the 40 year period
    in a list by multiplying each year's change by the previous year's 
    cumulative change and putting the value in a new list
    """
    cum_rand_change_40 = rand_change_40.copy()
    for i, change in enumerate(rand_change_40):
        if i >= 1:
            cum_rand_change_40[i] = cum_rand_change_40[i-1]*change
    return cum_rand_change_40


if __name__ == '__main__':
    
    mu, sigma = 0.1377, 0.23 # mean and standard deviation
    initial_investment_amount = 30_000
    last_year_amount = []

    # see how much we will get on average after 100 trials.
    for _ in range(100):
        # random changes over 40 years
        rand_change_40 = 1 + np.random.normal(mu, sigma, size=(40))

        # cumulative random changes over 40 years
        cum_rand_change_40 = get_change_over_time_list(rand_change_40)

        return_over_40 = initial_investment_amount*cum_rand_change_40
        last_year_amount.append(return_over_40[-1])

        # plot data for trial
        plt.plot(return_over_40, linewidth=1, color='r', alpha=.5)
    
    # print summary statistics for the amount remaining in last year:
    df = pd.DataFrame(data={'last_year_amount': last_year_amount})
    print(df.describe().round(2).apply(lambda s: s.apply('{:,}'.format)))
    print('avg rate per year:', format(round(initial_investment_amount*(1+mu)**40, 2), ','))

    # format graph better
    ax = plt.gca()

    ax.set(xlim=(0,40), ylim=(1,10_000_000))
    ax.ticklabel_format(style='plain')
    ax.get_yaxis().set_major_formatter(
        matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    plt.title('Investing in QQQ for 40 years (100 Samples)')

    plt.show()
