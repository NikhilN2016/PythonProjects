stage.set_background("volcano")
ufo = codesters.Sprite("ufo")
ufo.set_size(0.4)
meteor1 = codesters.Sprite("meteor2", -230, 230)
meteor1.set_size(0.5)
meteor2 = codesters.Sprite("meteor2", 230, -230)
meteor2.set_size(0.5)
timer = 30
timer_display = codesters.Display(timer)
def mouse_move():
    x = stage.mouse_x()
    y = stage.mouse_y()
    ufo.set_position(x, y)
stage.event_mouse_move(mouse_move)
stage.wait(2)
meteor1.set_x_speed(3)
meteor1.set_y_speed(5)
meteor2.set_x_speed(2)
meteor2.set_y_speed(5)
def interval():
    global timer
    timer -= 1
    timer_display.update(timer)
    if timer == 0:
        win_text = codesters.Text("YOU WON THE GAME", 0, 0, "green")
stage.event_interval(interval, 1)
def collision(sprite, hit_sprite):
    sprite.go_to(0,0)
    sprite.turn_left(360)
    y = random.choice([-230,230])
    x = random.choice([-230,230])
    hit_sprite.go_to(x,y)
    hit_sprite.set_x_speed(random.randint(2,5))
    hit_sprite.set_y_speed(random.randint(2,5))
    global timer
    timer = 30
ufo.event_collision(collision)


