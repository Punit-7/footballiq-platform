import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="[%(asctime)s : %(message)s ]")

project_name = "footballiq-platform"
base_dir = Path(__file__).resolve().parent

directories = [
    base_dir / "data" / "raw",
    base_dir / "data" / "processed",
    base_dir / "notebooks",
    base_dir / "src" / "data_engineering",
    base_dir / "src" / "ml",
    base_dir / "src" / "deep_learning",
    base_dir / "src" / "nlp",
    base_dir / "src" / "genai",
    base_dir / "src" / "api",
    base_dir / "src" / "utils",
    base_dir / "tests",
    base_dir / "docker",
    base_dir / ".github" / "workflows",
    base_dir / "configs",
    base_dir / "docs",
    base_dir / "app_streamlit",
]

files = [
    base_dir / "src" / "data_engineering" / "__init__.py",
    base_dir / "src" / "ml" / "__init__.py",
    base_dir / "src" / "deep_learning" / "__init__.py",
    base_dir / "src" / "nlp" / "__init__.py",
    base_dir / "src" / "genai" / "__init__.py",
    base_dir / "src" / "api" / "__init__.py",
    base_dir / "src" / "utils" / "__init__.py",
    base_dir / "tests" / "__init__.py",
    base_dir / "docker" / "Dockerfile",
    base_dir / "docker" / "docker-compose.yml",
    base_dir / ".github" / "workflows" / ".gitkeep",
    base_dir / "configs" / "config.yaml",
    base_dir / "docs" / "architecture.md",
    base_dir / "docs" / "data_dictionary.md",
    base_dir / "app_streamlit" / "app.py",
    base_dir / "requirements.txt",
    base_dir / "README.md",
]

for directory in directories:
    directory.mkdir(parents=True, exist_ok=True)
    logging.info("Creating directory: %s", directory)

for file_path in files:
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not file_path.exists() or file_path.stat().st_size == 0:
        file_path.touch()
        logging.info("Creating empty file: %s", file_path)
    else:
        logging.info("%s already exists", file_path)

logging.info("Scaffold complete for %s", project_name)
