def traducir_entrada(respuestas):
    return {
        'AgeCategory': respuestas['Edad'].replace("o más", " or older"),
        'GenHealth': {
            "Pobre": "Poor",
            "Regular": "Fair",
            "Buena": "Good",
            "Muy buena": "Very good",
            "Excelente": "Excellent"
        }[respuestas['Salud general']],
        'DiffWalking': "Yes" if respuestas['Dificultad al caminar'] == "Sí" else "No",
        'Diabetic': {
            "Sí": "Yes",
            "No": "No",
            "No, prediabetes": "No, borderline diabetes",
            "Sí (embarazo)": "Yes (during pregnancy)"
        }[respuestas['Diabetes']],
        'PhysicalHealth': respuestas['Días de mala salud física (últimos 30)'],
        'Smoking': "Yes" if respuestas['Fuma'] == "Sí" else "No",
        'PhysicalActivity': "Yes" if respuestas['Actividad física'] == "Sí" else "No",
        'SkinCancer': "Yes" if respuestas['Cáncer de piel'] == "Sí" else "No"
    }
