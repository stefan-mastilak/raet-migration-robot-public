## visma-raet-migration
### General: 
* Robot type: On-Prem solution
* Customer: Visma Raet Netherlands
* Trigerring: schedule based 
<br></br>
### Visma Raet migration robot tasks:
* PDOL migration (Payroll files)
* SDOL migration (Personnel files)
* MLM migration (Medical leave files)
<br></br>
### Repository content:
* lib\base_actions - actions applicable for all migration types
* lib\base_checks - checks applicable for all migration types
* lib\base_migration - common for all migration types
* lib\credentials_handler - credentials fetcher
* lib\kpi_handler - KPI handling for all migration types
* lib\sftp_handler - SFTP communication handling for all migration types
* lib\slack_handler - Slack reporting for all migration types
* lib\zip_handler - zip handling for all migration types

* mig\mlm_migration - mlm migration runner
* mig\pdol_migration - pdol migration runner
* mig\sdol_migration - sdol migration runner

* config.py --> robot configuration file
* main_pdol.py --> main PDOL migration script
* main_sdol.py --> main SDOL migration script
* main_mlm.py --> main MLM migration script
* MigrationToolRobot_DO_NOT_DELETE.bat --> MigrationTool robot script
* requirements.txt --> Python requirements file
<br></br>
### Robot runtime environment:
* Windows server 
  * logon via vpn
* Installed components:
  * Python 
    * version: 3.8.10 
  * OpenJDK
    * version: jdk-11.0.13.8-hotspot
  * Jenkins
    * version: 2.319.2
    * Home: D:\Jenkins
    * admin account: ipa_adm
    * pdol-robot job --> triggering main_pdol.py
    * sdol-robot job --> triggering main_sdol.py
    * mlm-robot job --> triggering main_mlm.py
    * mig-robot-pipeline --> trigerring pdol, sdol and mlm jobs based on the schedule 
    * schedule configuration: 07:00 and 17:00 - Monday to Friday
 * Robot home: 
    * D:\Robots\visma-raet-migration
 * Robot venv: 
    * D:\Robots\venvs\visma-raet-migration-venv
 * Migration files home: 
    * D:\MigVisma 
 * Migration tool script:
    * D:\MigVisma\MigrationToolRobot.bat 
<br></br>

### Reporting:
* AutoMate KPI framework:
  *  GCP Project: prod-amkpi-cm
  *  BigQuery Database: transaction_items_kpi
     * Robot ID: IPA-0019
     * Process ID: BNL-0003   
* Slack
  * #ipa-mig-raet-reports
    * each robot execution result is posted here, including execution logfile 
<br></br>

### Workflows:
* Migration robot:<br></br>
![service_diagram](https://user-images.githubusercontent.com/74961891/155693218-82d01570-4bc9-493a-a40e-7f2ecf15c717.png)
<br></br>
### Migration processes:
* PDOL Migration workflow:<br></br>
![pdol_mig](https://user-images.githubusercontent.com/74961891/151948811-401d7b4f-dc4d-482e-82b3-5b80d61790b6.png)

* SDOL Migration workflow:<br></br>
![sdol_mig](https://user-images.githubusercontent.com/74961891/151948738-84780258-5cb2-4a7f-aa9f-75983c98ebe1.png)

* MLL Migration workflow:<br></br>
![mlm_mig_](https://user-images.githubusercontent.com/74961891/154425641-e9a2dd63-8b51-4a6a-acd7-6cfe27161740.png)
