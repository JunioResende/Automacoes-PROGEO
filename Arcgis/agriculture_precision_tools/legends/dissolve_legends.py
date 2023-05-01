import arcpy

# 3_Argila
Input = "3_Argila_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\3_Argila.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "3", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 4_Areia

Input = "4_Areia_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\4_Areia.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "4", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 5_Silte

Input = "5_Silte_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\5_Silte.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "5", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 6_Materia_Organica

Input = "6_Materia_Organica_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\6_Materia_Organica.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "6", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 7_Carbono_Organico

Input = "7_Carbono_Organico_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\7_Carbono_Organico.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "7", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 8_CTC_Total

Input = "8_CTC_Total_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\8_CTC_Total.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "8", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 9_pH_Cloreto_de_Calcio

Input = "9_pH_Cloreto_de_Calcio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\9_pH_Cloreto_de_Calcio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(Field_Percent_Added, "atribute", "9", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 10_Saturacao_de_Bases

Input = "10_Saturacao_de_Bases_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\10_Saturacao_de_Bases.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "10", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 11_Calcio

Input = "11_Calcio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\11_Calcio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "11", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 12_Magnesio

Input = "12_Magnesio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\12_Magnesio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "12", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 13_Calcio_Mais_Magnesio

Input = "13_Calcio_Mais_Magnesio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\13_Calcio_Mais_Magnesio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "13", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 14_Aluminio

Input = "14_Aluminio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\14_Aluminio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "14", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 15_Hidrogenio_Mais_Aluminio

Input = "15_Hidrogenio_Mais_Aluminio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\15_Hidrogenio_Mais_Aluminio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "15", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 16_Saturacao_por_Aluminio

Input = "16_Saturacao_por_Aluminio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\16_Saturacao_por_Aluminio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "16", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 17_Potassio_ppm

Input = "17_Potassio_ppm_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\17_Potassio_ppm.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "17", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 18_Fosforo_Mehlich

Input = "18_Fosforo_Mehlich_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\18_Fosforo_Mehlich.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "18", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 19_Potassio

Input = "19_Potassio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\19_Potassio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "19", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 20_Enxofre

Input = "20_Enxofre_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\20_Enxofre.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "20", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 21_Boro

Input = "21_Boro_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\21_Boro.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "21", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 22_Calcio_CTC

Input = "22_Calcio_CTC_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\22_Calcio_CTC.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "22", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 23_Magnesio_CTC

Input = "23_Magnesio_CTC_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\23_Magnesio_CTC.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "23", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 24_Potassio_CTC

Input = "24_Potassio_CTC_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\24_Potassio_CTC.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "24", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 25_Hidrogenio_Mais_Aluminio_CTC

Input = "25_Hidrogenio_Mais_Aluminio_CTC_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\25_Hidrogenio_Mais_Aluminio_CTC.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "25", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 26_Relacao_Calcio_Magnesio

Input = "26_Relacao_Calcio_Magnesio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\26_Relacao_Calcio_Magnesio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "26", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 27_Relacao_Calcio_Potassio

Input = "27_Relacao_Calcio_Potassio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\27_Relacao_Calcio_Potassio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "27", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 28_Relacao_Magnesio_Potassio

Input = "28_Relacao_Magnesio_Potassio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\28_Relacao_Magnesio_Potassio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "28", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 29_Cobre

Input = "29_Cobre_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\29_Cobre.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "29", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 30_Ferro

Input = "30_Ferro_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\30_Ferro.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "30", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 31_Manganes

Input = "31_Manganes_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\31_Manganes.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "31", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 32_Zinco

Input = "32_Zinco_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\32_Zinco.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "32", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")


# 33_Sodio

Input = "33_Sodio_poly"
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Walmir Rocha Carrijo\\2023\\Fazenda Rio Verde\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\33_Sodio.shp"
Atribute_Field_Added = Output
Field_Area_Added = Atribute_Field_Added
Field_Percent_Added = Field_Area_Added
Field_Atribute_Calculated = Field_Percent_Added
Field_Area_Calculated = Field_Atribute_Calculated
Field_Percent_Calculated = Field_Area_Calculated

arcpy.Dissolve_management(Input, Output, "dis", "",
                          "MULTI_PART", "DISSOLVE_LINES")

arcpy.AddField_management(Output, "atribute", "SHORT",
                          "2", "", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Atribute_Field_Added, "area",
                          "DOUBLE", "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.AddField_management(Field_Area_Added, "percent", "DOUBLE",
                          "10", "2", "", "", "NULLABLE", "NON_REQUIRED", "")

arcpy.CalculateField_management(
    Field_Percent_Added, "atribute", "33", "VB", "")

arcpy.CalculateField_management(
    Field_Atribute_Calculated, "area", "!shape.area!/10000", "PYTHON_9.3", "")

arcpy.CalculateField_management(
    Field_Area_Calculated, "percent", "([area]*100)/299.98", "VB", "")
