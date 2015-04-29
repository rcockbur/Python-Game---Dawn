import pygame, people, calendar, menu, random
from pygame import display, key, time, USEREVENT
from pygame.rect import Rect

MENU_WIDTH = 200

MARRIAGE = USEREVENT + 1
BIRTHDAY = USEREVENT + 2
DEATH = USEREVENT + 3
BIRTH = USEREVENT + 4
ADULTHOOD = USEREVENT + 5
PREGNANT = USEREVENT + 6
CREATE = USEREVENT + 7

MONTHS_AS_CHILD = 12 * 16
MONTHS_PREGNANT = 9
MAXLIFE = 12 * 80
MAXCONCEIVE = 12*5

pygame.init() 
display.init()
display.set_mode((640,480))
display_rect = display.get_surface().get_rect()

M = menu.Menu(display_rect, MENU_WIDTH)
menuOffsetX = display_rect.width - MENU_WIDTH
menuRect = Rect(menuOffsetX, 0, MENU_WIDTH, display_rect.height)


display.get_surface().blit(M.getSurface(), (display_rect.width - MENU_WIDTH, 0))
pygame.display.flip()

clock = time.Clock()
timeStamp = time.get_ticks()
P = people.People()
C = calendar.Calendar()

detailsAdam = {"mID": None, "fID": None, "gender": "male", "name": "Adam"}
createAdam = pygame.event.Event(CREATE, detailsAdam)
C.addPlan((0, createAdam))

detailsEve = {"mID": None, "fID": None, "gender": "female", "name": "Eve"}
createEve = pygame.event.Event(CREATE, detailsEve)
C.addPlan((0, createEve))

month = {0: "Jan", 1: "Feb", 2: "Mar", 3: "Apr", 4: "May", 5: "June", 6: "July", 7: "Aug", 8: "Sept", 9: "Oct", 10: "Nov", 11: "Dec"}

def getDate():
    return "Year: " + str(C.month / 12) + " Month: " + month[C.month % 12] 

def lifeSpan():
    return random.randint(1, MAXLIFE)

def monthsToConveive():
    return random.randint(1, 12*5)

def planAdulthood(pID):
    detailsAdult = {"pID": pID}
    eventAdult = pygame.event.Event(ADULTHOOD, detailsAdult)
    C.addPlan((C.month + MONTHS_AS_CHILD, eventAdult))
    
def planBirth(mID, fID):
    detailsBirth = {"fID": fID, "mID": mID, "gender": None, "name": None}
    eventBirth = pygame.event.Event(BIRTH, detailsBirth)
    C.addPlan((C.month + MONTHS_PREGNANT, eventBirth))
    
def planPregnancy(mID, fID):
    detailsPregnancy = {"fID": fID, "mID": mID}
    eventPregnancy = pygame.event.Event(PREGNANT, detailsPregnancy)
    C.addPlan((C.month + monthsToConveive(), eventPregnancy))
    
def planDeath(pID, maxLife):
    detailsDeath = {"pID": pID}
    eventDeath = pygame.event.Event(DEATH, detailsDeath)
    if (maxLife == True):
        C.addPlan((C.month + MAXLIFE, eventDeath))
    else:
        C.addPlan((C.month + lifeSpan(), eventDeath))
    
    
def gender(pID):
    return P.everyone[pID].gender

def alive(pID):
    return pID in P.living


mainLoop = True
while(mainLoop):
    clock.tick(24)
    
    pressed = key.get_pressed()
    alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
    ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
    
    #process controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()                       
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c and ctrl_held:
                pygame.quit()
                quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if menuRect.collidepoint(event.pos):
                print("menu")
                buttonText = M.getButton(event.pos[0] - menuOffsetX, event.pos[1])
                if buttonText != None:
                    print(buttonText)
            #print (event.pos)
            #print (event.button)       
                       
    pygame.event.pump()
#     if pygame.event.peek(): print("yes")
#     else: print("no")
    
    if(time.get_ticks()-timeStamp >= 3000):
        #if pygame.event.peek(): print("before"),
        print(getDate())
        #print("Month " + str(C.month))
        
        for event in C.getTodaysEvents():
            
            if event.type == CREATE:
                pID = P.birth(C.month, event.mID, event.fID, event.gender, event.name)
                planAdulthood(pID)
                planDeath(pID, True)
            
            elif event.type == BIRTH:
                if (event.fID not in P.living):
                    continue
                pID = P.birth(C.month, event.mID, event.fID, event.gender, event.name)
                planAdulthood(pID)
                if (event.mID not in P.living):
                    continue
                planPregnancy(event.mID, event.fID)
                planDeath(pID, False)
                
            elif event.type == ADULTHOOD:
                if (event.pID not in P.living):
                    continue
                P.adulthood(event.pID)
                spouse = P.findSpouse(event.pID)
                if (spouse != None):
                    if (gender(event.pID) == "male"):
                        P.marriage(event.pID, spouse)
                        planPregnancy(event.pID, spouse)
                    else:
                        P.marriage(spouse, event.pID)
                        planPregnancy(spouse, event.pID)
                
                
            elif event.type == PREGNANT:
                if (event.mID not in P.living):
                    continue
                if (P.pregnant(event.mID, event.fID)):
                    planBirth(event.mID, event.fID)            
                
            elif event.type == DEATH:
                if (event.pID not in P.living):
                    continue
                pID = P.death(event.pID, C.month)
                if (pID != None):
                    spouse = P.findSpouse(pID)
                    if (spouse != None):
                        if (gender(pID) == "male"):
                            P.marriage(pID, spouse)
                            planPregnancy(pID, spouse)
                        else:
                            P.marriage(spouse, pID)
                            planPregnancy(spouse, pID)
        
        C.nextMonth()
        timeStamp = time.get_ticks()
        #if pygame.event.peek(): print("after")
        
