import requests
import yaml
import csv
import time


def load_yaml_file(yaml_path="config.yaml") -> dict:
    """
    Loads a yaml-file.
    """
    with open(yaml_path, "r") as stream:
        try:
            config = yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            print(exc)
    return config


def write_to_csv(time, temp, hum, dist):
    data = [time, temp, hum, dist]
    with open("data.csv", "w", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)


def write_data_to_api(temp, hum, dist, config_path):
    """
    Writes data to the API.
    """
    config = load_yaml_file(config_path)
    url = "https://api.thingspeak.com/update"
    params = {
        "api_key": config["API_KEY"],
        "field1": temp,
        "field2": hum,
        "field3": dist,
    }
    try:
        r = requests.get(url, params=params)
        print(r.raise_for_status())
    except requests.exceptions.RequestException as e:
        print(e)


def write_bulk_to_api(file_name, config_path):
    """
    Writes data from a csv-file to the API.
    """
    config = load_yaml_file(config_path)
    channel_id = 2012287
    url = f"https://api.thingspeak.com/channels/{channel_id}/bulk_update.csv"
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            params = {
                "api_key": config["API_KEY"],
                "field1": row[0],
                "field2": row[1],
                "field3": row[2],
            }
            try:
                r = requests.get(url, params=params)

            except requests.exceptions.RequestException as e:
                print(e)

            time.sleep(1)


if __name__ == "__main__":
    write_csv_to_api(file_name="test.csv", config_path="config.yaml")
