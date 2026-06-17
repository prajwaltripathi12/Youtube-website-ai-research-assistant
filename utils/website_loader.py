import requests

from bs4 import BeautifulSoup

from langchain_community.document_loaders import (
    UnstructuredURLLoader
)


def get_website_text(url):

    try:

        loader = UnstructuredURLLoader(
            urls=[url]
        )

        docs = loader.load()

        return "\n".join(
            d.page_content
            for d in docs
        )

    except Exception:

        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=15
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for tag in soup(
            ["script", "style", "nav"]
        ):
            tag.decompose()

        return soup.get_text(
            separator="\n",
            strip=True
        )
