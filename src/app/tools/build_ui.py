from pathlib import Path
import subprocess
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]

UI_ROOT = PROJECT_ROOT / "ui"
OUT_ROOT = PROJECT_ROOT / "ui_generated"


for ui in UI_ROOT.rglob("*.ui"):
    rel = ui.relative_to(UI_ROOT)             # panels/foo.ui    
    out = OUT_ROOT / rel                      # ui_generated/panels/foo.ui

    out = out.with_suffix("")  
    out = out.with_name(out.name + "_ui.py")

    out.parent.mkdir(parents=True, exist_ok=True)
    
    uic = Path(sys.executable).with_name("pyside6-uic.exe") 

    subprocess.run(
        [str(uic), str(ui), "-o", str(out)],
        check=True
    )
