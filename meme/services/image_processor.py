import cv2
import os

def overlay_caption(image_path, caption):
    image = cv2.imread(image_path)
    h, w, _ = image.shape

    cv2.putText(
        image,
        caption,
        (30, h - 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, 
        (255, 255, 255),
        2,
        cv2.LINE_AA
    )

    output_path = f"media/memes/{os.path.basename(image_path)}"
    cv2.imwrite(output_path, image)

    return output_path