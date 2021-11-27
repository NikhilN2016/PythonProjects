ufo = codesters.Sprite("ufo", 0, 0)
ufo.set_size(0.3)
speed = 50
ufo.set_color("black")
ufo.pen_down()
def right_key():
    ufo.move_right(speed)
stage.event_key("right", right_key)
def left_key():
    ufo.move_left(speed)
stage.event_key("left", left_key)
def up_key():
    ufo.move_up(speed)
stage.event_key("up", up_key)
def down_key():
    ufo.move_down(speed)
stage.event_key("down", down_key)
def w_key():
    ufo.move_up(speed)
stage.event_key("w", w_key)
def a_key():
    ufo.move_left(speed)
stage.event_key("a", a_key)
def s_key():
    ufo.move_down(speed)
stage.event_key("s", s_key)
def d_key():
    ufo.move_right(speed)
stage.event_key("d", d_key)
def e_key():
    ufo.pen_down()
stage.event_key("e", e_key)
def r_key():
    ufo.pen_up()
stage.event_key("r", r_key)
def click(ufo):
    colour = ufo.ask("Enter a colour")
    ufo.set_color(colour)
ufo.event_click(click)
def z_key():
    x = int(ufo.ask("Enter an integer (X)"))
    y = int(ufo.ask("Enter an integer (Y)"))
    ufo.glide_to(x, y)
stage.event_key("z", z_key)



