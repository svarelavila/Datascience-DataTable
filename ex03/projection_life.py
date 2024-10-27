from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files. It focuses on data from
    the year 1900 and visualizes the correlation between GNP and life
    expectancy through a scatter plot.
    """
<<<<<<< HEAD
    try:
        # Load data from CSV files
        income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        life_expectancy_years = load("life_expectancy_years.csv")

        # Check if any of the loas is None
        if income_data is None or life_expectancy_years is None:
            raise ValueError("Error: One or more CSV files could not be loaded.")
    
    except Exception as e:
        raise RuntimeError(f"Unexpected error during file loading: {e}")
=======
    # Load data from CSV files
    income_data = load(
        "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
        )
    life_expectancy_years = load("life_expectancy_years.csv")
>>>>>>> 3361dc0f213b434d6bb8dbef4db91498fc08efbb

    # Define the year of interest
    year_1900_column = '1900'

    # Check if the year column exists in both dataset
    if (year_1900_column not in income_data.columns or
            year_1900_column not in life_expectancy_years.columns):
        raise ValueError(
            f"Year {year_1900_column} not found in one of the data sets."
        )

    # Extract data for the year 1900
    gnp_1900 = income_data[year_1900_column].dropna()  # Remove NaN values
    life_expectancy_1900 = (
        life_expectancy_years[year_1900_column].dropna()  # Remove NaN values
    )
    # Ensure that both DataFrames have the same index
    common_index = gnp_1900.index.intersection(life_expectancy_1900.index)
    gnp_1900 = gnp_1900[common_index]
    life_expectancy_1900 = life_expectancy_1900[common_index]

    # Create the scatter plot
    plt.figure(figsize=(10, 6))
<<<<<<< HEAD
    plt.scatter(gnp_1900, life_expectancy_1900, color='blue', alpha=0.7, edgecolors='w', s=100)
=======
    plt.scatter(gnp_1900, life_expectancy_1900, color='green', alpha=0.7,
                edgecolors='w', s=100)
>>>>>>> 3361dc0f213b434d6bb8dbef4db91498fc08efbb
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    plt.tight_layout()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.show()


if __name__ == "__main__":
    main()
