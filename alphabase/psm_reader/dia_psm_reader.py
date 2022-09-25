# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbdev_nbs/psm_reader/dia_psm_reader.ipynb.

# %% auto 0
__all__ = ['SpectronautReader', 'SwathReader', 'DiannReader']

# %% ../../nbdev_nbs/psm_reader/dia_psm_reader.ipynb 3
import pandas as pd
import numpy as np

from alphabase.psm_reader.psm_reader import (
    psm_reader_provider, psm_reader_yaml
)

from alphabase.psm_reader.maxquant_reader import (
    MaxQuantReader
)

# %% ../../nbdev_nbs/psm_reader/dia_psm_reader.ipynb 4
class SpectronautReader(MaxQuantReader):
    def __init__(self,
        *,
        column_mapping:dict = None,
        modification_mapping:dict = None,
        fdr = 0.01,
        keep_decoy = False,
        mod_sep = '[]',
        underscore_for_ncterm=True,
        fixed_C57 = False,
        mod_seq_columns=psm_reader_yaml[
            'spectronaut'
        ]['mod_seq_columns'],
        csv_sep = '\t',
        rt_unit = 'irt',
        **kwargs,
    ):
        """Reader for Spectronaut's output library TSV/CSV.

        Other parameters, please see `MaxQuantReader` 
        in `alphabase.psm_reader.maxquant_reader`

        Parameters
        ----------
        csv_sep : str, optional
            Delimiter for TSV/CSV, by default '\t'
        """
        super().__init__(
            column_mapping=column_mapping,
            modification_mapping=modification_mapping,
            fdr=fdr, keep_decoy=keep_decoy,
            mod_sep=mod_sep,
            underscore_for_ncterm=underscore_for_ncterm,
            mod_seq_columns = mod_seq_columns,
            fixed_C57=fixed_C57,
            rt_unit=rt_unit,
            **kwargs,
        )
        self.csv_sep = csv_sep

        self.mod_seq_column = 'ModifiedPeptide'

        self._min_max_rt_norm = True

    def _init_column_mapping(self):
        self.column_mapping = psm_reader_yaml[
            'spectronaut'
        ]['column_mapping']
    
    def _load_file(self, filename):
        df = pd.read_csv(filename, sep=self.csv_sep)
        self._find_mod_seq_column(df)
        if 'ReferenceRun' in df.columns:
            df.drop_duplicates([
                'ReferenceRun',self.mod_seq_column, 'PrecursorCharge'
            ], inplace=True)
        else:
            df.drop_duplicates([
                self.mod_seq_column, 'PrecursorCharge'
            ], inplace=True)
        df.reset_index(drop=True, inplace=True)
        
        return df

class SwathReader(SpectronautReader):
    def __init__(self,
        *,
        column_mapping:dict = None,
        modification_mapping:dict = None,
        fdr = 0.01,
        keep_decoy = False,
        mod_sep = '()',
        underscore_for_ncterm=False,
        fixed_C57 = False,
        mod_seq_columns=psm_reader_yaml[
            'spectronaut'
        ]['mod_seq_columns'],
        csv_sep = '\t',
        **kwargs,
    ):
        """ 
        SWATH or OpenSWATH library, similar to `SpectronautReader`
        """
        super().__init__(
            column_mapping=column_mapping,
            modification_mapping=modification_mapping,
            fdr=fdr, keep_decoy=keep_decoy,
            mod_sep=mod_sep,
            underscore_for_ncterm=underscore_for_ncterm,
            fixed_C57=fixed_C57,
            mod_seq_columns=mod_seq_columns,
            csv_sep=csv_sep,
            **kwargs,
        )

# %% ../../nbdev_nbs/psm_reader/dia_psm_reader.ipynb 10
class DiannReader(SpectronautReader):
    def __init__(self,
        *,
        column_mapping:dict = None,
        modification_mapping:dict = None,
        fdr = 0.01,
        keep_decoy = False,
        mod_sep = '()',
        underscore_for_ncterm=False,
        fixed_C57 = False,
        csv_sep = '\t',
        rt_unit = 'minute',
        **kwargs,
    ):
        """
        Also similar to `MaxQuantReader`, 
        but different in column_mapping and modificatin_mapping
        """
        super().__init__(
            column_mapping=column_mapping,
            modification_mapping=modification_mapping,
            fdr=fdr, keep_decoy=keep_decoy,
            mod_sep=mod_sep,
            underscore_for_ncterm=underscore_for_ncterm,
            fixed_C57=fixed_C57,
            csv_sep=csv_sep,
            rt_unit=rt_unit,
            **kwargs,
        )
        self.mod_seq_column = 'Modified.Sequence'
        self._min_max_rt_norm = False

    def _init_column_mapping(self):
        self.column_mapping = psm_reader_yaml[
            'diann'
        ]['column_mapping']
    
    def _load_file(self, filename):
        df = pd.read_csv(filename, sep=self.csv_sep)

        return df

psm_reader_provider.register_reader(
    'spectronaut', SpectronautReader
)
psm_reader_provider.register_reader(
    'openswath', SwathReader
)
psm_reader_provider.register_reader(
    'swath', SwathReader
)
psm_reader_provider.register_reader(
    'diann', DiannReader
)
