import json
import os
import time

import gradio as gr
import numpy as np
import requests

from PIL import Image

# Replace the URL with the appropriate endpoint for your application
URL = 'http://127.0.0.1:8188/prompt'

# Replace OUTPUT_DIR with the directory where your output images will be saved
OUTPUT_DIR = '/Users/brianyuan/Developer/ML/ComfyUI/output'

def get_latest_image(folder):
    files = os.listdir(folder)
    image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    image_files.sort(key=lambda x: os.path.getmtime(os.path.join(folder, x)))
    latest_image = os.path.join(folder, image_files[-1]) if image_files else None
    return latest_image

def start_queue(prompt_workflow):
    p = {'prompt': prompt_workflow}
    data = json.dumps(p).encode('utf-8')
    requests.post(URL, data=data)

def generate_image(prompt_text, steps=None, input_image=None):
    # Replace 'text_workflow_api.json' and 'image_workflow_api.json' with the appropriate paths for your workflow files
    if input_image is None:
        workflow_file = "text_workflow_api.json"
    else:
        workflow_file = "image_workflow_api.json"
    
    print(workflow_file)

    with open(workflow_file, "r") as file_json:
        prompt = json.load(file_json)
        prompt['6']['inputs']['text'] = f'AI image of a {prompt_text}'
        if steps:
            prompt['3']['inputs']['steps'] = steps

    if input_image is not None:
        image = Image.fromarray(input_image)
        min_side = min(image.size)
        scale_factor = 512 / min_side
        new_size = (round(image.size[0] * scale_factor), round(image.size[1] * scale_factor))
        resized_image = image.resize(new_size)

        # Replace the path below with the directory where your input images will be saved
        resized_image.save('/Users/brianyuan/Developer/ML/ComfyUI/input/input_image.jpg')

    previous_image = get_latest_image(OUTPUT_DIR)

    start_queue(prompt)

    while True:
        latest_image = get_latest_image(OUTPUT_DIR)
        if latest_image != previous_image:
            return latest_image
        
        time.sleep(1)

demo = gr.Interface(fn=generate_image, inputs=['text', 'text', 'image'], outputs=['image'])

demo.launch(share=True)