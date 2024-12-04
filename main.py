from multiprocessing import Pool
from datetime import datetime

def read_info(name):
    
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:  #
                break
            all_data.append(line.strip())

def measure_time_linear(filenames):

    start_time = datetime.now()
    for filename in filenames:
        read_info(filename)
    end_time = datetime.now()
    print(f"Линейное выполнение: {end_time - start_time}")

def measure_time_parallel(filenames):

    start_time = datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = datetime.now()
    print(f"Параллельное выполнение: {end_time - start_time}")

if __name__ == '__main__':

    filenames = [f'./file {number}.txt' for number in range(1, 5)]


    print("Запуск линейного выполнения...")
    measure_time_linear(filenames)

