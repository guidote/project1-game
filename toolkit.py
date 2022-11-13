def mouse_over_rect(rect, mouse):
    if rect.collidepoint(mouse):
        return True
    else:
        return False

