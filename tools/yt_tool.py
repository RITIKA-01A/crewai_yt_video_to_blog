# from crewai_tools import YoutubeChannelSearchTool

# ## Initialise the tool with a specific yt channel to handle the target search
# yt_tool=YoutubeChannelSearchTool(youtube_channel_handler='@krishnaik06')
from langchain.tools import tool

@tool
def youtube_channel_search(query: str) -> str:
    """Search Krishnaik's YouTube channel for videos about the query."""
    channel = "krishnaik06"
    search_query = query.replace(" ", "+")
    url = f"https://www.youtube.com/@{channel}/search?query={search_query}"
    return f"🔎 Found videos for '{query}': {url}"


