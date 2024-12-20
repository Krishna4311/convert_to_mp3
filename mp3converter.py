import os
from pydub import AudioSegment


def convert_to_mp3(input_path, output_folder):

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Check if input is a file or folder
    if os.path.isfile(input_path):
        files_to_convert = [input_path]
    elif os.path.isdir(input_path):
        files_to_convert = [
            os.path.join(input_path, file)
            for file in os.listdir(input_path)
            if file.endswith(('.wav', '.ogg', '.flac', '.aac', '.mp4', '.m4a', '.wma', '.mp3'))
        ]
    else:
        print("Invalid input path.")
        return
    
    for file_path in files_to_convert:
        try:
            # Extract file name without extension
            file_name = os.path.splitext(os.path.basename(file_path))[0]
            output_path = os.path.join(output_folder, f"{file_name}.mp3")
            
            # Load the audio file
            audio = AudioSegment.from_file(file_path)
            
            # Export to MP3
            audio.export(output_path, format="mp3")
            print(f"Converted: {file_path} -> {output_path}")
        except Exception as e:
            print(f"Error converting {file_path}: {e}")


input_path = "input file/folder"  # Path to a file or folder
output_folder = "outputfolder"  # Folder to save MP3 files
convert_to_mp3(input_path, output_folder)
