while True:
    try:
        uzunlik = int(input("x, 0 o'yini. O'lchamni kiriting(3 dan katta, 7 dan kichik. Tugatish uchun '10' ni kiriting):"))
    except:
        print("butun son kiriting!")
    else:
        if uzunlik==10:
            break
        elif uzunlik>2 and uzunlik<7:
            gal = 1
            sonlar = list(range(uzunlik))
            x_lar = []
            o_lar = []
            tugash = True
            x=0
            o=0
            while tugash:
                son_ch=1
                print("\n")
                for son in sonlar:
                    bir_xil_x_cho=0
                    bir_xil_o_cho=0
                    for son in sonlar:
                        if son_ch in x_lar:
                            print("x", "   ", end='')
                            bir_xil_x_cho +=1
                        elif son_ch in o_lar:
                            print("0", "   ", end='')
                            bir_xil_o_cho +=1
                        else:
                            if son_ch>9:
                                print(son_ch, "  ", end='')
                            else:
                                print(son_ch, "   ", end='')
                        son_ch +=1
                        if bir_xil_x_cho == uzunlik:
                            x=1
                            
                        elif bir_xil_o_cho == uzunlik:
                            o=1
                            
                    print("\n")
                i=1
                bir_xil_x_g = 0
                bir_xil_o_g = 0
                bir_xil_x_g_t = 0
                bir_xil_o_g_t = 0
                uzunlik_k = uzunlik
                while i <= uzunlik**2:
                    if i in x_lar:
                        bir_xil_x_g +=1
                    elif i in o_lar:
                        bir_xil_o_g +=1
                    if  uzunlik_k in x_lar:
                        bir_xil_x_g_t +=1
                    elif uzunlik_k in o_lar:
                        bir_xil_o_g_t +=1
                        
                    uzunlik_k += uzunlik-1
                    i +=uzunlik+1
                i=1
                while i<=uzunlik:
                    b_xil_x_tp = 0
                    b_xil_o_tp = 0
                    tp=i
                    w=1
                    while w <= uzunlik:
                        if tp in x_lar:
                            b_xil_x_tp +=1
                        elif tp in o_lar:
                            b_xil_o_tp +=1
                        tp +=uzunlik
                        w +=1
                    i +=1
                    if b_xil_x_tp == uzunlik:
                        x=1
                    elif b_xil_o_tp == uzunlik:
                        o=1
                    
                if x or bir_xil_x_g == uzunlik or bir_xil_x_g_t == uzunlik:
                    print("x yutdi")
                    tugash=False
                elif o or bir_xil_o_g == uzunlik or bir_xil_o_g_t == uzunlik:
                    print("0 yutdi")
                    tugash=False
                elif len(x_lar)+len(o_lar)==uzunlik**2:
                    print("durrang")
                    tugash=False
                else:
                    if gal: 
                        try:
                            index = int(input("x ning indexini kiriting: "))
                        except:
                            print("indexni xato kiritdingiz!")
                        else:
                            if index not in o_lar and index not in x_lar:
                                x_lar.append(index)
                                gal=gal-1
                            else:
                                print("indexni xato kiritdingiz!")
                    else:
                        try:
                            index = int(input("0 ning indexini kiriting: "))
                        except:
                            print("indexni xato kiritdingiz!")
                        else:
                            if index not in o_lar and index not in x_lar:
                                o_lar.append(index)
                                gal = gal+1
                            else:
                                print("indexni xato kiritdingiz!")
                
        else:
            print("Xato! 2 dan katta, 7 dan kichik son kiriting")
            

