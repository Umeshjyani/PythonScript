def find_missing_keys(json1, json2):
    for key in json1:
        if key not in json2:
            print(f"Key '{key}' is missing in the second object")

# Example JSON-like objects (dictionaries)
json1 = {
    "name": "John",
    "age": 25,
    "city": "New York",
    "country": "USA"
}

json2 = {
    "name": "John",
    "city": "New York"
}

# Call the function
find_missing_keys(json1, json2)