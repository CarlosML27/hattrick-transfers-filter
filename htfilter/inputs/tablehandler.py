from abc import ABC, abstractmethod

import pandas as pd


class TableHandler(ABC):
    @abstractmethod
    def parse_to_dataframe(self, table_data) -> pd.DataFrame:
        pass
