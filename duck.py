import pygame

class Duck(pygame.sprite.Sprite):
    
    img_actual_width = 23
    img_actual_height = 24

    def __init__(self, pos, group):
        super().__init__(group)
        # general attributes
        self.image = pygame.Surface((self.img_actual_width * 5, self.img_actual_height * 5))
        self.rect = self.image.get_rect(center = pos)
        
        # movement attributes
        self.direction = pygame.math.Vector2()
        self.position = pygame.math.Vector2(self.rect.center)
        self.velocity = 150
        
        #animation attributes
        self.import_animations()
        self.action = 'idle'
        self.index = 0
        
    def import_animations(self):
        self.animations = {'up': [], 'down': [], 'left': [], 'right': [], "idle": []}
        
        self.animations['up'].append(pygame.image.load('data/gfx/waddle_up_0.png'))
        self.animations['up'].append(pygame.image.load('data/gfx/waddle_up_1.png'))
        
        self.animations['down'].append(pygame.image.load('data/gfx/waddle_down_0.png'))
        self.animations['down'].append(pygame.image.load('data/gfx/waddle_down_1.png'))
        
        self.animations['left'].append(pygame.image.load('data/gfx/waddle_left_0.png'))
        self.animations['left'].append(pygame.image.load('data/gfx/waddle_left_1.png'))
        
        self.animations['right'].append(pygame.image.load('data/gfx/waddle_right_0.png'))
        self.animations['right'].append(pygame.image.load('data/gfx/waddle_right_1.png'))
        
        self.animations['idle'].append(pygame.image.load('data/gfx/waddle_idle_0.png'))
        self.animations['idle'].append(pygame.image.load('data/gfx/waddle_idle_1.png'))
        
    def animate(self, dt):
        self.index +=2 * dt
        if self.index >= len(self.animations[self.action]):
            self.index = 0
        self.image = self.animations[self.action][int(self.index)]
        
        self.width = self.image.get_width()*5
        self.height = self.image.get_height()*5
        self.image = pygame.transform.scale(self.image, (self.width, self.height))
            
    def duck_direction(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.action = 'right'
            if self.rect.right >= 700:
                self.direction.x = 0 
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.action = 'left'
            if self.rect.left <= 0:
                self.direction.x = 0 
        else:
            self.direction.x = 0
            self.action = 'idle'
        
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.action = 'up'
            if self.rect.top <= 0:
                self.direction.y = 0 
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.action = 'down'
            if self.rect.bottom >= 450:
                self.direction.y = 0 
        else:
            self.direction.y = 0
            
    def duck_move(self, dt):
        #normal vector - normalize speed in every direction
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.position += self.direction * self.velocity * dt
        self.rect.center = self.position

    def update(self, dt):
        self.duck_direction()
        self.duck_move(dt)
        self.animate(dt)
    
    def check_pick_up(self, x, y):
        return self.rect.collidepoint(x, y)
        