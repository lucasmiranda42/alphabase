# AUTOGENERATED BY NBDEV! DO NOT EDIT!

__all__ = ["index", "modules", "custom_doc_links", "git_url"]

index = {"AA_CHEM": "aa.ipynb",
         "reset_AA_mass": "aa.ipynb",
         "ret_set_AA_df": "aa.ipynb",
         "AA_ASCII_MASS": "aa.ipynb",
         "AA_DF": "aa.ipynb",
         "calc_sequence_mass": "aa.ipynb",
         "calc_AA_masses_for_same_len_seqs": "aa.ipynb",
         "calc_sequence_masses_for_same_len_seqs": "aa.ipynb",
         "calc_AA_masses_for_var_len_seqs": "aa.ipynb",
         "common_const_dict": "element.ipynb",
         "MASS_PROTON": "element.ipynb",
         "MASS_ISOTOPE": "element.ipynb",
         "truncate_isotope": "element.ipynb",
         "MAX_ISOTOPE_LEN": "element.ipynb",
         "EMPTY_DIST": "element.ipynb",
         "reset_elements": "element.ipynb",
         "load_elem_yaml": "element.ipynb",
         "CHEM_INFO_DICT": "element.ipynb",
         "CHEM_MONO_MASS": "element.ipynb",
         "CHEM_ISOTOPE_DIST": "element.ipynb",
         "CHEM_MONO_IDX": "element.ipynb",
         "MASS_H2O": "element.ipynb",
         "MASS_NH3": "element.ipynb",
         "parse_formula": "element.ipynb",
         "calc_mass_from_formula": "element.ipynb",
         "abundance_convolution": "element.ipynb",
         "one_element_dist": "element.ipynb",
         "formula_dist": "element.ipynb",
         "load_mod_yaml": "modification.ipynb",
         "load_modloss_importance": "modification.ipynb",
         "update_all_by_MOD_DF": "modification.ipynb",
         "MOD_INFO_DICT": "modification.ipynb",
         "MOD_CHEM": "modification.ipynb",
         "MOD_MASS": "modification.ipynb",
         "MOD_LOSS_MASS": "modification.ipynb",
         "MOD_DF": "modification.ipynb",
         "calc_modification_mass": "modification.ipynb",
         "calc_mod_masses_for_same_len_seqs": "modification.ipynb",
         "calc_modification_mass_sum": "modification.ipynb",
         "calc_modloss_mass_with_importance": "modification.ipynb",
         "calc_modloss_mass": "modification.ipynb",
         "parse_ap": "alphapept_reader.ipynb",
         "get_x_tandem_score": "alphapept_reader.ipynb",
         "AlphaPeptReader": "alphapept_reader.ipynb",
         "SpectronautReader": "dia_search_reader.ipynb",
         "DiannReader": "dia_search_reader.ipynb",
         "parse_mod_seq": "maxquant_reader.ipynb",
         "MaxQuantReader": "maxquant_reader.ipynb",
         "MSFraggerPepXML": "msfragger_reader.ipynb",
         "mass_mapped_mods": "msfragger_reader.ipynb",
         "mod_mass_tol": "msfragger_reader.ipynb",
         "convert_one_pFind_mod": "pfind_reader.ipynb",
         "translate_pFind_mod": "pfind_reader.ipynb",
         "get_pFind_mods": "pfind_reader.ipynb",
         "parse_pfind_protein": "pfind_reader.ipynb",
         "pFindReader": "pfind_reader.ipynb",
         "translate_other_modification": "psm_reader.ipynb",
         "keep_modifications": "psm_reader.ipynb",
         "psm_reader_yaml": "psm_reader.ipynb",
         "PSMReaderBase": "psm_reader.ipynb",
         "PSMReaderProvider": "psm_reader.ipynb",
         "psm_reader_provider": "psm_reader.ipynb",
         "get_charged_frag_types": "fragment.ipynb",
         "parse_charged_frag_type": "fragment.ipynb",
         "init_zero_fragment_dataframe": "fragment.ipynb",
         "init_fragment_dataframe_from_other": "fragment.ipynb",
         "init_fragment_by_precursor_dataframe": "fragment.ipynb",
         "update_sliced_fragment_dataframe": "fragment.ipynb",
         "get_sliced_fragment_dataframe": "fragment.ipynb",
         "concat_precursor_fragment_dataframes": "fragment.ipynb",
         "calc_fragment_mz_values_for_same_nAA": "fragment.ipynb",
         "create_fragment_mz_dataframe_by_sort_precursor": "fragment.ipynb",
         "create_fragment_mz_dataframe": "fragment.ipynb",
         "create_fragment_mz_dataframe_ignore_old_idxes": "fragment.ipynb",
         "calc_delta_modification_mass": "mass_calc.ipynb",
         "calc_mod_delta_masses_for_same_len_seqs": "mass_calc.ipynb",
         "calc_b_y_and_peptide_mass": "mass_calc.ipynb",
         "calc_peptide_masses_for_same_len_seqs": "mass_calc.ipynb",
         "calc_b_y_and_peptide_masses_for_same_len_seqs": "mass_calc.ipynb",
         "get_reduced_mass": "mobility.ipynb",
         "ccs_to_mobility_bruker": "mobility.ipynb",
         "mobility_to_ccs_bruker": "mobility.ipynb",
         "ccs_to_mobility_bruker_for_df": "mobility.ipynb",
         "mobility_to_ccs_bruker_for_df": "mobility.ipynb",
         "CCS_IM_COEF": "mobility.ipynb",
         "IM_GAS_MASS": "mobility.ipynb",
         "refine_precursor_df": "precursor.ipynb",
         "is_precursor_refined": "precursor.ipynb",
         "update_precursor_mz": "precursor.ipynb",
         "reset_precursor_df": "precursor.ipynb",
         "is_precursor_sorted": "precursor.ipynb",
         "calc_precursor_mz": "precursor.ipynb",
         "get_mod_seq_hash": "precursor.ipynb",
         "get_mod_seq_charge_hash": "precursor.ipynb",
         "hash_mod_seq": "precursor.ipynb",
         "hash_mod_seq_charge": "precursor.ipynb",
         "hash_precursor_df": "precursor.ipynb",
         "detect_duplicated_items": "precursor.ipynb",
         "DecoyLib": "decoy_library.ipynb",
         "DiaNNDecoyLib": "decoy_library.ipynb",
         "DecoyLibProvider": "decoy_library.ipynb",
         "decoy_lib_provider": "decoy_library.ipynb",
         "SpecLibBase": "library_base.ipynb",
         "load_yaml": "yaml_utils.ipynb",
         "save_yaml": "yaml_utils.ipynb"}

modules = ["constants/aa.py",
           "constants/element.py",
           "constants/modification.py",
           "io/psm_reader/alphapept_reader.py",
           "io/psm_reader/dia_search_reader.py",
           "io/psm_reader/maxquant_reader.py",
           "io/psm_reader/msfragger_reader.py",
           "io/psm_reader/pfind_reader.py",
           "io/psm_reader/psm_reader.py",
           "peptide/fragment.py",
           "peptide/mass_calc.py",
           "peptide/mobility.py",
           "peptide/precursor.py",
           "spectrum_library/decoy_library.py",
           "spectrum_library/library_base.py",
           "yaml_utils.py"]

doc_url = "https://MannLabs.github.io/alphabase/"

git_url = "https://github.com/MannLabs/alphabase/tree/main/"

def custom_doc_links(name): return None
