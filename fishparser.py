#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

import requests
from bs4 import BeautifulSoup

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36",
}


def get_data(url):

    res = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(res.text, "lxml")
    fs = [
        f.text.strip().lower()
        for f in soup.find(
            string=re.compile(r"англо-русский словарь названий рыб", re.IGNORECASE)
        ).find_all_next("b")
        if f
    ]
    return [f for f in fs if f.isalpha() and re.search("[a-z]", f) and not "fish" in f]


def main():
    url = "https://study-english.info/vocabulary-fish.php"
    fs_all = get_data(url)
    print(fs_all)


if __name__ == "__main__":
    main()
