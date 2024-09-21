# Performing Google Search using Python code

try:
  from googlesearch import search
except ImportError:
  print("No module named 'google' found")

# to search
query = "facebook"

for j in search(query, tld="com", num=5, stop=5, pause=2):
  print(j)
