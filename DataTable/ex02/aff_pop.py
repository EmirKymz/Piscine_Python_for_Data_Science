from load_csv import load
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

#Create a program that calls the load function from the first exercise, loads the file
#population_total.csv, and displays the country information of your campus versus other
#country of your choice. Your graph must have a title, a legend for each axis and a
#legend for each graph.
#You must display the years from 1800 to 2050.
#For example, for the 42 campuses in France we will have this result.

def convert_to_value(value):
    pop = []
    for i in value:
        if i.endswith("M"):
            pop.append(float(i[:-1]) * 1e6)
        elif i.endswith("k"):
            pop.append(float(i[:-1]) * 1e3)
        else:
            pop.append(float(i))
    return pop

def millions(x, pos):
    'The two args are the value and tick position'
    return '%1.0fM' % (x * 1e-6)

def main():
    file = load("population_total.csv")
    if file is not None:
        campus = file[file["country"] == "France"].iloc[0:, 1:]
        years = campus.columns.astype(int)
        population = convert_to_value(campus.values[0])
        plt.plot(years, population, label="France")
        campus = file[file["country"] == "Belgium"].iloc[0:, 1:]
        population = convert_to_value(campus.values[0])
        plt.plot(years, population, label="Belgium")
        plt.xlabel("year")
        plt.ylabel("Population")
        plt.title("France x Belgium Population Projections")
        plt.legend()
        gca = plt.gca() # get current axes
        gca.yaxis.set_major_formatter(ticker.FuncFormatter(millions))
        #plt.savefig('grafik.png') 
        plt.show()
    return 0

if __name__ == "__main__":
    main() 