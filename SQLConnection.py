from revoscalepy import RxInSqlServer, RxLocalSeq

# Load the connection string and compute context definitions.
connection_string = "Driver=ODBC Driver 13 for SQL Server;Server=13.91.49.253;Database=Hospital;Uid=revotester;Pwd=T3sterPwd"
sql = RxInSqlServer(connection_string=connection_string)
local = RxLocalSeq()

# column_info = rx_create_col_info(LoS)  # Not supported yet.
#col_type_and_factor_info = {"irondef": {"type": "factor", "levels":["0", "1"]},
#                           "psychother": {"type": "factor", "levels":["0", "1"]},
#                           "pulse": {"type": "numeric"},
#                           "malnutrition": {"type": "factor", "levels":["0", "1"]},
#                           "pneum": {"type": "factor", "levels":["0", "1"]},
#                           "respiration": {"type": "numeric"},
#                           "eid": {"type": "integer"},
#                           "hematocrit": {"type": "numeric"},
#                           "sodium": {"type": "numeric"},
#                           "psychologicaldisordermajor": {"type": "factor", "levels":["0", "1"]},
#                           "hemo": {"type": "factor", "levels":["0", "1"]},
#                           "dialysisrenalendstage": {"type": "factor", "levels":["0", "1"]},
#                           "discharged": {"type": "factor"},
#                           "facid": {"type": "factor", "levels":["B", "A", "E", "D", "C"]},
#                           "rcount": {"type": "factor", "levels":["0", "5+", "1", "4", "2", "3"]},
#                           "substancedependence": {"type": "factor", "levels":["0", "1"]},
#                           "number_of_issues": {"type": "factor", "levels":["0", "2", "1", "3", "4", "5", "6", "7", "8", "9"]},
#                           "bmi": {"type": "numeric"},
#                           "secondarydiagnosisnonicd9": {"type": "factor", "levels":["4", "1", "2", "3", "0", "7", "6", "10", "8", "5", "9"]},
#                           "glucose": {"type": "numeric"},
#                           "vdate": {"type": "factor"},
#                           "asthma": {"type": "factor", "levels":["0", "1"]},
#                           "depress": {"type": "factor", "levels":["0", "1"]},
#                           "gender": {"type": "factor", "levels":["F", "M"]},
#                           "fibrosisandother": {"type": "factor", "levels":["0", "1"]},
#                           "lengthofstay": {"type": "numeric"},
#                           "neutrophils": {"type": "numeric"},
#                           "bloodureanitro": {"type": "numeric"},
#                           "creatinine": {"type": "numeric"}}

#col_type_info = {"eid": {'type': 'integer'},
#                "vdate": {'type': 'character'},
#                "rcount": {'type': 'character'},
#                "gender": {'type': 'factor'},
#                "dialysisrenalendstage": {'type': 'factor'},
#                "asthma": {'type': 'factor'},
#                "irondef": {'type': 'factor'},
#                "pneum": {'type': 'factor'},
#                "substancedependence": {'type': 'factor'},
#                "psychologicaldisordermajor": {'type': 'factor'},
#                "depress": {'type': 'factor'},
#                "psychother": {'type': 'factor'},
#                "fibrosisandother": {'type': 'factor'},
#                "malnutrition": {'type': 'factor'},
#                "hemo": {'type': 'factor'},
#                "hematocrit": {'type': 'numeric'},
#                "neutrophils": {'type': 'numeric'},
#                "sodium": {'type': 'numeric'},
#                "glucose": {'type': 'numeric'},
#                "bloodureanitro": {'type': 'numeric'},
#                "creatinine": {'type': 'numeric'},
#                "bmi": {'type': 'numeric'},
#                "pulse": {'type': 'numeric'},
#                "respiration": {'type': 'numeric'},
#                "secondarydiagnosisnonicd9": {'type': 'factor'},
#                "discharged": {'type': 'character'},
#                "facid": {'type': 'factor'},
#                "lengthofstay": {'type': 'integer'}}