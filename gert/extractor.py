from pdf2image import convert_from_path
from PIL.Image import Image
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

        # Find name of the course
        for line in text.split("\n"):
            if line.startswith(" "):
                course_mapping[line] = images[i]
                break

    return course_mapping


def get_info_and_graph(image: Image) -> Image:
    """Crop out the course info on top of the page
    We only want to display this info once
    """
    space_top = 150
    total_height = 450
    left, top, right, bottom = image.getbbox()
    top = space_top
    bottom = space_top + total_height
    return image.crop((left, top, right, bottom))
