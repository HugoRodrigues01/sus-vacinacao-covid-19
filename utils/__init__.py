from pickle import dump, load, loads
import os

OBJECT: dict = {"nome":"hugo"}
PATH: str = "page_data.dat"


# Will create the file if it not exists
if not os.path.exists(PATH):

    with open(PATH, "xb") as file:
        pass


class PagesPickle:

    @staticmethod
    def add_pickle(obj: any) -> None:
        """
        This function going to add a new object in file binery
        """

        with open(PATH, "wb") as file:

            dump(obj, file)
    
    @staticmethod
    @property
    def get_pickle() -> dict:

        with open(PATH, "rb") as files:

            r = files.read()

            return load(r)

PagesPickle.add_pickle(OBJECT)
print(PagesPickle.get_pickle)