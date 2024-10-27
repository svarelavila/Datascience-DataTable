from load_csv import load
import matplotlib.pyplot as plt

def population_conversion(pop_str):
    """
    Preprocesses the population string to convert it into
    a numeric value in standard form.

    Args:
        pop_str (str): Population string with or without
        the 'M' suffix for million or 'k' suffix for thousand.

    Returns:
        float: Numeric population value.

    Raises:
        ValueError: If the population string cannot be converted to a float.
    """
    try:
        if pop_str.endswith("M"):
            return float(pop_str[:-1]) * 1e6
        elif pop_str.endswith("k"):
            return float(pop_str[:-1]) * 1e3
        else:
            return float(pop_str)
    except ValueError as e:
        raise ValueError(f"Error processing population value '{pop_str}': {e}")

def main():
    """
    Loads population data from a CSV file, processes and
    plots the population comparison of Spain and Italy.
    """
    try:
        df = load("population_total.csv")

        if df is None:
            raise FileNotFoundError("The dataset could not be loaded.")

        # Countries to compare
        country1 = "Spain"
        country2 = "Italy"

        # Check if the countries are in the dataset
        if country1 not in df['country'].values or country2 not in df['country'].values:
            raise ValueError(f"One or both countries are not in the dataset: {country1}, {country2}")

        # Filter the data of the selected countries
        country1_data = df[df['country'] == country1].iloc[:, 1:]
        country2_data = df[df['country'] == country2].iloc[:, 1:]

        # Flatten the data and convert to numeric format
        country1_pop = country1_data.values.flatten()
        country2_pop = country2_data.values.flatten()
        years = country1_data.columns.astype(int)

        # Process population data
        try:
            country1_pop = [population_conversion(pop) for pop in country1_pop]
            country2_pop = [population_conversion(pop) for pop in country2_pop]
        except ValueError as e:
            raise ValueError(f"Error processing population data: {e}")

        # Create the plot
        plt.plot(years, country1_pop, color='blue', label=country1)
        plt.plot(years, country2_pop, color='green', label=country2)

        plt.title("Population Projections")
        plt.xlabel("Year")
        plt.xticks(range(1800, 2051, 40), range(1800, 2051, 40))
        plt.xlim(1790, 2050)
        plt.ylabel("Population")
        plt.legend(loc='lower right')
        plt.tight_layout()

        max_pop = max(max(country1_pop), max(country2_pop))
        y_ticks = [i * 20e6 for i in range(int(max_pop / 20e6) + 1)]
        y_ticks = [tick for tick in y_ticks if tick != 0]  # Remove 0M
        plt.yticks(y_ticks, ["{:,.0f}M".format(pop / 1e6) for pop in y_ticks])

        plt.show()

    except (FileNotFoundError, ValueError) as error:
        print(__name__ + ":", error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
