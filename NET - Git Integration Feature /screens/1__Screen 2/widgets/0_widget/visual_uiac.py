import pandas
import pandas as pd
from codex_widget_factory_lite.visuals.table_simulator import TableSimulator

def generate_simulator_df():
    columns = ['header', 'input_type', 'id', 'label', 'value', 'options', 'max', 'min', 'steps', 'control']
    data = [['inputs', 'number', 'A', 'A', 12, '', 100, 0, 1, ''],
            ['inputs', 'number', 'B', 'B', 31, '', 100, 0, 1, ''],
            ['inputs', 'text', 'ID', 'ID', 'id3', '', '', '', '', '']]
    simulator_data = pd.DataFrame(columns=columns, data=data)
    return simulator_data

def generate_main_df(simulator_options):
    df = pd.DataFrame(data=[[8, 15, 'id1'], [12, 23, 'id2']], columns=['A', 'B', 'ID'])
    if len(simulator_options.keys())>0:
        sim_input_dict = {option:[value] for option, value in simulator_options.items()}
        new_entry = pd.DataFrame(sim_input_dict)
        temp = df.copy()
        temp = pd.concat([temp, new_entry], ignore_index=True)
        main_df = temp.copy()
    else:
        main_df = df.copy()
    main_df['Select'] = 'Add'
    main_df.reset_index(inplace=True,drop=True)
    return main_df

def generate_aux_df(main_data,flag=None,old_main_df=None):
    aux_temp = main_data.copy()
    aux_temp['Result'] = aux_temp.apply(lambda x: x['A']+x['B'] if x['Select']=='Add' else x['A']*x['B'], axis=1)
    aux_df = aux_temp[['ID', 'Select', 'Result']]
    return aux_df

main_buttons = pd.DataFrame([
    {
        "name": "Calulate",
        "variant": "contained",
        "type": "primary",
        "action": "change",
        "action_flag_type": "User Input Finalize"
    },
    {
        "name": "Reset",
        "variant": "outlined",
        "type": "reset",
        "action": "reset",
        "action_flag_type": "random"
    },
    ])

aux_buttons = pd.DataFrame([
    {
        "name": "Download Scenario Sheet",
        "variant": "contained",
        "type": "primary",
        "action": "download",
        "action_flag_type": "Download Scenario"
    }
    ])

simulator_buttons = pd.DataFrame([
    {
        "name": "Analyze Changes",
        "variant": "contained",
        "type": "primary",
        "action": "change",
        "action_flag_type": "Simlator Analyse Changes"
    },
    {
        "name": "Reset to Defalut",
        "variant": "outlined",
        "type": "reset",
        "action": "reset",
        "action_flag_type": "random"
    }])

def get_simulator_option_input(self, simulator_screen_json):
    options_dict = {}
    for section_n in simulator_screen_json["simulator_options"]["sections"]:
        for input_n in section_n["inputs"]:
            try:
                options_dict[input_n["id"]] = input_n["value"]
            except:
                temp_val = 1
    return options_dict

import copy

simulator_df = generate_simulator_df()
if "action_type" in globals().keys():
    if action_type=="Simlator Analyse Changes":
        simulator_options = get_simulator_option_input(screen_data)
        main_df = generate_main_df(simulator_options)
        aux_df = generate_aux_df(main_df)
    elif action_type=="User Input Finalize":
        main_df = get_main_table_user_input(screen_data)
        aux_df = generate_aux_df(main_df)
    else:
        main_df = generate_main_df({})
        aux_df = generate_aux_df(main_df)
    main_indicator_df = pd.DataFrame([[""]*3+["dropdown"]]*main_df.shape[0], columns=main_df.columns)
    main_extra_values = {"Select": ['Add', 'Multiply']}
    table_output = TableSimulator(main_table=main_df, aux_table=aux_df, simulator_options_table=simulator_df,
                                main_indicator_option_table=main_indicator_df, aux_indicator_option_table="",
                                main_alt_behaviour_table=False, aux_alt_behaviour_table=False,
                                main_suffix_option_table="", aux_suffix_option_table="",
                                main_prefix_option_table="", aux_prefix_option_table="",
                                main_formatted_option_table=False, aux_formatted_option_table=False,
                                main_buttons_table=main_buttons, aux_buttons_table=aux_buttons,
                                simulator_buttons_table=simulator_buttons, main_table_name="",aux_table_name="",
                                main_extra_values=main_extra_values,screen_json = screen_data)
    table_output.add_tooltip(isTooltip=True, tooltip_text="This is a tooltip", placement="top")
    output=table_output.json_string
else:
    main_df = generate_main_df({})
    aux_df =  generate_aux_df(main_df)
    main_indicator_df = pd.DataFrame([[""]*3+["dropdown"]]*main_df.shape[0], columns=main_df.columns)
    main_extra_values = {"Select": ['Add', 'Multiply']}
    table_output = TableSimulator(main_table=main_df, aux_table=aux_df, simulator_options_table=simulator_df,
                                main_indicator_option_table=main_indicator_df, aux_indicator_option_table="",
                                main_alt_behaviour_table=False, aux_alt_behaviour_table=False,
                                main_suffix_option_table="", aux_suffix_option_table="",
                                main_prefix_option_table="", aux_prefix_option_table="",
                                main_formatted_option_table=False, aux_formatted_option_table=False,
                                main_buttons_table=main_buttons, aux_buttons_table=aux_buttons,
                                simulator_buttons_table=simulator_buttons, main_table_name="",aux_table_name="",
                                main_extra_values=main_extra_values, screen_json = None)
    table_output.add_tooltip(isTooltip=True, tooltip_text="This is a tooltip", placement="top")
    output=table_output.json_string
import json
dynamic_outputs = output