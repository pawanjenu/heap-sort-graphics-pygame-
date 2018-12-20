# Pygame template - skeleton for a new pygame project
import pygame
import random
from os import path
from numpy import ones,vstack
from numpy.linalg import lstsq

WIDTH = 1000
HEIGHT = 1000
FPS = 60
img_dir = path.join(path.dirname(__file__), 'img')


# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
font_name = pygame.font.match_font('arial')
player_img = pygame.image.load(path.join(img_dir, "circle.png"))

# initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
screen.fill(WHITE)

def text(surf,text,size,x,y):
    font = pygame.font.Font(font_name,size)
    text_surf = font.render(text,True,BLUE)
    text_rect = text_surf.get_rect()
    text_rect.midtop = (x,y)
    surf.blit(text_surf,text_rect)


class Each_array(pygame.sprite.Sprite):
    def __init__(self,x,y,val,i,a,b):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.Font(font_name,23)
        self.image = font.render(str(val),True,BLUE)
        #self.image2 = font.render(str(val),True,BLUE)
        #self.image.fill(BLACK)

        self.rect = self.image.get_rect()
       
        self.rect.x = x
        self.rect.y = y
        self.speedx = 5
        self.val = val

        
    def change_clr(self):
        font = pygame.font.Font(font_name,23)
        self.image = font.render(str(self.val),True,RED)
        #pygame.draw.rect(screen,RED,(self.rect.centerx-15,self.rect.centery-15,30,30),2)

    def change_bk(self):
        font = pygame.font.Font(font_name,23)
        self.image = font.render(str(self.val),True,BLUE)

    def update(self):
        pygame.draw.rect(screen,BLACK,(self.rect.centerx-15,self.rect.centery-15,30,30),2)


        
class Each_circle(pygame.sprite.Sprite):
    def __init__(self,x,y,val,i,a,b):
        pygame.sprite.Sprite.__init__(self)
        font = pygame.font.Font(font_name,23)
        self.image = font.render(str(val),True,BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = a
        self.rect.y = b
        self.val = val


    def change_clr(self):
        #font = pygame.font.Font(font_name,23)
        #self.image = font.render(str(self.val),True,RED)
        pygame.draw.circle(screen,RED,[self.rect.x+7,self.rect.y+12],20,8)

    def change_place(self,i):
        self.rect.x = 50+i*50
        self.rect.y = 500

        
    def change_bk(self):
        font = pygame.font.Font(font_name,23)
        self.image = font.render(str(self.val),True,BLACK)
        
    def update(self):   
        pygame.draw.circle(screen,BLUE,[self.rect.x+7,self.rect.y+12],20,2)


class Each_line(pygame.sprite.Sprite):
    def __init__(self,x,y,a,b):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((0,0))
        self.rect = self.image.get_rect()
        self.x1 = x
        self.y1 = y
        self.a1 = a
        self.b1 = b



    def update(self):
        pygame.draw.aaline(screen,BLACK,(self.x1,self.y1),(self.a1,self.b1))
        #pygame.draw.lines(screen,BLACK,False,[(self.x1,self.y1),(self.a1,self.b1)],1)



def show_array(i):
    pygame.draw.rect(screen,BLACK,(50+i*30+30,30,30,30),2)

def drawcircle(x,y,color):
    pygame.draw.circle(screen,color,[x,y],20,2)
      

all_sprites = pygame.sprite.Group()
circles = pygame.sprite.Group()
texts = pygame.sprite.Group()

x = 0
y = 0

def coordinates(n):
    B = []
    x = 450
    a = x
    b = x
    k = 1
    y = 1
    for i in range(n):
        for j in range(k):
            B.append(a)
            B.append(b)
            x = int(B[0]/(k*2))
            a = B[y-1]
            b = a+x
            a = a-x
            y = y+1
        k = k*2
        if B[1]==B[0]:     #Pop only 2nd element...
            B.pop(1)
            
            
    R = []
    a = 50
    k = 1
    for i in range(n):
        for j in range(k):
            R.append(a)
        a += 150	
        k = k*2
        
    A = []
    for i in range(n):
        A.append([])
        A[i].append(B[i])
        A[i].append(R[i])
        
    return A


A = coordinates(8)



'''m = []
p = []
index = 0
for i in range(8):
    m.append(Each_array(50+i*40+30,20,i,i,A[i][0],A[i][1]))
    p.append( Each_circle(50+i*40+30,20,i,i,A[i][0],A[i][1]))
    #show_array(i)
    index+=1
    all_sprites.add(m[i])
    texts.add(m[i])
    
    
    all_sprites.add(p[i])'''


def swap_array(a,b):
    if_swap=True
    #a.change_box()
    #b.change_box()
    '''a.change_clr()
    b.change_clr()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(1500)'''
 
    temp = a.rect.x
    if a.rect.x < b.rect.x:
        while temp < b.rect.x:
            clock.tick(FPS)
            
            screen.fill(WHITE)
            #a.change_box()
            a.change_clr()
            b.change_clr()
            a.rect.x+=3
            b.rect.x-=3            
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()

    else:
        while temp > b.rect.x:
            clock.tick(FPS)
            screen.fill(WHITE)
            a.change_clr()
            b.change_clr()
            a.rect.x-=3
            b.rect.x+=3
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()

    #if_swap = False
    a.change_bk()
    b.change_bk()
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()


def swap_circle(a,b):
    tempax=a.rect.x
    tempay =a.rect.y
    tempbx =b.rect.x
    tempby=b.rect.y
    a1=a.rect.x
    b1 =a.rect.y
    a2 =b.rect.x
    b2 =b.rect.y
    points = [(a1,b1),(a2,b2)]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords,ones(len(x_coords))]).T
    m, c = lstsq(A, y_coords)[0]
    if a.rect.y < b.rect.y:
        is_a_top = True
    else:
        is_a_top = False

    a.change_clr()
    b.change_clr()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    #pygame.time.delay(1500)
    if is_a_top:
        x1 =a.rect.x
        y1 = a.rect.y
        x2 = b.rect.x
        y2 = b.rect.y
        bi = y1-m*x1
        if(x1>x2):
            is_left = True
        else:
            is_left = False
 
        while a.rect.y < tempby:
            clock.tick(180)
            screen.fill(WHITE)
            #bi = y1-m*x1
            a.change_clr()
            b.change_clr()

            if is_left:
                x1-=1.5
            else:
                x1+=1.5
            y1+=1.5
            y = m*x1 + bi
            x = (y1-bi)/m
            a.rect.x  =x1= x
            a.rect.y = y1= y
            if is_left:
                x2+=1.5
            else:
                x1-=1.5
            y2-=1.5
            y = m*x2 + bi
            x = (y2-bi)/m
            b.rect.x  =x2= x
            b.rect.y  = y2=y
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()

    else:
        x1 = a.rect.x
        y1 = a.rect.y
        x2 = b.rect.x
        y2 = b.rect.y
        bi = y2-m*x2
        if(x1>x2):
            is_left = False
        else:
            is_left = True
        
        while a.rect.y > tempby:
            clock.tick(180)
            screen.fill(WHITE)
            #bi = int(y2-m*x2)
            a.change_clr()
            b.change_clr()
            
            if is_left:
                x1+=1.5
            else:
                x1-=1.5
            y1-=1.5
            y = m*x1 + bi
            x = (y1-bi)/m
            
            a.rect.x =x1 = x
            a.rect.y = y1 = y
            if is_left:
                x2-=1.5
            else:
                x2+=1.5
            y2+=1.5
            y = m*x2 + bi
            x = (y2-bi)/m
            b.rect.x =x2 = x
            b.rect.y =y2 = y
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
    if_swap = False
    #clock.tick(FPS)
    #screen.fill(WHITE)
    a.rect.y = tempby
    a.rect.x = tempbx
    b.rect.x = tempax
    b.rect.y = tempay
    a.change_bk()
    b.change_bk()
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()

#swap_array(m[1],m[7])

#swap_circle(p[7],p[0])

def heapify(arr, n, i, m, p):
    #screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    largest = i  # Initialize largest as root
    l = 2 * i + 1     # left = 2*i + 1
    r = 2 * i + 2     # right = 2*i + 2
 
    # See if left child of root exists and is
    # greater than root
    if l < n and arr[i] < arr[l]:
        largest = l
        m[i].change_clr()
        m[l].change_clr()
        p[i].change_clr()
        p[l].change_clr()
        #screen.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.delay(3000)
        m[i].change_bk()
        m[l].change_bk()
        p[i].change_bk()
        p[l].change_bk()
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()

 
    # See if right child of root exists and is
    # greater than root
    if r < n and arr[largest] < arr[r]:
        m[largest].change_clr()
        m[r].change_clr()
        p[largest].change_clr()
        p[r].change_clr()
        largest = r
        
        #screen.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.delay(1000)
        m[largest].change_bk()
        m[r].change_bk()
        p[largest].change_bk()
        p[r].change_bk()
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
 
    # Change root, if needed
    if largest != i:
        text(screen,"as "+ str(arr[largest]) + ">" + str(arr[i])+ " we swap them",18,300,400)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        pygame.time.delay(4000)
        arr[i],arr[largest] = arr[largest],arr[i]  # swap
        #arr[i] ,arr[lar] = arr[lar] ,arr[i]
        m[i] ,m[largest] = m[largest] ,m[i]
        p[i] ,p[largest] = p[largest] ,p[i]
        swap_array(m[i],m[largest])
        
        swap_circle(p[i],p[largest])
        screen.fill(WHITE)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
 
        # Heapify the root.
        heapify(arr, n, largest, m, p)
 
# The main function to sort an array of given size
def heapSort(arr):
    m = []
    p = []
    q = []
    n = len(arr)
    for i in range(n):
        m.append(Each_array(50+i*40+30,20,arr[i],i,A[i][0],A[i][1]))
        p.append( Each_circle(50+i*40+30,20,arr[i],i,A[i][0],A[i][1]))
        all_sprites.add(m[i])
        all_sprites.add(p[i])
    created = 0
    for i in range(n):
        l = 2*i +1
        r = 2*i +2
        if l < n:
            q.append(Each_line(p[i].rect.x,p[i].rect.y,p[l].rect.x,p[r].rect.y))
            #all_sprites.add(q[i])
            created+=1

        if r < n:
            q.append(Each_line(p[i].rect.x,p[i].rect.y,p[r].rect.x,p[r].rect.y))
            #all_sprites.add(q[i])
            created+=1
        all_sprites.add(q)
        print(created)
        
 
    # Build a maxheap.
    for i in range(n, -1, -1):
        heapify(arr, n, i, m, p)
 
    # One by one extract elements
    for i in range(n-1, 0, -1):
        if arr[0] > arr[i]:

            m[i].change_clr()
            m[0].change_clr()
            p[i].change_clr()
            p[0].change_clr()
            #screen.fill(WHITE)
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.delay(3000)
            arr[i], arr[0] = arr[0], arr[i]   # swap
            m[i] ,m[0] = m[0] ,m[i]
            p[i] ,p[0] = p[0] ,p[i]
            swap_array(m[i],m[0]) 
            swap_circle(p[i],p[0])
            text(screen,"extracting the element:"+str(arr[i]),18,300,400)
            #screen.fill(WHITE)
            p[i].change_clr()  
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.delay(3000) 
            p[i].change_bk()
            

            
            p[i].change_clr()  
            p[i].change_place(i)
            q[i-1].kill()
            screen.fill(WHITE)
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            p[i].change_bk()
            
            heapify(arr, i, 0, m, p)

    p[0].change_clr()
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    pygame.time.delay(2000) 
    p[0].change_bk()
    #pygame.time.delay(1000)   
    p[0].change_place(i-1)
    screen.fill(WHITE)
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    






arr = [12,8,7,2,9,6,14]
heapSort(arr)

n= len(arr)
print ("Sorted array is")
for i in range(n):
    print (arr[i])




'''def heapsort( arr ):
      # convert aList to heap
    length = len( arr ) - 1
    leastParent = length // 2
    m = []
    p = []
   
    for i in range(length+1):
        m.append(Each_array(50+i*40+30,20,arr[i],i,A[i][0],A[i][1]))
        p.append( Each_circle(50+i*40+30,20,arr[i],i,A[i][0],A[i][1]))
        all_sprites.add(m[i])
        all_sprites.add(p[i])

    for i in range ( leastParent, -1, -1 ):
        moveDown( arr, i, length, m, p )
 
  # flatten heap into sorted array
    for i in range ( length, 0, -1 ):
        if arr[0] > arr[i]:
            swap( arr, 0, i )
            m[i] ,m[0] = m[0] ,m[i]
            p[i] ,p[0] = p[0] ,p[i]
            swap_array(m[0],m[i])
            swap_circle(p[0],p[i])
            #m[i].kill()
            p[i].change_place(i)
            
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            moveDown( arr, 0, i - 1,m,p )
 
 
def moveDown( aList, first, last, m, p ):
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    largest = 2 * first + 1
    while largest <= last:
    # right child exists and is larger than left child
        if ( largest < last ) and ( aList[largest] < aList[largest + 1] ):
            m[largest].change_clr()
            m[largest+1].change_clr()
            p[largest].change_clr()
            p[largest+1].change_clr()
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            pygame.time.delay(600)
            largest += 1
 
    # right child is larger than parent
        if arr[largest] > arr[first]:
            swap( aList, largest, first )
            m[largest] ,m[first] = m[first] ,m[largest]
            p[largest] ,p[first] = p[first] ,p[largest]
            swap_array(m[largest],m[first])
            swap_circle(p[largest],p[first])
            all_sprites.update()
            all_sprites.draw(screen)
            pygame.display.flip()
            # move down to largest child
            first = largest;
            largest = 2 * first + 1
        else:
            return # force exit
 
 
def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

arr = [12,2,5,1]
heapsort(arr)

n= len(arr)
print ("Sorted array is")
for i in range(n):
    print (arr[i]) '''

score = 0
# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # Update
    screen.fill(WHITE)

    #m[2].rect.x+=3
    #m[2].rect.y+=3

    


    

    all_sprites.update()


    # Draw / render
    all_sprites.draw(screen)
        
    


    pygame.display.flip()

pygame.quit()