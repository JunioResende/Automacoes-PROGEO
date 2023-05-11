# 3_Argila
import arcpy

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "3_Argila_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\3_Argila.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"3_Argila_g\">=0 And \"3_Argila_g\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "3", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "3_Argila_g MIN;3_Argila_g MAX;3_Argila_g MEAN;3_Argila_g SUM;3_Argila_g COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 4_Areia

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "4_Areia_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\4_Areia.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"4_Areia_g_\">=0 And \"4_Areia_g_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "4", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "4_Areia_g_ MIN;4_Areia_g_ MAX;4_Areia_g_ MEAN;4_Areia_g_ SUM;4_Areia_g_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 5_Silte

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "5_Silte_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\5_Silte.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"5_Silte_g_\">=0 And \"5_Silte_g_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "5", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "5_Silte_g_ MIN;5_Silte_g_ MAX;5_Silte_g_ MEAN;5_Silte_g_ SUM;5_Silte_g_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 6_Materia_Organica

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "6_Materia_Organica_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\6_Materia_Organica.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"6_Materia_\">=0 And \"6_Materia_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "6", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "6_Materia_ MIN;6_Materia_ MAX;6_Materia_ MEAN;6_Materia_ SUM;6_Materia_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 7_Carbono_Organico

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "7_Carbono_Organico_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\7_Carbono_Organico.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"7_Carbono_\">=0 And \"7_Carbono_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "7", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "7_Carbono_ MIN;7_Carbono_ MAX;7_Carbono_ MEAN;7_Carbono_ SUM;7_Carbono_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 8_CTC_Total

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "8_CTC_Total_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\8_CTC_Total.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"8_CTC_Tota\">=0 And \"8_CTC_Tota\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "8", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "8_CTC_Tota MIN;8_CTC_Tota MAX;8_CTC_Tota MEAN;8_CTC_Tota SUM;8_CTC_Tota COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 9_pH_Cloreto_de_Calcio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "9_pH_Cloreto_de_Calcio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\9_pH_Cloreto_de_Calcio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"9_pH_Clore\">=0 And \"9_pH_Clore\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "9", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "9_pH_Clore MIN;9_pH_Clore MAX;9_pH_Clore MEAN;9_pH_Clore SUM;9_pH_Clore COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 10_Saturacao_de_Bases

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "10_Saturacao_de_Bases_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\10_Saturacao_de_Bases.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"10_Saturac\">=0 And \"10_Saturac\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "10", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "10_Saturac MIN;10_Saturac MAX;10_Saturac MEAN;10_Saturac SUM;10_Saturac COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 11_Calcio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "11_Calcio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\11_Calcio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"11_Calcio_\">=0 And \"11_Calcio_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "11", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "11_Calcio_ MIN;11_Calcio_ MAX;11_Calcio_ MEAN;11_Calcio_ SUM;11_Calcio_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 12_Magnesio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "12_Magnesio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\12_Magnesio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"12_Magnesi\">=0 And \"12_Magnesi\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "12", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "12_Magnesi MIN;12_Magnesi MAX;12_Magnesi MEAN;12_Magnesi SUM;12_Magnesi COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 13_Calcio_Mais_Magnesio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "13_Calcio_Mais_Magnesio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\13_Calcio_Mais_Magnesio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"13_Calcio_\">=0 And \"13_Calcio_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "13", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "13_Calcio_ MIN;13_Calcio_ MAX;13_Calcio_ MEAN;13_Calcio_ SUM;13_Calcio_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 14_Aluminio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "14_Aluminio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\14_Aluminio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"14_Alumini\">=0 And \"14_Alumini\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "14", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "14_Alumini MIN;14_Alumini MAX;14_Alumini MEAN;14_Alumini SUM;14_Alumini COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 15_Hidrogenio_Mais_Aluminio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "15_Hidrogenio_Mais_Aluminio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\15_Hidrogenio_Mais_Aluminio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"15_Hidroge\">=0 And \"15_Hidroge\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "15", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "15_Hidroge MIN;15_Hidroge MAX;15_Hidroge MEAN;15_Hidroge SUM;15_Hidroge COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 16_Saturacao_por_Aluminio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "16_Saturacao_por_Aluminio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\16_Saturacao_por_Aluminio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"16_Saturac\">=0 And \"16_Saturac\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "16", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "16_Saturac MIN;16_Saturac MAX;16_Saturac MEAN;16_Saturac SUM;16_Saturac COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 17_Potassio_ppm

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "17_Potassio_ppm_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\17_Potassio_ppm.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"17_Potassi\">=0 And \"17_Potassi\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "17", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "17_Potassi MIN;17_Potassi MAX;17_Potassi MEAN;17_Potassi SUM;17_Potassi COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 18_Fosforo_Mehlich

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "18_Fosforo_Mehlich_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\18_Fosforo_Mehlich.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"18_Fosforo\">=0 And \"18_Fosforo\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "18", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "18_Fosforo MIN;18_Fosforo MAX;18_Fosforo MEAN;18_Fosforo SUM;18_Fosforo COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 19_Potassio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "19_Potassio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\19_Potassio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"19_Potassi\">=0 And \"19_Potassi\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "19", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "19_Potassi MIN;19_Potassi MAX;19_Potassi MEAN;19_Potassi SUM;19_Potassi COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 20_Enxofre

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "20_Enxofre_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\20_Enxofre.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"20_Enxofre\">=0 And \"20_Enxofre\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "20", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "20_Enxofre MIN;20_Enxofre MAX;20_Enxofre MEAN;20_Enxofre SUM;20_Enxofre COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 21_Boro

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "21_Boro_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\21_Boro.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"21_Boro_mg\">=0 And \"21_Boro_mg\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "21", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "21_Boro_mg MIN;21_Boro_mg MAX;21_Boro_mg MEAN;21_Boro_mg SUM;21_Boro_mg COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 22_Calcio_CTC

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "22_Calcio_CTC_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\22_Calcio_CTC.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"22_Calcio_\">=0 And \"22_Calcio_\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "22", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "22_Calcio_ MIN;22_Calcio_ MAX;22_Calcio_ MEAN;22_Calcio_ SUM;22_Calcio_ COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 23_Magnesio_CTC

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "23_Magnesio_CTC_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\23_Magnesio_CTC.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"23_Magnesi\">=0 And \"23_Magnesi\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "23", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "23_Magnesi MIN;23_Magnesi MAX;23_Magnesi MEAN;23_Magnesi SUM;23_Magnesi COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 24_Potassio_CTC

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "24_Potassio_CTC_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\24_Potassio_CTC.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"24_Potassi\">=0 And \"24_Potassi\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "24", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "24_Potassi MIN;24_Potassi MAX;24_Potassi MEAN;24_Potassi SUM;24_Potassi COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 25_Hidrogenio_Mais_Aluminio_CTC

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "25_Hidrogenio_Mais_Aluminio_CTC_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\25_Hidrogenio_Mais_Aluminio_CTC.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"25_Hidroge\">=0 And \"25_Hidroge\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "25", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "25_Hidroge MIN;25_Hidroge MAX;25_Hidroge MEAN;25_Hidroge SUM;25_Hidroge COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 26_Relacao_Calcio_Magnesio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "26_Relacao_Calcio_Magnesio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\26_Relacao_Calcio_Magnesio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"26_Relacao\">=0 And \"26_Relacao\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "26", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "26_Relacao MIN;26_Relacao MAX;26_Relacao MEAN;26_Relacao SUM;26_Relacao COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 27_Relacao_Calcio_Potassio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "27_Relacao_Calcio_Potassio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\27_Relacao_Calcio_Potassio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"27_Relacao\">=0 And \"27_Relacao\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "27", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "27_Relacao MIN;27_Relacao MAX;27_Relacao MEAN;27_Relacao SUM;27_Relacao COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 28_Relacao_Magnesio_Potassio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "28_Relacao_Magnesio_Potassio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\28_Relacao_Magnesio_Potassio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"28_Relacao\">=0 And \"28_Relacao\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "28", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "28_Relacao MIN;28_Relacao MAX;28_Relacao MEAN;28_Relacao SUM;28_Relacao COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 29_Cobre

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "29_Cobre_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\29_Cobre.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"29_Cobre_m\">=0 And \"29_Cobre_m\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "29", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "29_Cobre_m MIN;29_Cobre_m MAX;29_Cobre_m MEAN;29_Cobre_m SUM;29_Cobre_m COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 30_Ferro

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "30_Ferro_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\30_Ferro.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"30_Ferro_m\">=0 And \"30_Ferro_m\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "30", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "30_Ferro_m MIN;30_Ferro_m MAX;30_Ferro_m MEAN;30_Ferro_m SUM;30_Ferro_m COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 31_Manganes

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "31_Manganes_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\31_Manganes.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"31_Mangane\">=0 And \"31_Mangane\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "31", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "31_Mangane MIN;31_Mangane MAX;31_Mangane MEAN;31_Mangane SUM;31_Mangane COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 32_Zinco

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "32_Zinco_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\32_Zinco.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"32_Zinco_m\">=0 And \"32_Zinco_m\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "32", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "32_Zinco_m MIN;32_Zinco_m MAX;32_Zinco_m MEAN;32_Zinco_m SUM;32_Zinco_m COUNT", "MULTI_PART", "DISSOLVE_LINES")

# 33_Sodio

Entrada = arcpy.GetParameterAsText(0)
if Entrada == '#' or not Entrada:
    Entrada = "33_Sodio_poly"

Field_Added = Entrada
Selected = Field_Added
Field_Calculated = Selected
Saida = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Bruno Vilela Sandoval Moreira\\2023\\Fazenda Santa Rosa\\Processado\\Shapefiles\\2- Calc Stats\\2-Dis_Fields\\33_Sodio.shp"

arcpy.AddField_management(Entrada, "dis", "SHORT", "3",
                          "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.SelectLayerByAttribute_management(
    Field_Added, "NEW_SELECTION", "\"33_Sodio_m\">=0 And \"33_Sodio_m\"<=2000")

arcpy.CalculateField_management(Selected, "dis", "33", "VB", "")

arcpy.Dissolve_management(Field_Calculated, Saida, "dis",
                          "33_Sodio_m MIN;33_Sodio_m MAX;33_Sodio_m MEAN;33_Sodio_m SUM;33_Sodio_m COUNT", "MULTI_PART", "DISSOLVE_LINES")


# ADD FIELDS
# 3_Argila

Entrada = "3_Argila"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 4_Areia

Entrada = "4_Areia"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 5_Silte

Entrada = "5_Silte"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 6_Materia_Organica

Entrada = "6_Materia_Organica"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 7_Carbono_Organico

Entrada = "7_Carbono_Organico"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 8_CTC_Total

Entrada = "8_CTC_Total"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 9_pH_Cloreto_de_Calcio

Entrada = "9_pH_Cloreto_de_Calcio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 10_Saturacao_de_Bases

Entrada = "10_Saturacao_de_Bases"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 11_Calcio

Entrada = "11_Calcio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 12_Magnesio

Entrada = "12_Magnesio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 13_Calcio_Mais_Magnesio

Entrada = "13_Calcio_Mais_Magnesio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 14_Aluminio

Entrada = "14_Aluminio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 15_Hidrogenio_Mais_Aluminio

Entrada = "15_Hidrogenio_Mais_Aluminio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 16_Saturacao_por_Aluminio

Entrada = "16_Saturacao_por_Aluminio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 17_Potassio_ppm

Entrada = "17_Potassio_ppm"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 18_Fosforo_Mehlich

Entrada = "18_Fosforo_Mehlich"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 19_Potassio

Entrada = "19_Potassio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 20_Enxofre

Entrada = "20_Enxofre"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 21_Boro

Entrada = "21_Boro"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 22_Calcio_CTC

Entrada = "22_Calcio_CTC"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 23_Magnesio_CTC

Entrada = "23_Magnesio_CTC"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 24_Potassio_CTC

Entrada = "24_Potassio_CTC"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 25_Hidrogenio_Mais_Aluminio_CTC

Entrada = "25_Hidrogenio_Mais_Aluminio_CTC"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 26_Relacao_Calcio_Magnesio

Entrada = "26_Relacao_Calcio_Magnesio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 27_Relacao_Calcio_Potassio

Entrada = "27_Relacao_Calcio_Potassio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 28_Relacao_Magnesio_Potassio

Entrada = "28_Relacao_Magnesio_Potassio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 29_Cobre

Entrada = "29_Cobre"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 30_Ferro

Entrada = "30_Ferro"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 31_Manganes

Entrada = "31_Manganes"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 32_Zinco

Entrada = "32_Zinco"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# 33_Sodio

Entrada = "33_Sodio"
MIN_ADDED = Entrada
MAX_Added = MIN_ADDED
MEAN_ADDED = MAX_Added
SUM_ADDED = MEAN_ADDED
COUNT_ADDED = SUM_ADDED

arcpy.AddField_management(Entrada, "MIN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MIN_ADDED, "MAX", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MAX_Added, "MEAN", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(MEAN_ADDED, "SUM", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(SUM_ADDED, "COUNT", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

# CALC FIELDS
# 3_Argila

Entrada = "3_Argila"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_3_Argi]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_3_Argi]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_3_Arg]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_3_Argi]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_3_Ar]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_3_Argi;MAX_3_Argi;MEAN_3_Arg;SUM_3_Argi;COUNT_3_Ar")

# 4_Areia

Entrada = "4_Areia"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_4_Arei]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_4_Arei]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_4_Are]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_4_Arei]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_4_Ar]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_4_Arei;MAX_4_Arei;MEAN_4_Are;SUM_4_Arei;COUNT_4_Ar")

# 5_Silte

Entrada = "5_Silte"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_5_Silt]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_5_Silt]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_5_Sil]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_5_Silt]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_5_Si]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_5_Silt;MAX_5_Silt;MEAN_5_Sil;SUM_5_Silt;COUNT_5_Si")

# 6_Materia_Organica

Entrada = "6_Materia_Organica"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_6_Mate]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_6_Mate]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_6_Mat]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_6_Mate]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_6_Ma]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_6_Mate;MAX_6_Mate;MEAN_6_Mat;SUM_6_Mate;COUNT_6_Ma")

# 7_Carbono_Organico

Entrada = "7_Carbono_Organico"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_7_Carb]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_7_Carb]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_7_Car]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_7_Carb]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_7_Ca]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_7_Carb;MAX_7_Carb;MEAN_7_Car;SUM_7_Carb;COUNT_7_Ca")

# 8_CTC_Total

Entrada = "8_CTC_Total"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_8_CTC_]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_8_CTC_]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_8_CTC]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_8_CTC_]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_8_CT]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_8_CTC_;MAX_8_CTC_;MEAN_8_CTC;SUM_8_CTC_;COUNT_8_CT")

# 9_pH_Cloreto_de_Calcio

Entrada = "9_pH_Cloreto_de_Calcio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_9_pH_C]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_9_pH_C]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_9_pH_]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_9_pH_C]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_9_pH]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_9_pH_C;MAX_9_pH_C;MEAN_9_pH_;SUM_9_pH_C;COUNT_9_pH")

# 10_Saturacao_de_Bases

Entrada = "10_Saturacao_de_Bases"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_10_Sat]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_10_Sat]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_10_Sa]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_10_Sat]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_10_S]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_10_Sat;MAX_10_Sat;MEAN_10_Sa;SUM_10_Sat;COUNT_10_S")

# 11_Calcio

Entrada = "11_Calcio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_11_Cal]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_11_Cal]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_11_Ca]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_11_Cal]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_11_C]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_11_Cal;MAX_11_Cal;MEAN_11_Ca;SUM_11_Cal;COUNT_11_C")

# 12_Magnesio

Entrada = "12_Magnesio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_12_Mag]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_12_Mag]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_12_Ma]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_12_Mag]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_12_M]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_12_Mag;MAX_12_Mag;MEAN_12_Ma;SUM_12_Mag;COUNT_12_M")

# 13_Calcio_Mais_Magnesio

Entrada = "13_Calcio_Mais_Magnesio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_13_Cal]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_13_Cal]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_13_Ca]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_13_Cal]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_13_C]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_13_Cal;MAX_13_Cal;MEAN_13_Ca;SUM_13_Cal;COUNT_13_C")

# 14_Aluminio

Entrada = "14_Aluminio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_14_Alu]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_14_Alu]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_14_Al]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_14_Alu]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_14_A]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_14_Alu;MAX_14_Alu;MEAN_14_Al;SUM_14_Alu;COUNT_14_A")

# 15_Hidrogenio_Mais_Aluminio

Entrada = "15_Hidrogenio_Mais_Aluminio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_15_Hid]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_15_Hid]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_15_Hi]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_15_Hid]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_15_H]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_15_Hid;MAX_15_Hid;MEAN_15_Hi;SUM_15_Hid;COUNT_15_H")

# 16_Saturacao_por_Aluminio

Entrada = "16_Saturacao_por_Aluminio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_16_Sat]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_16_Sat]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_16_Sa]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_16_Sat]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_16_S]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_16_Sat;MAX_16_Sat;MEAN_16_Sa;SUM_16_Sat;COUNT_16_S")

# 17_Potassio_ppm

Entrada = "17_Potassio_ppm"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_17_Pot]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_17_Pot]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_17_Po]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_17_Pot]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_17_P]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_17_Pot;MAX_17_Pot;MEAN_17_Po;SUM_17_Pot;COUNT_17_P")

# 18_Fosforo_Mehlich

Entrada = "18_Fosforo_Mehlich"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_18_Fos]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_18_Fos]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_18_Fo]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_18_Fos]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_18_F]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_18_Fos;MAX_18_Fos;MEAN_18_Fo;SUM_18_Fos;COUNT_18_F")

# 19_Potassio

Entrada = "19_Potassio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_19_Pot]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_19_Pot]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_19_Po]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_19_Pot]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_19_P]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_19_Pot;MAX_19_Pot;MEAN_19_Po;SUM_19_Pot;COUNT_19_P")

# 20_Enxofre

Entrada = "20_Enxofre"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_20_Enx]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_20_Enx]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_20_En]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_20_Enx]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_20_E]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_20_Enx;MAX_20_Enx;MEAN_20_En;SUM_20_Enx;COUNT_20_E")

# 21_Boro

Entrada = "21_Boro"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_21_Bor]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_21_Bor]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_21_Bo]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_21_Bor]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_21_B]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_21_Bor;MAX_21_Bor;MEAN_21_Bo;SUM_21_Bor;COUNT_21_B")

# 22_Calcio_CTC

Entrada = "22_Calcio_CTC"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_22_Cal]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_22_Cal]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_22_Ca]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_22_Cal]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_22_C]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_22_Cal;MAX_22_Cal;MEAN_22_Ca;SUM_22_Cal;COUNT_22_C")

# 23_Magnesio_CTC

Entrada = "23_Magnesio_CTC"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_23_Mag]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_23_Mag]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_23_Ma]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_23_Mag]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_23_M]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_23_Mag;MAX_23_Mag;MEAN_23_Ma;SUM_23_Mag;COUNT_23_M")

# 24_Potassio_CTC

Entrada = "24_Potassio_CTC"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_24_Pot]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_24_Pot]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_24_Po]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_24_Pot]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_24_P]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_24_Pot;MAX_24_Pot;MEAN_24_Po;SUM_24_Pot;COUNT_24_P")

# 25_Hidrogenio_Mais_Aluminio_CTC

Entrada = "25_Hidrogenio_Mais_Aluminio_CTC"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_25_Hid]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_25_Hid]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_25_Hi]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_25_Hid]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_25_H]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_25_Hid;MAX_25_Hid;MEAN_25_Hi;SUM_25_Hid;COUNT_25_H")

# 26_Relacao_Calcio_Magnesio

Entrada = "26_Relacao_Calcio_Magnesio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_26_Rel]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_26_Rel]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_26_Re]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_26_Rel]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_26_R]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_26_Rel;MAX_26_Rel;MEAN_26_Re;SUM_26_Rel;COUNT_26_R")

# 27_Relacao_Calcio_Potassio

Entrada = "27_Relacao_Calcio_Potassio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_27_Rel]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_27_Rel]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_27_Re]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_27_Rel]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_27_R]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_27_Rel;MAX_27_Rel;MEAN_27_Re;SUM_27_Rel;COUNT_27_R")

# 28_Relacao_Magnesio_Potassio

Entrada = "28_Relacao_Magnesio_Potassio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_28_Rel]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_28_Rel]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_28_Re]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_28_Rel]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_28_R]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_28_Rel;MAX_28_Rel;MEAN_28_Re;SUM_28_Rel;COUNT_28_R")

# 29_Cobre

Entrada = "29_Cobre"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_29_Cob]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_29_Cob]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_29_Co]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_29_Cob]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_29_C]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_29_Cob;MAX_29_Cob;MEAN_29_Co;SUM_29_Cob;COUNT_29_C")

# 30_Ferro

Entrada = "30_Ferro"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_30_Fer]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_30_Fer]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_30_Fe]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_30_Fer]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_30_F]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_30_Fer;MAX_30_Fer;MEAN_30_Fe;SUM_30_Fer;COUNT_30_F")

# 31_Manganes

Entrada = "31_Manganes"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_31_Man]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_31_Man]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_31_Ma]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_31_Man]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_31_M]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_31_Man;MAX_31_Man;MEAN_31_Ma;SUM_31_Man;COUNT_31_M")

# 32_Zinco

Entrada = "32_Zinco"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_32_Zin]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_32_Zin]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_32_Zi]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_32_Zin]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_32_Z]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_32_Zin;MAX_32_Zin;MEAN_32_Zi;SUM_32_Zin;COUNT_32_Z")

# 33_Sodio

Entrada = "33_Sodio"
MIN_CALC = Entrada
MAX_Calc = MIN_CALC
MEAN_Calc = MAX_Calc
SUM_Calc = MEAN_Calc
COUNT_Calc = SUM_Calc

arcpy.CalculateField_management(Entrada, "MIN", "[MIN_33_Sod]", "VB", "")

arcpy.CalculateField_management(MIN_CALC, "MAX", "[MAX_33_Sod]", "VB", "")

arcpy.CalculateField_management(MAX_Calc, "MEAN", "[MEAN_33_So]", "VB", "")

arcpy.CalculateField_management(MEAN_Calc, "SUM", "[SUM_33_Sod]", "VB", "")

arcpy.CalculateField_management(SUM_Calc, "COUNT", "[COUNT_33_S]", "VB", "")

arcpy.DeleteField_management(
    Entrada, "MIN_33_Sod;MAX_33_Sod;MEAN_33_So;SUM_33_Sod;COUNT_33_S")
