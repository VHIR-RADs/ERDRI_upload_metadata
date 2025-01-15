import pandas as pd

pd_radeep = pd.read_csv('input/RADeepRegistry_DataDictionary_2025-01-15.csv')

# get the number of rows and columns
print(pd_radeep.shape)

# Add row description with column Variable / Field Name hpo_row_2, hpo_row_3, hpo_row_4, hpo_row_5

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpo_row_2', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpo_row_3', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpo_row_4', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpo_row_5', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'new_novel_row2', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'new_novel_row3', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'new_novel_row4', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'new_novel_row5', 'Field Label'] = 'Add new row'


# find row with column Variable / Field Name = age and substitute value of column Field Label for 'Calculated age of the patient'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'age', 'Field Label'] = 'Calculated age of the patient'

# delete content of column Choices, Calculations, OR Slider Labels for rows where column Variable / Field Name = hpoid_1, hpoid_2, hpoid_3, hpoid_4, hpoid_5
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpoid_1', 'Choices, Calculations, OR Slider Labels'] = None
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpoid_2', 'Choices, Calculations, OR Slider Labels'] = None
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpoid_3', 'Choices, Calculations, OR Slider Labels'] = None
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpoid_4', 'Choices, Calculations, OR Slider Labels'] = None
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'hpoid_5', 'Choices, Calculations, OR Slider Labels'] = None

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'novelsymbol_r1', 'Field Label'] = 'Enter the symbol for the novel variant'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'novelsymbol_r2', 'Field Label'] = 'Enter the symbol for the novel variant'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'novelsymbol_r3', 'Field Label'] = 'Enter the symbol for the novel variant'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'novelsymbol_r4', 'Field Label'] = 'Enter the symbol for the novel variant'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'novelsymbol_r5', 'Field Label'] = 'Enter the symbol for the novel variant'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele1_r1', 'Field Label'] = 'Enter the variant allele 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele1_r2', 'Field Label'] = 'Enter the variant allele 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele1_r3', 'Field Label'] = 'Enter the variant allele 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele1_r4', 'Field Label'] = 'Enter the variant allele 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele1_r5', 'Field Label'] = 'Enter the variant allele 1'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele2_r1', 'Field Label'] = 'Enter the variant allele 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele2_r2', 'Field Label'] = 'Enter the variant allele 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele2_r3', 'Field Label'] = 'Enter the variant allele 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele2_r4', 'Field Label'] = 'Enter the variant allele 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'var_allele2_r5', 'Field Label'] = 'Enter the variant allele 2'

# years
'''
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'year_immigration', 'Text Validation Max'] = '2024'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'splenectomy_year', 'Text Validation Max'] = '2024'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'transfusion_year', 'Text Validation Max'] = '2024'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'transplant_year', 'Text Validation Max'] = '2024'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'cholecystectomy_date', 'Text Validation Max'] = '2024'
'''

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'timestamp', 'Field Note'] = 'dd-mm-yyyy'

# descritions
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_bc_1', 'Field Label'] = 'Ongoing bone complication 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_bc_2', 'Field Label'] = 'Ongoing bone complication 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_bc_3', 'Field Label'] = 'Ongoing bone complication 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_bc_4', 'Field Label'] = 'Ongoing bone complication 4'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_bc_5', 'Field Label'] = 'Ongoing bone complication 5'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_cpd_1', 'Field Label'] = 'Ongoing cardiac and pulmonar pain disorder 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_cpd_2', 'Field Label'] = 'Ongoing cardiac and pulmonar pain disorder 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_cpd_3', 'Field Label'] = 'Ongoing cardiac and pulmonar pain disorder 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_cpd_4', 'Field Label'] = 'Ongoing cardiac and pulmonar pain disorder 4'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_cpd_5', 'Field Label'] = 'Ongoing cardiac and pulmonar pain disorder 5'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_1', 'Field Label'] = 'Ongoing neurological disorder 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_2', 'Field Label'] = 'Ongoing neurological disorder 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_3', 'Field Label'] = 'Ongoing neurological disorder 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_4', 'Field Label'] = 'Ongoing neurological disorder 4'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_5', 'Field Label'] = 'Ongoing neurological disorder 5'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_nd_6', 'Field Label'] = 'Ongoing neurological disorder 6'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_1', 'Field Label'] = 'Ongoing endocrine disorder 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_2', 'Field Label'] = 'Ongoing endocrine disorder 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_3', 'Field Label'] = 'Ongoing endocrine disorder 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_4', 'Field Label'] = 'Ongoing endocrine disorder 4'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_5', 'Field Label'] = 'Ongoing endocrine disorder 5'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_6', 'Field Label'] = 'Ongoing endocrine disorder 6'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_endo_7', 'Field Label'] = 'Ongoing endocrine disorder 7'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_1', 'Field Label'] = 'Ongoing liver and kidney disorder 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_2', 'Field Label'] = 'Ongoing liver and kidney disorder 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_3', 'Field Label'] = 'Ongoing liver and kidney disorder 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_4', 'Field Label'] = 'Ongoing liver and kidney disorder 4'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_5', 'Field Label'] = 'Ongoing liver and kidney disorder 5'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_6', 'Field Label'] = 'Ongoing liver and kidney disorder 6'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_lkd_7', 'Field Label'] = 'Ongoing liver and kidney disorder 7'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_vhd_1', 'Field Label'] = 'Ongoing visual and hearing disorder 1'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_vhd_2', 'Field Label'] = 'Ongoing visual and hearing disorder 2'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_vhd_3', 'Field Label'] = 'Ongoing visual and hearing disorder 3'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'ongoing_vhd_4', 'Field Label'] = 'Ongoing visual and hearing disorder 4'

pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_2', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_3', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_4', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_5', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_6', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_7', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_8', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_9', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_10', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_11', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_12', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_13', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_14', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_15', 'Field Label'] = 'Add new row'
pd_radeep.loc[pd_radeep['Variable / Field Name'] == 'add_acute_scd_row_16', 'Field Label'] = 'Add new row'


# store the changes in a new csv file
pd_radeep.to_csv('output/radeep_erdri.csv', index=False)