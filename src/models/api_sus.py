import requests
import json
import sys
from typing import Any, Dict
from configs.global_conf import URL_GET, URL_POST, USER, PASS


class APISUSControl:

    # The API´s data
    __data: requests.Response | list = []

    # The number of page of API
    __number_page: int = 1

    @classmethod
    def api_start(cls) -> None:

        # Get data of SUS´s API
        cls.__data = requests.get(URL_GET, auth=(USER, PASS))

    @classmethod
    def get_data(cls) -> Dict[Any, Any]:
        """
        This function going to get datas using SUS´s API.
        """

        # Converting the data for a dictionary type
        return cls.__data.json()

    @classmethod
    def post_data(cls) -> None:
        """
        This function use POST of HTTP method, and get the next page of datas of API.
        """

        # get the id for the next page
        payload: str = json.dumps({"scroll_id": cls.__data.json()["_scroll_id"]})

        headers: dict = {"Content-Type": "application/json"}

        # Get the next page of SUS´s API
        cls.__data = requests.request(
            "POST", URL_POST, headers=headers, auth=(USER, PASS), data=payload
        )

        cls.__number_page += 1

    @classmethod
    @property
    def get_number_page(cls) -> int:

        return cls.__number_page
