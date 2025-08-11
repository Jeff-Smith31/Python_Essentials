import json

def read_and_write_json():
    d = {
        "firstName": "Tom",
        "lastName": "Jack",
        "gender": "male",
        "age": 35,
        "address": {
            "streetAddress": "126",
            "city": "San Jone",
            "state": "CA",
            "postalCode": "95150"
        },
        "phoneNumbers": [
            {"type": "home", "number": "4083627627"}
        ]
    }

    filename = "/content/sample_data/sample1.json"

    with open(filename, 'w') as f:
        json.dump(d, f)

# Read the JSON file and also print the file content in JSON format.
    with open(filename, 'r') as f:
        d = json.load(f)

        print(json.dumps(d, indent=2))

    # Output
    '''{
        "firstName": "Tom",
        "lastName": "Jack",
        "gender": "male",
        "age": 35,
        "address": {
            "streetAddress": "126",
            "city": "San Jone",
            "state": "CA",
            "postalCode": "95150"
        },
        "phoneNumbers": [
            {
                "type": "home",
                "number": "4083627627"
            }
        ]
    }'''