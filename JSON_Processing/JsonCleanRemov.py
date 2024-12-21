import arxiv
import os
import json
import time
# Define the categories you want to download
categories = ["econ.GN", "econ.TH"]

# Create a directory to save the downloaded files
os.makedirs("arxiv_papers", exist_ok=True)

def fetch_paper_info(category, max_results=2000):
    client = arxiv.Client()
    search = arxiv.Search(
        query=f"cat:{category}",
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    papers = []
    for result in client.results(search):
        paper_info = {
            "id": result.entry_id,
            "title": result.title,
            "abstract": result.summary,
            "authors": [author.name for author in result.authors],
            "categories": result.primary_category,
            "published": result.published.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "updated": result.updated.strftime("%Y-%m-%dT%H:%M:%SZ")
        }
        papers.append(paper_info)
        print(f"Fetched info for {result.title}")

    # Save the paper information to a JSON file
    info_path = f"arxiv_papers/{category}_papers.json"
    with open(info_path, 'w') as f:
        json.dump(papers, f, indent=4)
    print(f"Saved info for {len(papers)} papers in {info_path}")

# Fetch paper information for each category in batches
for category in categories:
    for _ in range(1):  # Adjust the range as needed to control the number of batches
        fetch_paper_info(category, max_results=2000)
        time.sleep(3)
