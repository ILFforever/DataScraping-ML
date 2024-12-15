import requests
import time
import xml.etree.ElementTree as ET

# Function to parse individual paper metadata from the API response
def parse_paper(entry):
    return {
        "id": entry.find("{http://www.w3.org/2005/Atom}id").text,
        "title": entry.find("{http://www.w3.org/2005/Atom}title").text.strip(),
        "abstract": entry.find("{http://www.w3.org/2005/Atom}summary").text.strip(),
        "authors": [
            author.find("{http://www.w3.org/2005/Atom}name").text
            for author in entry.findall("{http://www.w3.org/2005/Atom}author")
        ],
        "categories": entry.find("{http://arxiv.org/schemas/atom}primary_category").attrib["term"],
        "published": entry.find("{http://www.w3.org/2005/Atom}published").text,
        "updated": entry.find("{http://www.w3.org/2005/Atom}updated").text,
    }

# Function to scrape all metadata from arXiv
def scrape_arxiv(output_file="arxiv_data.json"):
    base_url = "http://export.arxiv.org/api/query"
    start = 0
    max_results = 100  # Maximum allowed by arXiv API
    all_papers = []

    while True:
        print(f"Fetching records {start} to {start + max_results - 1}...")

        # Query parameters for arXiv API
        params = {
            "search_query": "all",  # Retrieve all papers
            "start": start,
            "max_results": max_results,
            "sortBy": "submittedDate",
            "sortOrder": "ascending",
        }

        # API request
        response = requests.get(base_url, params=params)
        if response.status_code != 200:
            print("Error fetching data from arXiv:", response.status_code)
            break

        # Parse XML response
        root = ET.fromstring(response.content)
        entries = root.findall("{http://www.w3.org/2005/Atom}entry")

        if not entries:
            print("No more entries to fetch.")
            break

        # Parse and store paper metadata
        for entry in entries:
            paper = parse_paper(entry)
            all_papers.append(paper)

        # Increment start for pagination
        start += max_results

        # Pause to avoid rate limiting (arXiv API allows 1 request/sec)
        time.sleep(1)

    # Save to a JSON file
    print(f"Saving {len(all_papers)} records to {output_file}...")
    import json
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)

    print("Scraping completed.")

# Run the scraper
if __name__ == "__main__":
    scrape_arxiv()
