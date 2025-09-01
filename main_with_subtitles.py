from Components.YoutubeDownloader import download_youtube_video
from Components.Edit import extractAudio, crop_video
from Components.Transcription import transcribeAudio
from Components.LanguageTasks import GetHighlight
from Components.FaceCrop import crop_to_vertical, combine_videos
from Components.Subtitles import add_subtitles_to_video

def main():
    print("🎬 AI YouTube Shorts Generator with Subtitles")
    print("=" * 50)
    
    url = input("Enter YouTube video URL: ")
    add_subs = input("Add subtitles to the final video? (y/n): ").lower().strip() == 'y'
    
    Vid = download_youtube_video(url)
    if Vid:
        Vid = Vid.replace(".webm", ".mp4")
        print(f"✅ Downloaded video successfully! at {Vid}")

        Audio = extractAudio(Vid)
        if Audio:
            print("🎵 Audio extracted successfully!")

            transcriptions = transcribeAudio(Audio)
            if len(transcriptions) > 0:
                print(f"📝 Transcription completed! Found {len(transcriptions)} segments")
                
                TransText = ""
                for text, start, end in transcriptions:
                    TransText += (f"{start} - {end}: {text}")

                start, stop = GetHighlight(TransText)
                if start != 0 and stop != 0:
                    print(f"🎯 Highlight identified: {start}s to {stop}s ({stop-start}s duration)")

                    Output = "Out.mp4"
                    crop_video(Vid, Output, start, stop)
                    print("✂️ Video cropped to highlight segment!")
                    
                    # Try vertical cropping (this might fail due to the known bug)
                    try:
                        croped = "croped.mp4"
                        crop_to_vertical("Out.mp4", croped)
                        combine_videos("Out.mp4", croped, "Final.mp4")
                        final_video = "Final.mp4"
                        print("📱 Vertical cropping completed!")
                    except Exception as e:
                        print(f"⚠️ Vertical cropping failed: {e}")
                        print("📹 Using horizontally cropped video instead")
                        final_video = "Out.mp4"
                    
                    # Add subtitles if requested
                    if add_subs:
                        print("💬 Adding subtitles...")
                        subtitle_output = final_video.replace('.mp4', '_with_subtitles.mp4')
                        
                        success = add_subtitles_to_video(
                            video_path=final_video,
                            transcriptions=transcriptions,
                            highlight_start=start,
                            highlight_end=stop,
                            output_path=subtitle_output,
                            method="ffmpeg"  # Use FFmpeg for better quality
                        )
                        
                        if success:
                            print(f"✅ Video with subtitles created: {subtitle_output}")
                            
                            # Also create a version with better audio compatibility
                            import subprocess
                            fixed_subtitle_output = subtitle_output.replace('.mp4', '_fixed.mp4')
                            cmd = [
                                'ffmpeg', '-i', subtitle_output, 
                                '-vcodec', 'libx264', '-acodec', 'aac', 
                                '-b:a', '128k', '-y', fixed_subtitle_output
                            ]
                            try:
                                subprocess.run(cmd, check=True, capture_output=True)
                                print(f"🔧 Audio-optimized version: {fixed_subtitle_output}")
                            except:
                                print("⚠️ Could not create audio-optimized version")
                        else:
                            print("❌ Failed to add subtitles")
                    
                    # Summary
                    print("\n" + "=" * 50)
                    print("🎉 PROCESSING COMPLETE!")
                    print("=" * 50)
                    print("Generated files:")
                    print(f"📁 Original video: {Vid}")
                    print(f"🎬 Highlight video: {final_video}")
                    if add_subs:
                        if success:
                            print(f"💬 With subtitles: {subtitle_output}")
                            if 'fixed_subtitle_output' in locals():
                                print(f"🔧 Audio-optimized: {fixed_subtitle_output}")
                    
                    print(f"\n🎯 Highlight timing: {start}s - {stop}s")
                    print(f"⏱️ Duration: {stop-start} seconds")
                    print("\n💡 To view your videos, run: open .")
                    
                else:
                    print("❌ Error in getting highlight")
            else:
                print("❌ No transcriptions found")
        else:
            print("❌ No audio file found")
    else:
        print("❌ Unable to Download the video")

if __name__ == "__main__":
    main()
