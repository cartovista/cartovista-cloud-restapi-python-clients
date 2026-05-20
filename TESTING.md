# Testing

Run the offline generated-client tests:

```powershell
python -m pip install -r requirements.txt -r test-requirements.txt
python -m unittest discover -s test -p "test_*.py" -v
```

The live API tests are included in the same discovery command, but they are
skipped unless the target environment is configured:

```powershell
$env:CARTOVISTA_HOST = "https://cloud-staging.cartovista.com"
$env:CARTOVISTA_TENANT = "cypresstest"
$env:CARTOVISTA_API_ADMIN_EMAIL = "<admin email>"
$env:CARTOVISTA_API_TEST_PASSWORD = "<password>"
$env:CARTOVISTA_PORTAL_API_KEY = "<portal api key>"
$env:CARTOVISTA_PORTAL_SECRET_KEY = "<portal secret key>"
$env:CARTOVISTA_LIVE_ALLOW_MUTATION = "true"
python -m unittest discover -s test -p "test_*.py" -v
```

CI sets `CARTOVISTA_REQUIRE_LIVE_CONFIG=true`, which makes missing live-test
configuration fail the run instead of skipping the integration suite. The
GitHub Actions workflow also validates these values before running the full
`test_*.py` discovery command.

The live suite uses `test/fixtures/Supermarches.zip` by default for the generic
portal upload endpoint and `test/fixtures/live_data_table.xlsx` for Excel
data-table import tests. Set `CARTOVISTA_LIVE_UPLOAD_FILE` to override the
portal upload fixture, `CARTOVISTA_LIVE_EXCEL_FILE` to override the workbook, or
`CARTOVISTA_LIVE_EXCEL_SHEET_NAME` to override the named-sheet import test
sheet. The default sheet is `Sheet1`.
