from youtube_transcript_api import YouTubeTranscriptApi
import re


def extract_video_id(url: str):
    patterns = [
        r"(?:v=)([A-Za-z0-9_-]{11})",
        r"youtu\.be/([A-Za-z0-9_-]{11})",
        r"shorts/([A-Za-z0-9_-]{11})",
    ]

    for pattern in patterns:
        match = re.search(pattern, url)

        if match:
            return match.group(1)

    return None


def get_transcript(video_id):

    try:
        api = YouTubeTranscriptApi()

        transcript = api.fetch(video_id)

        return " ".join(
            item.text
            for item in transcript
        )

    except Exception as e:

        print(f"Transcript Error: {e}")

        return None
