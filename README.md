# Networking-Tracker
Excel/Google Sheets tracker for networking strategies.


# Networking Strategies Tracker

A comprehensive tracker for managing and documenting networking approaches. This project helps you keep track of strategies, contacts, follow-ups, and completed actions in one place.

## Features

- Contains **100+ networking strategies** (online, offline, events, content creation, referrals, etc.)
- Columns include:
  - Strategy
  - Date
  - Completed (tick box)
  - Contact Name
  - Contact Number
- Compatible with **Google Sheets** (checkboxes) and **Excel** (manual or developer checkboxes)
- Python code available to **generate Excel tracker automatically**

## How to Use

### Google Sheets
1. Upload the Excel file to Google Drive.
2. Open with Google Sheets.
3. Select the `Completed` column → Insert → Checkbox.
4. Check/uncheck as you complete each strategy.

### Excel
1. Open the Excel file.
2. Enable **Developer tab**: File → Options → Customize Ribbon → Check Developer.
3. Insert checkboxes in the `Completed` column.

### Python (Optional)
- Use the provided Colab notebook to **generate the tracker**:
```python
# Install dependencies
!pip install pandas openpyxl

# Run the provided code to create Excel tracker

