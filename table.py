"""record test code"""

from python_graphql_client import GraphqlClient
import feedparser
import httpx
import json
import pathlib
import re
import os
import datetime


def fetch_weekly():
    content = feedparser.parse("https://weekly.tw93.fun/rss.xml")["entries"]

    entries = [
        "* <a href='{url}' target='_blank'>{title}</a> - {published}".format(
            title=entry["title"],
            url=entry["link"].split("#")[0],
            published=datetime.datetime.strptime(
                entry["published"], "%a, %d %b %Y %H:%M:%S %Z"
            ).strftime("%Y-%m-%d"),
        )
        for entry in content
    ]

    return "\n".join(entries[:5])


print(fetch_weekly())

"""
* <a href='https://weekly.tw93.fun/posts/157-%E5%BC%95%E5%8A%9B%E5%89%A7%E5%9C%BA/' target='_blank'>第157期 - 引力剧场</a> - 2023-12-18
"""
