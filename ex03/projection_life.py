from load_csv import load
import matplotlib.pyplot as plt

def main():
    """
    Loads data for Gross National Product (GNP) per capita
    and life expectancy from separate CSV files. It focuses on data from
    the year 1900 and visualizes the correlation between GNP and life
    expectancy through a scatter plot.
    """
    # Cargar los datos desde los archivos CSV
    income_data = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life_expectancy_years = load("life_expectancy_years.csv")
    
    # Definir el año de interés
    year_1900_column = '1900'
    
    # Verificar si la columna del año existe en ambos conjuntos de datos
    if year_1900_column not in income_data.columns or year_1900_column not in life_expectancy_years.columns:
        raise ValueError(f"Year {year_1900_column} not found in one of the data sets.")
    
    # Extraer los datos para el año 1900
    gnp_1900 = income_data[year_1900_column].dropna()  # Eliminar valores NaN
    life_expectancy_1900 = life_expectancy_years[year_1900_column].dropna()  # Eliminar valores NaN
    
    # Asegurar que los DataFrames tengan el mismo índice (es decir, los mismos países)
    common_index = gnp_1900.index.intersection(life_expectancy_1900.index)
    gnp_1900 = gnp_1900[common_index]
    life_expectancy_1900 = life_expectancy_1900[common_index]
    
    # Crear el gráfico de dispersión
    plt.figure(figsize=(10, 6))
    plt.scatter(gnp_1900, life_expectancy_1900, color='green', alpha=0.7, edgecolors='w', s=100)
    
    # Título y etiquetas
    plt.title("1900")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    
    # Configurar el eje x con escala logarítmica para una mejor visualización
    plt.xscale("log")
    plt.xticks(ticks=[300, 1000, 10000], labels=['300', '1k', '10k'])
    
    # Mejorar el diseño
    plt.tight_layout()
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    
    # Mostrar el gráfico
    plt.show()

if __name__ == "__main__":
    main()
