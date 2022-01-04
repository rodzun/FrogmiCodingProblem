# FrogmiCodingProblem

El repositorio cuenta con dos archivos de extensión .py y un directorio.

* **CodingProblem.py:** Contiene las clases(POO) que constituyen la solución del Coding Problem.
* **CodingProblem_test.py:** Contiene los tests para el archivo anterior haciendo uso del framework unittest.
* **Directorio htmlcov:** Directorio generado por la herramienta **coverage.py** (https://coverage.readthedocs.io/) utilizado para el análisis de cobertura de pruebas unitarias.

## Uso 

### CodingProblem.py

1. Ejecutar el archivo CodingProblem.py.

   ```bash
   py CodingProblem.py
   ```
2. Se mostrará una demostración de las funcionalidades precargadas en el archivo. 

   ```bash
   #Número de incidentes creados
   Number of Incidents: 4, 
   
   #Descripción detallada de los incidentes
   Incidents: 
   [Incident Description: Prueba, Status: Solved, Date Open: 01/04/2022, 04:10:53, Date Solved: 01/04/2022, 04:10:53, 
   Incident Description: Prueba, Status: Solved, Date Open: 01/03/2022, 00:35:22, Date Solved: 01/04/2022, 04:10:53, 
   Incident Description: Prueba, Status: Solved, Date Open: 01/04/2022, 11:35:22, Date Solved: 01/04/2022, 04:10:53,    
   Incident Description: Prueba, Status: Open, Date Open: 01/01/2022, 11:35:22, Date Solved: None]
   
   #Resultado de la función incident_status() con rango de fechas que incluye los incidentes anteriores
   {'open_cases': 1, 'closed_cases': 3, 'average_solution': '6:43:40.485138', 'maximum_solution': '2 days, 16:35:30.726876'}    
   
   #Resultado de la función incident_status() con rango de fechas que NO incluye los incidentes anteriores
   {'open_cases': 0, 'closed_cases': 0, 'average_solution': '0', 'maximum_solution': '0:00:00'}
    ```
    
### CodingProblem_test.py

1. Ejecutar el archivo CodingProblem_test.py.

   ```bash
   py CodingProblem_test.py
   ```
2. Se mostrará el resultado de los 11 tests propuestos.   
   
   ```bash
   test_details (__main__.IncidentTest) ... ok
   test_repr_open (__main__.IncidentTest) ... ok
   test_repr_solved (__main__.IncidentTest) ... ok
   test_add_incident (__main__.StoreTest) ... ok
   test_average_solution (__main__.StoreTest) ... ok
   test_average_solution_zero_incidents (__main__.StoreTest) ... ok      
   test_maximum_solution (__main__.StoreTest) ... ok
   test_open_cases (__main__.StoreTest) ... ok
   test_solve_incident (__main__.StoreTest) ... ok
   test_solved_cases (__main__.StoreTest) ... ok
   test_str (__main__.StoreTest) ... ok
 
   ----------------------------------------------------------------------
   Ran 11 tests in 0.011s

   OK
   ``` 
   
### htmlcov > index.html

1. Abrir el archivo en un navegador. 
   
   ![image](https://user-images.githubusercontent.com/41459351/148038856-67f7198d-8914-4be2-8a28-297ef0127e3d.png)
   
Para replicar los resultados es necesario:

1. Instalar la herramienta **coverage.py**.

   ```bash
   pip install coverage
   ```

2. Correr el archivo de tests con la herramienta.
   
   ```bash
   coverage run CodingProblem_test.py
   ```

3. Generar directorio **htmlcov** con el archivo **index.html** dentro.

   ```bash
   coverage html
   ```
   
4. Para un mayor detalle sobre la cobertura de pruebas unitarias linea por linea se encuentra el archivo **CodingProblem_test_py.html**.


