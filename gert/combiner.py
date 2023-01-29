from PIL.Image import Image

__all__ = ["combine"]


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


def combine(previous: Image, current: Image) -> Image:
    """Combine the distributions of two years"""
    result = previous.copy()
    current_cropped = get_info_and_graph(current)
    result.paste(current_cropped, (0, 150 + 450 + 50))

    # Cut off extra whitespace at the bottom
    left, top, right, bottom = result.getbbox()
    return result.crop((left, top, right, 1135))
