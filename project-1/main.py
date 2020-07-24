import csv
import numpy as np

def write_csv():
    with open('ProductDetails.csv') as product_details_csv:
        product_details_data = list(csv.reader(product_details_csv))
        product_details_data = product_details_data[1:]
        product_details_data = product_details_data[:-15]
        product_details_data_np = np.array(product_details_data)

    with open('ProductPerformance.csv') as product_performance_csv:
        product_performance_data = list(csv.reader(product_performance_csv))
        product_performance_data = product_performance_data[1:]
        product_performance_data = product_performance_data[:-8]
        product_performance_data_np = np.array(product_performance_data)

    # Sort product_performance by first column,
    # based on index of first column in first column of product_details

    compare_list = list(product_details_data_np[:, 0])
    print("Sorting...")
    product_performance_data.sort(key=lambda row: compare_list.index(row[0]))
    product_performance_data_out = np.array(product_performance_data)
    np.savetxt("ProductPerformanceSorted.csv", product_performance_data_out, delimiter=",", fmt='%s')
    print("Done!")

def read_csv(data_list, start_val, end_val):

    perf_data_list_np = data_list

    # start_val = 818
    # end_val = 4068

    sum = 0
    check_start_val = True
    first_run = True
    
    prev_row = perf_data_list_np[0]
    for i, row in enumerate(perf_data_list_np):

        # handling a certain range
        if check_start_val and float(row[0]) != start_val:
            continue
        else:
            check_start_val = False
            if first_run:
                prev_row = row
                first_run = False

        if row[0] != prev_row[0]:
            try:
                sum += float(prev_row[4])
                # print(sum)
            except ValueError:
                # pass
                check_val = prev_row[0]
                current_index = i - 2
                while True:
                    if current_index < 0:
                        break
                    test_row = perf_data_list_np[current_index]
                    if test_row[0] != check_val:
                        break
                    try:
                        sum += float(test_row[4])
                        break
                    except ValueError:
                        current_index -= 1

            # handling a certain range
            if float(prev_row[0]) == end_val:
                break

        prev_row = row
    
    return sum
    
if __name__ == "__main__":

    # Comment to avoid overhead
    write_csv()

    values = [
        (818, 137668),
        (99015, 116778),
        (1157, 144477),
        (1363, 146411),
        (35, 141817),
        (442, 146031),
        (204, 146558),
        (2385, 146559),
        (21, 146615),
        (2212, 144443),
        (1413, 146511),
        (47694, 145645),
        (1989, 146659),
        (37614, 146037),
    ]

    with open('ProductPerformanceSorted.csv') as perf_data:
        perf_data_list = list(csv.reader(perf_data))
        perf_data_list_np = np.array(perf_data_list)

    for (i, j) in values:
        print("{}, {}: {}".format(i, j, read_csv(perf_data_list_np, i, j)))
