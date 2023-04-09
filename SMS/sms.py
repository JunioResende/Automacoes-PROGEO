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
execution_atribute_time = 30

pyautogui.click(select_atribute_coordinate_X,
                select_atribute_coordinate_Y,
                duration=2)
pyautogui.press('down')
sleep(execution_atribute_time)
pyautogui.click(x=center_map_coordinate_X,
                y=center_map_coordinate_Y,
                button='right',
                duration=2)
pyautogui.click(export_button_coordinate_X,
                export_button_coordinate_Y,
                duration=2)
pyautogui.click(init_export_coordinate_X,
                init_export_coordinate_Y,
                duration=2)
pyautogui.click(export_format_coordinate_X,
                export_format_coordinate_Y,
                duration=2)
sleep(2)
pyautogui.write('10_Saturacao_de_Bases', interval=0.3)
pyautogui.press('enter')
sleep(5)
