import sys
import logging
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]
data_dir = project_root / "data"
reports_dir = project_root / "reports"
models_dir = project_root / "models"

raw_dir = data_dir / "raw"              # I'm storing the raw Excel from NHS found in readme
interim_dir = data_dir / "interim"      # Partially processed data files will sit here alongside clean unmerged data.
processed_dir = data_dir / "processed"  # Fully engineered and cleaned and merged data set for modelling

raw_file = "IUCADC_Data_KPI_Combined_Time_Series-to-Mar-2025-Revised-Apr24-to-Mar25-inclusive.xlsx"
nhs111_iuc_data = raw_dir / raw_file


def setup_logging(debug: bool = False) -> logging.Logger:
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[logging.StreamHandler(sys.stdout)],
        force=True,
    )
    return logging.getLogger("nhs111_triage")