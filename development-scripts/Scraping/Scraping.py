import arxiv
import json

# Function to fetch paper metadata using the official arXiv API wrapper
def fetch_arxiv_data(output_file="arxiv_data.json"):
    client = arxiv.Client()
    query = arxiv.Search(
        query="all",  # Retrieve all papers
        max_results=50,  # Number of papers for test version
        sort_by=arxiv.SortCriterion.SubmittedDate
    )

    all_papers = []

    print("Starting data fetch...")

    # Iterate over results and fetch metadata
    for result in client.results(query):
        paper = {
            "id": result.entry_id,
            "title": result.title,
            "abstract": result.summary,
            "authors": [author.name for author in result.authors],
            "categories": result.primary_category,
            "published": result.published.isoformat(),
            "updated": result.updated.isoformat(),
        }
        all_papers.append(paper)

        print(f"Fetched: {result.title}")

    print(f"Fetched {len(all_papers)} papers. Saving to {output_file}...")

    # Save to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_papers, f, ensure_ascii=False, indent=2)

    print("Data fetch completed.")

# Run the scraper
if __name__ == "__main__":
    fetch_arxiv_data()
