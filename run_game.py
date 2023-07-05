import pygame
import sys
import modules.settings as m_set
import modules.rect as m_rect
import modules.data_base as m_data

pygame.init()
screen = pygame.display.set_mode((m_set.set.SCREEN_WIDTH, m_set.set.SCREEN_HEIGHT))
pygame.display.set_caption('CROSS/ZERO')

font = pygame.font.SysFont(None, size = 220, bold = True)
cross = font.render("X", 0, (255, 0, 0), (75, 70, 240))

font1 = pygame.font.SysFont(None, size = 220, bold = True)
zero = font1.render("O", 0, (0, 0, 255), (75, 70, 240))

BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
BUTTON_X = 0
BUTTON_Y = -100
BUTTON_RADIUS = 16
win = 0

mous_button = pygame.mouse.get_pressed()

game = True
mouse_pos = pygame.mouse.get_pressed()
reset_button = pygame.Rect(300, -500, 100, 50)
mous_button = pygame.mouse.get_pressed()



def run_game():
    global zero
    global cross
    while game:
        win = 0
        screen.fill(m_set.set.SCREEN_COLOR)
        m_rect.square.draw_square(screem_game = screen)
        mouse_pos = pygame.mouse.get_pos()
        if win == 0:
            if m_data.list_cell[0] == 1 and win == 0:
                screen.blit(zero, (60, 50))
        
            if m_data.list_cell[1] == 1 and win == 0:
                screen.blit(zero, (250, 50))
            
            if m_data.list_cell[2] == 1 and win == 0:
                screen.blit(zero, (420, 50))
            
            if m_data.list_cell[3] == 1 and win == 0:
                screen.blit(zero, (50, 225))
            
            if m_data.list_cell[4] == 1 and win == 0:
                screen.blit(zero, (250, 225))
            
            if m_data.list_cell[5] == 1 and win == 0:
                screen.blit(zero, (420, 225))
            
            if m_data.list_cell[6] == 1 and win == 0:
                screen.blit(zero, (50, 400))
            
            if m_data.list_cell[7] == 1 and win == 0:
                screen.blit(zero, (250, 400))
            
            if m_data.list_cell[8] == 1 and win == 0:
                screen.blit(zero, (420, 400))
            
            if m_data.list_cell[0] == 2 and win == 0:
                screen.blit(cross, (50, 50))
            
            if m_data.list_cell[1] == 2 and win == 0:
                screen.blit(cross, (250, 50))
            
            if m_data.list_cell[2] == 2 and win == 0:
                screen.blit(cross, (420, 50))
            
            if m_data.list_cell[3] == 2 and win == 0:
                screen.blit(cross, (50, 225))
            
            if m_data.list_cell[4] == 2 and win == 0:
                screen.blit(cross, (250, 225))
            
            if m_data.list_cell[5] == 2 and win == 0:
                screen.blit(cross, (420, 225))
            
            if m_data.list_cell[6] == 2 and win == 0:
                screen.blit(cross, (50, 400))
            
            if m_data.list_cell[7] == 2 and win == 0:
                screen.blit(cross, (250, 400))
            
            if m_data.list_cell[8] == 2 and win == 0:
                screen.blit(cross, (420, 400))
        if m_data.list_cell[0] == 1  and m_data.list_cell[1] == 1 and m_data.list_cell[2] == 1 and win == 0:

            pygame.draw.line(screen, (255, 0, 0), (120, 120), (480, 120), width= 5)
            win += 1
        elif m_data.list_cell[0] == 2 and m_data.list_cell[1] == 2 and m_data.list_cell[2] == 2 and win == 0:
            print("Верхня горизонтальна перемога хрестиків")
            pygame.draw.line(screen, (255, 0, 0), (120, 120), (480, 120), width= 5)
            win += 1
        elif m_data.list_cell[3] == 1 and m_data.list_cell[4] == 1 and m_data.list_cell[5] == 1 and win == 0:
            print("Верхня горизонтальна перемога ноликів")
            pygame.draw.line(screen, (255, 0, 0), (125, 290), (485, 290), width= 5)
            win += 1
        elif m_data.list_cell[3] == 2 and m_data.list_cell[4] == 2 and m_data.list_cell[5] == 2 and win == 0:
            print("cередня горизонтальна перемога хрестиків")
            pygame.draw.line(screen, (255, 0, 0), (125, 290), (485, 290), width= 5)
            win += 1
        elif m_data.list_cell[6] == 1 and m_data.list_cell[7] == 1 and m_data.list_cell[8] == 1 and win == 0:
            print("нижня горизонтальна перемога ноликів")
            pygame.draw.line(screen,(255, 0, 0), (120, 475), (475, 475), width= 5)
            win += 1
        elif m_data.list_cell[6] == 2 and m_data.list_cell[7] == 2 and m_data.list_cell[8] == 2 and win == 0:
            print("Верхня горизонтальна перемога хрестиків")
            pygame.draw.line(screen,(255, 0, 0), (120, 475), (475, 475), width= 5)
            win += 1
            # Вертикальна перемога 
        if m_data.list_cell[0] == 1 and m_data.list_cell[3] == 1 and m_data.list_cell[6] == 1 and win == 0:
            print("Ліва вертикальна перемога ноликів")
            pygame.draw.line(screen,(255, 0, 0), (120, 120), (120, 485), width= 5)
            win += 1
        elif m_data.list_cell[0] == 2 and m_data.list_cell[3] == 2 and m_data.list_cell[6] == 2 and win == 0:
            pygame.draw.line(screen,(255, 0, 0), (110, 120), (110, 485), width= 5)
            win += 1
        if m_data.list_cell[1] == 1 and m_data.list_cell[4] == 1 and m_data.list_cell[7] == 1 and win == 0:
            print("2 стовп")
            pygame.draw.line(screen,(255, 0, 0), (310, 120), (310, 475), width= 5)
            win += 1
        elif m_data.list_cell[1] == 2 and m_data.list_cell[4] == 2 and m_data.list_cell[7] == 2 and win == 0:
            print("3 стовп")
            pygame.draw.line(screen,(255, 0, 0), (310, 120), (310, 475), width= 5)
            win += 1
        if m_data.list_cell[2] == 1 and m_data.list_cell[5] == 1 and m_data.list_cell[8] == 1 and win == 0:
            print("2 стовп")
            win += 1
            pygame.draw.line(screen,(255, 0, 0), (490, 120), (490, 475), width= 5)
        elif m_data.list_cell[2] == 2 and m_data.list_cell[5] == 2 and m_data.list_cell[8] == 2 and win == 0:
            print("2 стовп")
            win += 1
            pygame.draw.line(screen,(255, 0, 0), (480, 120), (480, 475), width= 5)
        # Діагональна перемога
        if m_data.list_cell[2] == 1 and m_data.list_cell[4] == 1 and m_data.list_cell[6] == 1 and win == 0:
            win += 1
            print("1 діагональ")
            pygame.draw.line(screen,(255, 0, 0), (120, 475), (475, 120), width= 5)

        elif m_data.list_cell[2] == 2 and m_data.list_cell[4] == 2 and m_data.list_cell[6] == 2 and win == 0:
            win += 1
            print("2 стовп")
            pygame.draw.line(screen,(255, 0, 0), (120, 475), (475, 120), width= 5)

        if m_data.list_cell[0] == 1 and m_data.list_cell[4] == 1 and m_data.list_cell[8] == 1 and win == 0:
            win += 1
            print("2 стовп")
            pygame.draw.line(screen,(255, 0, 0), (120, 120), (475, 475), width= 5)

        elif m_data.list_cell[0] == 2 and m_data.list_cell[4] == 2 and m_data.list_cell[8] == 2 and win == 0:
            print("2 стовп")
            win += 1
            pygame.draw.line(screen,(255, 0, 0), (120, 120), (475, 475), width= 5)
        for event in pygame.event.get():
           
            if event.type == pygame.QUIT:
                sys.exit()   
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and win == 0:
                if 200 > mouse_pos[0] > 50 and 200 > mouse_pos[1] > 50:
                    if m_data.choise[0] == 'cross' and m_data.list_cell[0] == 0:
                        m_data.list_cell[0] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero' and m_data.list_cell[0] == 0:
                        m_data.list_cell[0] = 2   
                        m_data.choise[0] = 'cross'
                elif 375 > mouse_pos[0] > 225 and 50 < mouse_pos[1] < 225:
                    if m_data.choise[0] == 'cross' and m_data.list_cell[1] == 0:
                        m_data.list_cell[1] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero' and m_data.list_cell[1] == 0:
                        m_data.list_cell[1] = 2   
                        m_data.choise[0] = 'cross'
                elif 550 > mouse_pos[0] > 400 and 50 < mouse_pos[1] < 200:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[2] == 0:
                        m_data.list_cell[2] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[2] == 0:
                        m_data.list_cell[2] = 2   
                        m_data.choise[0] = 'cross'   
                elif  200 > mouse_pos[0] > 50 and  225 < mouse_pos[1] < 375:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[3] == 0:
                        m_data.list_cell[3] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[3] == 0:
                        m_data.list_cell[3] = 2   
                        m_data.choise[0] = 'cross'      
                elif 200 < mouse_pos[0] < 375 and 370 > mouse_pos[1] > 225:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[4] == 0:
                        m_data.list_cell[4] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[4] == 0:
                        m_data.list_cell[4] = 2   
                        m_data.choise[0] = 'cross'
                elif 550 > mouse_pos[0] > 400 and 375 > mouse_pos[1] > 225:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[5] == 0:
                        m_data.list_cell[5] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[5] == 0:
                        m_data.list_cell[5] = 2   
                        m_data.choise[0] = 'cross'
                elif 200 > mouse_pos[0] > 50 and 550 > mouse_pos[1] > 400:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[6] == 0:
                        m_data.list_cell[6] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[6] == 0:
                        m_data.list_cell[6] = 2   
                        m_data.choise[0] = 'cross'
                elif 370 > mouse_pos[0] > 225 and 550 > mouse_pos[1] > 400:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[7] == 0:
                        m_data.list_cell[7] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[7] == 0:
                        m_data.list_cell[7] = 2   
                        m_data.choise[0] = 'cross'
                elif 550 > mouse_pos[0] > 400 and 550 > mouse_pos[1] > 400:
                    if m_data.choise[0] == 'cross'and m_data.list_cell[8] == 0:
                        m_data.list_cell[8] = 1   
                        m_data.choise[0] = 'zero'
                    elif m_data.choise[0] == 'zero'and m_data.list_cell[8] == 0:
                        m_data.list_cell[8] = 2   
                        m_data.choise[0] = 'cross'
                    
                print(win)
                print(m_data.list_cell)  
                print(m_data.choise)
                print(f"Mouse clicked at ({mouse_pos[0]}, {mouse_pos[1]})")
                # reset()
                # m_win.gorisontal_win()
                # m_win.vertical_win()
                # m_win.diaganol_win()
        pygame.display.update()          
        
        
             
        
        
