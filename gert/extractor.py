from pdf2image import convert_from_path
from PIL.Image import Image
from PIL.ImageDraw import Draw
from pypdf import PdfReader

__all__ = ["extract"]


def extract(file: str) -> dict[str, Image]:
    course_mapping = {}
    images = convert_from_path(file)

    is_first_page = True
    reader = PdfReader(file)
    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        # The first page has some extra info on top of it that we want to strip out first
        if is_first_page:

            left, _, right, bottom = list(images[i].getbbox())

            # 452 is the total width above the start of the text
            # 60 is the height that we want (on all other pages)
            images[i] = images[i].crop((left, 452 - 60, right, bottom))

            is_first_page = False

        thicken_boxes(images[i])

        # Find name of the course
        for line in text.split("\n"):
            if line.startswith(" "):
                course_mapping[line.strip()] = images[i]
                break

    return course_mapping


def thicken_boxes(image: Image):
    """Apply an extra border to the boxes because the PDF conversion destroys them"""
    line_width = 3

    left, top = 54, 274
    right, bottom = 776, 598

    draw = Draw(image, mode="RGB")
    draw.line((left, top, right, top), fill=(0, 0, 0), width=line_width)
    draw.line((left, top, left, bottom), fill=(0, 0, 0), width=line_width)
    draw.line((left, bottom, right, bottom), fill=(0, 0, 0), width=line_width)
    draw.line((right, top, right, bottom), fill=(0, 0, 0), width=line_width)

    # Second rectangle
    left += 822
    right += 822
    top -= 3
    bottom -= 2

    draw.line((left, top, right, top), fill=(0, 0, 0), width=line_width)
    draw.line((left, top, left, bottom), fill=(0, 0, 0), width=line_width)
    draw.line((left, bottom, right, bottom), fill=(0, 0, 0), width=line_width)
    draw.line((right, top, right, bottom), fill=(0, 0, 0), width=line_width)
