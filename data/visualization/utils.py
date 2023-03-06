from pathlib import Path
import PIL.Image as pilimg

TaskNotFound = Exception(
    "Task that you provided is not valid."
)

def dataloader_image(task, list_img_path, list_label_path):
    if task == "classification":
        pass
    elif task == "detection":
        pass
    elif task == "segmentation":
        pass
    else:
        raise TaskNotFound
    

if __name__ == "__main__":
    pass