; Installeur Windows du Compagnon Warframe (Inno Setup 6).
; Compilé par GitHub Actions (.github/workflows/release.yml) à partir de build\app :
;   Python embarqué + outil + base. Le modèle d'IA (llama.cpp + Qwen3 1.7B, ~1,8 Go) est téléchargé au premier lancement.
; Pas besoin de droits administrateur : installation dans le profil de l'utilisateur.

#ifndef AppVersion
  #define AppVersion "0.0.0"
#endif

[Setup]
AppId={{6C1E7B2A-4F3D-4B8E-9A51-2D7C0F9E3A14}
AppName=Compagnon Warframe
AppVersion={#AppVersion}
AppPublisher=XeniX13
AppPublisherURL=https://github.com/xenix13/warframe-compagnion
DefaultDirName={localappdata}\CompagnonWarframe
DefaultGroupName=Compagnon Warframe
DisableProgramGroupPage=yes
PrivilegesRequired=lowest
OutputDir=..\dist
OutputBaseFilename=CompagnonWarframe-Setup-{#AppVersion}
Compression=lzma2/max
SolidCompression=yes
WizardStyle=modern
UninstallDisplayName=Compagnon Warframe

[Languages]
Name: "french"; MessagesFile: "compiler:Languages\French.isl"

[Tasks]
Name: "desktopicon"; Description: "Créer un raccourci sur le bureau"; GroupDescription: "Raccourcis :"

[Files]
Source: "..\build\app\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\Compagnon Warframe"; Filename: "{app}\lancer.bat"; WorkingDir: "{app}"
Name: "{group}\Mettre à jour les données"; Filename: "{app}\mise-a-jour.bat"; WorkingDir: "{app}"
Name: "{group}\Désinstaller"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Compagnon Warframe"; Filename: "{app}\lancer.bat"; WorkingDir: "{app}"; Tasks: desktopicon

[Run]
Filename: "{app}\lancer.bat"; Description: "Lancer le Compagnon Warframe (le premier lancement télécharge le modèle d'IA, ~1,8 Go)"; Flags: postinstall nowait shellexec skipifsilent

[UninstallDelete]
; données générées et modèle téléchargé (les loadouts du joueur sont dans base-warframe\06-builds-joueur : supprimés aussi)
Type: filesandordirs; Name: "{app}\companion-data"
Type: filesandordirs; Name: "{app}\moteur-ia"
Type: filesandordirs; Name: "{app}\base-warframe"
Type: filesandordirs; Name: "{app}\python"
Type: filesandordirs; Name: "{app}\wfcompanion"
