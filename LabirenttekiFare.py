def labirenti_yaz( matris ):  
    print("Farenin izlediği yol: ")
    for i in matris:
        for j in i:
            print(str(j) + " ", end ="")
        print("")
    print("Fare çıkışa ulaştı 🧀 🐁") 
 

def sartları_kontrol_et( labirent, x, y ):
     
    if x >= 0 and x < 10 and y >= 0 and y < 10 and labirent[x][y] == 1:
        return True
    else:
        return False
 

    
def farenin_izledigi_yol( labirent ):
     
    matris = [ [ "-" for j in range(10) ] for i in range(10) ]  # 10x10 luk  yan çizgilerden oluşan matris (Sağlanan şartları tutması için)
     
    if hareket_et(labirent, 0, 1, matris) == False:             #başlangıç noktası
        print("Fare çıkışı bulamadı");                          
        return False
     
    labirenti_yaz(matris)
    return True
  


def hareket_et(labirent, x, y, matris):
    
    if x == 9 and y == 9 and labirent[x][y]== 1:   #çıkış koordinatları
        matris[x][y] = 1
        return True
    
    if sartları_kontrol_et(labirent, x, y) == True:  
        
        if matris[x][y] == 1:
            return False
        
        matris[x][y] = 1
        
        if hareket_et(labirent, x + 1, y, matris) == True:   #sağa hareket et
            return True
        
        if hareket_et(labirent, x, y + 1, matris) == True:   #aşağı hareket et
            return True 
        
        if hareket_et(labirent, x - 1, y, matris) == True:   #sola hareket et
            return True
        
        if hareket_et(labirent, x, y - 1, matris) == True:   #yukarı hareke et
            return True 
        
        matris[x][y] = "*"                                   # yanlış yola girdiğinde * işaretini koy
        return False

labirent = [
             [0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,0,0,0,0],
             [0,1,0,0,0,0,1,1,1,0],
             [0,1,1,1,1,1,1,0,0,0],
             [0,0,0,1,0,0,1,0,0,0],
             [0,0,0,1,0,0,1,0,0,0],
             [0,0,0,1,0,0,1,1,1,1],
             [1,1,1,1,0,0,0,0,0,1],
             [0,1,0,1,1,1,0,0,0,1]
                                   ]
farenin_izledigi_yol( labirent )