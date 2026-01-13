import cv2

def add_caption(image_path, caption):
    image = cv2.imread(image_path)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1
    thichness = 2
    color = (255, 255, 255)

    height, width, _ = image.shape
    position = (50, height - 50)

    cv2.putText(
        image,
        caption,
        position,
        font,
        font_scale,
        color,
        thichness,
        cv2.LINE_AA
    )

    output_path = "output_meme.jpg"
    cv2.imwrite(output_path, image)

    return output_path
