# convert_to_mp3
# Audio File Converter

A Python script that converts audio files from various formats (e.g., WAV, OGG, FLAC, AAC, MP4, M4A, WMA) to MP3 format using the `pydub` library.

## Features

- Supports converting individual audio files.
- Supports batch conversion of all supported audio files in a folder.
- Automatically creates the output folder if it does not exist.
- Error handling for invalid paths and unsupported formats.

## Requirements

Before running the script, ensure you have the following installed:

1. **Python 3.6+**
2. **Dependencies:**
   - `pydub`: Python library for audio file processing.
   - `ffmpeg` or `libav`: Required by `pydub` for audio processing.

### Installing Dependencies

To install the required Python package, run:

```bash
pip install pydub
```

Make sure `ffmpeg` or `libav` is installed and added to your system's PATH. For installation instructions, refer to the official [FFmpeg documentation](https://ffmpeg.org/).

## Usage

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/audio-file-converter.git
cd audio-file-converter
```

### 2. Run the Script

Use the following command to run the script:

```bash
python convert_to_mp3.py
```

### 3. Script Parameters

Update the `input_path` and `output_folder` variables in the script to match your use case:

- `input_path`: Path to the input file or folder containing audio files to convert.
- `output_folder`: Path to the folder where the converted MP3 files will be saved.

### Example:

#### Convert a Single File
Set `input_path` to the path of the file you want to convert:

```python
input_path = "path/to/audio/file.wav"
output_folder = "path/to/output/folder"
```

#### Convert All Files in a Folder
Set `input_path` to the folder containing the audio files:

```python
input_path = "path/to/input/folder"
output_folder = "path/to/output/folder"
```

## Script Explanation

The script performs the following steps:

1. Checks if the output folder exists and creates it if not.
2. Determines whether the input path is a file or a folder.
3. Collects all supported audio files for conversion.
4. Iterates through the audio files and converts each to MP3 format using `pydub`.
5. Saves the converted MP3 files to the specified output folder.

## Error Handling

- If an invalid input path is provided, the script will display an error message and terminate.
- If any file fails to convert, the script will log the error and proceed with the next file.

## Supported Formats

The script supports the following input formats:
- WAV
- OGG
- FLAC
- AAC
- MP4
- M4A
- WMA
- MP3

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvement, please create an issue or submit a pull request.

## GNU License
This project is licensed under GNU license.See the [`LICENSE`](LICENSE) file for details.

## Acknowledgments

- [pydub](https://github.com/jiaaro/pydub) - Python library for audio file manipulation.
- [FFmpeg](https://ffmpeg.org/) - Tool for handling multimedia data.

