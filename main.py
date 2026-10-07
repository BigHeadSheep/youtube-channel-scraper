from src.scraper import scrape_channel
from src.export_excel import export_to_excel


CHANNEL_URL = "https://www.youtube.com/@MissPhonics/videos"

OUTPUT_FILE = "data/youtube_videos.xlsx"


def main():
    videos = scrape_channel(CHANNEL_URL)

    if not videos:
        print("No videos found.")
        return

    export_to_excel(
        videos,
        OUTPUT_FILE,
    )

    print(f"Done. Exported {len(videos)} videos.")


if __name__ == "__main__":
    main()