import os
import sys

"""
Add the /src in path of python

This path will short the path of imports
"""
sys.path.append(os.getcwd() + "/src")


# Configs of main window
WINDOW_TITLE: str = "SUS vacinação covid-19"
WIDTH: int = 700
HEIGHT: int = 500

# Configs of SUS´s API
USER: str = "imunizacao_public"
PASS: str = "qlto5t&7r_@+#Tlstigi"
URL_GET: str = "https://imunizacao-es.saude.gov.br/_search?scroll=1m"
URL_POST: str = "https://imunizacao-es.saude.gov.br/_search/scroll?scroll=1m"
