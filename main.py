import pygame, people, calendar
from pygame import display, key, time, USEREVENT


pygame.init() 
display.init()
display.set_mode((200,200))

clock = time.Clock()
timeStamp = time.get_ticks()
P = people.People()
C = calendar.Calendar()

MARRIAGE = USEREVENT + 1
BIRTHDAY = USEREVENT + 2
DEATH = USEREVENT + 3
BIRTH = USEREVENT + 4
ADULTHOOD = USEREVENT + 5
PREGNANT = USEREVENT + 6
CREATE = USEREVENT + 7

DAYS_AS_CHILD = 18
DAYS_PREGNANT = 1
DAYS_TO_CONCEIVE = 1

detailsAdam = {"mID": None, "fID": None, "gender": "male", "name": "Adam"}
createAdam = pygame.event.Event(CREATE, detailsAdam)
C.addPlan((1, createAdam))

detailsEve = {"mID": None, "fID": None, "gender": "female", "name": "Eve"}
createEve = pygame.event.Event(CREATE, detailsEve)
C.addPlan((2, createEve))

def planAdulthood(pID):
    detailsAdult = {"pID": pID}
    eventAdult = pygame.event.Event(ADULTHOOD, detailsAdult)
    C.addPlan((C.today + DAYS_AS_CHILD, eventAdult))
    
def planBirth(mID, fID):
    detailsBirth = {"fID": fID, "mID": mID, "gender": None, "name": None}
    eventBirth = pygame.event.Event(BIRTH, detailsBirth)
    C.addPlan((C.today + DAYS_PREGNANT, eventBirth))
    
def planPregnancy(mID, fID):
    detailsPregnancy = {"fID": fID, "mID": mID}
    eventPregnancy = pygame.event.Event(PREGNANT, detailsPregnancy)
    C.addPlan((C.today + DAYS_TO_CONCEIVE, eventPregnancy))
    
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
    for event in pygame.event.get(pygame.QUIT):
        pygame.quit()
        quit()                       
    for event in pygame.event.get(pygame.KEYDOWN):
        if event.key == pygame.K_c and ctrl_held:
            pygame.quit()
            quit()                         
    pygame.event.pump()
    
    if(time.get_ticks()-timeStamp >= 3000):
        print("Day " + str(C.today))
        for event in C.getTodaysEvents():
            
            if event.type == CREATE:
                pID = P.birth(C.today, event.mID, event.fID, event.gender, event.name)
                planAdulthood(pID)
            
            if event.type == BIRTH:
                if (event.mID not in P.living):
                    continue
                pID = P.birth(C.today, event.mID, event.fID, event.gender, event.name)
                planAdulthood(pID)
                
            if event.type == ADULTHOOD:
                if (event.pID not in P.living):
                    continue
                partnerID = P.adulthood(event.pID)
                if (partnerID != None):
                    if (gender(event.pID) == "male"):
                        P.marriage(event.pID, partnerID)
                        planPregnancy(event.pID, partnerID)
                    else:
                        P.marriage(partnerID, event.pID)
                        planPregnancy(partnerID, event.pID)
                
            if event.type == PREGNANT:
                if (event.mID not in P.living):
                    continue
                P.pregnant(event.mID, event.fID)
                planBirth(event.mID, event.fID)            
                
            if event.type == DEATH:
                pass
        
        C.nextDay()
        timeStamp = time.get_ticks()
        
