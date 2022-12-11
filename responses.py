import random
import cthulhu


def handle_response_command(message) -> str:
    p_message = message.lower()
    if p_message == 'hello':
        return 'Hey, there!'

    if p_message == 'roll':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "`This is a help message that you can modify.`"


def handle_response_text(message) -> str:
    p_message = message.lower()
    cthulu_content = cthulhu.get_content(p_message)
    if not cthulu_content:
        cthulu_content = cthulhu.get_content(p_message.title())

    if cthulu_content:
        return cthulu_content


def handle_response_image(message) -> str:
    p_message = message.lower()
    cthulu_image = cthulhu.get_page_image(p_message)
    if not cthulu_image:
        cthulu_image = cthulhu.get_page_image(p_message.title())
    if not cthulu_image:
        cthulu_image = cthulhu.get_image(p_message)
    if not cthulu_image:
        cthulu_image = cthulhu.get_image(p_message.title())

    if cthulu_image:
        return cthulu_image


