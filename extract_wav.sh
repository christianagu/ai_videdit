#!/bin/bash
count=0
directory="C:/Users/xuts/Desktop/dev/ai_videdit/data"
output_dir="C:/Users/xuts/Desktop/dev/ai_videdit/audio_wav"

for wav in "$directory"/*; do
    output="output${count}"
    echo "Processing: $wav"
    echo "ffmpeg -i \"$wav\" -vn \"$output_dir/${output}.wav\""
    # Uncomment the next line to actually run ffmpeg
    ffmpeg -i "$wav" -vn "$output_dir/${output}.wav"
    ((count++))
done