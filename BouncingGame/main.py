ufo1 = codesters.Sprite("ufo")
opponent = codesters.Sprite("ufo", 100, 200)
ball = codesters.Circle(100, 100, 100, "blue")
ball.set_size(0.3)
ufo1.set_size(0.4)
opponent.set_size(0.4)
def right_key():
    ufo1.move_right(20)
    
stage.event_key("right", right_key)
def left_key():
    ufo1.move_left(20)

stage.event_key("left", left_key)
def a_key():
    opponent.move_left(20)

stage.event_key("a", a_key)
def d_key():
    opponent.move_right(20)

stage.event_key("d", d_key)
def collision(sprite, hit_sprite):
    ufo1collides = hit_sprite.get_image_name() 
    if ufo1collides == "ufo":
        ufo1.say("I hit something!")
        stage.wait(2)
        ufo1.say("")
        
        
ufo1.event_collision(collision)
def collision(sprite, hit_sprite):
    opponentcollides  = hit_sprite.get_image_name()
    if opponentcollides == "ufo":
        opponent.say("HEY YOUR IN MY WAY!!!")
        stage.wait(2)
        opponent.say("")
        
opponent.event_collision(collision)
ball.move_down(70)
stage.set_bounce(.8)
def collision(sprite, hit_sprite):
    ballcollides = hit_sprite.get_image_name()
    if ballcollides == "ufo":
        ball.move_up(133)
ball.event_collision(collision)



