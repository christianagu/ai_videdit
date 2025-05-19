from diffusers import VideoToVideoPipeline

pipeline = VideoToVideoPipeline.from_pretrained("modelscope/video-diffusion")
video = pipeline("your_input_video.mp4")
video.save("stylized_output.mp4")
