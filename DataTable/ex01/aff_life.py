import matplotlib.pyplot as plt
from load_csv import load

def main():
    file = load("life_expectancy_years.csv")
    if file is not None:
        campus = file[file["country"] == "France"].iloc[0:, 1:]
        years = campus.columns.astype(int)
        life_expectancy = campus.values[0].astype(float)
        plt.plot(years, life_expectancy, label="France")
        plt.xlabel("year")
        plt.ylabel("Life expectancy")
        plt.title("France life expectancy Projections")
        plt.legend()
        plt.savefig('grafik.png') 
        # plt.show()
    return 0


if __name__ == "__main__":
    main()