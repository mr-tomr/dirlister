import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def list_items(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed to access {url}")
            return []

        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a')

        items = []
        for link in links:
            href = link.get('href')
            if href and not href.startswith('?') and href not in ('../', '/'):
                full_url = urljoin(url, href)
                items.append((full_url, href.endswith('/')))

        return items
    except requests.RequestException as e:
        print(f"Error accessing {url}: {e}")
        return []

def enumerate_items(url, visited, depth=0):
    if url in visited:
        return

    visited.add(url)

    items = list_items(url)
    if not items:
        print(f"No listable directories or files found at {url}")
        return

    indent = "  " * depth
    for item_url, is_directory in items:
        print(f"{indent}{item_url}")
        if is_directory:
            enumerate_items(item_url, visited, depth + 1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python WebDirEnumerator.py <URL>")
        sys.exit(1)

    target_url = sys.argv[1]
    visited_urls = set()
    print(f"Enumerating directories and files from {target_url}")
    enumerate_items(target_url, visited_urls)
