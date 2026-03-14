from __future__ import annotations

from abc import ABC, abstractmethod

import pandas as pd


class DataClient(ABC):
    @abstractmethod
    def fetch(self, *args, **kwargs) -> pd.DataFrame:
        """Fetch data from a source and return a dataframe."""
