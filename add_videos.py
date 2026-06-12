import re

file_path = r'src\pages\Services\categoryData.js'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Array of awesome, stable, free looping video URLs from Mixkit
mixkit_videos = [
    # Abstract fluid/smoke
    "https://assets.mixkit.co/videos/preview/mixkit-blue-and-pink-abstract-smoke-in-the-dark-2292-large.mp4",
    # Coding/Developer
    "https://assets.mixkit.co/videos/preview/mixkit-software-developer-working-on-code-1748-large.mp4",
    # Abstract Data lines / Cyber
    "https://assets.mixkit.co/videos/preview/mixkit-digital-animation-of-a-globe-loop-32906-large.mp4",
    # Tech/Server room
    "https://assets.mixkit.co/videos/preview/mixkit-high-tech-server-room-animation-43891-large.mp4",
    # Binary Code Loop
    "https://assets.mixkit.co/videos/preview/mixkit-abstract-technology-loop-with-binary-code-32777-large.mp4",
    # Clean UI/UX motion graphics proxy
    "https://assets.mixkit.co/videos/preview/mixkit-futuristic-abstract-shapes-in-a-loop-32986-large.mp4"
]

# We need to inject these into every item inside the "extendedCapabilities" array.
# Let's write a targeted regex replace.

def replace_image_with_video(match):
    full_str = match.group(0)
    # the group contains everything up to "image": "..."
    # We will just append the video field right after it.
    
    # We need to cycle through the 6 videos per category.
    # We can do this safely by tracking how many replacements we've made.
    global vid_index
    vid = mixkit_videos[vid_index % 6]
    vid_index += 1
    
    # Check if 'video' is already there to avoid duplicates
    if '"video":' in full_str:
        return full_str
        
    return full_str + f',\n        "video": "{vid}"'

vid_index = 0
# Pattern matches "image": "..." exactly.
new_content = re.sub(r'("image":\s*"[^"]+")', replace_image_with_video, content)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Injected looping background videos!")
