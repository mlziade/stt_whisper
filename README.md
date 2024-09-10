# STT Tool

## Author

<div id="badges">
  <a href="https://www.linkedin.com/in/mlziade/">
    <img src="https://img.shields.io/badge/LinkedIn-blue?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Badge"/>
  </a>
  <a href="https://github.com/mlziade">
    <img src="https://img.shields.io/badge/Github-black?style=for-the-badge&logo=github&logoColor=white" alt="Youtube Badge"/>
  </a>
</div>

## About

A Free STT Tool using [OpenAi Whisper](https://github.com/openai/whisper) that recives .mp4 files and extracts it audio content as .txt files with timestamps.

## Installation Process

### Python

Installation Link [here](https://www.python.org/downloads/)

### Pip

Open CMD and paste

````
python -m ensurepip --upgrade
````

Chololatey

Follow instructions [here](https://chocolatey.org/install)

### Pytorch

Installation Link [here](https://pytorch.org/get-started/locally/)

Choose:

- PyTorch Build : **Stable**
- Your OS : **Windows**
- Package : **Pip**
- Language : **Python**
- Compute Platform: **CUDA 11.8** or **CPU**

And run command, for example:

````
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
````

### ffmpeg

On an CMD window with Administrative Permissions:

````
choco install ffmpeg
````

### Requirements

On an CMD window on the root folder

````
pip install -r requirements.txt
````

