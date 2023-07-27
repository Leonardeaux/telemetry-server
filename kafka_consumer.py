from kafka import KafkaConsumer
import ast


def start_consume():
    consumer = KafkaConsumer(
        'topic1',
        bootstrap_servers=['localhost:29092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: x.decode('utf-8'))

    for message in consumer:
        data = ast.literal_eval(message.value)
        print(data['averageSpeed'])
        try:
            with open('data.csv', 'a') as fichier:
                fichier.write(f"{data['laps']}, {data['averageSpeed']}\n")
                fichier.close()

        except:
            pass


if __name__ == '__main__':
    start_consume()
