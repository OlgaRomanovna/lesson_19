import jsonschema
import requests
from requests import Response
from utils import load_schema


def test_get_single_user_successfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/get_single_user.json")

    result: Response = requests.get(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_post_create_succesfully():
    url = "https://reqres.in/api/users"
    schema = load_schema("json_schemes/post_user.json")

    result: Response = requests.post(url)

    assert result.status_code == 201
    jsonschema.validate(result.json(), schema)


def test_put_update_succesfully():
    url = "https://reqres.in/api/users/2"
    schema = load_schema("json_schemes/put_user.json")

    result: Response = requests.put(url)

    assert result.status_code == 200
    jsonschema.validate(result.json(), schema)


def test_delete_succesfully():
    url = "https://reqres.in/api/users/2"

    result: Response = requests.delete(url)

    assert result.status_code == 204


def test_get_single_user_not_found_unsuccessfully():
    url = "https://reqres.in/api/users/23"

    result: Response = requests.get(url)

    assert result.status_code == 404
    assert result.json() == {}


def test_post_register_unsuccessfully():
    url = "https://reqres.in/api/register"
    schema = load_schema("json_schemes/post_with_error.json")

    result: Response = requests.post(url)

    assert result.status_code == 400
    jsonschema.validate(result.json(), schema)


