import pyautogui
from time import sleep

# Variaveis legendas e estatisticas
Argila_1 = "Acima de 600,00 -- (0ha - 0%)"
Argila_2 = "500,00 - 600,00 -- (110,68ha - 11%)"
Argila_3 = "450,00 - 500,00 -- (492,4ha - 48,96%)"
Argila_4 = "400,00 - 450,00 -- (204,14ha - 20,3%)"
Argila_5 = "350,00 - 400,00 -- (79,41ha - 7,9%)"
Argila_6 = "300,00 - 350,00 -- (45,8ha - 4,55%)"
Argila_7 = "250,00 - 300,00 -- (34,68ha - 3,45%)"
Argila_8 = "220,00 - 250,00 -- (15,54ha - 1,55%)"
Argila_9 = "180,00 - 220,00 -- (17,23ha - 1,71%)"
Argila_10 = "120,00 - 180,00 -- (5,88ha - 0,58%)"
Argila_11 = "Abaixo de 120,00 -- (0ha - 0%)"
Areia_1 = "Acima de 800,00 -- (0,19ha - 0,02%)"
Areia_2 = "700,00 - 800,00 -- (30,58ha - 3,04%)"
Areia_3 = "600,00 - 700,00 -- (63,08ha - 6,27%)"
Areia_4 = "550,00 - 600,00 -- (63,52ha - 6,32%)"
Areia_5 = "500,00 - 550,00 -- (117,35ha - 11,67%)"
Areia_6 = "450,00 - 500,00 -- (219,45ha - 21,82%)"
Areia_7 = "400,00 - 450,00 -- (449,46ha - 44,69%)"
Areia_8 = "350,00 - 400,00 -- (62,12ha - 6,18%)"
Areia_9 = "Abaixo de 350,00 -- (0ha - 0%)"
Silte_1 = "Acima de 250,00 -- (0ha - 0%)"
Silte_2 = "200,00 - 250,00  -- (0ha - 0%)"
Silte_3 = "150,00 - 200,00 -- (4,86ha - 0,48%)"
Silte_4 = "100,00 - 150,00 -- (237,84ha - 23,65%)"
Silte_5 = "50,00 - 100,00 -- (727,92ha - 72,37%)"
Silte_6 = "Abaixo de 50,00 -- (35,14ha - 3,49%)"
Mat_Or_1 = "Acima de 38,00 -- Alto  (8,05ha - 0,8%)"
Mat_Or_2 = "35,00 - 38,00 -- Medio Alto  (6,91ha - 0,69%)"
Mat_Or_3 = "33,00 - 35,00 -- Medio  (22,26ha - 2,21%)"
Mat_Or_4 = "28,00 - 33,00 -- Medio  (452,24ha - 44,96%)"
Mat_Or_5 = "25,00 - 28,00 -- Medio Baixo  (256,27ha - 25,48%)"
Mat_Or_6 = "22,00 - 25,00 -- Baixo  (154,94ha - 15,41%)"
Mat_Or_7 = "20,00 - 22,00 -- Baixo  (34,97ha - 3,48%)"
Mat_Or_8 = "17,00 - 20,00 -- Muito Baixo  (39,78ha - 3,96%)"
Mat_Or_9 = "Abaixo de 17,00 -- Muito Baixo  (30,35ha - 3,02%)"
Carb_Or_1 = "Acima de 20,00 -- Muito Alto  (17,27ha - 1,72%)"
Carb_Or_2 = "18,00 - 20,00 -- Alto  (107,86ha - 10,72%)"
Carb_Or_3 = "16,00 - 18,00 -- Medio Alto  (408,88ha - 40,65%)"
Carb_Or_4 = "14,00 - 16,00 -- Medio  (263,98ha - 26,25%)"
Carb_Or_5 = "12,00 - 14,00 -- Baixo  (128,5ha - 12,78%)"
Carb_Or_6 = "Abaixo de 12,00 -- Muito Baixo  (79,27ha - 7,88%)"
CTC_1 = "Acima de 9,00 -- Muito Bom  (353,11ha - 35,11%)"
CTC_2 = "8,00 - 9,00 -- Muito Bom  (396,71ha - 39,44%)"
CTC_3 = "7,00 - 8,00 -- Bom  (174,51ha - 17,35%)"
CTC_4 = "6,00 - 7,00 --Bom  (56,21ha - 5,59%)"
CTC_5 = "5,00 - 6,00 -- Medio  (25,23ha - 2,51%)"
CTC_6 = "4,00 - 5,00 -- Baixo  (0ha - 0%)"
CTC_7 = "3,00 - 4,00 -- Muito Baixo  (0ha - 0%)"
CTC_8 = "1,60 - 3,00 -- Muito Baixo  (0ha - 0%)"
CTC_9 = "Abaixo de 1,60 -- Muito Baixo  (0ha - 0%)"
pH_1 = "Acima de 6,40 -- Muito Alto  (0ha - 0%)"
pH_2 = "6,00 - 6,40 -- Alto  (2,9ha - 0,29%)"
pH_3 = "5,40 - 6,00 -- Ideal  (9,16ha - 0,91%)"
pH_4 = "5,00 - 5,40 -- Medio  (82ha - 8,15%)"
pH_5 = "4,50 - 5,00 -- Baixo  (791,87ha - 78,73%)"
pH_6 = "Abaixo de 4,50 -- Muito Baixo  (119,84ha - 11,92%)"
Sat_B_1 = "Acima de 60,00 -- Alto  (10,39ha - 1,03%)"
Sat_B_2 = "55,00 - 60,00 -- Medio Alto  (2,94ha - 0,29%)"
Sat_B_3 = "50,00 - 55,00 -- Medio  (15,71ha - 1,56%)"
Sat_B_4 = "45,00 - 50,00 -- Medio  (52,31ha - 5,2%)"
Sat_B_5 = "40,00 - 45,00 -- Baixo  (143,92ha - 14,31%)"
Sat_B_6 = "35,00 - 40,00 -- Baixo  (265,01ha - 26,35%)"
Sat_B_7 = "30,00 - 35,00 -- Muito Baixo  (264,04ha - 26,25%)"
Sat_B_8 = "25,00 - 30,00 -- Muito Baixo  (143ha - 14,22%)"
Sat_B_9 = "Abaixo de 25,00 -- Muito Baixo  (108,44ha - 10,78%)"
Cal_1 = "Acima de 5,00 -- Muito Alto  (2,68ha - 0,27%)"
Cal_2 = "4,00 - 5,00 -- Alto  (5,76ha - 0,57%)"
Cal_3 = "3,50 - 4,00 --  Medio  (5,1ha - 0,51%)"
Cal_4 = "3,00 - 3,50 -- Medio  (39,13ha - 3,89%)"
Cal_5 = "2,50 - 3,00 -- Medio  (177,26ha - 17,62%)"
Cal_6 = "2,00 - 2,50 -- Baixo  (394,16ha - 39,19%)"
Cal_7 = "1,50 - 2,00 -- Baixo  (256,02ha - 25,46%)"
Cal_8 = "1,00 - 1,50 -- Muito Baixo  (87,95ha - 8,74%)"
Cal_9 = "0,40 - 1,00 -- Muito Baixo  (37,72ha - 3,75%)"
Cal_10 = "Abaixo de 0,40 -- Muito Baixo  (0ha - 0%)"
Mg_1 = "Acima de 5,00 -- Alto  (0ha - 0%)"
Mg_2 = "4,50 - 5,00 -- Alto  (0ha - 0%)"
Mg_3 = "4,00 - 4,50 -- Alto  (0ha - 0%)"
Mg_4 = "3,50 - 4,00 -- Alto  (0ha - 0%)"
Mg_5 = "3,00 - 3,50 -- Alto  (2,1ha - 0,21%)"
Mg_6 = "2,50 - 3,00 -- Alto  (2,9ha - 0,29%)"
Mg_7 = "2,00 - 2,50 -- Alto  (3,2ha - 0,32%)"
Mg_8 = "1,50 - 2,00 -- Alto  (3,99ha - 0,4%)"
Mg_9 = "1,00 - 1,50 -- Medio  (10,23ha - 1,02%)"
Mg_10 = "0,90 - 1,00 -- Medio  (134,23ha - 13,35%)"
Mg_11 = "0,50 - 0,90 -- Baixo  (732,53ha - 72,83%)"
Mg_12 = "Abaixo de 0,50 -- Baixo  (116,58ha - 11,59%)"
Ca_mais_Mg_1 = "Acima de 7,00 -- Muito Alto  (6,73ha - 0,67%)"
Ca_mais_Mg_2 = "5,55 - 7,00 -- Alto  (5,15ha - 0,51%)"
Ca_mais_Mg_3 = "5,00 - 5,55 -- Medio Alto  (3,18ha - 0,32%)"
Ca_mais_Mg_4 = "4,70 - 5,00 -- Baixo  (6,17ha - 0,61%)"
Ca_mais_Mg_5 = "4,30 - 4,70 -- Baixo  (19,35ha - 1,92%)"
Ca_mais_Mg_6 = "1,70 - 4,30 -- Muito Baixo  (965,19ha - 95,97%)"
Al_1 = "0,60 - 1,00 -- Alto  (6,3ha - 0,63%)"
Al_2 = "0,50 - 0,60 -- Adequado  (3,71ha - 0,37%)"
Al_3 = "0,20 - 0,50 -- Medio Bom  (84,86ha - 8,44%)"
Al_4 = "0,00 - 0,20 -- Baixo  (910,89ha - 90,57%)"
HAL_1 = "6,00 - 7,00 -- Muito Alto  (239,08ha - 23,77%)"
HAL_2 = "5,00 - 6,00 -- Alto  (522,69ha - 51,97%)"
HAL_3 = "4,00 - 5,00 -- Medio  (219,77ha - 21,85%)"
HAL_4 = "3,00 - 4,00 -- Medio  (17,31ha - 1,72%)"
HAL_5 = "2,00 - 3,00 -- Baixo  (4,48ha - 0,45%)"
HAL_6 = "1,00 - 2,00 -- Muito Baixo  (2,44ha - 0,24%)"
Sat_Al_1 = "Acima de 6,00 -- Muito Alto  (261,57ha - 26,01%)"
Sat_Al_2 = "4,00 - 6,00 -- Alto  (153,93ha - 15,3%)"
Sat_Al_3 = "2,00 - 4,00 -- Medio  (371,13ha - 36,9%)"
Sat_Al_4 = "Abaixo de 2,00 -- Baixo  (219,14ha - 21,79%)"
K_ppm_1 = "Acima de 160,00 -- Muito Alto  (0ha - 0%)"
K_ppm_2 = "140,00 -  160,00 -- Muito Alto  (0ha - 0%)"
K_ppm_3 = "120,00 - 140,00 -- Muito Alto  (0ha - 0%)"
K_ppm_4 = "100,00 - 120,00 -- Alto  (0,56ha - 0,06%)"
K_ppm_5 = "90,00 - 100,00 -- Alto  (0,99ha - 0,1%)"
K_ppm_6 = "80,00 - 90,00 -- Adequado  (9,23ha - 0,92%)"
K_ppm_7 = "75,00 - 80,00 -- Adequado  (10,83ha - 1,08%)"
K_ppm_8 = "70,00 - 75,00 -- Adequado  (17,73ha - 1,76%)"
K_ppm_9 = "65,00 - 70,00 -- Medio  (29,99ha - 2,98%)"
K_ppm_10 = "60,00 - 65,00 -- Medio  (47,36ha - 4,71%)"
K_ppm_11 = "55,00 - 60,00 --  Medio  (69,25ha - 6,89%)"
K_ppm_12 = "50,00 - 55,00 -- Medio  (95,42ha - 9,49%)"
K_ppm_13 = "45,00 - 50,00 -- Medio  (116,48ha - 11,58%)"
K_ppm_14 = "40,00 - 45,00 -- Medio Baixo  (180,16ha - 17,91%)"
K_ppm_15 = "35,00 - 40,00 -- Medio Baixo  (166,37ha - 16,54%)"
K_ppm_16 = "30,00 - 35,00 -- Medio Baixo  (135,69ha - 13,49%)"
K_ppm_17 = "25,00 - 30,00 -- Baixo  (85,68ha - 8,52%)"
K_ppm_18 = "20,00 - 25,00 -- Baixo  (31,36ha - 3,12%)"
K_ppm_19 = "15,00 - 20,00 -- Muito Baixo  (7,9ha - 0,79%)"
K_ppm_20 = "Abaixo de 15,00 -- Muito Baixo  (0,76ha - 0,08%)"
P_Meh_1 = "Acima de 14,00 -- Bom  (172,96ha - 17,2%)"
P_Meh_2 = "10,00 - 14,00 -- Medio  (223,81ha - 22,25%)"
P_Meh_3 = "5,00 - 10,00 -- Baixo  (546,38ha - 54,32%)"
P_Meh_4 = "Abaixo de 5,00 -- Muito Baixo  (62,61ha - 6,23%)"
K_1 = "0,28 - 0,44 -- Alto  (0,15ha - 0,01%)"
K_2 = "0,24 - 0,28 -- Alto  (0,73ha - 0,07%)"
K_3 = "0,21 - 0,24 -- Medio Alto  (6,76ha - 0,67%)"
K_4 = "0,17 - 0,21 -- Medio  (53,25ha - 5,29%)"
K_5 = "0,14 - 0,17 -- Medio Baixo  (132,18ha - 13,14%)"
K_6 = "0,13 - 0,14 -- Baixo  (75,52ha - 7,51%)"
K_7 = "0,03 - 0,13 -- Baixo  (737,18ha - 73,3%)"
S_1 = "10,00 - 18,00 -- Muito Alto  (1001,27ha - 99,55%)"
S_2 = "9,00 - 10,00 -- Alto  (2,85ha - 0,28%)"
S_3 = "4,90 - 9,00 -- Medio  (1,65ha - 0,16%)"
S_4 = "2,50 - 4,90 -- Baixo  (0ha - 0%)"
S_5 = "1,00 - 2,50 -- Muito Baixo  (0ha - 0%)"
B_1 = "Acima de 0,90 -- Muito Alto  (0ha - 0%)"
B_2 = "0,60 - 0,90 -- Alto  (2,02ha - 0,2%)"
B_3 = "0,35 - 0,60 -- Medio  (100,35ha - 9,98%)"
B_4 = "0,15 - 0,35 -- Baixo  (903,4ha - 89,82%)"
B_5 = "Abaixo de 0,15 -- Muito Baixo  (0ha - 0%)"
Ca_CTC_1 = "Acima de 70,00 -- Muito Alto  (0ha - 0%)"
Ca_CTC_2 = "60,00 - 70,00 -- Ideal  (0ha - 0%)"
Ca_CTC_3 = "50,00 - 60,00 -- Ideal  (0,49ha - 0,05%)"
Ca_CTC_4 = "40,00 - 50,00 -- Bom  (7,29ha - 0,72%)"
Ca_CTC_5 = "30,00 - 40,00 -- Medio  (121,14ha - 12,04%)"
Ca_CTC_6 = "25,00 - 30,00 -- Baixo  (366,95ha - 36,48%)"
Ca_CTC_7 = "20,00 - 25,00 -- Baixo  (336,77ha - 33,48%)"
Ca_CTC_8 = "15,00 - 20,00 -- Muito Baixo  (134,16ha - 13,34%)"
Ca_CTC_9 = "Abaixo de 15,00 -- Muito Baixo  (38,96ha - 3,87%)"
Mg_CTC_1 = "Acima de 20,00 -- Muito Alto  (12,14ha - 1,21%)"
Mg_CTC_2 = "15,00 - 20,00 -- Alto  (20,44ha - 2,03%)"
Mg_CTC_3 = "10,00 - 15,00 -- Medio  (247,87ha - 24,64%)"
Mg_CTC_4 = "7,00 - 10,00 -- Baixo  (454,12ha - 45,15%)"
Mg_CTC_5 = "Abaixo 7,00 -- Baixo  (271,2ha - 26,96%)"
K_CTC_1 = "Acima de 6,00 -- Muito Alto  (0ha - 0%)"
K_CTC_2 = "5,00 - 6,00 -- Alto  (0ha - 0%)"
K_CTC_3 = "3,00 - 5,00 -- Adequado  (0,28ha - 0,03%)"
K_CTC_4 = "2,00 - 3,00 -- Medio  (32,86ha - 3,27%)"
K_CTC_5 = "1,00 - 2,00 -- Baixo  (793,04ha - 78,85%)"
K_CTC_6 = "Abaixo de 1,00 -- Muito Baixo  (179,59ha - 17,86%)"
HAL_CTC_1 = "Acima de 60,00 -- Muito Alto  (783,4ha - 77,89%)"
HAL_CTC_2 = "40,00 - 60,00 -- Muito Alto  (212,04ha - 21,08%)"
HAL_CTC_3 = "36,00 - 40,00 -- Alto  (1,79ha - 0,18%)"
HAL_CTC_4 = "33,00 - 36,00 -- Medio  (1,25ha - 0,12%)"
HAL_CTC_5 = "25,00 - 33,00 -- Baixo  (2,99ha - 0,3%)"
HAL_CTC_6 = "Abaixo de 25,00 -- Muito Baixo  (4,3ha - 0,43%)"
Ca_Mg_1 = "Acima de 5,00 -- Muito Alto  (59,08ha - 5,87%)"
Ca_Mg_2 = "4,00 - 5,00 -- Alto  (58,62ha - 5,83%)"
Ca_Mg_3 = "3,00 - 4,00 -- Adequado  (421,99ha - 41,96%)"
Ca_Mg_4 = "2,00 - 3,00 -- Medio  (454,11ha - 45,15%)"
Ca_Mg_5 = "1,10 - 2,00 -- Baixo  (11,76ha - 1,17%)"
Ca_Mg_6 = "Abaixo de 1,10 -- Baixo  (0,21ha - 0,02%)"
Ca_K_1 = "Acima de 15,00 -- Alto  (824,75ha - 82%)"
Ca_K_2 = "14,90- 15,00 -- Adequado  (5,03ha - 0,5%)"
Ca_K_3 = "12,00 - 14,90 -- Medio Baixo  (130,88ha - 13,01%)"
Ca_K_4 = "9,00 - 12,00 -- Medio  (43,07ha - 4,28%)"
Ca_K_5 = "7,00 - 9,00 -- Muito Baixo  (2,03ha - 0,2%)"
Ca_K_6 = "Abaixo de 7,00 -- Muito Baixo  (0ha - 0%)"
Mg_K_1 = "6,00 - 7,00 -- Muito Alto  (623,9ha - 62,03%)"
Mg_K_2 = "5,00 - 6,00 -- Alto Bom  (177,32ha - 17,63%)"
Mg_K_3 = "4,90 - 5,00 -- Adequado  (14,59ha - 1,45%)"
Mg_K_4 = "3,00 - 4,90 -- Medio  (150,56ha - 14,97%)"
Mg_K_5 = "2,00 - 3,00 -- Baixo  (25ha - 2,49%)"
Mg_K_6 = "1,00 - 2,00 -- Muito Baixo  (14,4ha - 1,43%)"
Mg_K_7 = "0,50 - 1,00 -- Muito Baixo  (0ha - 0%)"
Cu_1 = "3,00 - 10,0 -- Alto  (0ha - 0%)"
Cu_2 = "1,50 - 3,00 -- Medio  (24,1ha - 2,4%)"
Cu_3 = "0,60 - 1,50 -- Baixo  (980,39ha - 97,48%)"
Cu_4 = "0,30 - 0,60 -- Baixo  (1,27ha - 0,13%)"
Fe_1 = "Acima de 220,00 -- Muito Alto  (0ha - 0%)"
Fe_2 = "83,00 - 220,00 -- Alto  (34,86ha - 3,47%)"
Fe_3 = "31,00 - 83,00 -- Medio  (876,41ha - 87,14%)"
Fe_4 = "20,00 - 31,00 -- Baixo  (89,14ha - 8,86%)"
Fe_5 = "Abaixo de 20,00 -- Muito Baixo  (5,35ha - 0,53%)"
Mn_1 = "Acima de 130,00 -- Alto  (0ha - 0%)"
Mn_2 = "12,00 - 130,00 -- Medio  (26,98ha - 2,68%)"
Mn_3 = "6,00 - 12,00 -- Baixo  (907,04ha - 90,18%)"
Mn_4 = "Abaixo de 6,00 -- Muito Baixo  (71,74ha - 7,13%)"
Zn_1 = "Acima de 5,00 -- Muito Alto  (0ha - 0%)"
Zn_2 = "1,60 - 5,00 -- Alto  (712,62ha - 70,85%)"
Zn_3 = "1,00 - 1,60 -- Medio  (244,27ha - 24,29%)"
Zn_4 = "Abaixo de 1,00 -- Baixo  (48,88ha - 4,86%)"
Na_1 = "Acima de 6,00 -- Muito Alto  (26,71ha - 2,66%)"
Na_2 = "4,44 - 6,00 -- Alto  (92,41ha - 9,19%)"
Na_3 = "2,95 - 4,44 -- Medio Alto  (497,78ha - 49,49%)"
Na_4 = "2,55 - 2,95 -- Medio  (194,19ha - 19,31%)"
Na_5 = "2,22 - 2,55 -- Medio Baixo  (98,06ha - 9,75%)"
Na_6 = "1,91 - 2,22 -- Baixo  (59,84ha - 5,95%)"
Na_7 = "Abaixo de 1,91 -- Muito Baixo  (36,77ha - 3,66%)"

min_3 = "Minimo: 168,26 g/dm³"
max_3 = "Maximo: 516,48 g/dm³"
med_3 = "Medio: 394,57 g/dm³"
total_3 = "Total: 26041,74 g/dm³"
count_3 = "Contagem: 66 "
min_4 = "Minimo: 386,82 g/dm³"
max_4 = "Maximo: 801,2 g/dm³"
med_4 = "Medio: 524,63 g/dm³"
total_4 = "Total: 28329,81 g/dm³"
count_4 = "Contagem: 54 "
min_5 = "Minimo: 40,52 g/dm³"
max_5 = "Maximo: 156,14 g/dm³"
med_5 = "Medio: 87,37 g/dm³"
total_5 = "Total: 2446,28 g/dm³"
count_5 = "Contagem: 28 "
min_6 = "Minimo: 15,53 g/dm³"
max_6 = "Maximo: 42,2 g/dm³"
med_6 = "Medio: 25,57 g/dm³"
total_6 = "Total: 1227,39 g/dm³"
count_6 = "Contagem: 48 "
min_7 = "Minimo: 10,13 g/dm³"
max_7 = "Maximo: 22,47 g/dm³"
med_7 = "Medio: 15,71 g/dm³"
total_7 = "Total: 628,35 g/dm³"
count_7 = "Contagem: 40 "
min_8 = "Minimo: 5,71 cmol/dm³"
max_8 = "Maximo: 9,55 cmol/dm³"
med_8 = "Medio: 7,88 cmol/dm³"
total_8 = "Total: 220,7 cmol/dm³"
count_8 = "Contagem: 28 "
min_9 = "Minimo: 4,33 "
max_9 = "Maximo: 6,1 "
med_9 = "Medio: 4,84 "
total_9 = "Total: 169,4 "
count_9 = "Contagem: 35 "
min_10 = "Minimo: 17,73 %"
max_10 = "Maximo: 67,8 %"
med_10 = "Medio: 37,73 %"
total_10 = "Total: 4263,4 %"
count_10 = "Contagem: 113 "
min_11 = "Minimo: 0,84 cmol/dm³"
max_11 = "Maximo: 5,28 cmol/dm³"
med_11 = "Medio: 2,28 cmol/dm³"
total_11 = "Total: 182,71 cmol/dm³"
count_11 = "Contagem: 80 "
min_12 = "Minimo: 0,3 cmol/dm³"
max_12 = "Maximo: 3,63 cmol/dm³"
med_12 = "Medio: 1,15 cmol/dm³"
total_12 = "Total: 73,55 cmol/dm³"
count_12 = "Contagem: 64 "
min_13 = "Minimo: 2,98 cmol/dm³"
max_13 = "Maximo: 7,74 cmol/dm³"
med_13 = "Medio: 5,01 cmol/dm³"
total_13 = "Total: 110,21 cmol/dm³"
count_13 = "Contagem: 22 "
min_14 = "Minimo: 0,07 cmol/dm³"
max_14 = "Maximo: 0,74 cmol/dm³"
med_14 = "Medio: 0,34 cmol/dm³"
total_14 = "Total: 6,43 cmol/dm³"
count_14 = "Contagem: 19 "
min_15 = "Minimo: 1,78 cmol/dm³"
max_15 = "Maximo: 6,51 cmol/dm³"
med_15 = "Medio: 5,12 cmol/dm³"
total_15 = "Total: 271,36 cmol/dm³"
count_15 = "Contagem: 53 "
min_16 = "Minimo: 0,99 %"
max_16 = "Maximo: 17,68 %"
med_16 = "Medio: 4,47 %"
total_16 = "Total: 232,39 %"
count_16 = "Contagem: 52 "
min_17 = "Minimo: 14,69 mg/dm³"
max_17 = "Maximo: 104,63 mg/dm³"
med_17 = "Medio: 49,13 mg/dm³"
total_17 = "Total: 7762,24 mg/dm³"
count_17 = "Contagem: 158 "
min_18 = "Minimo: 3,85 mg/dm³"
max_18 = "Maximo: 22,16 mg/dm³"
med_18 = "Medio: 9,13 mg/dm³"
total_18 = "Total: 474,67 mg/dm³"
count_18 = "Contagem: 52 "
min_19 = "Minimo: 0,1 cmol/dm³"
max_19 = "Maximo: 0,28 cmol/dm³"
med_19 = "Medio: 0,16 cmol/dm³"
total_19 = "Total: 6,9 cmol/dm³"
count_19 = "Contagem: 42 "
min_20 = "Minimo: 8,09 mg/dm³"
max_20 = "Maximo: 14,39 mg/dm³"
med_20 = "Medio: 9,78 mg/dm³"
total_20 = "Total: 68,48 mg/dm³"
count_20 = "Contagem: 7 "
min_21 = "Minimo: 0,3 mg/dm³"
max_21 = "Maximo: 0,65 mg/dm³"
med_21 = "Medio: 0,38 mg/dm³"
total_21 = "Total: 5,77 mg/dm³"
count_21 = "Contagem: 15 "
min_22 = "Minimo: 12,04 %"
max_22 = "Maximo: 50,96 %"
med_22 = "Medio: 23,93 %"
total_22 = "Total: 1818,78 %"
count_22 = "Contagem: 76 "
min_23 = "Minimo: 4,04 %"
max_23 = "Maximo: 25 %"
med_23 = "Medio: 9,99 %"
total_23 = "Total: 479,68 %"
count_23 = "Contagem: 48 "
min_24 = "Minimo: 0,84 %"
max_24 = "Maximo: 3,07 %"
med_24 = "Medio: 1,34 %"
total_24 = "Total: 40,24 %"
count_24 = "Contagem: 30 "
min_25 = "Minimo: 20,98 %"
max_25 = "Maximo: 67,73 %"
med_25 = "Medio: 51,92 %"
total_25 = "Total: 1765,13 %"
count_25 = "Contagem: 34 "
min_26 = "Minimo: 1,01 "
max_26 = "Maximo: 6,75 "
med_26 = "Medio: 3,42 "
total_26 = "Total: 95,83 "
count_26 = "Contagem: 28 "
min_27 = "Minimo: 8,55 "
max_27 = "Maximo: 23,59 "
med_27 = "Medio: 13,1 "
total_27 = "Total: 655,1 "
count_27 = "Contagem: 50 "
min_28 = "Minimo: 1,51 "
max_28 = "Maximo: 6,47 "
med_28 = "Medio: 4,79 "
total_28 = "Total: 383,08 "
count_28 = "Contagem: 80 "
min_29 = "Minimo: 0,57 mg/dm³"
max_29 = "Maximo: 1,85 mg/dm³"
med_29 = "Medio: 1,41 mg/dm³"
total_29 = "Total: 9,88 mg/dm³"
count_29 = "Contagem: 7 "
min_30 = "Minimo: 15,32 mg/dm³"
max_30 = "Maximo: 115,25 mg/dm³"
med_30 = "Medio: 42,02 mg/dm³"
total_30 = "Total: 1008,52 mg/dm³"
count_30 = "Contagem: 24 "
min_31 = "Minimo: 5,21 mg/dm³"
max_31 = "Maximo: 14,67 mg/dm³"
med_31 = "Medio: 8,2 mg/dm³"
total_31 = "Total: 155,71 mg/dm³"
count_31 = "Contagem: 19 "
min_32 = "Minimo: 0,79 mg/dm³"
max_32 = "Maximo: 2,17 mg/dm³"
med_32 = "Medio: 1,34 mg/dm³"
total_32 = "Total: 40,18 mg/dm³"
count_32 = "Contagem: 30 "
min_33 = "Minimo: 1,65 mg/dm³"
max_33 = "Maximo: 9,22 mg/dm³"
med_33 = "Medio: 3,29 mg/dm³"
total_33 = "Total: 181,19 mg/dm³"
count_33 = "Contagem: 55 "


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
pyautogui.write('Calcio (cmol/dm)', interval=0.1)
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
pyautogui.write('Magnesio (cmol/dm)', interval=0.1)
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
pyautogui.write('Calcio mais Magnesio (cmol/dm)', interval=0.1)
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
pyautogui.write('Aluminio (cmol/dm)', interval=0.1)
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
pyautogui.write('Hidrogenio mais Aluminio (cmol/dm)', interval=0.1)
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
pyautogui.write('Potassio ppm (mg/dm)', interval=0.1)
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
pyautogui.write('Fosforo Mehlich (mg/dm)', interval=0.1)
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
pyautogui.write('Potassio (cmol/dm)', interval=0.1)
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
pyautogui.write('Enxofre (mg/dm)', interval=0.1)
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
pyautogui.write('Boro (mg/dm)', interval=0.1)
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
pyautogui.write('Calcio CTC (%)', interval=0.1)
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
pyautogui.write('Magnesio CTC (%)', interval=0.1)
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
pyautogui.write('Potassio CTC (%)', interval=0.1)
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
pyautogui.write('Hidrogenio mais Aluminio CTC (%)', interval=0.1)
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
pyautogui.write('Relacao Calcio Magnesio', interval=0.1)
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
pyautogui.write('Relacao Calcio Potassio', interval=0.1)
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
pyautogui.write('Relacao Magenesio Potassio', interval=0.1)
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
pyautogui.write('Cobre (mg/dm)', interval=0.1)
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
pyautogui.write('Ferro (mg/dm)', interval=0.1)
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
pyautogui.write('Manganes (mg/dm)', interval=0.1)
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
pyautogui.write('Zinco (mg/dm)', interval=0.1)
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
pyautogui.write('Sodio (mg/dm)', interval=0.1)
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
