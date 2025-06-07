# Screaming Frog & Cursor: The Ultimate SEO Workflow Guide for Mac

This guide will walk you through setting up and using Screaming Frog SEO Spider from within the Cursor editor on a Mac. The goal is to create highly efficient, repeatable, and scalable technical SEO audit workflows tailored to your specific business needs.

**Current Date:** June 7, 2025

### **Part 1: The One-Time Setup (5 Minutes)**

This is the most critical step. To avoid typing a long, complex path every time, we will create a simple command-line alias.

#### 1.1: Open Your Shell Profile in Cursor
Your Mac uses a configuration file to set up your terminal environment. Most modern Macs use `Zsh`.

1.  Open the integrated terminal in Cursor (`Terminal` > `New Terminal` or `Ctrl+~`).
2.  Type the following command in the terminal and press Enter to open the profile file in a new Cursor tab:
    ```bash
    cursor ~/.zshrc
    ```
    *If this command fails or the file is empty, you might be using the older Bash shell. Try `cursor ~/.bash_profile` instead.*

#### 1.2: Add the Screaming Frog Alias
1.  Scroll to the bottom of the `.zshrc` (or `.bash_profile`) file that opened in Cursor.
2.  Copy and paste the following line exactly as it is:

    ```bash
    # Alias for Screaming Frog SEO Spider
    alias screamingfrog='/Applications/Screaming\ Frog\ SEO\ Spider.app/Contents/MacOS/ScreamingFrogSEOSpiderLauncher'
    ```
3.  Save the file (`File` > `Save` or `Cmd+S`).
4.  Close and reopen the terminal in Cursor for the change to take effect.

#### 1.3: Test the Alias
In the new terminal window, type `screamingfrog --help` and press Enter. You should see a long list of available Screaming Frog commands. If you see this, your setup is successful. If you get a "command not found" error, double-check the path in your profile file.

---

### **Part 2: Core Workflows (Choose Your Business Type)**

Now we move to the practical, day-to-day commands. These workflows are run from the Cursor terminal.

#### **Workflow A: The Solo Consultant / Freelancer**
*Focus: Efficiency for single-client projects and customized audits.*

##### **Option 1: The Quick Health Check**
This is your go-to for a fast, comprehensive data pull on a new client's site. It runs "headless" (no UI) and exports all standard CSV reports.

```bash
# Command for a quick health check
screamingfrog --crawl https://www.client-website.com --headless --output-folder ~/Desktop/Client-Website-Crawl --export-csv all
```
**How it Works:**
* `--crawl [URL]`: The website you are auditing.
* `--headless`: Runs the entire crawl in the terminal without opening the app interface.
* `--output-folder [path]`: Creates a folder on your Desktop to save all the files.
* `--export-csv all`: Exports every standard report (internal_all.csv, directives_all.csv, etc.) as a separate CSV file.

##### **Option 2: The Deep-Dive Configured Audit**
This is for delivering specialized audits (e.g., E-commerce vs. SaaS) using pre-saved settings.

**Step 1: Create the Configuration in the App**
1.  Open the Screaming Frog app normally.
2.  Configure it exactly as you need for a specific audit type.
    * Connect APIs (`Configuration > API Access`).
    * Set up JavaScript rendering (`Configuration > Spider > Rendering`).
    * Exclude certain URL patterns (`Configuration > Exclude`).
    * Set crawl speed (`Configuration > Speed`).
3.  Once configured, save the settings via `File > Configuration > Save As...`. Give it a descriptive name like `Ecommerce_Client_Config.seospiderconfig` and save it in a known location (e.g., `~/Documents/SF-Configs/`).

**Step 2: Run the Audit in Cursor**
Now you can call that specific configuration from the command line.

```bash
# Command for a configured deep-dive
screamingfrog --crawl https://www.ecommerce-client.com \
--headless \
--config ~/Documents/SF-Configs/Ecommerce_Client_Config.seospiderconfig \
--output-folder ~/Documents/Client_Audits/Ecommerce-Client \
--export-tabs "Internal:HTML,Page Titles:Missing,Canonicals:Non-Indexable"
```
**Pro-Tips:**
* `--config [path]`: Your secret weapon. It loads all your saved settings.
* `--export-tabs "[TabName:FilterName],[TabName:FilterName]"`: This provides laser-focused exports. Instead of getting dozens of files, you get *only* the data you need for your report (e.g., just the missing page titles). This is a huge time-saver.

---

#### **Workflow B: The SEO Agency / High-Volume Operator**
*Focus: Maximum automation and scalability for managing many clients.*

This workflow uses a shell script to audit multiple websites in one go.

**Step 1: Create the Script File in Cursor**
1.  In Cursor, create a new file named `run_client_audits.sh`.
2.  Copy and paste the entire script below into this file.

**Step 2: Customize and Run the Script**

```bash
#!/bin/bash
#
# Screaming Frog Bulk Audit Script for SEO Agencies
#

# --- 1. CUSTOMIZE THIS SECTION ---
# Add all client websites you want to audit inside the parentheses.
CLIENTS=(
  "https://client-alpha.com"
  "https://client-bravo.com"
  "https://client-charlie.com"
  "https://some-other-site.net"
)

# Specify the parent folder for all your audit outputs.
AUDIT_PARENT_DIR="~/Documents/Client_Audits"

# Specify the path to your standard agency configuration file.
# Create this first using the method in Workflow A, Option 2.
AGENCY_CONFIG="~/Documents/SF-Configs/Standard_Agency_Config.seospiderconfig"
# --- END CUSTOMIZATION ---


# Get the current date for timestamping, e.g., 2025-06-07
TODAY=$(date +%Y-%m-%d)
echo "Starting batch audit for $TODAY..."
echo "================================================="

# Loop through each client in the array
for client in "${CLIENTS[@]}"; do
  # Create a clean folder name from the URL (e.g., https://client-alpha.com -> client-alpha.com)
  FOLDER_NAME=$(echo "$client" | sed 's|https://||' | sed 's|http://||' | sed 's|/||g')
  OUTPUT_PATH="$AUDIT_PARENT_DIR/$FOLDER_NAME/$TODAY"

  echo "► CRAWLING: $client"
  echo "  Saving results to: $OUTPUT_PATH"

  # Create the directory if it doesn't exist
  mkdir -p "$OUTPUT_PATH"

  # Execute the Screaming Frog command
  screamingfrog --crawl "$client" \
                --headless \
                --config "$AGENCY_CONFIG" \
                --output-folder "$OUTPUT_PATH" \
                --save-crawl \
                --export-csv all

  echo "✔ COMPLETE: Crawl for $client finished."
  echo "-------------------------------------------------"
done

echo "================================================="
echo "✅ All client audits are complete."
```

**Step 3: Execute the Script**
1.  **Make it executable (one-time only):** In the Cursor terminal, run `chmod +x run_client_audits.sh`.
2.  **Run the script:** In the terminal, simply type `./run_client_audits.sh` and press Enter.

You can now walk away. The script will crawl each site sequentially, creating neatly organized, timestamped folders for every client, all using your standard agency configuration.

---

#### **Workflow C: The In-House SEO / Migration Specialist**
*Focus: Bulk URL analysis and scheduled, recurring site monitoring.*

##### **Option 1: Validating a URL List (List Mode)**
Perfect for site migrations, log file analysis, or checking a list of pages from PPC campaigns.

**Step 1: Create Your URL List**
In Cursor, create a file named `urllist.txt`. Paste one URL per line.

**Step 2: Run the Crawl in List Mode**
```bash
# Command to crawl a list of URLs
screamingfrog --crawl ~/path/to/urllist.txt \
--headless \
--output-folder ~/Desktop/Migration-Check \
--export-report "All Redirects"
```
**How it Works:**
* When `--crawl` points to a `.txt` file, it automatically enables **List Mode**.
* `--export-report "[Report Name]"`: Exports one of the specialized reports from the `Reports` menu (e.g., "All Redirects", "Crawl Overview", "Orphan Pages"). This is extremely useful for migration analysis.

##### **Option 2: Automated Weekly Health Monitoring (using `cron`)**
This sets up your Mac to automatically run a crawl at a scheduled time.

**Step 1: Create Your Crawl Script**
Create a script just like in Workflow B, but for a single site. Save it as `weekly_health_check.sh`. Make sure it has an absolute path for the output folder (e.g., `/Users/yourusername/Documents/Health_Checks`).

**Step 2: Schedule the Job with `cron`**
1.  In the Cursor terminal, type `crontab -e` to open the cron task editor.
2.  Press `i` to enter "insert mode".
3.  Add the following line to schedule the script to run every Monday at 2:00 AM:
    ```cron
    0 2 * * 1 /bin/zsh /Users/yourusername/path/to/your/weekly_health_check.sh
    ```
4.  Press `Esc`, then type `:wq` and press Enter to save and quit.

Your Mac will now automatically perform a technical audit every week, providing a continuous record of your site's health without you lifting a finger. 