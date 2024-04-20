import matplotlib.pyplot as plt
import seaborn as sns
import mplcyberpunk

def plots(calculation):
    # Set the cyberpunk style
    plt.style.use('cyberpunk')
    plt.figure(figsize=(15, 8))

    # Plotting multiple lines with markers and different colors
    sns.lineplot(data=calculation, y='cumulative_growth_SMA_6', x=calculation.index, label='Strategy', marker='o')

    # Adding a title and labels
    plt.title("Strategy Cumulative Growth | Starting point at 50 000 SEK")
    plt.xlabel('Time')
    plt.ylabel('Cumulative Growth')

    # Add gradient fill and glow effect
    mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.2, gradient_start='zero')
    mplcyberpunk.make_lines_glow()

    # # Display the legend
    # plt.legend(title='Strategy type')

    plt.show()