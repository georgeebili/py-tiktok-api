from moviepy.editor import VideoFileClip
import os

def get_video_details(video_path):
    try:
        video = VideoFileClip(video_path)
        
        # Get video duration in seconds
        duration = video.duration
        
        # Get frame rate (frames per second)
        frame_rate = video.fps
        
        # Get video resolution (width x height)
        resolution = video.size
        
        # Get number of frames in the video
        num_frames = int(video.fps * video.duration)
        
        # Calculate video size in bytes
        video_size = os.path.getsize(video_path)
        
        # Print the video details
        print(f"Video Duration: {duration} seconds")
        print(f"Frame Rate: {frame_rate} FPS")
        print(f"Resolution: {resolution[0]}x{resolution[1]}")
        print(f"Number of Frames: {num_frames}")
        print(f"Video Size: {video_size} bytes")
        
        video.close()
    except Exception as e:
        print(f"Error: {str(e)}")

# Replace with the path to your video file
video_file_path = 'C:/Users/george/Downloads/part1.mp4'

# Call the function to get video details
get_video_details(video_file_path)
