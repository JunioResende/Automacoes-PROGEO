import pyautogui
from time import sleep

# Variaveis legendas e estatisticas
Argila_1 = "Acima de 600,00 -- (11,3ha - 1,16%)"
Argila_2 = "500,00 - 600,00 -- (370,49ha - 37,98%)"
Argila_3 = "450,00 - 500,00 -- (269,19ha - 27,6%)"
Argila_4 = "400,00 - 450,00 -- (153,68ha - 15,75%)"
Argila_5 = "350,00 - 400,00 -- (82,19ha - 8,43%)"
Argila_6 = "300,00 - 350,00 -- (24,78ha - 2,54%)"
Argila_7 = "250,00 - 300,00 -- (15,54ha - 1,59%)"
Argila_8 = "220,00 - 250,00 -- (8,41ha - 0,86%)"
Argila_9 = "180,00 - 220,00 -- (11,09ha - 1,14%)"
Argila_10 = "120,00 - 180,00 -- (15,27ha - 1,57%)"
Argila_11 = "Abaixo de 120,00 -- (13,54ha - 1,39%)"
Areia_1 = "Acima de 800,00 -- (21,38ha - 2,19%)"
Areia_2 = "700,00 - 800,00 -- (26,95ha - 2,76%)"
Areia_3 = "600,00 - 700,00 -- (40,37ha - 4,14%)"
Areia_4 = "550,00 - 600,00 -- (82,28ha - 8,43%)"
Areia_5 = "500,00 - 550,00 -- (153,89ha - 15,78%)"
Areia_6 = "450,00 - 500,00 -- (269,43ha - 27,62%)"
Areia_7 = "400,00 - 450,00 -- (266,5ha - 27,32%)"
Areia_8 = "350,00 - 400,00 -- (103,45ha - 10,61%)"
Areia_9 = "Abaixo de 350,00 -- (11,23ha - 1,15%)"
Silte_1 = "Acima de 250,00 -- (0ha - 0%)"
Silte_2 = "200,00 - 250,00  -- (0ha - 0%)"
Silte_3 = "150,00 - 200,00 -- (0ha - 0%)"
Silte_4 = "100,00 - 150,00 -- (0ha - 0%)"
Silte_5 = "50,00 - 100,00 -- (975,48ha - 100%)"
Silte_6 = "Abaixo de 50,00 -- (0ha - 0%)"
Mat_Or_1 = "Acima de 38,00 -- Alto  (100,2ha - 10,27%)"
Mat_Or_2 = "35,00 - 38,00 -- Medio Alto  (130,84ha - 13,41%)"
Mat_Or_3 = "33,00 - 35,00 -- Medio  (131,66ha - 13,5%)"
Mat_Or_4 = "28,00 - 33,00 -- Medio  (341,22ha - 34,98%)"
Mat_Or_5 = "25,00 - 28,00 -- Medio Baixo  (129,14ha - 13,24%)"
Mat_Or_6 = "22,00 - 25,00 -- Baixo  (63,28ha - 6,49%)"
Mat_Or_7 = "20,00 - 22,00 -- Baixo  (23,16ha - 2,37%)"
Mat_Or_8 = "17,00 - 20,00 -- Muito Baixo  (22,9ha - 2,35%)"
Mat_Or_9 = "Abaixo de 17,00 -- Muito Baixo  (33,08ha - 3,39%)"
Carb_Or_1 = "Acima de 20,00 -- Muito Alto  (262,8ha - 26,94%)"
Carb_Or_2 = "18,00 - 20,00 -- Alto  (236,75ha - 24,27%)"
Carb_Or_3 = "16,00 - 18,00 -- Medio Alto  (226,51ha - 23,22%)"
Carb_Or_4 = "14,00 - 16,00 -- Medio  (130,55ha - 13,38%)"
Carb_Or_5 = "12,00 - 14,00 -- Baixo  (56,8ha - 5,82%)"
Carb_Or_6 = "Abaixo de 12,00 -- Muito Baixo  (62,06ha - 6,36%)"
CTC_1 = "Acima de 9,00 -- Muito Bom  (721,05ha - 73,92%)"
CTC_2 = "8,00 - 9,00 -- Muito Bom  (152,61ha - 15,64%)"
CTC_3 = "7,00 - 8,00 -- Bom  (60,42ha - 6,19%)"
CTC_4 = "6,00 - 7,00 --Bom  (16,84ha - 1,73%)"
CTC_5 = "5,00 - 6,00 -- Medio  (10,39ha - 1,07%)"
CTC_6 = "4,00 - 5,00 -- Baixo  (13,3ha - 1,36%)"
CTC_7 = "3,00 - 4,00 -- Muito Baixo  (0,88ha - 0,09%)"
CTC_8 = "1,60 - 3,00 -- Muito Baixo  (0ha - 0%)"
CTC_9 = "Abaixo de 1,60 -- Muito Baixo  (0ha - 0%)"
pH_1 = "Acima de 6,40 -- Muito Alto  (0ha - 0%)"
pH_2 = "6,00 - 6,40 -- Alto  (0ha - 0%)"
pH_3 = "5,40 - 6,00 -- Ideal  (122,68ha - 12,58%)"
pH_4 = "5,00 - 5,40 -- Medio  (467,77ha - 47,95%)"
pH_5 = "4,50 - 5,00 -- Baixo  (383,52ha - 39,32%)"
pH_6 = "Abaixo de 4,50 -- Muito Baixo  (1,51ha - 0,15%)"
Sat_B_1 = "Acima de 60,00 -- Alto  (270,46ha - 27,73%)"
Sat_B_2 = "55,00 - 60,00 -- Medio Alto  (163,29ha - 16,74%)"
Sat_B_3 = "50,00 - 55,00 -- Medio  (169,57ha - 17,38%)"
Sat_B_4 = "45,00 - 50,00 -- Medio  (164,98ha - 16,91%)"
Sat_B_5 = "40,00 - 45,00 -- Baixo  (133,24ha - 13,66%)"
Sat_B_6 = "35,00 - 40,00 -- Baixo  (57,92ha - 5,94%)"
Sat_B_7 = "30,00 - 35,00 -- Muito Baixo  (12,46ha - 1,28%)"
Sat_B_8 = "25,00 - 30,00 -- Muito Baixo  (3,02ha - 0,31%)"
Sat_B_9 = "Abaixo de 25,00 -- Muito Baixo  (0,54ha - 0,06%)"
Cal_1 = "Acima de 5,00 -- Muito Alto  (39,2ha - 4,02%)"
Cal_2 = "4,00 - 5,00 -- Alto  (117,95ha - 12,09%)"
Cal_3 = "3,50 - 4,00 --  Medio  (126,11ha - 12,93%)"
Cal_4 = "3,00 - 3,50 -- Medio  (213,03ha - 21,84%)"
Cal_5 = "2,50 - 3,00 -- Medio  (242,66ha - 24,88%)"
Cal_6 = "2,00 - 2,50 -- Baixo  (177,75ha - 18,22%)"
Cal_7 = "1,50 - 2,00 -- Baixo  (51,06ha - 5,23%)"
Cal_8 = "1,00 - 1,50 -- Muito Baixo  (7,71ha - 0,79%)"
Cal_9 = "0,40 - 1,00 -- Muito Baixo  (0ha - 0%)"
Cal_10 = "Abaixo de 0,40 -- Muito Baixo  (0ha - 0%)"
Mg_1 = "Acima de 5,00 -- Alto  (0ha - 0%)"
Mg_2 = "4,50 - 5,00 -- Alto  (1,56ha - 0,16%)"
Mg_3 = "4,00 - 4,50 -- Alto  (0ha - 0%)"
Mg_4 = "3,50 - 4,00 -- Alto  (0ha - 0%)"
Mg_5 = "3,00 - 3,50 -- Alto  (5,86ha - 0,6%)"
Mg_6 = "2,50 - 3,00 -- Alto  (12,26ha - 1,26%)"
Mg_7 = "2,00 - 2,50 -- Alto  (53,84ha - 5,52%)"
Mg_8 = "1,50 - 2,00 -- Alto  (166,74ha - 17,09%)"
Mg_9 = "1,00 - 1,50 -- Medio  (333,43ha - 34,18%)"
Mg_10 = "0,90 - 1,00 -- Medio  (337,48ha - 34,6%)"
Mg_11 = "0,50 - 0,90 -- Baixo  (64,32ha - 6,59%)"
Mg_12 = "Abaixo de 0,50 -- Baixo  (0ha - 0%)"
Ca_mais_Mg_1 = "Acima de 7,00 -- Muito Alto  (66,06ha - 6,77%)"
Ca_mais_Mg_2 = "5,55 - 7,00 -- Alto  (188,77ha - 19,35%)"
Ca_mais_Mg_3 = "5,00 - 5,55 -- Medio Alto  (135,14ha - 13,85%)"
Ca_mais_Mg_4 = "4,70 - 5,00 -- Baixo  (87,44ha - 8,96%)"
Ca_mais_Mg_5 = "4,30 - 4,70 -- Baixo  (116,91ha - 11,98%)"
Ca_mais_Mg_6 = "1,70 - 4,30 -- Muito Baixo  (381,16ha - 39,07%)"
Al_1 = "0,60 - 1,00 -- Alto  (5,84ha - 0,6%)"
Al_2 = "0,50 - 0,60 -- Adequado  (2,83ha - 0,29%)"
Al_3 = "0,20 - 0,50 -- Medio Bom  (53,98ha - 5,53%)"
Al_4 = "0,00 - 0,20 -- Baixo  (912,83ha - 93,58%)"
HAL_1 = "6,00 - 7,00 -- Muito Alto  (73,79ha - 7,56%)"
HAL_2 = "5,00 - 6,00 -- Alto  (216,86ha - 22,23%)"
HAL_3 = "4,00 - 5,00 -- Medio  (343,09ha - 35,17%)"
HAL_4 = "3,00 - 4,00 -- Medio  (241,19ha - 24,73%)"
HAL_5 = "2,00 - 3,00 -- Baixo  (78,48ha - 8,05%)"
HAL_6 = "1,00 - 2,00 -- Muito Baixo  (22,07ha - 2,26%)"
Sat_Al_1 = "Acima de 6,00 -- Muito Alto  (45,98ha - 4,71%)"
Sat_Al_2 = "4,00 - 6,00 -- Alto  (39,43ha - 4,04%)"
Sat_Al_3 = "2,00 - 4,00 -- Medio  (165,74ha - 16,99%)"
Sat_Al_4 = "Abaixo de 2,00 -- Baixo  (724,32ha - 74,25%)"
K_ppm_1 = "Acima de 160,00 -- Muito Alto  (355,78ha - 36,47%)"
K_ppm_2 = "140,00 -  160,00 -- Muito Alto  (184,34ha - 18,9%)"
K_ppm_3 = "120,00 - 140,00 -- Muito Alto  (140,4ha - 14,39%)"
K_ppm_4 = "100,00 - 120,00 -- Alto  (76,34ha - 7,83%)"
K_ppm_5 = "90,00 - 100,00 -- Alto  (32,89ha - 3,37%)"
K_ppm_6 = "80,00 - 90,00 -- Adequado  (25,34ha - 2,6%)"
K_ppm_7 = "75,00 - 80,00 -- Adequado  (11,15ha - 1,14%)"
K_ppm_8 = "70,00 - 75,00 -- Adequado  (11,28ha - 1,16%)"
K_ppm_9 = "65,00 - 70,00 -- Medio  (11,17ha - 1,15%)"
K_ppm_10 = "60,00 - 65,00 -- Medio  (10,93ha - 1,12%)"
K_ppm_11 = "55,00 - 60,00 --  Medio  (9,4ha - 0,96%)"
K_ppm_12 = "50,00 - 55,00 -- Medio  (8,18ha - 0,84%)"
K_ppm_13 = "45,00 - 50,00 -- Medio  (8,1ha - 0,83%)"
K_ppm_14 = "40,00 - 45,00 -- Medio Baixo  (10,4ha - 1,07%)"
K_ppm_15 = "35,00 - 40,00 -- Medio Baixo  (10,99ha - 1,13%)"
K_ppm_16 = "30,00 - 35,00 -- Medio Baixo  (14,17ha - 1,45%)"
K_ppm_17 = "25,00 - 30,00 -- Baixo  (13,51ha - 1,38%)"
K_ppm_18 = "20,00 - 25,00 -- Baixo  (20,04ha - 2,05%)"
K_ppm_19 = "15,00 - 20,00 -- Muito Baixo  (18,87ha - 1,93%)"
K_ppm_20 = "Abaixo de 15,00 -- Muito Baixo  (2,06ha - 0,21%)"
P_Meh_1 = "Acima de 14,00 -- Bom  (145,84ha - 14,95%)"
P_Meh_2 = "10,00 - 14,00 -- Medio  (134,2ha - 13,76%)"
P_Meh_3 = "5,00 - 10,00 -- Baixo  (394,19ha - 40,41%)"
P_Meh_4 = "Abaixo de 5,00 -- Muito Baixo  (301,25ha - 30,88%)"
K_1 = "0,28 - 0,44 -- Alto  (724,99ha - 74,32%)"
K_2 = "0,24 - 0,28 -- Alto  (53,22ha - 5,46%)"
K_3 = "0,21 - 0,24 -- Medio Alto  (32,62ha - 3,34%)"
K_4 = "0,17 - 0,21 -- Medio  (34,84ha - 3,57%)"
K_5 = "0,14 - 0,17 -- Medio Baixo  (23,74ha - 2,43%)"
K_6 = "0,13 - 0,14 -- Baixo  (6,4ha - 0,66%)"
K_7 = "0,03 - 0,13 -- Baixo  (99,67ha - 10,22%)"
S_1 = "10,00 - 18,00 -- Muito Alto  (564,15ha - 57,83%)"
S_2 = "9,00 - 10,00 -- Alto  (65,67ha - 6,73%)"
S_3 = "4,90 - 9,00 -- Medio  (246,79ha - 25,3%)"
S_4 = "2,50 - 4,90 -- Baixo  (94,97ha - 9,74%)"
S_5 = "1,00 - 2,50 -- Muito Baixo  (3,89ha - 0,4%)"
B_1 = "Acima de 0,90 -- Muito Alto  (0ha - 0%)"
B_2 = "0,60 - 0,90 -- Alto  (0ha - 0%)"
B_3 = "0,35 - 0,60 -- Medio  (197,89ha - 20,29%)"
B_4 = "0,15 - 0,35 -- Baixo  (777,58ha - 79,71%)"
B_5 = "Abaixo de 0,15 -- Muito Baixo  (0ha - 0%)"
Ca_CTC_1 = "Acima de 70,00 -- Muito Alto  (0ha - 0%)"
Ca_CTC_2 = "60,00 - 70,00 -- Ideal  (0ha - 0%)"
Ca_CTC_3 = "50,00 - 60,00 -- Ideal  (6,78ha - 0,7%)"
Ca_CTC_4 = "40,00 - 50,00 -- Bom  (118,09ha - 12,11%)"
Ca_CTC_5 = "30,00 - 40,00 -- Medio  (479,25ha - 49,13%)"
Ca_CTC_6 = "25,00 - 30,00 -- Baixo  (266,76ha - 27,35%)"
Ca_CTC_7 = "20,00 - 25,00 -- Baixo  (93,64ha - 9,6%)"
Ca_CTC_8 = "15,00 - 20,00 -- Muito Baixo  (9,89ha - 1,01%)"
Ca_CTC_9 = "Abaixo de 15,00 -- Muito Baixo  (1,06ha - 0,11%)"
Mg_CTC_1 = "Acima de 20,00 -- Muito Alto  (290,41ha - 29,77%)"
Mg_CTC_2 = "15,00 - 20,00 -- Alto  (346,09ha - 35,48%)"
Mg_CTC_3 = "10,00 - 15,00 -- Medio  (305,19ha - 31,29%)"
Mg_CTC_4 = "7,00 - 10,00 -- Baixo  (31,93ha - 3,27%)"
Mg_CTC_5 = "Abaixo 7,00 -- Baixo  (1,85ha - 0,19%)"
K_CTC_1 = "Acima de 6,00 -- Muito Alto  (11,23ha - 1,15%)"
K_CTC_2 = "5,00 - 6,00 -- Alto  (74,66ha - 7,65%)"
K_CTC_3 = "3,00 - 5,00 -- Adequado  (648,89ha - 66,52%)"
K_CTC_4 = "2,00 - 3,00 -- Medio  (118,62ha - 12,16%)"
K_CTC_5 = "1,00 - 2,00 -- Baixo  (68,09ha - 6,98%)"
K_CTC_6 = "Abaixo de 1,00 -- Muito Baixo  (53,98ha - 5,53%)"
HAL_CTC_1 = "Acima de 60,00 -- Muito Alto  (75,38ha - 7,73%)"
HAL_CTC_2 = "40,00 - 60,00 -- Muito Alto  (629,8ha - 64,56%)"
HAL_CTC_3 = "36,00 - 40,00 -- Alto  (100,47ha - 10,3%)"
HAL_CTC_4 = "33,00 - 36,00 -- Medio  (65,09ha - 6,67%)"
HAL_CTC_5 = "25,00 - 33,00 -- Baixo  (87,43ha - 8,96%)"
HAL_CTC_6 = "Abaixo de 25,00 -- Muito Baixo  (17,3ha - 1,77%)"
Ca_Mg_1 = "Acima de 5,00 -- Muito Alto  (0ha - 0%)"
Ca_Mg_2 = "4,00 - 5,00 -- Alto  (0ha - 0%)"
Ca_Mg_3 = "3,00 - 4,00 -- Adequado  (19,95ha - 2,05%)"
Ca_Mg_4 = "2,00 - 3,00 -- Medio  (428,6ha - 43,94%)"
Ca_Mg_5 = "1,10 - 2,00 -- Baixo  (487,8ha - 50,01%)"
Ca_Mg_6 = "Abaixo de 1,10 -- Baixo  (39,13ha - 4,01%)"
Ca_K_1 = "Acima de 15,00 -- Alto  (192,14ha - 19,7%)"
Ca_K_2 = "14,90- 15,00 -- Adequado  (1,98ha - 0,2%)"
Ca_K_3 = "12,00 - 14,90 -- Medio Baixo  (90,3ha - 9,26%)"
Ca_K_4 = "9,00 - 12,00 -- Medio  (194,65ha - 19,95%)"
Ca_K_5 = "7,00 - 9,00 -- Muito Baixo  (275,3ha - 28,22%)"
Ca_K_6 = "Abaixo de 7,00 -- Muito Baixo  (221,1ha - 22,67%)"
Mg_K_1 = "6,00 - 7,00 -- Muito Alto  (288,84ha - 29,61%)"
Mg_K_2 = "5,00 - 6,00 -- Alto Bom  (113,24ha - 11,61%)"
Mg_K_3 = "4,90 - 5,00 -- Adequado  (15,18ha - 1,56%)"
Mg_K_4 = "3,00 - 4,90 -- Medio  (416,64ha - 42,71%)"
Mg_K_5 = "2,00 - 3,00 -- Baixo  (119,19ha - 12,22%)"
Mg_K_6 = "1,00 - 2,00 -- Muito Baixo  (19,09ha - 1,96%)"
Mg_K_7 = "0,50 - 1,00 -- Muito Baixo  (3,31ha - 0,34%)"
Cu_1 = "3,00 - 10,0 -- Alto  (262,51ha - 26,91%)"
Cu_2 = "1,50 - 3,00 -- Medio  (505,51ha - 51,82%)"
Cu_3 = "0,60 - 1,50 -- Baixo  (190,89ha - 19,57%)"
Cu_4 = "0,30 - 0,60 -- Baixo  (16,56ha - 1,7%)"
Fe_1 = "Acima de 220,00 -- Muito Alto  (20,09ha - 2,06%)"
Fe_2 = "83,00 - 220,00 -- Alto  (221,89ha - 22,75%)"
Fe_3 = "31,00 - 83,00 -- Medio  (603,74ha - 61,89%)"
Fe_4 = "20,00 - 31,00 -- Baixo  (113,6ha - 11,65%)"
Fe_5 = "Abaixo de 20,00 -- Muito Baixo  (16,15ha - 1,66%)"
Mn_1 = "Acima de 130,00 -- Alto  (0ha - 0%)"
Mn_2 = "12,00 - 130,00 -- Medio  (449,68ha - 46,1%)"
Mn_3 = "6,00 - 12,00 -- Baixo  (506,38ha - 51,91%)"
Mn_4 = "Abaixo de 6,00 -- Muito Baixo  (19,43ha - 1,99%)"
Zn_1 = "Acima de 5,00 -- Muito Alto  (715,25ha - 73,32%)"
Zn_2 = "1,60 - 5,00 -- Alto  (215,3ha - 22,07%)"
Zn_3 = "1,00 - 1,60 -- Medio  (18,52ha - 1,9%)"
Zn_4 = "Abaixo de 1,00 -- Baixo  (26,41ha - 2,71%)"
Na_1 = "Acima de 6,00 -- Muito Alto  (30,18ha - 3,09%)"
Na_2 = "4,44 - 6,00 -- Alto  (161,69ha - 16,58%)"
Na_3 = "2,95 - 4,44 -- Medio Alto  (583,83ha - 59,85%)"
Na_4 = "2,55 - 2,95 -- Medio  (113,3ha - 11,61%)"
Na_5 = "2,22 - 2,55 -- Medio Baixo  (48,29ha - 4,95%)"
Na_6 = "1,91 - 2,22 -- Baixo  (23,25ha - 2,38%)"
Na_7 = "Abaixo de 1,91 -- Muito Baixo  (14,94ha - 1,53%)"

min_3 = "Minimo: 98,22 g/dm³"
max_3 = "Maximo: 610,53 g/dm³"
med_3 = "Medio: 367,67 g/dm³"
total_3 = "Total: 23530,72 g/dm³"
count_3 = "Contagem: 64 "
min_4 = "Minimo: 339,35 g/dm³"
max_4 = "Maximo: 836,75 g/dm³"
med_4 = "Medio: 517,99 g/dm³"
total_4 = "Total: 32633,55 g/dm³"
count_4 = "Contagem: 63 "
min_5 = "Minimo: 50 g/dm³"
max_5 = "Maximo: 50 g/dm³"
med_5 = "Medio: 50 g/dm³"
total_5 = "Total: 50 g/dm³"
count_5 = "Contagem: 1 "
min_6 = "Minimo: 13,99 g/dm³"
max_6 = "Maximo: 43,49 g/dm³"
med_6 = "Medio: 29,58 g/dm³"
total_6 = "Total: 3283,68 g/dm³"
count_6 = "Contagem: 111 "
min_7 = "Minimo: 9,25 g/dm³"
max_7 = "Maximo: 23,19 g/dm³"
med_7 = "Medio: 16,62 g/dm³"
total_7 = "Total: 1329,83 g/dm³"
count_7 = "Contagem: 80 "
min_8 = "Minimo: 3,87 cmol/dm³"
max_8 = "Maximo: 10,54 cmol/dm³"
med_8 = "Medio: 7,7 cmol/dm³"
total_8 = "Total: 431,15 cmol/dm³"
count_8 = "Contagem: 56 "
min_9 = "Minimo: 4,45 "
max_9 = "Maximo: 5,53 "
med_9 = "Medio: 5,13 "
total_9 = "Total: 277,08 "
count_9 = "Contagem: 54 "
min_10 = "Minimo: 23,7 %"
max_10 = "Maximo: 67,94 %"
med_10 = "Medio: 46,06 %"
total_10 = "Total: 6541,17 %"
count_10 = "Contagem: 142 "
min_11 = "Minimo: 1,35 cmol/dm³"
max_11 = "Maximo: 6,33 cmol/dm³"
med_11 = "Medio: 3,17 cmol/dm³"
total_11 = "Total: 425,09 cmol/dm³"
count_11 = "Contagem: 134 "
min_12 = "Minimo: 0,49 cmol/dm³"
max_12 = "Maximo: 4,55 cmol/dm³"
med_12 = "Medio: 1,89 cmol/dm³"
total_12 = "Total: 225,33 cmol/dm³"
count_12 = "Contagem: 119 "
min_13 = "Minimo: 3,54 cmol/dm³"
max_13 = "Maximo: 9,12 cmol/dm³"
med_13 = "Medio: 5,34 cmol/dm³"
total_13 = "Total: 561 cmol/dm³"
count_13 = "Contagem: 105 "
min_14 = "Minimo: 0,07 cmol/dm³"
max_14 = "Maximo: 0,73 cmol/dm³"
med_14 = "Medio: 0,4 cmol/dm³"
total_14 = "Total: 9,14 cmol/dm³"
count_14 = "Contagem: 23 "
min_15 = "Minimo: 1,7 cmol/dm³"
max_15 = "Maximo: 6,55 cmol/dm³"
med_15 = "Medio: 4,29 cmol/dm³"
total_15 = "Total: 411,94 cmol/dm³"
count_15 = "Contagem: 96 "
min_16 = "Minimo: 0,84 %"
max_16 = "Maximo: 11,47 %"
med_16 = "Medio: 4,6 %"
total_16 = "Total: 197,78 %"
count_16 = "Contagem: 43 "
min_17 = "Minimo: 13,74 mg/dm³"
max_17 = "Maximo: 194,91 mg/dm³"
med_17 = "Medio: 87,67 mg/dm³"
total_17 = "Total: 16833,58 mg/dm³"
count_17 = "Contagem: 192 "
min_18 = "Minimo: 3 mg/dm³"
max_18 = "Maximo: 24,31 mg/dm³"
med_18 = "Medio: 9,63 mg/dm³"
total_18 = "Total: 616,51 mg/dm³"
count_18 = "Contagem: 64 "
min_19 = "Minimo: 0,08 cmol/dm³"
max_19 = "Maximo: 0,37 cmol/dm³"
med_19 = "Medio: 0,2 cmol/dm³"
total_19 = "Total: 12,61 cmol/dm³"
count_19 = "Contagem: 63 "
min_20 = "Minimo: 2,3 mg/dm³"
max_20 = "Maximo: 13,09 mg/dm³"
med_20 = "Medio: 7,63 mg/dm³"
total_20 = "Total: 412,14 mg/dm³"
count_20 = "Contagem: 54 "
min_21 = "Minimo: 0,29 mg/dm³"
max_21 = "Maximo: 0,39 mg/dm³"
med_21 = "Medio: 0,36 mg/dm³"
total_21 = "Total: 7,18 mg/dm³"
count_21 = "Contagem: 20 "
min_22 = "Minimo: 13,93 %"
max_22 = "Maximo: 52,75 %"
med_22 = "Medio: 30,37 %"
total_22 = "Total: 2794,13 %"
count_22 = "Contagem: 92 "
min_23 = "Minimo: 6,46 %"
max_23 = "Maximo: 24,79 %"
med_23 = "Medio: 14,69 %"
total_23 = "Total: 852,19 %"
count_23 = "Contagem: 58 "
min_24 = "Minimo: 0,73 %"
max_24 = "Maximo: 6,47 %"
med_24 = "Medio: 3,72 %"
total_24 = "Total: 223,09 %"
count_24 = "Contagem: 60 "
min_25 = "Minimo: 20,9 %"
max_25 = "Maximo: 64,95 %"
med_25 = "Medio: 38,56 %"
total_25 = "Total: 4048,87 %"
count_25 = "Contagem: 105 "
min_26 = "Minimo: 1,05 "
max_26 = "Maximo: 3,29 "
med_26 = "Medio: 2,16 "
total_26 = "Total: 56,1 "
count_26 = "Contagem: 26 "
min_27 = "Minimo: 4,53 "
max_27 = "Maximo: 29,9 "
med_27 = "Medio: 11,57 "
total_27 = "Total: 913,96 "
count_27 = "Contagem: 79 "
min_28 = "Minimo: 0,6 "
max_28 = "Maximo: 6,46 "
med_28 = "Medio: 4,08 "
total_28 = "Total: 305,95 "
count_28 = "Contagem: 75 "
min_29 = "Minimo: 0,4 mg/dm³"
max_29 = "Maximo: 4,7 mg/dm³"
med_29 = "Medio: 2,13 mg/dm³"
total_29 = "Total: 78,96 mg/dm³"
count_29 = "Contagem: 37 "
min_30 = "Minimo: 9,55 mg/dm³"
max_30 = "Maximo: 299,56 mg/dm³"
med_30 = "Medio: 78,82 mg/dm³"
total_30 = "Total: 3783,19 mg/dm³"
count_30 = "Contagem: 48 "
min_31 = "Minimo: 5,18 mg/dm³"
max_31 = "Maximo: 17,88 mg/dm³"
med_31 = "Medio: 9,19 mg/dm³"
total_31 = "Total: 229,72 mg/dm³"
count_31 = "Contagem: 25 "
min_32 = "Minimo: 0,65 mg/dm³"
max_32 = "Maximo: 9,68 mg/dm³"
med_32 = "Medio: 3,61 mg/dm³"
total_32 = "Total: 93,96 mg/dm³"
count_32 = "Contagem: 26 "
min_33 = "Minimo: 1,66 mg/dm³"
max_33 = "Maximo: 7,02 mg/dm³"
med_33 = "Medio: 3,45 mg/dm³"
total_33 = "Total: 344,65 mg/dm³"
count_33 = "Contagem: 100 "


# Variaveis posicao da legenda
# argila
argila_Position_X = "19,6992 cm"
argila_Position_Y = "8,7221 cm"
argila_Size_Width = "8,3742 cm"
argila_Size_Height = "6,2709 cm"

# areia
areia_Position_X = "19,6992 cm"
areia_Position_Y = "10,111 cm"
areia_Size_Width = "7,7119 cm"
areia_Size_Height = "4,8891 cm"

# silte
silte_Position_X = "19,6992 cm"
silte_Position_Y = "11,7065 cm"
silte_Size_Width = "8,0845 cm"
silte_Size_Height = "3,2936 cm"

# materia_or
materia_or_Position_X = "19,6992 cm"
materia_or_Position_Y = "10,6216 cm"
materia_or_Size_Width = "8,9006 cm"
materia_or_Size_Height = "4,3785 cm"

# carb_or
carb_or_Position_X = "19,6992 cm"
carb_or_Position_Y = "12,114 cm"
carb_or_Size_Width = "8,9006 cm"
carb_or_Size_Height = "2,8861 cm"

# ctc
ctc_Position_X = "19,6992 cm"
ctc_Position_Y = "10,3847 cm"
ctc_Size_Width = "8,9006 cm"
ctc_Size_Height = "4,6154 cm"

# ph
ph_Position_X = "19,6992 cm"
ph_Position_Y = "11,9012 cm"
ph_Size_Width = "8,9006 cm"
ph_Size_Height = "3,0989 cm"

# sat_bas
sat_bas_Position_X = "19,6992 cm"
sat_bas_Position_Y = "10,3055 cm"
sat_bas_Size_Width = "8,9005 cm"
sat_bas_Size_Height = "4,6946 cm"

# ca
ca_Position_X = "19,6992 cm"
ca_Position_Y = "9,7606 cm"
ca_Size_Width = "8,6809 cm"
ca_Size_Height = "5,2395 cm"

# mg
mg_Position_X = "19,6992 cm"
mg_Position_Y = "7,684 cm"
mg_Size_Width = "8,6775 cm"
mg_Size_Height = "7,2748 cm"

# ca_mais_mg
ca_mais_mg_Position_X = "19,6992 cm"
ca_mais_mg_Position_Y = "11,9474 cm"
ca_mais_mg_Size_Width = "8,5324 cm"
ca_mais_mg_Size_Height = "3,0527 cm"

# al
al_Position_X = "19,6992 cm"
al_Position_Y = "12,9983 cm"
al_Size_Width = "7,9506 cm"
al_Size_Height = "2,0018 cm"

# hal
hal_Position_X = "19,6992 cm"
hal_Position_Y = "11,9485 cm"
hal_Size_Width = "8,4465 cm"
hal_Size_Height = "3,0516 cm"

# sat_al
sat_al_Position_X = "19,6992 cm"
sat_al_Position_Y = "12,9952 cm"
sat_al_Size_Width = "8,7193 cm"
sat_al_Size_Height = "2,0049 cm"

# k_ppm
k_ppm_Position_X = "19,6992 cm"
k_ppm_Position_Y = "5,5674 cm"
k_ppm_Size_Width = "8,3328 cm"
k_ppm_Size_Height = "9,4327 cm"

# p_meh
p_meh_Position_X = "19,6992 cm"
p_meh_Position_Y = "13,1809 cm"
p_meh_Size_Width = "8,3328 cm"
p_meh_Size_Height = "1,8192 cm"

# k
k_Position_X = "19,6992 cm"
k_Position_Y = "11,7568 cm"
k_Size_Width = "7,3742 cm"
k_Size_Height = "3,2433 cm"

# s
s_Position_X = "19,6992 cm"
s_Position_Y = "12,7081 cm"
s_Size_Width = "7,5701 cm"
s_Size_Height = "2,292 cm"

# b
b_Position_X = "19,6992 cm"
b_Position_Y = "12,7081 cm"
b_Size_Width = "6,7675 cm"
b_Size_Height = "2,2898 cm"

# ca_ctc
ca_ctc_Position_X = "19,6992 cm"
ca_ctc_Position_Y = "10,8021 cm"
ca_ctc_Size_Width = "7,55 cm"
ca_ctc_Size_Height = "4,198 cm"

# mg_ctc
mg_ctc_Position_X = "19,6992 cm"
mg_ctc_Position_Y = "12,6935 cm"
mg_ctc_Size_Width = "7,55 cm"
mg_ctc_Size_Height = "2,3066 cm"

# k_ctc
k_ctc_Position_X = "19,6992 cm"
k_ctc_Position_Y = "12,2206 cm"
k_ctc_Size_Width = "7,7459 cm"
k_ctc_Size_Height = "2,7795 cm"

# hal_ctc
hal_ctc_Position_X = "19,6992 cm"
hal_ctc_Position_Y = "12,2206 cm"
hal_ctc_Size_Width = "7,7658 cm"
hal_ctc_Size_Height = "2,8743 cm"

# ca_mg
ca_mg_Position_X = "19,6992 cm"
ca_mg_Position_Y = "12,2206 cm"
ca_mg_Size_Width = "7,2187 cm"
ca_mg_Size_Height = "2,8743 cm"

# cak
cak_Position_X = "19,6992 cm"
cak_Position_Y = "12,2206 cm"
cak_Size_Width = "8,1571 cm"
cak_Size_Height = "2,8743 cm"

# mgk
mgk_Position_X = "19,6992 cm"
mgk_Position_Y = "11,6296 cm"
mgk_Size_Width = "7,3744 cm"
mgk_Size_Height = "3,3705 cm"

# cu
cu_Position_X = "19,6992 cm"
cu_Position_Y = "13,1839 cm"
cu_Size_Width = "6,7876 cm"
cu_Size_Height = "1,8162 cm"

# fe
fe_Position_X = "19,6992 cm"
fe_Position_Y = "12,6225 cm"
fe_Size_Width = "8,3328 cm"
fe_Size_Height = "2,3776 cm"

# mn
mn_Position_X = "19,6992 cm"
mn_Position_Y = "13,1751 cm"
mn_Size_Width = "7,3747 cm"
mn_Size_Height = "1,825 cm"

# zn
zn_Position_X = "19,6992 cm"
zn_Position_Y = "13,1751 cm"
zn_Size_Width = "7,3747 cm"
zn_Size_Height = "1,8814 cm"

# na
na_Position_X = "19,6992 cm"
na_Position_Y = "11,6296 cm"
na_Size_Width = "7,7459 cm"
na_Size_Height = "3,3705 cm"


# Argila
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Argila', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Argila (g/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_3, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_3, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_3, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_3, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_3, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('03', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('11')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
pyautogui.click(647, 406, duration=0.5)
sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
# pyautogui.click(635, 296, duration=0.5)
# sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 10
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 11
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Argila_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Argila_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Argila_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Argila_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Argila_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Argila_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Argila_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Argila_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Argila_9, interval=0.1)
pyautogui.press('enter')
# 10
pyautogui.write(Argila_10, interval=0.1)
pyautogui.press('enter')
# 11
pyautogui.write(Argila_11, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(argila_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(argila_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(argila_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(argila_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('3_Argila', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Areia
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Areia', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Areia (g/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_4, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_4, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_4, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_4, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('04', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
pyautogui.click(647, 406, duration=0.5)
sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
# pyautogui.click(635, 296, duration=0.5)
# sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Areia_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Areia_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Areia_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Areia_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Areia_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Areia_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Areia_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Areia_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Areia_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(areia_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(areia_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(areia_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(areia_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('4_Areia', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Silte
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Silte', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Silte (g/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_5, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_5, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_5, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_5, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_5, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('05', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
sleep(1)
# select green blue scale
pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
# pyautogui.click(635, 296, duration=0.5)
# sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Silte_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Silte_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Silte_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Silte_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Silte_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Silte_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(silte_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(silte_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(silte_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(silte_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('5_Silte', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Materia Organica
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Materia Organica', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Materia Organica (g/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_6, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_6, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_6, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_6, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('06', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Mat_Or_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Mat_Or_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Mat_Or_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Mat_Or_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Mat_Or_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Mat_Or_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Mat_Or_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Mat_Or_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Mat_Or_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(materia_or_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(materia_or_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(materia_or_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(materia_or_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('6_Materia_Organica', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Carbono Organico
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Carbono Organico', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Carbono Organico (g/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_7, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_7, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_7, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_7, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_7, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('07', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Carb_Or_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Carb_Or_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Carb_Or_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Carb_Or_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Carb_Or_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Carb_Or_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(carb_or_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(carb_or_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(carb_or_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(carb_or_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('7_Carbono_Organico', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# CTC Total
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('CTC Total', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('CTC Total (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_8, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_8, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_8, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_8, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_8, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('08', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(CTC_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(CTC_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(CTC_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(CTC_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(CTC_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(CTC_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(CTC_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(CTC_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(CTC_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ctc_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ctc_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ctc_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ctc_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('8_CTC_Total', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# pH Cloreto de Calcio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('pH Cloreto de Calcio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('pH Cloreto de Calcio', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_9, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_9, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_9, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_9, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('09', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(pH_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(pH_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(pH_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(pH_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(pH_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(pH_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ph_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ph_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ph_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ph_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('9_pHCaCl', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Saturacao de Bases
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Saturacao de Bases', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Saturacao de Bases (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_10, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_10, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_10, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_10, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_10, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('10', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Sat_B_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Sat_B_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Sat_B_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Sat_B_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Sat_B_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Sat_B_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Sat_B_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Sat_B_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Sat_B_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_bas_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_bas_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_bas_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_bas_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('10_Saturacao_de_Bases', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Calcio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Calcio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Ca (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_11, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_11, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_11, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_11, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_11, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('11', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('10')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 10
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Cal_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Cal_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Cal_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Cal_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Cal_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Cal_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Cal_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Cal_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Cal_9, interval=0.1)
pyautogui.press('enter')
# 10
pyautogui.write(Cal_10, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('11_Calcio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)

# Magnesio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Magnesio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Mg (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_12, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_12, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_12, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_12, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_12, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('12', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('12')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 10
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 11
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 12
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Mg_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Mg_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Mg_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Mg_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Mg_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Mg_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Mg_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Mg_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Mg_9, interval=0.1)
pyautogui.press('enter')
# 10
pyautogui.write(Mg_10, interval=0.1)
pyautogui.press('enter')
# 11
pyautogui.write(Mg_11, interval=0.1)
pyautogui.press('enter')
# 12
pyautogui.write(Mg_12, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('12_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Calcio mais Magnesio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Calcio mais Magnesio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Ca + Mg (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_13, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_13, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_13, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_13, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_13, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('13', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Ca_mais_Mg_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Ca_mais_Mg_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Ca_mais_Mg_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Ca_mais_Mg_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Ca_mais_Mg_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Ca_mais_Mg_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mais_mg_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mais_mg_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mais_mg_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mais_mg_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('13_Calcio_mais_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Aluminio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Aluminio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Al (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_14, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_14, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_14, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_14, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_14, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('14', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Al_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Al_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Al_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Al_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1016, 351, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(al_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(al_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(al_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(al_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('14_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Hidrogenio mais Aluminio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Hidrogenio mais Aluminio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('H + Al (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_15, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_15, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_15, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_15, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_15, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('15', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(HAL_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(HAL_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(HAL_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(HAL_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(HAL_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(HAL_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1066, 254, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('15_Hidrogenio_mais_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Saturacao por Aluminio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Saturacao por Aluminio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Saturacao por Aluminio (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_16, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_16, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_16, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_16, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_16, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('16', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Sat_Al_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Sat_Al_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Sat_Al_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Sat_Al_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1066, 254, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_al_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_al_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_al_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(sat_al_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('16_Saturacao_por_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Potassio ppm
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Potassio ppm', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('K ppm (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_17, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_17, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_17, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_17, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_17, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('17', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('20')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 10
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 11
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 12
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 13
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 14
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 15
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 16
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 17
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 18
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 19
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 20
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(K_ppm_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(K_ppm_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(K_ppm_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(K_ppm_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(K_ppm_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(K_ppm_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(K_ppm_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(K_ppm_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(K_ppm_9, interval=0.1)
pyautogui.press('enter')
# 10
pyautogui.write(K_ppm_10, interval=0.1)
pyautogui.press('enter')
# 11
pyautogui.write(K_ppm_11, interval=0.1)
pyautogui.press('enter')
# 12
pyautogui.write(K_ppm_12, interval=0.1)
pyautogui.press('enter')
# 13
pyautogui.write(K_ppm_13, interval=0.1)
pyautogui.press('enter')
# 14
pyautogui.write(K_ppm_14, interval=0.1)
pyautogui.press('enter')
# 15
pyautogui.write(K_ppm_15, interval=0.1)
pyautogui.press('enter')
# 16
pyautogui.write(K_ppm_16, interval=0.1)
pyautogui.press('enter')
# 17
pyautogui.write(K_ppm_17, interval=0.1)
pyautogui.press('enter')
# 18
pyautogui.write(K_ppm_18, interval=0.1)
pyautogui.press('enter')
# 19
pyautogui.write(K_ppm_19, interval=0.1)
pyautogui.press('enter')
# 20
pyautogui.write(K_ppm_20, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ppm_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ppm_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ppm_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ppm_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('17_Potassio_ppm', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Fosforo Mehlich
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Fosforo Mehlich', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('P-Mehlich (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_18, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_18, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_18, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_18, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_18, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('18', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(P_Meh_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(P_Meh_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(P_Meh_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(P_Meh_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1058, 423, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(p_meh_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(p_meh_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(p_meh_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(p_meh_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('18_Fosforo_Mehlich', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Potassio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Potassio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('K (cmol/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_19, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_19, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_19, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_19, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_19, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('19', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('7')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)

sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(K_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(K_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(K_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(K_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(K_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(K_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(K_7, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('19_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Enxofre
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Enxofre', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('S (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_20, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_20, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_20, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_20, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_20, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('20', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('5')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(S_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(S_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(S_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(S_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(S_5, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(s_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(s_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(s_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(s_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('20_Enxofre', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Boro
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Boro', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('B (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_21, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_21, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_21, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_21, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_21, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('21', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('5')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(B_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(B_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(B_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(B_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(B_5, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(b_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(b_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(b_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(b_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('21_Boro', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Calcio CTC
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Calcio CTC', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Ca CTC (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_22, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_22, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_22, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_22, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_22, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('22', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 8
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# 9
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# rool page down
pyautogui.click(901, 452, duration=0.5)
# rool page up
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
pyautogui.click(906, 319, duration=0.5)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Ca_CTC_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Ca_CTC_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Ca_CTC_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Ca_CTC_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Ca_CTC_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Ca_CTC_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Ca_CTC_7, interval=0.1)
pyautogui.press('enter')
# 8
pyautogui.write(Ca_CTC_8, interval=0.1)
pyautogui.press('enter')
# 9
pyautogui.write(Ca_CTC_9, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_ctc_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_ctc_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_ctc_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_ctc_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('22_Calcio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Magnesio CTC
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Magnesio CTC', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Mg CTC (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_23, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_23, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_23, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_23, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_23, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('23', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('5')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Mg_CTC_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Mg_CTC_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Mg_CTC_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Mg_CTC_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Mg_CTC_5, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1057, 279, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_ctc_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_ctc_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_ctc_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mg_ctc_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('23_Magnesio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Potassio CTC
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Potassio CTC', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('K CTC (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_24, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_24, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_24, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_24, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_24, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('24', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('9')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(K_CTC_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(K_CTC_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(K_CTC_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(K_CTC_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(K_CTC_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(K_CTC_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ctc_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ctc_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ctc_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(k_ctc_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('24_Potassio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Hidrogenio mais Aluminio CTC
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Hidrogenio mais Aluminio CTC', interval=0.1)
pyautogui.press('right')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('H + Al CTC (%)', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_25, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_25, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_25, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_25, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_25, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('25', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
pyautogui.click(523, 394, button='right', duration=0.5)
pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(HAL_CTC_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(HAL_CTC_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(HAL_CTC_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(HAL_CTC_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(HAL_CTC_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(HAL_CTC_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_ctc_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_ctc_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_ctc_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(hal_ctc_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('25_Hidrogenio_mais_Aluminio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Relacao Calcio Magnesio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Relacao Calcio Magnesio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Ca/Mg', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_26, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_26, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_26, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_26, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_26, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('26', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Ca_Mg_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Ca_Mg_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Ca_Mg_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Ca_Mg_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Ca_Mg_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Ca_Mg_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mg_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mg_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mg_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(ca_mg_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('26_Relacao_Calcio_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Relacao Calcio Potassio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Relacao Calcio Potassio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Ca/K', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_27, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_27, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_27, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_27, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_27, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('27', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('6')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Ca_K_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Ca_K_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Ca_K_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Ca_K_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Ca_K_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Ca_K_6, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cak_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cak_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cak_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cak_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('27_Relacao_Calcio_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Relacao Magenesio Potassio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Relacao Magenesio Potassio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Mg/K', interval=0.1)
sleep(1)
# pyautogui.press('left')
# pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_28, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_28, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_28, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_28, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_28, interval=0.1)
pyautogui.press('enter')
sleep(1)
# pyautogui.click(721, 252, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(723, 270, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(726, 285, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# pyautogui.click(715, 297, duration=0.5)
# pyautogui.hotkey('ctrl', 'alt', '3')
# sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('28', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('7')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Mg_K_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Mg_K_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Mg_K_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Mg_K_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Mg_K_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Mg_K_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Mg_K_7, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1000, 234, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mgk_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mgk_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mgk_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mgk_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('28_Relacao_Magnesio_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Cobre
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Cobre ', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Cu (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_29, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_29, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_29, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_29, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_29, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('29', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Cu_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Cu_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Cu_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Cu_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1041, 292, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cu_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cu_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cu_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(cu_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('29_Cobre', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Ferro
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Ferro ', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Feo (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_30, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_30, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_30, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_30, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_30, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('30', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('5')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Fe_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Fe_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Fe_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Fe_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Fe_5, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1041, 292, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(fe_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(fe_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(fe_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(fe_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('30_Ferro', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Manganes
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Manganes ', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Mn (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_31, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_31, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_31, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_31, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_31, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('31', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Mn_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Mn_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Mn_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Mn_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1041, 292, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mn_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mn_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mn_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(mn_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('31_Manganes', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Zinco
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Zinco ', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Zn (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_32, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_32, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_32, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_32, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_32, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('32', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('4')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Zn_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Zn_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Zn_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Zn_4, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1041, 292, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(zn_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(zn_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(zn_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(zn_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('32_Zinco', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)


# Sodio
# Activate box
pyautogui.click(49, 176, duration=0.5)
sleep(1)
# alter title
pyautogui.doubleClick(1009, 185, duration=0.5)
sleep(1)
pyautogui.write('Sodio', interval=0.1)
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)

# alter legend title
pyautogui.doubleClick(1007, 287, duration=0.5)
sleep(1)
pyautogui.write('Na (mg/dm)', interval=0.1)
sleep(1)
pyautogui.press('left')
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter stats
pyautogui.doubleClick(950, 559, duration=0.5)
sleep(1)
pyautogui.write(min_33, interval=0.1)
pyautogui.press('enter')
pyautogui.write(max_33, interval=0.1)
pyautogui.press('enter')
pyautogui.write(med_33, interval=0.1)
pyautogui.press('enter')
pyautogui.write(total_33, interval=0.1)
pyautogui.press('enter')
pyautogui.write(count_33, interval=0.1)
pyautogui.press('enter')
sleep(1)
pyautogui.click(721, 252, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(723, 270, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(726, 285, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
pyautogui.click(715, 297, duration=0.5)
pyautogui.hotkey('ctrl', 'alt', '3')
sleep(1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# alter number page
pyautogui.doubleClick(1123, 642, duration=0.5)
pyautogui.write('33', interval=0.1)
pyautogui.click(665, 538, duration=0.5)
sleep(1)
# classify shp
pyautogui.doubleClick(88, 174, duration=0.5)
sleep(1)
# Symbology
pyautogui.click(584, 126, duration=0.5)
sleep(1)
# Quanties
pyautogui.click(384, 246, duration=0.5)
sleep(1)
# Select dis
pyautogui.click(710, 232, duration=0.5)
sleep(1)
pyautogui.press('down')
sleep(1)
# Classify
pyautogui.doubleClick(806, 254, duration=0.5)
pyautogui.write('7')
sleep(1)
# color ramp
pyautogui.click(714, 297, duration=0.5)
# select brown scale
# pyautogui.click(647, 406, duration=0.5)
# sleep(1)
# select green blue scale
# pyautogui.click(644, 52, duration=0.5)
# sleep(1)
# select red yellow green scale
pyautogui.click(635, 296, duration=0.5)
sleep(1)
# flip symbols
# pyautogui.click(523, 394, button='right', duration=0.5)
# pyautogui.click(595, 403, duration=0.5)
# remove border
# 1
pyautogui.doubleClick(521, 339, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 2
pyautogui.doubleClick(524, 357, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 3
pyautogui.doubleClick(527, 374, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 4
pyautogui.doubleClick(528, 392, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 5
pyautogui.doubleClick(525, 407, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 6
pyautogui.doubleClick(533, 425, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# 7
pyautogui.doubleClick(529, 442, duration=0.5)
pyautogui.click(907, 364, duration=0.5)
pyautogui.click(992, 387, duration=0.5)
pyautogui.click(816, 577, duration=0.5)
# rool page down
pyautogui.click(901, 452, duration=0.5)
sleep(1)
# insert labels legend
pyautogui.click(755, 339, duration=0.5)
sleep(1)
# 1
pyautogui.write(Na_1, interval=0.1)
pyautogui.press('enter')
# 2
pyautogui.write(Na_2, interval=0.1)
pyautogui.press('enter')
# 3
pyautogui.write(Na_3, interval=0.1)
pyautogui.press('enter')
# 4
pyautogui.write(Na_4, interval=0.1)
pyautogui.press('enter')
# 5
pyautogui.write(Na_5, interval=0.1)
pyautogui.press('enter')
# 6
pyautogui.write(Na_6, interval=0.1)
pyautogui.press('enter')
# 7
pyautogui.write(Na_7, interval=0.1)
pyautogui.press('enter')
sleep(1)
# finish ok
pyautogui.click(810, 618, duration=0.5)
sleep(3)
# Legend
# Select Legend
pyautogui.doubleClick(1041, 292, duration=0.5)
sleep(2)
# items
pyautogui.click(444, 140, duration=0.5)
pyautogui.click(431, 215, duration=0.5)
# style
pyautogui.click(470, 562, duration=0.5)
pyautogui.click(442, 403, duration=0.5)
# ok
pyautogui.click(732, 553, duration=0.5)
# size and position
pyautogui.click(616, 143, duration=0.5)
# position X
pyautogui.click(491, 189, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(na_Position_X, interval=0.1)
# position Y
pyautogui.click(493, 214, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(na_Position_Y, interval=0.1)
# position Width
pyautogui.click(690, 190, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(na_Size_Width, interval=0.1)
# position Height
pyautogui.click(689, 217, duration=0.5)
pyautogui.hotkey('ctrl', 'a')
pyautogui.write(na_Size_Height, interval=0.1)
# finish ok
pyautogui.click(794, 598, duration=0.5)
# export map
# file
pyautogui.click(20, 35, duration=0.5)
# export map
pyautogui.click(82, 337, duration=0.5)
sleep(5)
# write map name
pyautogui.doubleClick(615, 394, duration=0.5)
pyautogui.write('33_Sodio', interval=0.1)
pyautogui.press('enter')
sleep(15)
# remove shp
pyautogui.click(89, 172, button='right', duration=0.5)
sleep(1)
pyautogui.click(134, 205, duration=0.5)
sleep(10)
