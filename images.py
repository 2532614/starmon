import pygame

def image(image_nom:str) -> None:
    screen_width = 1296
    screen_height = 936
    screen = pygame.display.set_mode((screen_width, screen_height))

    #déterminer les coordonnés du menu 
    x_images = 648
    y_images = 468

    #déterminé les pdf et les dimentions
    images_image = pygame.image.load(f"{image_nom}.png").convert_alpha()
    images_image = pygame.transform.scale(images_image,(1296,936))
    images_rect = images_image.get_rect()
    screen.fill((255, 255, 255)) 

    #centrer les images
    images_rect.center = (x_images, y_images)
    #montrer le menu
    screen.blit(images_image, images_rect)


    #mettre à jour la tab
    pygame.display.update()

    #attendre que le menu soit fermé
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.quit()