# Anastasiou Nikolas rs20095
# Orizontio Diktio

# Include Libraries
import numpy as np
import matplotlib.pyplot as plt
from fpdf import FPDF



def input_data(data_fileName):
    data = np.loadtxt(open(data_fileName,'rt').readlines()[:-3], delimiter=' ', dtype=str)

    return data

def org_data(raw_data, temp_name, gon_data, s_data, n, all_data, all_data_name, name_codes):

    for i in range(n):
        # add data to arrays from raw_data
        temp_name.append(raw_data[i][0])
        tmp = list(temp_name[i])
        tmp_cnt = 0

        for k in range(len(tmp)):
            if tmp[k] == '-':
                tmp_cnt += 1

        if tmp_cnt == 1:
            s_data[i, 0] = raw_data[i][1]
            temp_name[i] = str(temp_name[i]) + '-0'
        else:
            gon_data[i, 0] = raw_data[i][1]

        all_data[i, 0] = raw_data[i][1]


        # save name to all_data_name list
        tmp = temp_name[i]
        a = tmp.split('-', 100)
        all_data_name.append(a)

        if tmp_cnt == 1:
            s_data_name.append(a)
        else:
            gon_data_name.append(a)

    # pernoume ta onoma twn korifwn apo thn pro-teleutea grammi
    with open(data_file_name, 'r') as file:
        line = file.readlines()[-2].splitlines()
        all_name_codes = str(line[0])

        tmp_name = all_name_codes
        tmp_name_2 = tmp_name.split('-', 100)
        #print(tmp_name_2)

        for i in range(len(tmp_name_2)):
            name_codes.append(tmp_name_2[i])

    # pernoume tis sintetagmenes tis staheris korifis kai tin gonia apo tin teleutea grammi
    with open(data_file_name, 'r') as file:
        line = file.readlines()[-1]
        line = line.split(' ', 100)

        global staheri_gonia
        global stahero_x
        global stahero_y

        staheri_gonia = float(line[2])
        stahero_x = float(line[0])
        stahero_y = float(line[1])


    return 0

def create_P(P, s_g, s_s, s_0, n, all_data_name):
    tmp_cnt = 0

    for i in range(n):
        for k in range(len(all_data_name[i])):
            if all_data_name[i][k] == '0':
                tmp_cnt = 1

        if tmp_cnt == 1:
            P[i,i] = (s_0**2)/(s_s**2)
        else:
            P[i,i] = (s_0**2)/(s_g**2)
        tmp_cnt = 0

    return 0

def create_b_gon(b_name_1, b_name_2, b_name_3, gon_data, gon_data_name):
    b_gon = 0
#
#if gon_data_name[i][2] == gon_data_name[k][0] and gon_data_name[k][1] == b_name_2 and gon_data_name[i][0] == b_name_1 and gon_data_name[k][2] == b_name_3:

    for i in range(len(gon_data)):
        for k in range(len(gon_data)):
            if gon_data_name[i][1] == gon_data_name[k][1] and gon_data_name[i][1] == b_name_2 and gon_data_name[i][0] == b_name_1 and gon_data_name[k][2] == b_name_3:
                b_gon = gon_data[i, 0] + gon_data[k, 0]
                #print(gon_data[i, 0] , gon_data[k, 0])
                #print(gon_data_name[i][1] , gon_data_name[k][1])
                break
            else:
                if gon_data_name[i][1] == gon_data_name[k][1] and gon_data_name[i][1] == b_name_2 and gon_data_name[i][0] == gon_data_name[k][0] and gon_data_name[i][2] == b_name_3 and gon_data_name[k][2] == b_name_1:
                    b_gon = gon_data[i, 0] - gon_data[k, 0]
                else:
                    if gon_data_name[i][1] == gon_data_name[k][1] and gon_data_name[i][1] == b_name_2 and gon_data_name[i][0] == b_name_1 and gon_data_name[k][0] == b_name_3:
                        b_gon = gon_data[i, 0] - gon_data[k, 0]

                if b_gon < 0:
                    #print('gon negative!')
                    b_gon = -b_gon

    return b_gon

def find_index(array_name):
    index_1 = 0
    index_2 = 0
    point_1_name = array_name[0]
    point_2_name = array_name[1]

    for i in range(len(name_codes)):
        if point_1_name == name_codes[i]:
            index_1 = i
        if point_2_name == name_codes[i]:
            index_2 = i

    return index_1, index_2

def check_a(a):

    if a > 400:
        while a > 400:
            a = a - 400
    if a < 0:
        while a < 0:
            a = a + 400

    return a

def ver_a(a_arxikes, staheri_gonia, gon_data, gon_data_name, name_codes):

    b_gon = find_gon(name_codes[len(name_codes)-1], name_codes[0], name_codes[1], gon_data, gon_data_name)

    a_ver = a_arxikes[len(name_codes)-1, 0] + b_gon + 200
    a_ver = check_a(a_ver)

    if int(a_ver) == int(staheri_gonia):
        return 0
    else:
        print('Problima me gonies dieuthinisis!')
        print('Staheri gonia', staheri_gonia_name[0],staheri_gonia_name[1], '=', staheri_gonia)
        print('Ypologismeni', a_ver)
        exit(1)

def cal_a_Arxikes_Times(gon_data, gon_data_name, name_codes, a_arxikes, staheri_gonia, staheri_gonia_name, a_arxikes_name):

    previous_a = staheri_gonia

    b_gons = np.zeros((len(name_codes), 1))

    a_arxikes[0, 0] = staheri_gonia
    a_arxikes_name.append(staheri_gonia_name)

    print('Gonies b kai Gonies Dieuthinisis Ypologismena (grad)')
    print(staheri_gonia_name[0],'-' , staheri_gonia_name[1], staheri_gonia, ', stahero')
    pdf.set_font("Helvetica", style='u', size=11.5,)
    pdf.cell(0, 12, txt = 'Gonies b kai Gonies Dieuthinisis Ypologismena (grad)', border=0, ln =2 , align = 'L')
    text = str('a gon ' + staheri_gonia_name[0] + '-' + staheri_gonia_name[1] +' = ' + str(staheri_gonia) + ', stathero')
    pdf.set_font("Helvetica" , size= 11,)

    pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')



    for i in range(len(name_codes)-1):

        if i == len(name_codes)-2:
            b_name_1 = name_codes[i]
            b_name_2 = name_codes[i + 1]
            b_name_3 = name_codes[0]
        else:
            b_name_1 = name_codes[i]
            b_name_2 = name_codes[i + 1]
            b_name_3 = name_codes[i + 2]

        b_gon = 0


        for k in range(len(gon_data)):
            if (gon_data_name[k][0] == b_name_1 or gon_data_name[k][0] == b_name_3) and gon_data_name[k][1] == b_name_2 and (gon_data_name[k][2] == b_name_3 or gon_data_name[k][2] == b_name_1):

                if gon_data_name[k][0] == b_name_3 and gon_data_name[k][2] == b_name_1:
                    b_gon = 400 - gon_data[k, 0]

                else:
                    b_gon = gon_data[k, 0]

        if b_gon == 0:
            b_gon = create_b_gon(b_name_1, b_name_2, b_name_3, gon_data, gon_data_name)



        b_gons[i, 0] = round(b_gon, 4)
        a = previous_a + b_gon + 200
        a = check_a(a)
        previous_a = a
        a_arxikes[i+1, 0] = round(a, 4)
        a_arxikes_name.append([b_name_2, b_name_3])

        print(b_name_1,'-',b_name_2,'-',b_name_3, '=', b_gon, ' a gon = ', a_arxikes_name[i+1][0], a_arxikes_name[i+1][1], '=', a_arxikes[i+1, 0])
        text = str(str(b_name_1) +' -' + str(b_name_2) + '-' + str(b_name_3) + ' = ' + str(b_gon) + ', a gon ' + str(a_arxikes_name[i+1][0]) + '-' + str(a_arxikes_name[i+1][1]) + ' = ' + str(a_arxikes[i+1, 0]))
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')


    print('\n')

    ver_a(a_arxikes, staheri_gonia, gon_data, gon_data_name, name_codes)

    return a_arxikes

def find_gon(b_name_1, b_name_2, b_name_3, gon_data, gon_data_name):

    b_gon = 0
    for k in range(len(gon_data)):
        if (gon_data_name[k][0] == b_name_1 or gon_data_name[k][0] == b_name_3) and gon_data_name[k][1] == b_name_2 and (gon_data_name[k][2] == b_name_3 or gon_data_name[k][2] == b_name_1):

            if gon_data_name[k][0] == b_name_3 and gon_data_name[k][2] == b_name_1:
                print('e3oteriki!')
                b_gon = 400 - gon_data[k, 0]
            else:
                b_gon = gon_data[k, 0]

    if b_gon == 0:
        b_gon = create_b_gon(b_name_1, b_name_2, b_name_3, gon_data, gon_data_name)

    return b_gon

def calc_s_from_nomo_imitonwn(point_1, point_2, s_data, s_data_name, gon_data, gon_data_name):

    for i in range(len(s_data_name)):
        s = 0

        if s_data_name[i][0] == point_1 or s_data_name[i][1] == point_1:
            d = s_data[i, 0]

            if s_data_name[i][0] == point_1:
                point_3 = s_data_name[i][1]
            else:
                point_3 = s_data_name[i][0]

            b_gon_1 = find_gon(point_1, point_2, point_3, gon_data, gon_data_name)
            b_gon_2 = find_gon(point_2, point_3, point_1, gon_data, gon_data_name)


            s = (d*np.sin(b_gon_2*np.pi/200))/np.sin(b_gon_1*np.pi/200)
            #print('Nomos imotonwn 1')
            #print(point_1, point_2, point_3, ' ', b_gon_1)
            #print(point_2, point_3, point_1, ' ', b_gon_2)
            #print(point_1, point_2, ' d=',round(s, 3))
            break

        else:
            if s_data_name[i][0] == point_2 or s_data_name[i][1] == point_2:
                d = s_data[i, 0]

                if s_data_name[i][0] == point_1:
                    point_3 = s_data_name[i][1]
                else:
                    point_3 = s_data_name[i][0]

                b_gon_1 = find_gon(point_2, point_1, point_3, gon_data, gon_data_name)
                b_gon_2 = find_gon(point_1, point_3, point_2, gon_data, gon_data_name)

                s = (d * np.sin(b_gon_2 * np.pi / 200)) / np.sin(b_gon_1 * np.pi / 200)
                #print('Nomos imotonwn 2')
                #print(point_1, point_2, point_3, ' ', round(b_gon_1, 4))
                #print(point_2, point_3, point_1, ' ', round(b_gon_2, 4))
                #print(point_1, point_2, ' d=',round(s, 3))
                break


    return round(s, 3)

def calc_s_Arxikes_Times(s_data, s_data_name, name_codes, s_arxikes, s_arxikes_name):
    print('Mikoi apo Dedomena kai Ypologismena (m)')
    pdf.set_font("Helvetica", style='u', size=11.5,)
    pdf.cell(0, 13, txt='Mikoi apo Dedomena kai Ypologismena (m)', border=0, ln=2, align='L')
    pdf.set_font("Helvetica", size= 11,)



    for i in range(len(name_codes)):
        if i == len(name_codes)-1:
            point_2 = name_codes[0]
        else:
            point_2 = name_codes[i + 1]

        point_1 = name_codes[i]

        temp_s = 0
        for k in range(len(s_data_name)):
            if (s_data_name[k][0] == point_1 and s_data_name[k][1] == point_2) or (s_data_name[k][0] == point_2 and s_data_name[k][1] == point_1):
                temp_s = s_data[k, 0]
                break
            else:
                temp_s = 0

        if temp_s == 0:
            s_arxikes[i, 0] = calc_s_from_nomo_imitonwn(point_1, point_2, s_data, s_data_name, gon_data, gon_data_name)
            if s_arxikes[i, 0] == 0:
                print('Problima me apostasi, den mporese na brethei!')
                exit(1)
            s_arxikes_name.append([point_1, point_2])
        else:
            s_arxikes[i, 0] = temp_s
            s_arxikes_name.append([point_1, point_2])

        print(point_1,'-',point_2, '=', round(s_arxikes[i, 0], 3))
        text = str(str(point_1) + '-' + str(point_2) + ' = ' + str(round(s_arxikes[i, 0], 3)))
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

    print('\n')

    return s_arxikes

def calc_x_y_Arxikes_Times(a_arxikes, name_codes, stahero_simeio_name, stahero_x, stahero_y, x_y_Arxikes_Times, x_y_Arxikes_Times_name):

    print('Arxikes Times (x, y)')
    pdf.set_font("Helvetica", style='u', size=11.5,)
    pdf.cell(0, 13, txt='Arxikes Times (x, y)', border=0, ln=2, align='L')
    pdf.set_font("Helvetica", size= 11,)


    prev_x = stahero_x
    prev_y = stahero_y

    x_y_Arxikes_Times[0, 0] = stahero_x
    x_y_Arxikes_Times[0, 1] = stahero_y
    x_y_Arxikes_Times_name.append([stahero_simeio_name])

    print('Stathero ', stahero_simeio_name)
    text = str(('Stathero: ' + str(stahero_simeio_name)))
    pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

    print(stahero_simeio_name, '=' , '(', stahero_x,',' ,stahero_y, ')')
    text = str(str(stahero_simeio_name) + ' = ' + '('+ str(stahero_x) +', ' + str(stahero_y) + ')')
    pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')



    for i in range(len(name_codes)-1):

        if i == len(name_codes):
            point_2 = name_codes[0]
        else:
            point_2 = name_codes[i+1]

        point_1 = name_codes[i]


        x = prev_x + s_arxikes[i, 0]*np.sin(a_arxikes[i, 0]*np.pi/200)
        prev_x = x
        x_y_Arxikes_Times[i+1, 0] = x

        y = prev_y + s_arxikes[i, 0]*np.cos(a_arxikes[i, 0]*np.pi/200)
        prev_y = y
        x_y_Arxikes_Times[i+1, 1] = y


        x_y_Arxikes_Times_name.append([point_2])

        print(x_y_Arxikes_Times_name[i+1][0], '=' ,'(', round(x, 3), ',' ,round(y, 3), ')')
        text = str(str(x_y_Arxikes_Times_name[i+1][0]) + '=' + '(' + str(round(x, 3)) + ', ' + str(round(y, 3)) + ')')
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

    print('\n')
    return x_y_Arxikes_Times

def check_tetartimorio(a, dx, dy):

    if dx > 0 and dy > 0:
        return a
    if (dx < 0 and dy < 0) or (dx > 0 and dy < 0):
        return a + 200
    if dx < 0 and dy > 0:
        return a + 400

def calc_dl_and_A(x_y_Arxikes_Times, x_y_Arxikes_Times_name, dl, all_data, all_data_name, A, name_codes, staheri_gonia_name, staheri_gonia):
    print('Kainouries gonies b kai Apostaseis s')
    pdf.set_font("Helvetica", style='u', size=11.5,)
    pdf.cell(0, 13, txt='Kainouries gonies b kai Apostaseis s', border=0, ln=2, align='L')
    pdf.set_font("Helvetica", size= 11,)


    name_codes_ = []
    name_codes_.append(name_codes[1])
    for i in range(len(name_codes) - 2):
        name_codes_.append(name_codes[i + 2])
        name_codes_.append('0')

    staheri_gonia = staheri_gonia * np.pi / 200

    for i in range(len(all_data_name)):
        # j, i, k
        point_1 = all_data_name[i][0]
        point_2 = all_data_name[i][1]
        point_3 = all_data_name[i][2]

        point_1_x = 0
        point_1_y = 0
        point_2_x = 0
        point_2_y = 0
        point_3_x = 0
        point_3_y = 0


        if point_3 != '0':

            for k in range(len(x_y_Arxikes_Times_name)):
                if x_y_Arxikes_Times_name[k][0] == point_1:
                    point_1_x = x_y_Arxikes_Times[k, 0]
                    point_1_y = x_y_Arxikes_Times[k, 1]

                if x_y_Arxikes_Times_name[k][0] == point_2:
                    point_2_x = x_y_Arxikes_Times[k, 0]
                    point_2_y = x_y_Arxikes_Times[k, 1]

                if x_y_Arxikes_Times_name[k][0] == point_3:
                    point_3_x = x_y_Arxikes_Times[k, 0]
                    point_3_y = x_y_Arxikes_Times[k, 1]

            dx_1 = point_3_x - point_2_x
            dy_1 = point_3_y - point_2_y

            # i, k
            a_1 = np.arctan( dx_1 / dy_1 )*(200/np.pi)
            a_1 = check_tetartimorio(a_1, dx_1 , dy_1)
            a_1 = check_a(a_1)


            dx_2 = point_1_x - point_2_x
            dy_2 = point_1_y - point_2_y

            # i, j
            a_2 = np.arctan( dx_2 / dy_2 )*(200/np.pi)
            a_2 = check_tetartimorio(a_2, dx_2 , dy_2)
            a_2 = check_a(a_2)

            b_gon_new = a_1 - a_2
            b_gon_new = check_a(b_gon_new)

            dl[i, 0] = (all_data[i, 0] - b_gon_new)*10000 # metatropi se cc apo grad, pio katw kathe sintelestis a ginete epi r_cc an oxi tote to afinoume grad auto

            print(point_1, '-', point_2, '-' ,point_3, '=',round(b_gon_new, 4))
            text = str(point_1 + '-' + point_2 + '-'  + point_3 + ' = ' + str(round(b_gon_new, 4)))
            pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

            dist_point_2_point_1 = np.sqrt( (point_2_x - point_1_x)**2 + (point_2_y - point_1_y)**2 )
            dist_point_2_point_3 = np.sqrt( (point_2_x - point_3_x)**2 + (point_2_y - point_3_y)**2 )

            a_1 = a_1 * np.pi / 200
            a_2 = a_2 * np.pi / 200
            #staheri_gonia = staheri_gonia * np.pi / 200
            a1, a2, a3, a4, a5, a6 = 0, 0, 0, 0, 0, 0


            if point_1 != staheri_gonia_name[1] and point_2 != staheri_gonia_name[1] and point_3 != staheri_gonia_name[1]:
                a1 = r_cc * ( np.cos(a_2) / dist_point_2_point_1 -  np.cos(a_1) / dist_point_2_point_3) # dx_i
                a2 = r_cc * (np.sin(a_1) / dist_point_2_point_3 - np.sin(a_2) / dist_point_2_point_1)  # dy_i

                a3 = - r_cc * (np.cos(a_2) / dist_point_2_point_1) # dx_j
                a4 = r_cc * (np.sin(a_2) / dist_point_2_point_1) # dy_j

                a5 = r_cc * (np.cos(a_1) / dist_point_2_point_3) # dx_k
                a6 = - r_cc * (np.sin(a_1) / dist_point_2_point_3) # dy_k

                if point_1 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0
                if point_2 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_3 == staheri_gonia_name[0]:
                    a5 = 0
                    a6 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a3
                        A[i, k+1] = a4
                    if point_2 == name_codes_[k]:
                        A[i, k] = a1
                        A[i, k+1] = a2
                    if point_3 == name_codes_[k]:
                        A[i, k] = a5
                        A[i, k+1] = a6



            if point_1 != staheri_gonia_name[1] and point_2 != staheri_gonia_name[1] and point_3 == staheri_gonia_name[1]:
                a1 = r_cc * ( np.cos(a_2) / dist_point_2_point_1 -  np.cos(a_1) / dist_point_2_point_3) # dx_i
                a2 = r_cc * (np.sin(a_1) / dist_point_2_point_3 - np.sin(a_2) / dist_point_2_point_1)  # dy_i

                a3 = - r_cc * (np.cos(a_2) / dist_point_2_point_1) # dx_j
                a4 = r_cc * (np.sin(a_2) / dist_point_2_point_1) # dy_j

                a5 = r_cc * (np.cos(a_1) / dist_point_2_point_3) * (np.sin(staheri_gonia)) - r_cc * (np.sin(a_1) / dist_point_2_point_3) * (np.cos(staheri_gonia)) # ds_a_stahero
                a6 = 0 #- r_cc * (np.sin(a_1) / dist_point_2_point_3) * (np.cos(staheri_gonia)) # dy_k

                if point_1 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0
                if point_2 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_3 == staheri_gonia_name[0]:
                    a5 = 0
                    a6 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a3
                        A[i, k + 1] = a4
                    if point_2 == name_codes_[k]:
                        A[i, k] = a1
                        A[i, k + 1] = a2
                    if point_3 == name_codes_[k]:
                        A[i, k] = a5


            if point_1 == staheri_gonia_name[1] and point_2 != staheri_gonia_name[1] and point_3 != staheri_gonia_name[1]:
                a1 = r_cc * ( np.cos(a_2) / dist_point_2_point_1 -  np.cos(a_1) / dist_point_2_point_3) # dx_i
                a2 = r_cc * (np.sin(a_1) / dist_point_2_point_3 - np.sin(a_2) / dist_point_2_point_1)  # dy_i

                a3 = - r_cc * (np.cos(a_2) / dist_point_2_point_1) * (np.sin(staheri_gonia)) + r_cc * (np.sin(a_2) / dist_point_2_point_1) * (np.cos(staheri_gonia)) # ds_a_stahero
                a4 = 0 #r_cc * (np.sin(a_2) / dist_point_2_point_1) # dy_j

                a5 = r_cc * (np.cos(a_1) / dist_point_2_point_3) # dx_k
                a6 = - r_cc * (np.sin(a_1) / dist_point_2_point_3) # dy_k

                if point_1 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0
                if point_2 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_3 == staheri_gonia_name[0]:
                    a5 = 0
                    a6 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a3
                    if point_2 == name_codes_[k]:
                        A[i, k ] = a1
                        A[i, k + 1] = a2
                    if point_3 == name_codes_[k]:
                        A[i, k] = a5
                        A[i, k + 1] = a6



            if point_1 != staheri_gonia_name[1] and point_2 == staheri_gonia_name[1] and point_3 != staheri_gonia_name[1]:
                a1 = r_cc * ( np.cos(a_2) / dist_point_2_point_1 -  np.cos(a_1) / dist_point_2_point_3) * (np.sin(staheri_gonia)) + r_cc * (np.sin(a_1) / dist_point_2_point_3 - np.sin(a_2) / dist_point_2_point_1) * (np.cos(staheri_gonia)) # ds_a_sthaero
                a2 = 0 # r_cc * (np.sin(a_1) / dist_point_2_point_3 - np.sin(a_2) / dist_point_2_point_1)  # dy_i

                a3 = - r_cc * (np.cos(a_2) / dist_point_2_point_1) # dx_j
                a4 = r_cc * (np.sin(a_2) / dist_point_2_point_1) # dy_j

                a5 = r_cc * (np.cos(a_1) / dist_point_2_point_3) # dx_k
                a6 = - r_cc * (np.sin(a_1) / dist_point_2_point_3) # dy_k

                if point_1 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0
                if point_2 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_3 == staheri_gonia_name[0]:
                    a5 = 0
                    a6 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k ] = a3
                        A[i, k + 1] = a4
                    if point_2 == name_codes_[k]:
                        A[i, k] = a1
                    if point_3 == name_codes_[k]:
                        A[i, k] = a5
                        A[i, k + 1] = a6

            # s54, x3, y3, x2, y2, x1, y1

            #print(round(A[i, 0]), round(A[i, 1]), round(A[i, 2]), round(A[i, 3]), round(A[i, 4]), round(A[i, 5]), round(A[i, 6]))
            #print(round(a1), round(a2), round(a3), round(a4), round(a5), round(a6))
            #break


        else:

            for k in range(len(x_y_Arxikes_Times_name)):
                if x_y_Arxikes_Times_name[k][0] == point_1:
                    point_1_x = x_y_Arxikes_Times[k, 0]
                    point_1_y = x_y_Arxikes_Times[k, 1]

                if x_y_Arxikes_Times_name[k][0] == point_2:
                    point_2_x = x_y_Arxikes_Times[k, 0]
                    point_2_y = x_y_Arxikes_Times[k, 1]

            dist_new = np.sqrt( (point_1_x - point_2_x)**2 + (point_1_y - point_2_y)**2 )

            dl[i, 0] =  all_data[i, 0] - dist_new

            print(point_1,'-',point_2,'=' ,round(dist_new, 3))
            text = str(point_1 + '-' + point_2 + ' = ' + str(round(dist_new, 3)))
            pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')



            dx_1 = point_2_x - point_1_x
            dy_1 = point_2_y - point_1_y

            # i, j
            a_1 = np.arctan( dx_1 / dy_1 )*(200/np.pi)
            a_1 = check_tetartimorio(a_1, dx_1 , dy_1)
            a_1 = check_a(a_1)
            a_1 = a_1 * np.pi / 200

            if point_1 != staheri_gonia_name[1] and point_2 != staheri_gonia_name[1]:
                a1 = -np.sin(a_1) # dx_i
                a2 = -np.cos(a_1) # dy_i

                a3 = np.sin(a_1) # dx_j
                a4 = np.cos(a_1) # dy_j

                if point_1 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_2 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a1
                        A[i, k + 1] = a2
                    if point_2 == name_codes_[k]:
                        A[i, k] = a3
                        A[i, k + 1] = a4


            if point_1 == staheri_gonia_name[1] and point_2 != staheri_gonia_name[1]:
                a1 = -np.sin(a_1) * np.sin(staheri_gonia) - np.cos(a_1)*np.cos(staheri_gonia) # dx_i
                a2 = 0#-np.cos(a_1) # dy_i

                a3 = np.sin(a_1) # dx_j
                a4 = np.cos(a_1) # dy_j

                if point_1 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_2 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a1
                    if point_2 == name_codes_[k]:
                        A[i, k] = a3
                        A[i, k + 1] = a4

            if point_1 != staheri_gonia_name[1] and point_2 == staheri_gonia_name[1]:
                a1 = -np.sin(a_1) # dx_i
                a2 = -np.cos(a_1) # dy_i

                a3 = np.sin(a_1) * np.sin(staheri_gonia) + np.cos(a_1) * np.cos(staheri_gonia) # dx_j
                a4 = 0#np.cos(a_1) # dy_j

                if point_1 == staheri_gonia_name[0]:
                    a1 = 0
                    a2 = 0
                if point_2 == staheri_gonia_name[0]:
                    a3 = 0
                    a4 = 0

                for k in range(len(name_codes_)):
                    if point_1 == name_codes_[k]:
                        A[i, k] = a1
                        A[i, k + 1] = a2
                    if point_2 == name_codes_[k]:
                        A[i, k] = a3

            #print(round(A[i, 0], 4), round(A[i, 1], 4), round(A[i, 2], 4), round(A[i, 3], 4), round(A[i, 4], 4), round(A[i, 5], 4), round(A[i, 6], 4))

    print('\n')
    return 0

def calc_new_x_y(x, staheri_gonia, x_y, x_y_Arxikes_Times, x_y_Arxikes_Times_name):


    dx_imistaherou = np.sin(staheri_gonia * np.pi / 200) * x[0, 0]
    dy_imistaherou = np.cos(staheri_gonia * np.pi / 200) * x[0, 0]

    x_y_Arxikes_Times[1, 0] = x_y_Arxikes_Times[1, 0] + dx_imistaherou
    x_y_Arxikes_Times[1, 1] = x_y_Arxikes_Times[1, 1] + dy_imistaherou

    offset = 0
    for i in range(len(x_y_Arxikes_Times)-2):
        x_y_Arxikes_Times[i + 2, 0] = x_y_Arxikes_Times[i + 2, 0] + x[i + 1 + offset, 0]
        x_y_Arxikes_Times[i + 2, 1] = x_y_Arxikes_Times[i + 2, 1] + x[i + 2 + offset, 0]
        offset += 1

    #print(x_y_Arxikes_Times)
    return 0

def calc_errors(Vx, errors, staheri_gonia, k):

    J = np.zeros((len(Vx), len(Vx)))

    J[0, 0] = np.sin(staheri_gonia * np.pi / 200)
    J[1, 0] = np.cos(staheri_gonia * np.pi / 200)

    for i in range(len(J) - 2):
        J[i + 2, i + 2] = 1

    Vx_imistaherou = J@Vx@np.transpose(J)

    errors[0, 0] = 0
    errors[0, 1] = 0
    errors[1, 0] = np.sqrt( Vx_imistaherou[0, 0] )
    errors[1, 1] = np.sqrt( Vx_imistaherou[1, 1] )


    offset = 0
    for i in range(k - 2):
        errors[i + 2, 0] = np.sqrt( Vx[i + 1 + offset, i + 1 + offset] )
        errors[i + 2, 1] = np.sqrt( Vx[i + 2 + offset, i + 2 + offset] )
        offset += 1


    return 0

def mikoi_t0_egsa87(s_data, x_meso):

    for i in range(len(s_data)):
        s_data[i, 0] = s_data[i, 0] * ( 0.9996 + 0.012311 * ( (x_meso/10**6)  - 0.5)**2 )

    return s_data

def save_to_txt(x_y_Arxikes_Times):

    with open("output.txt", 'w') as log:
        for i in range(len(x_y_Arxikes_Times)):
            log.write(str(round(x_y_Arxikes_Times[i, 0], 3)))
            log.write(', ')
            log.write(str(round(x_y_Arxikes_Times[i, 1], 3)))
            log.write('\n')

    return 0

def print_apotelesmta(x_y_Arxikes_Times, x_y_Arxikes_Times_name, errors):

    print('Telika Apotelemsta')
    pdf.set_font("Helvetica", style='u', size=11.5, )
    pdf.cell(0, 13, txt='Telika Apotelemsta', border=0, ln=2, align='L')
    pdf.set_font("Helvetica", size=11)

    for k in range(len(x_y_Arxikes_Times)):
        print(x_y_Arxikes_Times_name[k][0], '(x, y) =', '(', round(x_y_Arxikes_Times[k, 0], 3), ',',
              round(x_y_Arxikes_Times[k, 1], 3), ')', '+-', '(', round(errors[k, 0], 4), ',', round(errors[k, 1], 4),
              ')')
        text = str(
            x_y_Arxikes_Times_name[k][0] + ' (x, y) = ' + '(' + str(round(x_y_Arxikes_Times[k, 0], 3)) + ', ' + str(
                round(x_y_Arxikes_Times[k, 1], 3)) + ')' + ' +- ' + '(' + str(round(errors[k, 0], 4)) + ', ' + str(
                round(errors[k, 1], 4)) + ')')
        pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

    print('\n')
    print('Sigma_0 =', round(s_0_[0][0] / s_0, 4), '\n')
    text = str('Sigma_0 = ' + str(round(s_0_[0][0] / s_0, 4)))
    pdf.cell(0, 10, txt=text, border=0, ln=2, align='L')

    return 0

def plot_data():

    plt.figure(figsize=(11.69, 8.27)) # bazoume to sxedio na einai se megethos A4

    x = np.zeros((len(x_y_Arxikes_Times)+1, 1))
    y = np.zeros((len(x_y_Arxikes_Times)+1, 1))

    for i in range(len(x_y_Arxikes_Times)):
        x[i, 0] = x_y_Arxikes_Times[i, 0]
        y[i, 0] = x_y_Arxikes_Times[i, 1]

        plt.text(x[i, 0], y[i, 0], name_codes[i],fontdict=None, fontsize=13.5, position= (x[i, 0], y[i, 0]+3.5))

    x[len(x_y_Arxikes_Times), 0] = x_y_Arxikes_Times[0, 0]
    y[len(x_y_Arxikes_Times), 0] = x_y_Arxikes_Times[0, 1]

    #plt.figure(figsize=(11.69, 8.27))

    plt.plot(x, y, '.b-', zorder=0)  # a blue color line
    plt.scatter(x, y, s=150, marker = '.', color='red')


    plt.title('Sxedio Diktiou')  # Title of the figure
    plt.ticklabel_format(useOffset=False, style='plain')
    plt.savefig("sxedio_diktiou.pdf", dpi=200)
    plt.show()

    return 0

def print_u_to_pdf(u_, all_data_name):

    pdf.add_page()
    pdf.set_font("Helvetica", style= 'u', size = 11.5)
    pdf.cell(0, 10, txt = 'Ypoloipa (Gonies se cc kai Apostasis se mm)', border=0, ln =2 , align = 'L')
    pdf.set_font("Helvetica", size= 11)

    for i in range(len(u_)):

        if all_data_name[i][2] != '0':
            text = str(str(all_data_name[i][0]) + ' - ' + str(all_data_name[i][1]) + ' - ' + str(all_data_name[i][2]) + '  = ' + str(round(u_[i][0], 1)))
            pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')

        else:
            text = str(str(all_data_name[i][0]) + ' - ' + str(all_data_name[i][1]) + '  = ' + str(round(u_[i][0]*1000, 1)))
            pdf.cell(0, 6, txt=text, border=0, ln=2, align='L')


    return 0


if __name__ == '__main__':

    data_file_name = "C:\\Users\\k280\\OneDrive\\Files\\Projectakia\\Geodesy_Projects\\Dedomena\\Orizontio_Diktio\\data_gon_dist_Ask.txt"

    # Apothikeusi se arxeio pdf
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", size = 16)
    pdf.cell(0, 10, txt = 'Apotelsmta Synorthosis Orizontiou Diktiou', border=1, ln =2 , align = 'C')
    pdf.set_font("Helvetica", size= 11)

    # input raw data from txt file
    raw_data = input_data(data_file_name)
    n = len(raw_data)
    r_cc = 636620


    # define arrays for data
    temp_name = []
    gon_data = np.zeros((n, 1))
    gon_data_name = []
    s_data = np.zeros((n, 1))
    s_data_name = []
    all_data = np.zeros((n, 1))
    all_data_name = []
    name_codes = []

    # stahera x,y kai gonia
    global staheri_gonia
    global stahero_x
    global stahero_y

    org_data(raw_data, temp_name, gon_data, s_data, n, all_data, all_data_name, name_codes)
    gon_data = np.trim_zeros(gon_data)
    s_data = np.trim_zeros(s_data)
    del temp_name


    mikoi_t0_egsa87(s_data, stahero_x) # anagogi mikwn sto esga87

    # dilosi staheris gonias kai simiou
    staheri_gonia_name =  [name_codes[0], name_codes[1]]
    stahero_simeio_name = name_codes[0]

    # sfalmata goniako kai grammiko kai authereta to s_0
    s_0 = 1
    s_g = 20 # cc
    s_s = 0.002 # meters


    # least squares solve
    k = len(np.unique(name_codes))  # number of korifes (or input from user)
    d = 3
    m = 2*k - d

    # arrays for A*x = dl + u solve
    P = np.zeros((n, n))
    A = np.zeros((n, m))
    L = np.zeros((n, 1))
    dl = np.zeros((n, 1))
    errors = np.zeros((k, 2))


    # generation of arrays from data
    create_P(P, s_g, s_s, s_0, n, all_data_name)


    # ypologismos goniwn dieuthinis a me to themeliodes
    a_arxikes = np.zeros((len(name_codes), 1))
    a_arxikes_name = []

    cal_a_Arxikes_Times(gon_data, gon_data_name, name_codes, a_arxikes, staheri_gonia, staheri_gonia_name, a_arxikes_name)
    #print(a_arxikes)
    #print(a_arxikes_name)


    # ypologismos mhkwn s me nomo sinimitonwn
    s_arxikes = np.zeros((len(name_codes), 1))
    s_arxikes_name = []

    calc_s_Arxikes_Times(s_data, s_data_name, name_codes, s_arxikes, s_arxikes_name)

    # x, y prosorina-Arxika
    x_y_Arxikes_Times = np.zeros((k, 2))
    x_y_Arxikes_Times_name = []

    calc_x_y_Arxikes_Times(a_arxikes, name_codes, stahero_simeio_name, stahero_x, stahero_y, x_y_Arxikes_Times, x_y_Arxikes_Times_name)

    # Elaxistrotetragoniki epilysi me epanali3eis (to sistima den einai gramiko)
    x_y = np.zeros((k, 2))

    for j in range(1): # den exei noima na kanei panw apo mia den allazoun ta telika noumera

        # Ypologismos pinakwn dl kai A 3ana
        # Dimiourgeia pinaka dl kai A mazi
        calc_dl_and_A(x_y_Arxikes_Times, x_y_Arxikes_Times_name, dl, all_data, all_data_name, A, name_codes,staheri_gonia_name, staheri_gonia)

        N = np.transpose(A) @ P @ A
        u = np.transpose(A) @ P @ dl
        x = np.linalg.inv(N) @ u
        u_ = A@x - dl
        s_0_ = np.sqrt( ( np.transpose(u_)@P@u_ ) / ( n - m ) )
        Vx = (s_0_**2)*np.linalg.inv(N)


        # ypologismos kainouriown x, y
        calc_new_x_y(x, staheri_gonia, x_y, x_y_Arxikes_Times, x_y_Arxikes_Times_name)

        # Ypologismos efalmatwn
        calc_errors(Vx, errors, staheri_gonia, k)

        save_to_txt(x_y_Arxikes_Times)



    print_apotelesmta(x_y_Arxikes_Times, x_y_Arxikes_Times_name, errors)

    print_u_to_pdf(u_, all_data_name)

    plot_data()


    pdf.output("Apotelesmta_Analytika.pdf")

    #np.set_printoptions(suppress=True)
    #np.set_printoptions(linewidth=np.inf)
    #print(P)



    
