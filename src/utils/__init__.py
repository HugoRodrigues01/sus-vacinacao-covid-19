from .worker import Worker, start_worker
from typing import Any, List
from rich import print


def format_datas(data) -> List:
    """
    This function will format all datas of API.
    """

    list_data: list = []

    for index, values in enumerate(data["hits"]["hits"]):

        headers: list = values["_source"].keys()
        infos: list = values["_source"].values()
        _id: str = values["_source"]["paciente_id"]

        list_data.append(
            {"headers": headers, "infos": infos, "id": _id, "index": index}
        )

    # print(list_data[0]["headers"])
    # print(list_data[0]["infos"])
    print(list_data[0]["id"])
    # print(len(list_data))
    # print(list(map(lambda v: v["id"], list_data)))
    return list_data
