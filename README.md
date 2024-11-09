Oraib: Arabic Text Enhancement Tool

Overview

Oraib is an Arabic multimodal LLM-based tool that assists with text correction, enhancement, and generation. It detects spelling, grammar, and stylistic errors in Arabic text and provides suggestions for improvement. Oraib also offers advanced features like diacritization and image captioning for Arabic content.

Features

Text Correction: Detects and corrects spelling and grammatical mistakes.
Stylistic Improvement: Suggests better phrasing and structure.
Arabic Diacritization: Automatically adds diacritics to text.
Image Captioning: Generates captions for Arabic images.
Installation

1. Clone the repository:
git clone https://github.com/Hebah-Soleman/Oraib.git
cd Oraib
2. Install dependencies:
pip install -r requirements.txt
3. Set up the environment:
Make sure you have the necessary environment variables configured for API access, if applicable.

Usage

1. Running the text correction tool:
```
from oraib import correct_text
result = correct_text("النص العربي هنا")
print(result)
```
2. Running the diacritization tool:
```
from oraib import diacritize_text
result = diacritize_text("النص بدون تشكيل")
print(result)
```
3. Using image captioning:
```
from oraib import generate_caption
caption = generate_caption("image_path_here")
print(caption)
```
Contributing

Feel free to fork this repository and submit pull requests for bug fixes and enhancements.

License

This project is licensed under the MIT License - see the LICENSE file for details.
