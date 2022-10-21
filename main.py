import extract_data
import time


class Static:
    path = "C:\\Users\\pere\\OneDrive - Universitat de les Illes Balears\\Documents\\UIB\\Recerca\Oxford University " \
           "Press\\scripts 2022\\"
    results = path + "results.csv"
    results_py = path + "results_py.csv"


def main():
    data = extract_data.parse_data(Static.results)
    expressives = extract_data.collect_data(data)
    extract_data.write_data(expressives, results_py=Static.results_py)


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Process finished with exit!")
    print("Execution time: %s seconds." % (time.time() - start_time))
