from pathlib import Path
from datetime import datetime


FullPAthToFile=Path.cwd()/"app_status.txt"
NewRule="\n"+"-"*20
current_time=datetime.now().strftime("%y-%m-%d %H:%M:%S")

if FullPAthToFile.exists():
    print("-"*20)
    print("Checking System Log at:",FullPAthToFile,NewRule)
    print("Status:Log file found.")
    Content=FullPAthToFile.read_text()
    AppendWord=f"[{current_time}] [INFO] Periodic system check passed."
    x=FullPAthToFile.write_text(Content+"\n"+AppendWord)
    print("Action:New status line append successfully.",NewRule)
    NewContent =FullPAthToFile.read_text()
    print(f"Current Log Content:{NewRule}\n{NewContent}") 
    print(f"[{current_time}] [INFO] Periodic system check passed.{NewRule}")
    
else:
    print("-"*20)
    ExistsWord="INFO:System run smoothly...!"
    print("Checking System Log at:",FullPAthToFile,NewRule)
    print("Status:Log file NOT found.")
    FullPAthToFile.touch()
    print(f"Action:Created new '{FullPAthToFile.name}' file.{NewRule}")
    FullPAthToFile.write_text(ExistsWord)
    print(f"Current Log Content:{NewRule}\n{ExistsWord}\n[{current_time}] [INIT] System log file initialized.{NewRule}")