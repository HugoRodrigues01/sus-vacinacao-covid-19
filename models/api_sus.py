import requests
import json
import sys

# Basic auth
USER: str = "imunizacao_public"
PASS: str = "qlto5t&7r_@+#Tlstigi"
URL_GET: str = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
URL_POST: str = "https://imunizacao-es.saude.gov.br/_search/scroll?scroll=1m"


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
    def get_data(cls) -> dict:
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


if __name__ == "__main__":
    # c0572794-7ec5-477a-b3e4-01c7de100083-i0b0

    api = APISUSControl()
    api.api_start()

    from rich import print

    novo = api.get_data()

    print(novo["hits"]["hits"])
    #
    # print(api.get_number_page)
    # # print(novo["hits"]["hits"])
    # api.post_data()
    #
    # print(api.get_number_page)

    print(novo.__sizeof__())
