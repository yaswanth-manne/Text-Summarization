from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfiguration:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfiguration:
    root_dir: Path
    STATUS_FILE: str
    ALL_REQUIRED_FILES: list