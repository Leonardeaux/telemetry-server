import acc_telemetry as acct
import os
import shutil
import time


def remove_files(directory):
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print(f'Erreur lors de la suppression de {file_path}. Raison: {e}')


def produce_files(file_path):
    remove_files(file_path)
    remove_files("C:/Users/enzol/spark_streaming/streaming_output")
    print("Start !")

    i = 0
    while True:

        with open(os.path.join(file_path, f'file{i}.json'), 'a') as f:
            for j in range(10):
                physics = acct.read_physics()
                if physics["speedKmh"] == 0:
                    continue
                message = '{' \
                          + '"timestamp":' + str(int(time.time())) \
                          + ',"gas":' + str(round(physics["gas"], 2)) \
                          + ',"brake":' + str(round(physics["brake"], 2)) \
                          + ',"speedKmh":' + str(int(physics["speedKmh"])) \
                          + '}\n'
                print(message)
                f.write(message)
                time.sleep(0.1)
        i += 1


if __name__ == '__main__':
    directory = "C:/Users/enzol/spark_streaming/streaming_input"
    produce_files(directory)