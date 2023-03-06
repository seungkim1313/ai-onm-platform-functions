import numpy as np
from pathlib import Path
import PIL.Image as pilimg

"""
It's a temp file for functions that I am not sure where to put.
"""

TaskNotFoundError = Exception(
    "Task that you provided is not valid."
)

InvalidParamError = Exception(
    "Parameters that you provided is invalid."
)

def dataloader_image(task, list_img_path, list_label_path):
    
    list_img = []
    list_label = []
    
    if task == "classification":
        if list_img_path == None or len(list_img_path) < 1: 
            raise InvalidParamError
        for img_path in list_img_path:
            if not img_path.exists():
                raise FileNotFoundError
            label = img_path.parent.name
            img = np.array(pilimg.open(img_path))
            list_img.append(img)
            list_label.append(label)
        return list_img, list_label
    elif task == "detection":
        pass
    elif task == "segmentation":
        pass
    else:
        raise TaskNotFoundError
    

if __name__ == "__main__":
    
    ## dataloader_image input test
    task = "classification"
    list_img_path = [
        Path("./sample_data/classification/paper/0a3UtNzl5Ll3sq8K.png"),
        Path("./sample_data/classification/paper/0cb6cVL8pkfi4wF6.png")
    ]
    list_label_path = []
    
    a, b = dataloader_image(task, list_img_path, list_label_path)
    print(len(a))
    print(b)

    
    
    