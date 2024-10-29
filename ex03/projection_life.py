from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files. It focuses on data from
    the year 1900 and visualizes the correlation between GNP and life
    expectancy through a scatter plot.
    """
    try:
        # Load data from CSV files
        income_data = load(
            "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
            )
        life_expectancy_years = load("life_expectancy_years.csv")

        # Check if any of the datasets is None
        if income_data is None or life_expectancy_years is None:
            raise ValueError("The dataset could not be loaded.")

        # Define the year of interest
        year_1900_column = '1900'

        # Check if the year column exists in both datasets
        if (year_1900_column not in income_data.columns or
                year_1900_column not in life_expectancy_years.columns):
            raise ValueError(
                f"Year {year_1900_column} not found in one of the datasets."
            )

        # Extract data for the year 1900
        gnp_1900 = income_data[year_1900_column].dropna()
        life_expectancy_1900 = (
            life_expectancy_years[year_1900_column].dropna()
          )
        # Ensure that both DataFrames have the same index
        common_index = gnp_1900.index.intersection(life_expectancy_1900.index)
        gnp_1900 = gnp_1900[common_index]
        life_expectancy_1900 = life_expectancy_1900[common_index]
        # Create the scatter plot
        plt.figure(figsize=(8, 6))
        plt.scatter(gnp_1900, life_expectancy_1900, color='blue', alpha=0.7,
                    edgecolors='w', s=100)
        plt.title(f"{year_1900_column}")
        plt.xlabel("Gross Domestic Product")
        plt.ylabel("Life Expectancy")
        plt.xscale("log")
        plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
        plt.tight_layout()
        plt.show()

    except ValueError as ve:
        print(f"Value Error: {ve}")
    except Exception as e:
        print(f"Error loading data: {e}")


if __name__ == "__main__":
    main()
