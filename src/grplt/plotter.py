import matplotlib.pyplot as plt
from cfg import config

def create_plot(data, title="Graph"):
    plt.style.use(config.settings['plot_style'])
    fig, ax = plt.subplots()
    data.plot(ax=ax)
    ax.set_title(title)
    return fig