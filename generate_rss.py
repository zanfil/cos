from datetime import datetime

today = datetime.utcnow()
day_and_month = today.strftime("%d %B")
pub_date = today.strftime("%a, %d %b %Y %H:%M:%S +0000")
guid = today.strftime("day-%Y%m%d")

rss = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
  <channel>
    <title>Dzień i miesiąc</title>
    <description>Codzienna informacja o dniu i miesiącu</description>
    <link>https://twojanazwa.github.io/rss-dzien/feed.xml</link>
    <lastBuildDate>{pub_date}</lastBuildDate>
    <item>
      <title>{day_and_month}</title>
      <description>Dzisiaj jest {day_and_month}.</description>
      <pubDate>{pub_date}</pubDate>
      <guid>{guid}</guid>
    </item>
  </channel>
</rss>"""

with open("feed.xml", "w", encoding="utf-8") as f:
    f.write(rss)
