import acc_telemetry as acct
import time
import json
from utils import param_to_message


def launch_dataset_feeding():
    previous_data = None

    with open("telemetry.json", 'w') as f:
        while True:
            physics = acct.read_physics()

            if physics["speedKmh"] < 1 or physics["gas"] < 0.01:
                continue

            if previous_data is not None:
                output_data = {
                    'speed': int(previous_data['speedKmh']),
                    'acceleration': round(previous_data["gas"], 2),
                    'speedT1': int(physics["speedKmh"])
                }
                f.write(json.dumps(output_data) + '\n')
                print(output_data)
            previous_data = physics
            time.sleep(0.5)


def launch_dataset_feeding_v2():
    with open("telemetry2.json", 'w') as f:
        while True:
            physics = acct.read_physics()

            if physics["speedKmh"] < 1 or physics["brake"] < 0.01:
                continue

            output_data = {
                'timestamp': int(time.time()),
                'speed': int(physics['speedKmh']),
                'brake': round(physics["brake"], 2),
                'steerAngle': round(physics["steerAngle"], 2),
                'abs': int(physics["abs"])
            }
            f.write(json.dumps(output_data) + '\n')
            print(output_data)
            time.sleep(1)


if __name__ == '__main__':
    launch_dataset_feeding_v2()