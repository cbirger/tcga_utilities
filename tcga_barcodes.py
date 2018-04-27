# Sample Types
# from https://gdc.cancer.gov/resources-tcga-users/tcga-code-tables/sample-type-codes

class TcgaSampleType:
    """Single Class for decoding two-digit sample type codes present in TCGA barcodes

    """

    class __TcgaSampleType:

        SAMPLE_TYPES_DESCRIPTION = 0
        SAMPLE_TYPES_LETTER_CODE = 1
        SAMPLE_TYPES_TN = 2
        TUMOR = 'tumor'
        NORMAL = 'normal'
        NA = 'na'

        # this table needs updating - TARGET data had some unknown sample type ids
        SAMPLE_TYPES = {'01': ['Primary Solid Tumor', 'TP', TUMOR],
                        '02' : ['Recurrent Solid Tumor', 'TR', TUMOR],
                        '03' : ['Primary Blood Derived Cancer - Peripheral Blood', 'TB', TUMOR],
                        '04' : ['Recurrent Blood Derived Cancer - Bone Marrow', 'TRBM', TUMOR],
                        '05' : ['Additional - New Primary', 'TAP', TUMOR],
                        '06' : ['Metastic', 'TM', TUMOR],
                        '07' : ['Additional Metastic', 'TAM', TUMOR],
                        '08' : ['Human Tumor Original Cells', 'THOC', TUMOR],
                        '09' : ['Primary Blood Derived Cancer - Bone Marrow', 'TBM', TUMOR],
                        '10' : ['Blood Derived Normal', 'NB', NORMAL],
                        '11' : ['Solid Tissue Normal', 'NT', NORMAL],
                        '12' : ['Buccal Cell Normal', 'NBC', NORMAL],
                        '13' : ['EBV Immortalized Normal', 'NEBV', NORMAL],
                        '14' : ['Bone Marrow Normal', 'NBM', NORMAL],
                        '15' : ['sample type 15', '15SH', NA],
                        '16' : ['sample type 16', '16SH', NA],
                        '20' : ['Control Analyte', 'CELLC', NA],
                        '40' : ['Recurrent Blood Derived Normal - Peripheral Blood', 'TRB', NORMAL],
                        '41' : ['Blood Derived Cancer - Bone Marrow, Post-treatment', 'TBD', TUMOR],
                        '42' : ['Blood Derived Cancer - Peripheral Blood, Post-treatement', 'TBD', TUMOR],
                        '50' : ['Cell Lines', 'CELL', NA],
                        '60' : ['Primary Xenograft Tissue', 'XP', NA],
                        '61' : ['Cell Line Derived Xenograft Tissue', 'XCL', NA],
                        '99' : ['sample type 99', '99SH', NA]}

    instance = None
    def __init__(self):
        if not TcgaSampleType.instance:
            TcgaSampleType.instance = TcgaSampleType.__TcgaSampleType()

    def getDescription(self, numeric_code):
        return self.instance.SAMPLE_TYPES[numeric_code][0]

    def getLetterCode(self, numeric_code):
        return self.instance.SAMPLE_TYPES[numeric_code][1]

    def getTumorNormalClassification(self, numeric_code):
        return self.instance.SAMPLE_TYPES[numeric_code][2]
        
class TcgaAliquotBarCode:

    def __init__(self, barcode, cohort):
        self._barcode = barcode
        self._cohort = cohort
        fields = barcode.split('-')
        self._tss = fields[1]
        self._participant = fields[2]
        self._sample_type = fields[3][:2]
        self._vial = fields[3][2:]
        self._portion = fields[4][:2]
        self._analyte = fields[4][2:]
        self._plate = fields[5]
        self._center = fields[6]
        
    @property
    def barcode(self):
        return self._barcode

    @property
    def cohort(self):
        return self._cohort

    @property
    def tss(self):
        return self._tss

    @property
    def participant(self):
        return self._participant

    @property
    def sample_type(self):
        return self._sample_type

    @property
    def vial(self):
        return self._vial

    @property
    def portion(self):
        return self._portion

    @property
    def analyte(self):
        return self._analyte

    @property
    def plate(self):
        return self._plate

    @property
    def center(self):
        return self._center
