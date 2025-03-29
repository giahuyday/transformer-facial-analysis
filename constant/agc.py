AGE_MAPPING = {
    0: "0-9",
    1: "10-19",
    2: "20-29",
    3: "30-39",
    4: "40-49",
    5: "50-59",
    6: "60+"
}

GENDER_MAPPING = {
    0: "Male",
    1: "Female"
}

RACE_MAPPING = {
    0: "Asian",
    1: "Black",
    2: "White",
    3: "Indian",
    4: "Other"
}

def map_age(age):
    return AGE_MAPPING.get(age, str(age))

def map_gender(gender):
    return GENDER_MAPPING.get(gender, str(gender))

def map_race(race):
    return RACE_MAPPING.get(race, str(race))