import datetime
import sys
import os

today = datetime.date.today()
date=today.strftime("%Y-%m-%d")
desc=sys.argv[1]
fname=f"_drafts/{date}-{desc}.md"
f = open(fname, "w")
f.write("---\n")
f.write(f'title: "{desc}"\n')
f.write(f"layout: post\n")
f.write(f"date: {date}\n")
f.write(f"categories: rant\n")
f.write(f"---\n")
f.close()
os.system(f"git add {fname}")
