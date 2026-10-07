from yt_dlp import YoutubeDL


DENO_PATH = r"C:\Users\yangd\.deno\bin\deno.exe"


def scrape_channel(channel_url: str) -> list[dict]:
    ydl_opts = {
        "quiet": True,
        "extract_flat": True,
        "skip_download": True,
        "js_runtimes": {
            "deno": {
                "path": DENO_PATH
            }
        },
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(channel_url, download=False)

    entries = info.get("entries", [])
    videos = []

    print(f"Found {len(entries)} videos.")

    for i, entry in enumerate(entries, start=1):
        video_id = entry.get("id")

        if not video_id:
            continue

        video_url = f"https://www.youtube.com/watch?v={video_id}"

        print(f"[{i}/{len(entries)}] Reading: {entry.get('title')}")

        video_opts = {
            "quiet": True,
            "skip_download": True,
            "js_runtimes": {
                "deno": {
                    "path": DENO_PATH
                }
            },
        }

        try:
            with YoutubeDL(video_opts) as video_ydl:
                video_info = video_ydl.extract_info(
                    video_url,
                    download=False,
                )

            videos.append(
                {
                    "upload_date": video_info.get("upload_date"),
                    "title": video_info.get("title"),
                    "description": video_info.get("description"),
                    "video_url": video_info.get("webpage_url"),
                }
            )

        except Exception as e:
            print(f"Failed to read {video_url}: {e}")

    return videos