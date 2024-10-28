from medicine_list.models import MedicineList,Manufacturer

def generate_manufacturer_data():
    manufacturer_data = [
        {
            "name": "Sundarban Pharmaceuticals",
            "description": "One of the largest pharmaceutical companies in Bangladesh, providing a wide range of medicines."
        },
        {
            "name": "Incepta Pharmaceuticals",
            "description": "A leading pharmaceutical company known for high-quality generics and branded medications."
        },
        {
            "name": "Beximco Pharmaceuticals",
            "description": "A prominent manufacturer focused on providing affordable healthcare solutions."
        },
        {
            "name": "Eskayef Pharmaceuticals",
            "description": "An innovative pharmaceutical company dedicated to improving the quality of healthcare in Bangladesh."
        }
    ]

    for item in manufacturer_data:
        manufacturer,_ = Manufacturer.objects.get_or_create(
            name = item['name'],
            description = item['description']
        )


def generate_medicine_data():
    medicine_data = [
        {"name": "Napa", "generic_name": "Paracetamol", "description": "Used to relieve pain and reduce fever.", "price": 1.50, "batch_number": 1021, "other_related_detailes": "500 mg tablet; for pain relief."},
        {"name": "Seclo", "generic_name": "Omeprazole", "description": "Used to treat acid reflux and peptic ulcer disease.", "price": 6.00, "batch_number": 1045, "other_related_detailes": "20 mg capsule; taken before meals."},
        {"name": "Losectil", "generic_name": "Omeprazole", "description": "Reduces stomach acid production.", "price": 5.50, "batch_number": 1098, "other_related_detailes": "20 mg capsule; for gastric issues."},
        {"name": "Cef-3", "generic_name": "Cefixime", "description": "Treats bacterial infections.", "price": 15.00, "batch_number": 1112, "other_related_detailes": "200 mg tablet; with or without food."},
        {"name": "Azithrocin", "generic_name": "Azithromycin", "description": "For bacterial infections.", "price": 25.00, "batch_number": 1150, "other_related_detailes": "500 mg tablet; once daily."},
        {"name": "Rimactane", "generic_name": "Rifampicin", "description": "Treats tuberculosis.", "price": 30.00, "batch_number": 1202, "other_related_detailes": "300 mg capsule; for TB therapy."},
        {"name": "Mycobutin", "generic_name": "Rifabutin", "description": "Used for TB and MAC.", "price": 45.00, "batch_number": 1244, "other_related_detailes": "150 mg capsule; daily for TB management."},
        {"name": "Alatrol", "generic_name": "Cetirizine", "description": "Relieves allergies.", "price": 2.00, "batch_number": 1275, "other_related_detailes": "10 mg tablet; once daily."},
        {"name": "Filmet", "generic_name": "Metronidazole", "description": "For GI infections.", "price": 8.00, "batch_number": 1301, "other_related_detailes": "400 mg tablet; for bacterial and parasitic infections."},
        {"name": "Monas", "generic_name": "Montelukast", "description": "Prevents asthma attacks.", "price": 18.50, "batch_number": 1350, "other_related_detailes": "10 mg tablet; daily dose."},
        {"name": "Renitidin", "generic_name": "Ranitidine", "description": "Reduces stomach acid.", "price": 3.50, "batch_number": 1403, "other_related_detailes": "150 mg tablet; taken before meals."},
        {"name": "Telfast", "generic_name": "Fexofenadine", "description": "Treats allergy symptoms.", "price": 10.00, "batch_number": 1444, "other_related_detailes": "120 mg tablet; taken once daily."},
        {"name": "Maxpro", "generic_name": "Esomeprazole", "description": "Used for GERD treatment.", "price": 12.00, "batch_number": 1482, "other_related_detailes": "20 mg tablet; taken before meals."},
        {"name": "Myolaxin", "generic_name": "Methocarbamol", "description": "Relieves muscle pain.", "price": 7.00, "batch_number": 1502, "other_related_detailes": "500 mg tablet; taken for muscle spasms."},
        {"name": "Nizonide", "generic_name": "Nitazoxanide", "description": "For intestinal infections.", "price": 20.00, "batch_number": 1523, "other_related_detailes": "500 mg tablet; treats parasitic infections."},
        {"name": "Xinc", "generic_name": "Zinc Sulphate", "description": "Supplement for immunity.", "price": 1.20, "batch_number": 1550, "other_related_detailes": "20 mg tablet; daily supplement."},
        {"name": "Ace", "generic_name": "Paracetamol", "description": "Reduces fever and pain.", "price": 1.40, "batch_number": 1572, "other_related_detailes": "500 mg tablet; for pain relief."},
        {"name": "Flucloxacillin", "generic_name": "Flucloxacillin", "description": "Antibiotic for skin infections.", "price": 22.00, "batch_number": 1595, "other_related_detailes": "500 mg capsule; four times daily."},
        {"name": "Vit-C", "generic_name": "Ascorbic Acid", "description": "Vitamin C supplement.", "price": 2.50, "batch_number": 1620, "other_related_detailes": "500 mg tablet; boosts immunity."},
        {"name": "Econazole", "generic_name": "Econazole Nitrate", "description": "Antifungal cream.", "price": 15.00, "batch_number": 1645, "other_related_detailes": "1% cream; applied twice daily."},
        {"name": "Fexo", "generic_name": "Fexofenadine", "description": "For allergy relief.", "price": 8.50, "batch_number": 1671, "other_related_detailes": "60 mg tablet; daily dose."},
        {"name": "Montair", "generic_name": "Montelukast", "description": "Used for allergy relief.", "price": 19.00, "batch_number": 1701, "other_related_detailes": "10 mg tablet; daily for asthma and allergies."},
        {"name": "Bivator", "generic_name": "Atorvastatin", "description": "Lowers cholesterol levels.", "price": 22.00, "batch_number": 1723, "other_related_detailes": "10 mg tablet; daily dose."},
        {"name": "Angilock", "generic_name": "Losartan", "description": "For blood pressure management.", "price": 15.00, "batch_number": 1752, "other_related_detailes": "50 mg tablet; daily dose for BP control."},
        {"name": "Amdocal", "generic_name": "Amlodipine", "description": "Treats high blood pressure.", "price": 8.00, "batch_number": 1778, "other_related_detailes": "5 mg tablet; daily dose."},
        {"name": "Clopirel", "generic_name": "Clopidogrel", "description": "Prevents blood clots.", "price": 30.00, "batch_number": 1800, "other_related_detailes": "75 mg tablet; once daily."},
        {"name": "Isotab", "generic_name": "Isosorbide Mononitrate", "description": "For heart conditions.", "price": 12.00, "batch_number": 1825, "other_related_detailes": "20 mg tablet; once or twice daily."},
        {"name": "Natrilix", "generic_name": "Indapamide", "description": "Treats high blood pressure.", "price": 9.50, "batch_number": 1852, "other_related_detailes": "1.5 mg tablet; daily dose for BP management."},
        {"name": "Neotack", "generic_name": "Enalapril", "description": "For blood pressure control.", "price": 10.00, "batch_number": 1870, "other_related_detailes": "5 mg tablet; once daily."},
        {"name": "Gluformin", "generic_name": "Metformin", "description": "Controls blood sugar.", "price": 5.50, "batch_number": 1903, "other_related_detailes": "500 mg tablet; twice daily for diabetes."},
        {"name": "Janumet", "generic_name": "Sitagliptin + Metformin", "description": "For diabetes management.", "price": 40.00, "batch_number": 1930, "other_related_detailes": "50/500 mg tablet; twice daily."},
        {"name": "Normosol", "generic_name": "Magnesium Sulfate", "description": "Replenishes magnesium levels.", "price": 3.00, "batch_number": 1955, "other_related_detailes": "50 mg injection; used in hospitals."},
        {"name": "Pantonix", "generic_name": "Pantoprazole", "description": "Reduces stomach acid.", "price": 7.00, "batch_number": 1984, "other_related_detailes": "40 mg tablet; before meals."},
        {"name": "Suran", "generic_name": "Sucralfate", "description": "Heals ulcers.", "price": 10.00, "batch_number": 2001, "other_related_detailes": "1g tablet; four times daily."},
        {"name": "Zosim", "generic_name": "Pipemidic Acid", "description": "Treats UTIs.", "price": 18.00, "batch_number": 2022, "other_related_detailes": "400 mg tablet; twice daily."},
        {"name": "Tonact", "generic_name": "Atorvastatin", "description": "Lowers cholesterol.", "price": 22.00, "batch_number": 2050, "other_related_detailes": "10 mg tablet; once daily."},
        {"name": "Acenac", "generic_name": "Aceclofenac", "description": "Pain and inflammation relief.", "price": 12.00, "batch_number": 2083, "other_related_detailes": "100 mg tablet; twice daily."},
        {"name": "Frusix", "generic_name": "Furosemide", "description": "Diuretic for fluid retention.", "price": 8.00, "batch_number": 2105, "other_related_detailes": "40 mg tablet; as directed by doctor."},
        {"name": "Zyloric", "generic_name": "Allopurinol", "description": "For gout management.", "price": 25.00, "batch_number": 2132, "other_related_detailes": "100 mg tablet; once daily."},
        {"name": "Lyrica", "generic_name": "Pregabalin", "description": "For nerve pain.", "price": 35.00, "batch_number": 2156, "other_related_detailes": "75 mg capsule; once daily."},
        {"name": "Atorva", "generic_name": "Atorvastatin", "description": "Cholesterol-lowering medication.", "price": 18.50, "batch_number": 2180, "other_related_detailes": "20 mg tablet; once daily."},
        {"name": "Peritox", "generic_name": "Hydroxyzine", "description": "Relieves allergy symptoms.", "price": 12.50, "batch_number": 2205, "other_related_detailes": "10 mg tablet; once daily for allergies."},
        {"name": "Zithrin", "generic_name": "Azithromycin", "description": "Broad-spectrum antibiotic.", "price": 26.00, "batch_number": 2230, "other_related_detailes": "500 mg tablet; once daily for 3 days."},
        {"name": "Metforal", "generic_name": "Metformin", "description": "Controls blood sugar.", "price": 5.80, "batch_number": 2262, "other_related_detailes": "500 mg tablet; twice daily for diabetes."},
        {"name": "Natriva", "generic_name": "Indapamide", "description": "For hypertension.", "price": 9.00, "batch_number": 2285, "other_related_detailes": "1.5 mg tablet; daily dose."},
        {"name": "Pantobid", "generic_name": "Pantoprazole", "description": "Gastroesophageal reflux treatment.", "price": 6.00, "batch_number": 2305, "other_related_detailes": "20 mg tablet; taken before meals."},
        {"name": "Hyocimax", "generic_name": "Hyoscine Butylbromide", "description": "Relieves muscle cramps.", "price": 14.00, "batch_number": 2330, "other_related_detailes": "10 mg tablet; for abdominal cramps."},
        {"name": "Ciproxin", "generic_name": "Ciprofloxacin", "description": "Antibiotic for infections.", "price": 20.00, "batch_number": 2355, "other_related_detailes": "500 mg tablet; twice daily."}
    ]

    for item in medicine_data:
        random_manufacturer = Manufacturer.objects.order_by('?').first()

        medicine_list,_ = MedicineList.objects.get_or_create(
            name = item['name'],
            generic_name = item['generic_name'],
            description = item['description'],
            price = item['price'],
            batch_number = item['batch_number'],
            other_related_detailes = item['other_related_detailes'],
            manufacturer = random_manufacturer
        )

def generate_data():
    generate_manufacturer_data()
    generate_medicine_data()
