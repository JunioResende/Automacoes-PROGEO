import arcpy

# 3_Argila
Input = "3_Argila_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\3_Argila.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\3_Argila.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 4_Areia

Input = "4_Areia_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\4_Areia.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\4_Areia.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 5_Silte

Input = "5_Silte_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\5_Silte.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\5_Silte.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 6_Materia_Organica

Input = "6_Materia_Organica_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\6_Materia_Organica.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\6_Materia_Organica.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 7_Carbono_Organico

Input = "7_Carbono_Organico_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\7_Carbono_Organico.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\7_Carbono_Organico.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 8_CTC_Total

Input = "8_CTC_Total_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\8_CTC_Total.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\8_CTC_Total.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 9_pH_Cloreto_de_Calcio

Input = "9_pH_Cloreto_de_Calcio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\9_pH_Cloreto_de_Calcio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\9_pH_Cloreto_de_Calcio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 10_Saturacao_de_Bases

Input = "10_Saturacao_de_Bases_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\10_Saturacao_de_Bases.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\10_Saturacao_de_Bases.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 11_Calcio

Input = "11_Calcio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\11_Calcio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\11_Calcio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 12_Magnesio

Input = "12_Magnesio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\12_Magnesio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\12_Magnesio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 13_Calcio_Mais_Magnesio

Input = "13_Calcio_Mais_Magnesio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\13_Calcio_Mais_Magnesio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\13_Calcio_Mais_Magnesio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 14_Aluminio

Input = "14_Aluminio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\14_Aluminio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\14_Aluminio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 15_Hidrogenio_Mais_Aluminio

Input = "15_Hidrogenio_Mais_Aluminio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\15_Hidrogenio_Mais_Aluminio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\15_Hidrogenio_Mais_Aluminio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 16_Saturacao_por_Aluminio

Input = "16_Saturacao_por_Aluminio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\16_Saturacao_por_Aluminio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\16_Saturacao_por_Aluminio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 17_Potassio_ppm

Input = "17_Potassio_ppm_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\17_Potassio_ppm.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\17_Potassio_ppm.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 18_Fosforo_Mehlich

Input = "18_Fosforo_Mehlich_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\18_Fosforo_Mehlich.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\18_Fosforo_Mehlich.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 19_Potassio

Input = "19_Potassio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\19_Potassio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\19_Potassio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 20_Enxofre

Input = "20_Enxofre_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\20_Enxofre.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\20_Enxofre.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 21_Boro

Input = "21_Boro_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\21_Boro.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\21_Boro.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 22_Calcio_CTC

Input = "22_Calcio_CTC_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\22_Calcio_CTC.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\22_Calcio_CTC.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 23_Magnesio_CTC

Input = "23_Magnesio_CTC_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\23_Magnesio_CTC.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\23_Magnesio_CTC.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 24_Potassio_CTC

Input = "24_Potassio_CTC_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\24_Potassio_CTC.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\24_Potassio_CTC.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 25_Hidrogenio_Mais_Aluminio_CTC

Input = "25_Hidrogenio_Mais_Aluminio_CTC_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\25_Hidrogenio_Mais_Aluminio_CTC.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\25_Hidrogenio_Mais_Aluminio_CTC.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 26_Relacao_Calcio_Magnesio

Input = "26_Relacao_Calcio_Magnesio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\26_Relacao_Calcio_Magnesio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\26_Relacao_Calcio_Magnesio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 27_Relacao_Calcio_Potassio

Input = "27_Relacao_Calcio_Potassio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\27_Relacao_Calcio_Potassio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\27_Relacao_Calcio_Potassio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 28_Relacao_Magnesio_Potassio

Input = "28_Relacao_Magnesio_Potassio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\28_Relacao_Magnesio_Potassio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\28_Relacao_Magnesio_Potassio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 29_Cobre

Input = "29_Cobre_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\29_Cobre.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\29_Cobre.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 30_Ferro

Input = "30_Ferro_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\30_Ferro.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\30_Ferro.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 31_Manganes

Input = "31_Manganes_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\31_Manganes.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\31_Manganes.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 32_Zinco

Input = "32_Zinco_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\32_Zinco.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\32_Zinco.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main


# 33_Sodio

Input = "33_Sodio_poly"
<<<<<<< HEAD
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Marcos Nogueira\\2023\\Fazenda Limoeiro 1\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\33_Sodio.shp"
=======
Output = "G:\\Meu Drive\\Projetos Geo\\Progeo\\Projetos PROGEO\\Márcio Farias de Resende\\2023\\Fazenda Paraiso\\Processado\\Shapefiles\\3-Legends\\2-Dis_Fields\\33_Sodio.shp"
>>>>>>> refs/remotes/origin/main
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
<<<<<<< HEAD
    Field_Area_Calculated, "percent", "([area]*100)/653.32", "VB", "")
=======
    Field_Area_Calculated, "percent", "([area]*100)/975.4779", "VB", "")
>>>>>>> refs/remotes/origin/main
