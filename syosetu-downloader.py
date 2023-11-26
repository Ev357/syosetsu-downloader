#!/usr/bin/env python3
import argparse
import os
import re
from pathlib import Path
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

parser = argparse.ArgumentParser()
parser.add_argument("url", help="The syosetu url (https://syosetu.top/...)")
parser.add_argument("-d", "--dir", help="Sets the output directory", default="output")
args = parser.parse_args()

print("Downloading chapters data...")
response = requests.get(args.url)
print("done")

parsed_url = urlparse(args.url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}"

soup = BeautifulSoup(response.text, "lxml")

chap_list = soup.find("div", class_="chaplist")
title = soup.find("h1", class_="entry-title")

path = Path(args.dir)
path.mkdir(parents=True, exist_ok=True)
path.cwd()

manga_folder: Path = path / title.string
manga_folder.mkdir(parents=True, exist_ok=True)
manga_folder.cwd()

print("Downloading chapters...")
for chapter_link in reversed(chap_list.find_all("a")):
    chapter_number = re.findall(r"Chapter (\d+(\.\d+)?)", chapter_link.string)[-1][0]

    chapter_folder: Path = manga_folder / chapter_link.string
    chapter_folder.mkdir(parents=True, exist_ok=True)
    chapter_folder.cwd()

    chapter_url = f"{base_url}{chapter_link['href']}"

    chapter_response = requests.get(chapter_url)
    chapter_soup = BeautifulSoup(chapter_response.text, "lxml")

    img_list = chapter_soup.find("div", class_="entry-content")

    for index, img_link in enumerate(tqdm(img_list.find_all("img"), desc=f"Chapter {chapter_number}", unit="page")):
        img_response = requests.get(img_link["data-src"])
        parsed_img_url = urlparse(img_link["data-src"])
        
        extension = os.path.splitext(parsed_img_url.path.split("/")[-1])[1]

        img = open(chapter_folder / f"Chapter_{chapter_number}_Page_{index + 1}{extension}", "wb")
        img.write(img_response.content)
        img.close()

print("done")
