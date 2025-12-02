library(rix)

# Environment to run some derivations
rix(
  date = "2025-11-24",
  r_pkgs = "reticulate",
  py_conf = list(
    "py_version" = "3.13",
    "py_pkgs" = c("pymssql", "sqlalchemy", "flask", "pandas")
  ),
  ide = "none",
  project_path = ".",
  overwrite = TRUE
)
