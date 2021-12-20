# AUTOGENERATED! DO NOT EDIT! File to edit: nbdev_nbs/io/psm_reader/alphapept_reader.ipynb (unless otherwise specified).

__all__ = ['parse_ap', 'get_x_tandem_score', 'AlphaPeptReader']

# Cell
import numba
import os
import pandas as pd
import numpy as np
import h5py

from alphabase.io.psm_reader.psm_reader import (
    PSMReaderBase, psm_reader_provider
)

@numba.njit
def parse_ap(precursor):
    """
    Parser to parse peptide strings
    """
    items = precursor.split('_')
    if len(items) == 3:
        decoy = 1
    else:
        decoy = 0
    modseq = items[0]
    charge = items[-1]

    parsed = []
    mods = []
    sites = []
    string = ""

    if modseq[0] == 'a':
        sites.append('0')
        mods.append('a')
        modseq = modseq[1:]
    elif modseq.startswith('tmt'):
        for l in range(3, len(modseq)):
            if modseq[l].isupper():
                break
        sites.append('0')
        mods.append(modseq[:l])
        modseq = modseq[l:]

    for i in modseq:
        string += i
        if i.isupper():
            parsed.append(i)
            if len(string) > 1:
                sites.append(str(len(parsed)))
                mods.append(string)
            string = ""

    return ''.join(parsed), ';'.join(mods), ';'.join(sites), charge, decoy

def get_x_tandem_score(df: pd.DataFrame) -> np.ndarray:
    b = df['b_hits'].astype('int').apply(lambda x: np.math.factorial(x)).values
    y = df['y_hits'].astype('int').apply(lambda x: np.math.factorial(x)).values
    x_tandem = np.log(b.astype('float')*y.astype('float')*df['matched_int'].values)

    x_tandem[x_tandem==-np.inf] = 0

    return x_tandem

class AlphaPeptReader(PSMReaderBase):
    def __init__(self,
        *,
        column_mapping:dict = None,
        modification_mapping:dict = None,
        fdr = 0.01,
        keep_decoy = False,
        **kwargs,
    ):
        super().__init__(
            column_mapping=column_mapping,
            modification_mapping=modification_mapping,
            fdr = fdr,
            keep_decoy = keep_decoy,
        )
        if fdr <= 0.1:
            self.hdf_dataset = 'peptide_fdr'

    def _init_column_mapping(self):
        self.column_mapping = {
            'sequence': 'naked_sequence',
            'rt':'rt',
            'spec_idx': ['scan_no','raw_idx'],
            'query_id': 'query_idx',
            'mobility': 'mobility',
            'score': 'score',
            'charge': 'charge',
            'raw_name': 'raw_name', #parse from `ms_data.hdf`` file
            'fdr': 'q_value',
            'decoy': 'decoy',
        }

    def _init_modification_mapping(self):
        self.modification_mapping = {
            'Carbamidomethyl@C': 'cC',
            'Oxidation@M': 'oxM',
            'Phospho@S': 'pS',
            'Phospho@T': 'pT',
            'Phospho@Y': 'pY',
            'Acetyl@Protein N-term': 'a',
        }

    def _load_file(self, filename):
        with h5py.File(filename, 'r') as _hdf:
            dataset = _hdf[self.hdf_dataset]
            df = pd.DataFrame({col:dataset[col] for col in dataset.keys()})
            df['raw_name'] = os.path.basename(filename)[:-len('.ms_data.hdf')]
            df['precursor'] = df['precursor'].str.decode('utf-8')
            if 'scan_no' in df.columns:
                df['scan_no'] = df['scan_no'].astype('int')
            df['charge'] = df['charge'].astype(int)

            if 'score' not in df.columns:
                df['score'] = get_x_tandem_score(df)
        return df

    def _load_modifications(self, df: pd.DataFrame):
        (
            _seqs, self._psm_df['mods'],
            self._psm_df['mod_sites'], _charges,
            self._psm_df['decoy']
        ) = zip(*df['precursor'].apply(parse_ap))
        self._psm_df.decoy = self._psm_df.decoy.astype(np.int8)

psm_reader_provider.register_reader('alphapept', AlphaPeptReader)