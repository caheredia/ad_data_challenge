import matplotlib.pyplot as plt 

def spark_plot(df, title):
    '''Plots sparklines for columns in df.

    Creates callouts for max and mean of each column.
    Saves plot with title as pdf in reports/figures folder.

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe to plot
    title : string
        plot title

    Returns
    -------
    matplotlib figure 
    '''
    fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(
        5, 1, sharex=True, figsize=(12, 4))

    for column, axess in zip(df.columns, (ax1, ax2, ax3, ax4, ax5)):
        df[column].plot(ax=axess, color='orange')
        axess.set_ylabel(str(column), rotation=0, labelpad=100, fontsize=16)
        axess.get_yaxis().set_ticks([])
        axess.set_xlabel('')
        axess.set_facecolor('.97')

        axess2 = axess.twinx()
        local_max = round(df[column].max(), 3)
        local_mean = round(df[column].mean(), 3)
        right_string = 'mean: {local_mean} max: {local_max}'.format(
            local_mean=local_mean,  local_max=local_max)
        axess2.set_ylabel(right_string, rotation=0,
                          labelpad=100, fontsize=14, color='gray')
        axess2.get_yaxis().set_ticks([])

    ax1.set_title(title, fontsize=18)

    fig.tight_layout()
    plt.savefig('reports/figures/'+title + '.pdf')
    return plt.show()