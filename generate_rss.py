from datetime import datetime

today = datetime.utcnow()
date_str = today.strftime("%d.%m.%y")
pub_date = today.strftime("%a, %d %b %Y %H:%M:%S +0000")

rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>Dzień i miesiąc</title>
    <description>Codzienna informacja o dniu i miesiącu</description>
    <link>https://zanfil.github.io/cos/feed.xml</link>
    <lastBuildDate>{pub_date}</lastBuildDate>
    <item>{date_str}</item>
  </channel>
</rss>"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(rss)
