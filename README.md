### 🧠 YouTube Blog Generator with CrewAI
- This project uses CrewAI to automate the process of researching YouTube videos and generating blog content based on them. It simulates a multi-agent workflow with specialized agents for research and content writing.

## 🚀 Overview

- Research Task 
Conducts in-depth research on a given YouTube topic by analyzing related video content from a specific channel.
Output: A 3-paragraph detailed report about the video content.\
---

- Write Task 
Summarizes the researched content and turns it into a well-written blog post.
Output: A blog post saved as new-blog-post.md.
---

## 🛠️ Agents & Tools
- Agents:

- blog_researcher: Gathers detailed video insights.

- blog_writer: Creates structured blog content.

- Tool Used:

 - yt_tool: A custom YouTube tool to fetch video and channel information
