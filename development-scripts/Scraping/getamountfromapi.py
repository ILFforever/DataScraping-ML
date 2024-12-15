import requests
import xml.etree.ElementTree as ET

# Define the query URL
query_url = "http://export.arxiv.org/api/query?search_query=all:quantum&start=0&max_results=1"

# Send the request
response = requests.get(query_url)

# Parse the XML response
root = ET.fromstring(response.content)

# Find the total number of results
total_results = root.find('{http://a9.com/-/spec/opensearch/1.1/}totalResults').text

print(f"Total number of results: {total_results}")
