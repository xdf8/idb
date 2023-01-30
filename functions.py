import requests
import yaml
import csv


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

    with open("data.csv", "a", encoding="UTF8") as f:
        writer = csv.writer(f)

        # write the data
        writer.writerow(data)


def write_data_to_api(temp, hum, dist, config):
    """
    Writes data to the API.
    """
    url = "https://api.thingspeak.com/update"
    params = {
        "api_key": config["API_KEY"],
        "field1": temp,
        "field2": hum,
        "field3": dist,
    }
    try:
        r = requests.get(url, params=params)

    except requests.exceptions.RequestException as e:
        print(e)
