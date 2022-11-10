
def check_pick_up(Duck, b_x, b_y, b_width, b_height):
    top = Duck.position.y + Duck.height/4
    bottom = Duck.position.y - Duck.height/4
    left = Duck.position.x - Duck.width/4
    right = Duck.position.x + Duck.width/4
    
    if (b_x >= left and b_x <= right):
        if (b_y <= top and b_y >= bottom):
            return True
    return False


def check_duck_position(previous_position_x, previous_position_y, position_x, position_y):
    if (position_x > previous_position_x and (position_x - previous_position_x)>10):
        return "right"
    elif (position_x < previous_position_x  and (previous_position_x - position_x)>10):
        return "left"
    elif (position_y > previous_position_y and (position_y - previous_position_y)>10):
        return "front"
    elif (position_y < previous_position_y and (previous_position_y - position_y)>10):
        return "back"   
    else:
        return "front" # TODO : idle
    
def mouse_over_rect(rect, mouse):
    if rect.collidepoint(mouse):
        return True
    else:
        return False

