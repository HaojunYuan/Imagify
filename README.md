# Imagify

Imagify is a versatile machine learning application powered by Gradio and ComfyUI. With Imagify, you can generate images from text prompts or modify existing images based on your inputs

## Setup Instructions

### 1. Install [ComfyUI](https://github.com/comfyanonymous/ComfyUI.git)

### 2. Create a Python Virtual Environment

It's recommended to use a Python virtual environment to manage dependencies for Imagify. Here's how to create a virtual environment using `venv`:

```bash
# Create a new directory for your project (optional)
mkdir imagify
cd imagify

# Create a virtual environment named 'venv'
python3 -m venv venv

# Activate the virtual environment
# For Windows:
venv\Scripts\activate
# For macOS/Linux:
source venv/bin/activate
```

### 3. Install Requirements

Once your virtual environment is activated, you need to install the required Python packages for Imagify. These packages are specified in the `requirements.txt` file.

```bash
# Install the required packages
pip install -r requirements.txt
```

### 4. Customize Paths (Optional)

Open the `app.py` file and customize the following paths according to your system:

- `URL`: Update this with the appropriate endpoint for your application.
- `OUTPUT_DIR`: Set this to the directory where your output images will be saved.
- Update the path for saving input images (`resized_image.save('/path/to/input_image.jpg')`) if necessary.

### 5. Launch Imagify

With the setup complete, you're ready to launch Imagify:

```bash
python app.py
```

## Usage

- **Text-to-Image**: Enter a text prompt describing the image you want to generate and click submit.
- **Image-to-Image**: Upload an image, optionally provide additional parameters, and click submit to process the image.

## License

Imagify is released under the [MIT License](LICENSE).
