from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load life expectancy data, filter for Spain, and display a line graph.

    Loads the life expectancy dataset from a CSV file, filters the data for
    Spain, and displays a line graph showing the life expectancy in Spain
    over the years. The x-axis of the graph includes year labels from
    1800 to 2080, with every 40th year label displayed and rotated for clarity.
    The graph includes a title, axis labels, legend, and grid.
    """
    try:

        df = load("life_expectancy_years.csv")

        # Check if load returned None
        if df is None:
            raise FileNotFoundError("The dataset could not be loaded.")

        # Filter for Spain's data
        spain_data = df[df['country'] == 'Spain']

        # Extract years and life expectancy values
        years = spain_data.columns[1:].astype(int)
        life_expectancy = spain_data.values[0][1:]

        # Plotting
        plt.plot(years, life_expectancy)
        plt.title('Spain Life Expectancy Projections')
        plt.xlabel('Year')
        plt.xticks(years[::40])
        plt.ylabel('Life Expectancy')
        plt.yticks(range(30, 91, 10))
        plt.show()

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
