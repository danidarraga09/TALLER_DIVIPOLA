import csv

from doublelinklist import DoubleLinkedList
from country import Country
from department import Department
from city import City


class Files:

    def read_divipola(self, file_path):

        countries = DoubleLinkedList()

        # Crear Colombia
        colombia = Country("CO", "Colombia")

        countries.append(colombia)

        # Diccionario para no repetir departamentos
        departments = {}

        with open(file_path, encoding="utf-8-sig") as file:

            reader = csv.DictReader(file)

            for row in reader:

                dept_code = row["Código Departamento"]
                dept_name = row["Nombre Departamento"]

                city_code = row["Código Municipio"]
                city_name = row["Nombre Municipio"]

                lat = row["Latitud"]
                lon = row["longitud"]

                # Crear departamento una sola vez
                if dept_code not in departments:

                    department = Department(
                        dept_code,
                        dept_name
                    )

                    countries.add_child(
                        colombia,
                        department
                    )

                    departments[dept_code] = department

                # Crear ciudad
                city = City(
                    city_code,
                    city_name,
                    lat,
                    lon
                )

                # Agregar ciudad al departamento
                countries.add_child(
                    departments[dept_code],
                    city
                )

        return countries

    # Convertir multilista a JSON
    def get_markers(self, multilist):

        markers = []

        current_country = multilist.head

        while current_country:

            if current_country.sub_list:

                current_department = current_country.sub_list.head

                while current_department:

                    if current_department.sub_list:

                        current_city = current_department.sub_list.head

                        while current_city:

                            markers.append({
                                "country": current_country.name,
                                "department": current_department.name,
                                "city": current_city.name,
                                "lat": current_city.lat,
                                "lon": current_city.lon
                            })

                            current_city = current_city.next

                    current_department = current_department.next

            current_country = current_country.next

        return markers