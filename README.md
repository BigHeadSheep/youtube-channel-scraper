# YouTube Channel Scraper

A simple Python tool for scraping video metadata from a YouTube channel and exporting the results to Excel.

The project uses `yt-dlp` to collect publicly available video information and `pandas` / `openpyxl` to create a formatted Excel workbook.

## Features

- Scrape videos from a YouTube channel
- Collect:
  - Upload date
  - Video title
  - Video description
  - Video URL
- Export results to Excel
- Sort videos from newest to oldest
- Freeze the Excel header row
- Add filters
- Wrap long text
- Create clickable YouTube links

## Project Structure

```text
youtube-channel-scraper/
│
├── data/
│   └── youtube_videos.xlsx
│
├── src/
│   ├── __init__.py
│   ├── scraper.py
│   └── export_excel.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Requirements

- Python 3.12+
- Deno
- Python packages listed in `requirements.txt`

The scraper uses Deno as a JavaScript runtime for YouTube extraction through `yt-dlp`.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/youtube-channel-scraper.git
cd youtube-channel-scraper
```

Create and activate a virtual environment.

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Install Deno

On Windows PowerShell:

```powershell
irm https://deno.land/install.ps1 | iex
```

Check that Deno is installed:

```bash
deno --version
```

## Usage

Open `main.py` and set the YouTube channel URL:

```python
CHANNEL_URL = "https://www.youtube.com/@MissPhonics/videos"
```

Set the output file if required:

```python
OUTPUT_FILE = "data/youtube_videos.xlsx"
```

Run the scraper:

```bash
python main.py
```

The program will scan the videos in the channel and display progress in the terminal:

```text
Found 261 videos.

[1/261] Reading: Video title...
[2/261] Reading: Video title...
[3/261] Reading: Video title...
```

When finished, the Excel file will be saved in:

```text
data/youtube_videos.xlsx
```

## Excel Output

The exported workbook contains four columns:

| Column | Description |
|---|---|
| `upload_date` | Date the video was uploaded |
| `title` | Video title |
| `description` | Description written below the video |
| `video_url` | Direct YouTube video link |

The output is sorted from newest to oldest.

## Notes

This project currently scrapes videos from the channel's `/videos` tab.

YouTube Shorts, livestreams, and other channel content may be stored in separate tabs and are not currently included.

The project does not download video files. It only retrieves publicly available video metadata.

You may occasionally see warnings from `yt-dlp` relating to `ffmpeg`. Since this project does not download video or audio, these warnings can generally be ignored.

## Possible Future Improvements

- Scrape multiple YouTube channels
- Scrape Shorts
- Scrape playlists
- Add video duration
- Add view count
- Add like count
- Add channel name
- Automatic content categorisation
- Keyword analysis
- Export multiple channels into separate Excel sheets

## Technologies

- Python
- yt-dlp
- pandas
- openpyxl
- Deno

## License

This project is intended for personal research and educational use.
