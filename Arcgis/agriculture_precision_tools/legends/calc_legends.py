import arcpy

# Argila
# Variaveis
input_shapefile = "3_Argila_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\3_Argila.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\" >=0 And \"3_Argila_g\"<120")
arcpy.CalculateField_management(input_shapefile, "dis", "11", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=120 And \"3_Argila_g\"<150")
arcpy.CalculateField_management(input_shapefile, "dis", "10", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=150 And \"3_Argila_g\"<150")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=180 And \"3_Argila_g\"<200")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=200 And \"3_Argila_g\"<220")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=220 And \"3_Argila_g\"<240")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=240 And \"3_Argila_g\"<260")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=260 And \"3_Argila_g\"<280")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=280 And \"3_Argila_g\"<300")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=300 And \"3_Argila_g\"<400")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"3_Argila_g\">=400 And \"3_Argila_g\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "3", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# Areia
# Variaveis
input_shapefile = "4_Areia_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\4_Areia.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\" >=0 And \"4_Areia_g_\"<350")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=350 And \"4_Areia_g_\"<400")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=400 And \"4_Areia_g_\"<450")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=450 And \"4_Areia_g_\"<500")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=500 And \"4_Areia_g_\"<550")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=550 And \"4_Areia_g_\"<600")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=600 And \"4_Areia_g_\"<700")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=700 And \"4_Areia_g_\"<800")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"4_Areia_g_\">=800 And \"4_Areia_g_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "4", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# Silte
# Variaveis
input_shapefile = "5_Silte_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\5_Silte.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\" >=0 And \"5_Silte_g_\"<50")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\">=50 And \"5_Silte_g_\"<100")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\">=100 And \"5_Silte_g_\"<150")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\">=150 And \"5_Silte_g_\"<200")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\">=200 And \"5_Silte_g_\"<250")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"5_Silte_g_\">=250 And \"5_Silte_g_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "5", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# Materia_Organica
# Variaveis
input_shapefile = "6_Materia_Organica_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\6_Materia_Organica.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\" >=0 And \"6_Materia_\"<17")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=17 And \"6_Materia_\"<20")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=20 And \"6_Materia_\"<22")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=22 And \"6_Materia_\"<25")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=25 And \"6_Materia_\"<28")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=28 And \"6_Materia_\"<33")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=33 And \"6_Materia_\"<35")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=35 And \"6_Materia_\"<38")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"6_Materia_\">=38 And \"6_Materia_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "6", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# Carbono_Organico
# Variaveis
input_shapefile = "7_Carbono_Organico_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\7_Carbono_Organico.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\" >=0 And \"7_Carbono_\"<12")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\">=12 And \"7_Carbono_\"<13.90")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\">=13.90 And \"7_Carbono_\"<15.80")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\">=15.80 And \"7_Carbono_\"<17.70")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\">=17.70 And \"7_Carbono_\"<19.60")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"7_Carbono_\">=19.60 And \"7_Carbono_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "7", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 8_CTC_Total_poly
# Variaveis
input_shapefile = "8_CTC_Total_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\8_CTC_Total.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\" >=0 And \"8_CTC_Tota\"<1.6")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=1.6 And \"8_CTC_Tota\"<3")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=3 And \"8_CTC_Tota\"<4")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=4 And \"8_CTC_Tota\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=5 And \"8_CTC_Tota\"<6")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=6 And \"8_CTC_Tota\"<7")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=7 And \"8_CTC_Tota\"<8")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=8 And \"8_CTC_Tota\"<9")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"8_CTC_Tota\">=9 And \"8_CTC_Tota\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "8", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 9_pH_Cloreto_de_Calcio
# Variaveis
input_shapefile = "9_pH_Cloreto_de_Calcio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\9_pH_Cloreto_de_Calcio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\" >=0 And \"9_pH_Clore\"<4.5")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\">=4.5 And \"9_pH_Clore\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\">=5 And \"9_pH_Clore\"<5.4")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\">=5.4 And \"9_pH_Clore\"<6")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\">=6 And \"9_pH_Clore\"<6.4")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"9_pH_Clore\">=6.4 And \"9_pH_Clore\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "9", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 10_Saturacao_de_Bases_poly
# Variaveis
input_shapefile = "10_Saturacao_de_Bases_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\10_Saturacao_de_Bases.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\" >=0 And \"10_Saturac\"<25")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=25 And \"10_Saturac\"<30")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=30 And \"10_Saturac\"<35")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=35 And \"10_Saturac\"<40")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=40 And \"10_Saturac\"<45")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=45 And \"10_Saturac\"<50")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=50 And \"10_Saturac\"<55")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=55 And \"10_Saturac\"<60")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"10_Saturac\">=60 And \"10_Saturac\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "10", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 11_Calcio_poly
# Variaveis
input_shapefile = "11_Calcio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\11_Calcio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\" >=0 And \"11_Calcio_\"<0.4")
arcpy.CalculateField_management(input_shapefile, "dis", "10", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=0.4 And \"11_Calcio_\"<1")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=1 And \"11_Calcio_\"<1.5")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=1.5 And \"11_Calcio_\"<2")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=2 And \"11_Calcio_\"<2.5")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=2.5 And \"11_Calcio_\"<3")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=3 And \"11_Calcio_\"<3.5")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=3.5 And \"11_Calcio_\"<4")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=4 And \"11_Calcio_\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"11_Calcio_\">=5 And \"11_Calcio_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "11", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 12_Magnesio_poly
# Variaveis
input_shapefile = "12_Magnesio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\12_Magnesio_poly.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\" >=0 And \"12_Magnesi\"<0.4")
arcpy.CalculateField_management(input_shapefile, "dis", "12", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=0.4 And \"12_Magnesi\"<1")
arcpy.CalculateField_management(input_shapefile, "dis", "11", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=1 And \"12_Magnesi\"<1.5")
arcpy.CalculateField_management(input_shapefile, "dis", "10", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=1.5 And \"12_Magnesi\"<2")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=2 And \"12_Magnesi\"<2.5")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=2.5 And \"12_Magnesi\"<3")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=3 And \"12_Magnesi\"<3.5")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=3.5 And \"12_Magnesi\"<4")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=4 And \"12_Magnesi\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=5 And \"12_Magnesi\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=4 And \"12_Magnesi\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"12_Magnesi\">=5 And \"12_Magnesi\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "12", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 13_Calcio_Mais_Magnesio_poly
# Variaveis
input_shapefile = "13_Calcio_Mais_Magnesio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\13_Calcio_Mais_Magnesio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\" >=0 And \"13_Calcio_\"<4.3")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\">=4.3 And \"13_Calcio_\"<4.7")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\">=4.7 And \"13_Calcio_\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\">=5 And \"13_Calcio_\"<5.55")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\">=5.55 And \"13_Calcio_\"<7")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"13_Calcio_\">=7 And \"13_Calcio_\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "13", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 14_Aluminio_poly
# Variaveis
input_shapefile = "14_Aluminio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\14_Aluminio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"14_Alumini\">=0 And \"14_Alumini\"<0.2")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"14_Alumini\">=0.2 And \"14_Alumini\"<0.5")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"14_Alumini\">=0.5 And \"14_Alumini\"<0.6")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"14_Alumini\">=0.6 And \"14_Alumini\"<1")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "14", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")

# 15_Hidrogenio_Mais_Aluminio_poly
# Variaveis
input_shapefile = "15_Hidrogenio_Mais_Aluminio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\15_Hidrogenio_Mais_Aluminio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\" >=0 And \"15_Hidroge\"<2")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\">=2 And \"15_Hidroge\"<3")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\">=3 And \"15_Hidroge\"<4")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\">=4 And \"15_Hidroge\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\">=5 And \"15_Hidroge\"<6")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"15_Hidroge\">=6 And \"15_Hidroge\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "15", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")

# 16_Saturacao_por_Aluminio_poly
# Variaveis
input_shapefile = "16_Saturacao_por_Aluminio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\16_Saturacao_por_Aluminio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"16_Saturac\">=0 And \"16_Saturac\"<2")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"16_Saturac\">=2 And \"16_Saturac\"<4")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"16_Saturac\">=4 And \"16_Saturac\"<6")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"16_Saturac\">=6 And \"16_Saturac\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "16", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 17_Potassio_ppm_poly
# Variaveis
input_shapefile = "17_Potassio_ppm_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\17_Potassio_ppm.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\" >=0 And \"17_Potassi\"<15")
arcpy.CalculateField_management(input_shapefile, "dis", "20", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=15 And \"17_Potassi\"<20")
arcpy.CalculateField_management(input_shapefile, "dis", "19", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=20 And \"17_Potassi\"<25")
arcpy.CalculateField_management(input_shapefile, "dis", "18", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=25 And \"17_Potassi\"<30")
arcpy.CalculateField_management(input_shapefile, "dis", "17", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=30 And \"17_Potassi\"<35")
arcpy.CalculateField_management(input_shapefile, "dis", "16", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=35 And \"17_Potassi\"<40")
arcpy.CalculateField_management(input_shapefile, "dis", "15", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=40 And \"17_Potassi\"<45")
arcpy.CalculateField_management(input_shapefile, "dis", "14", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=45 And \"17_Potassi\"<50")
arcpy.CalculateField_management(input_shapefile, "dis", "13", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=50 And \"17_Potassi\"<55")
arcpy.CalculateField_management(input_shapefile, "dis", "12", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=55 And \"17_Potassi\"<60")
arcpy.CalculateField_management(input_shapefile, "dis", "11", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=60 And \"17_Potassi\"<65")
arcpy.CalculateField_management(input_shapefile, "dis", "10", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=65 And \"17_Potassi\"<70")
arcpy.CalculateField_management(input_shapefile, "dis", "9", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=70 And \"17_Potassi\"<75")
arcpy.CalculateField_management(input_shapefile, "dis", "8", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=75 And \"17_Potassi\"<80")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=80 And \"17_Potassi\"<90")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=90 And \"17_Potassi\"<100")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=100 And \"17_Potassi\"<120")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=120 And \"17_Potassi\"<140")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=140 And \"17_Potassi\"<160")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"17_Potassi\">=160 And \"17_Potassi\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "17", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")

# 18_Fosforo_Mehlich_poly
# Variaveis
input_shapefile = "18_Fosforo_Mehlich_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\18_Fosforo_Mehlich.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"18_Fosforo\">=0 And \"18_Fosforo\"<5")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"18_Fosforo\">=5 And \"18_Fosforo\"<10")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"18_Fosforo\">=10 And \"18_Fosforo\"<14")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"18_Fosforo\">=14 And \"18_Fosforo\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "18", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 19_Potassio_poly
# Variaveis
input_shapefile = "19_Potassio_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\19_Potassio.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\" >=0 And \"19_Potassi\"<0.13")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.13 And \"19_Potassi\"<0.14")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.14 And \"19_Potassi\"<0.17")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.17 And \"19_Potassi\"<0.21")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.21 And \"19_Potassi\"<0.24")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.24 And \"19_Potassi\"<0.28")
arcpy.CalculateField_management(input_shapefile, "dis", "2", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"19_Potassi\">=0.28 And \"19_Potassi\"<1")
arcpy.CalculateField_management(input_shapefile, "dis", "1", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "19", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 20_Enxofre_poly
# Variaveis
input_shapefile = "20_Enxofre_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\20_Enxofre.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"20_Enxofre\" >=0 And \"20_Enxofre\"<2.5")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"20_Enxofre\">=2.5 And \"20_Enxofre\"<4.9")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"20_Enxofre\">=4.9 And \"20_Enxofre\"<9")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"20_Enxofre\">=9 And \"20_Enxofre\"<10")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"20_Enxofre\">=10 And \"20_Enxofre\"<18")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "20", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")


# 21_Boro_poly
# Variaveis
input_shapefile = "21_Boro_poly"
export_shapefile = "C:\\Users\\junio\\Desktop\\Nova pasta\\21_Boro.shp"

arcpy.AddField_management(input_shapefile, "dis", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

# Select and Calculate
arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"21_Boro_mg\" >=0 And \"21_Boro_mg\"<0.15")
arcpy.CalculateField_management(input_shapefile, "dis", "7", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"21_Boro_mg\">=0.15 And \"21_Boro_mg\"<0.35")
arcpy.CalculateField_management(input_shapefile, "dis", "6", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"21_Boro_mg\">=0.35 And \"21_Boro_mg\"<0.60")
arcpy.CalculateField_management(input_shapefile, "dis", "5", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"21_Boro_mg\">=0.60 And \"21_Boro_mg\"<0.9")
arcpy.CalculateField_management(input_shapefile, "dis", "4", "VB", "")

arcpy.SelectLayerByAttribute_management(
    input_shapefile, "NEW_SELECTION", "\"21_Boro_mg\">=0.90 And \"21_Boro_mg\"<1000")
arcpy.CalculateField_management(input_shapefile, "dis", "3", "VB", "")

# Dissolve
arcpy.Dissolve_management(
    input_shapefile, export_shapefile, "dis", "", "MULTI_PART", "DISSOLVE_LINES")
arcpy.AddField_management(export_shapefile, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(export_shapefile, "atribute", "21", "VB", "")
arcpy.AddField_management(export_shapefile, "area", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "area", "!shape.area!/10000", "PYTHON_9.3", "")
arcpy.AddField_management(export_shapefile, "percent",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")
arcpy.CalculateField_management(
    export_shapefile, "percent", "([area]*100)/513.50", "VB", "")
