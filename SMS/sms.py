import pyautogui
from time import sleep

# Coordenada Selecionar atributo
select_atribute_coordinate_X = 1167
select_atribute_coordinate_Y = 222

# Coordenadas centro do mapa
center_map_coordinate_X = 788
center_map_coordinate_Y = 451

# Coordenadas botao exportar
export_button_coordinate_X = 848
export_button_coordinate_Y = 413

# Coordenadas botao iniciar processo de exportacao de arquivo generico
init_export_coordinate_X = 602
init_export_coordinate_Y = 605

# Coordenadas exportar para o formato de arquivo selecionado
export_format_coordinate_X = 518
export_format_coordinate_Y = 600

# Tempo de execução do atributo
execution_atribute_time = 20

# 10_Saturacao_de_Bases
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('10_Saturacao_de_Bases', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 11_Calcio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('11_Calcio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 12_Magnesio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('12_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 13_Calcio_Mais_Magnesio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('13_Calcio_Mais_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 14_Aluminio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('14_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 15_Hidrogenio_Mais_Aluminio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('15_Hidrogenio_Mais_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 16_Saturacao_por_Aluminio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('16_Saturacao_por_Aluminio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 17_Potassio_ppm
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('17_Potassio_ppm', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 18_Fosforo_Mehlich
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('18_Fosforo_Mehlich', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 19_Potassio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('19_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 20_Enxofre
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('20_Enxofre', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 21_Boro
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('21_Boro', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 22_Calcio_CTC
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('22_Calcio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 23_Magnesio_CTC
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('23_Magnesio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 24_Potassio_CTC
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('24_Potassio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 25_Hidrogenio_Mais_Aluminio_CTC
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('25_Hidrogenio_Mais_Aluminio_CTC', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 26_Relacao_Calcio_Magnesio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('26_Relacao_Calcio_Magnesio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 27_Relacao_Calcio_Potassio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('27_Relacao_Calcio_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 28_Relacao_Magnesio_Potassio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('28_Relacao_Magnesio_Potassio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 29_Cobre
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('29_Cobre', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 3_Argila
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('3_Argila', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 30_Ferro
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('30_Ferro', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 31_Manganes
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('31_Manganes', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 32_Zinco
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('32_Zinco', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 33_Sodio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('33_Sodio', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 4_Areia
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('4_Areia', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 5_Silte
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('5_Silte', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 6_Materia_Organica
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('6_Materia_Organica', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 7_Carbono_Organico
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('7_Carbono_Organico', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 8_CTC_Total
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('8_CTC_Total', interval=0.1)
pyautogui.press('enter')
sleep(5)

# 9_pH_Cloreto_de_Calcio
pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=0.5)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=0.5)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=0.5)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=0.5)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=0.5)
sleep(2)
pyautogui.write('9_pH_Cloreto_de_Calcio', interval=0.1)
pyautogui.press('enter')
sleep(5)
