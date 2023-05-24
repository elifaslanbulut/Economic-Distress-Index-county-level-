# GIS profile to use with ArcGIS Online
gis_profile = 'ba'

# US Census Bureau database to use
api_database = 'ACSDT5Y2021'

# Variables to retrieve from US Census Bureau database
api_variables = [
    'B19001_001',  # full households
    'B19001_002',  # less than 10k
    'B19001_003',  # between 10-14k
    'B19001_004',  # between 15-19k
    'B19001_005',  # between 20-24k
    'B19001_006',  # between 25-29k

    'B19001B_001',  # african american total households
    'B19001B_002',  # less than 10k
    'B19001B_003',  # between 10-14k
    'B19001B_004',  # between 15-19k
    'B19001B_005',  # between 20-24k
    'B19001B_006',  # between 25-29k

    'B19001C_001',  # american indian and alaska native total households
    'B19001C_002',  # less than 10k
    'B19001C_003',  # between 10-14k
    'B19001C_004',  # between 15-19k
    'B19001C_005',  # between 20-24k
    'B19001C_006',  # between 25-29k

    'B19001D_001',  # asian total households
    'B19001D_002',  # less than 10k
    'B19001D_003',  # between 10-14k
    'B19001D_004',  # between 15-19k
    'B19001D_005',  # between 20-24k
    'B19001D_006',  # between 25-29k

    'B19001E_001',  # native hawaiian or pacific islander total households
    'B19001E_002',  # less than 10k
    'B19001E_003',  # between 10-14k
    'B19001E_004',  # between 15-19k
    'B19001E_005',  # between 20-24k
    'B19001E_006',  # between 25-29k

    'B19001H_001',  # nonhispanic white total households
    'B19001H_002',  # less than 10k
    'B19001H_003',  # between 10-14k
    'B19001H_004',  # between 15-19k
    'B19001H_005',  # between 20-24k
    'B19001H_006',  # between 25-29k

    'B19001I_001',  # hispanic or latino total households
    'B19001I_002',  # less than 10k
    'B19001I_003',  # between 10-14k
    'B19001I_004',  # between 15-19k
    'B19001I_005',  # between 20-24k
    'B19001I_006',  # between 25-29k

    'B15003_001',  # education attainment, total, for pop 25 years and over
    'B15003_025',  # Doctorate degree
    'B15003_024',  # Professional school degree
    'B15003_023',  # Master's degree
    'B15003_022',  # Bachelor's degree
    'B15003_021',  # Associate's degree
    'B15003_020',  # some college - 1 or more year
    'B15003_019',  # some college - less than 1 year
    'B15003_018',  # GED or alternative credential
    'B15003_017',  # high school diploma

    'B17001_001',  # Poverty status in the past 12 months
    'B17001_002',  # Income in the past 12 months below poverty level

    'B23025_002',  # in Labor Force - for the population 16 years and over
    'B23025_005',  # Unemployed

    'B19058_002',  # with cash public assistance or Food Stamps/SNAP
    'B19058_001',  # Total estimate

    'B19056_002',  # with Supplemental Security Income (SSI)
    'B19056_001',  # Total estimate
]

# Percent Variables to Calculate
percent_variable_lst = [
    {
        'name': 'pct_less_than_30K',
        'alias': 'Low Income',
        'numerators': ['B19001_002E', 'B19001_003E', 'B19001_004E', 'B19001_005E', 'B19001_006E'],
        'denominator': 'B19001_001E',
        'coefficient': 1.0
    },
    {
        'name': 'pct_less_than_high_school',
        'alias': 'Less than High School Degree',
        'numerators': ['B17001_002E'],
        'denominator': 'B17001_001E',
        'coefficient': 1.0
    },
    {
        'name': 'pct_below_poverty',
        'alias': 'Below Poverty Line',
        'numerators': ['B17001_002E'],
        'denominator': 'B17001_001E',
        'coefficient': 1.0
    },
    {
        'name': 'pct_with_SNAP',
        'alias': 'Cash Public Assistance or Food Stamps/SNAP',
        'numerators': ['B19058_002E'],
        'denominator': 'B19058_001E',
        'coefficient': 1.0
    },
    {
        'name': 'pct_with_SSI',
        'alias': 'Supplemental Security Income (SSI)',
        'numerators': ['B19056_002E'],
        'denominator': 'B19056_001E',
        'coefficient': 1.0
    }
]
