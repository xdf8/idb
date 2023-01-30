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


def write_to_csv(temp, hum, dist, file_name):
    data = [temp, hum, dist]
    with open(file_name, "w", encoding="UTF8") as f:
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
