# AI Youtube Shorts Generator with Subtitles 🎬

AI Youtube Shorts Generator is an enhanced Python tool designed to generate engaging YouTube shorts from long-form videos. By leveraging the power of GPT-4 and Whisper, it extracts the most interesting highlights, detects speakers, crops the content vertically for shorts, and **now includes automatic subtitle generation**. This enhanced version includes bug fixes and new features.

If you wish to add shorts generation into your application, here is an api to create shorts from long form videos :- https://docs.vadoo.tv/docs/guide/create-ai-clips

### Youtube tutorial -> https://youtu.be/dKMueTMW1Nw

### Medium tutorial -> https://medium.com/@anilmatcha/ai-youtube-shorts-generator-in-python-a-complete-tutorial-c3df6523b362

![longshorts](https://github.com/user-attachments/assets/3f5d1abf-bf3b-475f-8abf-5e253003453a)

[Demo Input Video](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator/blob/main/videos/Blinken%20Admires%20'Friend%20Jai'%20As%20Indian%20EAM%20Gets%20Savage%20In%20Munich%3B%20'I'm%20Smart%20Enough...'%20%7C%20Watch.mp4)

[Demo Output Video](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator/blob/main/Final.mp4)

## Features

### Core Features
- **Video Download**: Given a YouTube URL, the tool downloads the video.
- **Transcription**: Uses Whisper to transcribe the video.
- **Highlight Extraction**: Utilizes OpenAI's GPT-4 to identify the most engaging parts of the video.
- **Speaker Detection**: Detects speakers in the video.
- **Vertical Cropping**: Crops the highlighted sections vertically, making them perfect for shorts.

### 🆕 Enhanced Features
- **🎬 Automatic Subtitles**: Generates professional subtitles synchronized to your highlight segments
- **🔧 Audio Compatibility**: Creates multiple output formats for maximum compatibility
- **📝 Improved OpenAI Integration**: Updated to work with latest OpenAI API (v1.0+)
- **⚡ Enhanced Error Handling**: Better error messages and fallback mechanisms
- **📋 Multiple Output Options**: Generate videos with or without subtitles

## Installation

### Prerequisites

- Python 3.7 or higher
- FFmpeg
- OpenCV

### Steps

1. Clone the repository:

   ```bash
   git clone https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator.git
   cd AI-Youtube-Shorts-Generator
   ```

2. Create a virtual environment

```bash
python3.10 -m venv venv
```

3. Activate a virtual environment:

```bash
source venv/bin/activate # On Windows: venv\Scripts\activate
```

4. Install the python dependencies:

```bash
pip install -r requirements.txt
```

---

1. Set up the environment variables.

Create a `.env` file in the project root directory and add your OpenAI API key:

```bash
OPENAI_API=your_openai_api_key_here
```

## Usage

### Basic Usage (Original)
1. Ensure your `.env` file is correctly set up with your OpenAI API key.
2. Run the main script and enter the desired YouTube URL when prompted:
   ```bash
   python main.py
   ```

### Enhanced Usage (With Subtitles) 🆕
1. Run the enhanced script for subtitle options:
   ```bash
   python main_with_subtitles.py
   ```
2. Choose whether to add subtitles when prompted
3. Get multiple output files:
   - Highlight video without subtitles
   - Video with professional subtitles (if selected)
   - Audio-optimized versions

### Add Subtitles to Existing Video
If you already processed a video and want to add subtitles:
```bash
python add_subtitles_to_existing.py
```

### Output Files
- `Out.mp4` - Main highlight video
- `Out_fixed.mp4` - Audio-compatible version
- `Out_with_subtitles.mp4` - Version with subtitles
- `videos/[original_name].mp4` - Full downloaded video

### Component Testing
Test individual components:
```bash
# Test video download
python Components/YoutubeDownloader.py

# Test transcription
python Components/Transcription.py

# Test subtitle generation
python Components/Subtitles.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Disclaimer

This is a v0.1 release and might have some bugs. Please report any issues on the [GitHub Repository](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator).

### Other useful Video AI Projects

[AI Influencer generator](https://github.com/SamurAIGPT/AI-Influencer-Generator)

[Text to Video AI](https://github.com/SamurAIGPT/Text-To-Video-AI)

[Faceless Video Generator](https://github.com/SamurAIGPT/Faceless-Video-Generator)

[AI B-roll generator](https://github.com/Anil-matcha/AI-B-roll)

[No-code AI Youtube Shorts Generator](https://www.vadoo.tv/clip-youtube-video)

[Sora AI Video Generator](https://www.vadoo.tv/sora-ai-video-generator)
