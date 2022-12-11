import requests
from bs4 import BeautifulSoup

MAIN_URL = "https://hplovecraft.fandom.com/es"
API_PATH = "/api.php?format=json"
BASE_URL = MAIN_URL + API_PATH


def get_page_image(title) -> str:
    parameters = "action=query&prop=pageimages&piprop=original&titles=" + title
    response_json = __get_json(parameters)
    image_info = list(response_json["query"]["pages"].values())[0]

    if "original" in image_info:
        source = image_info["original"]["source"]
        return source


def get_image(title) -> str:
    parameters = "action=query&generator=images&prop=imageinfo&iiprop=url&titles=" + title
    response_json = __get_json(parameters)

    if "query" in response_json:
        image_info = list(response_json["query"]["pages"].values())[0]["imageinfo"]
        source = image_info[0]["url"]
        return source


def get_content(title):
    parameters = "action=parse&prop=text&page=" + title
    response_json = __get_json(parameters)

    if "parse" in response_json:
        response_html = response_json["parse"]["text"]["*"]
        soup = BeautifulSoup(response_html, "html.parser")
        main_div = soup.find_all("div", class_="mw-parser-output")[0]
        p_elements = main_div.find_all("p")
        return p_elements[1].get_text()


def __get_json(url_parameters):
    url = BASE_URL
    if url_parameters:
        url = url + "&" + url_parameters
    print(url)
    response = requests.get(url)
    response_json = response.json()
    return response_json
