# Helper Script to Import Annotated Files into an Existing INCEpTION Project 

This small script renames files from the UIMA CAS XMI or UIMA CAS JSON export directory of INCEpTION so that annotations can be imported back into the INCEpTION UI under the correct username.

### Introduction
When using the [INCEpTION annotation tool](https://inception-project.github.io/), you may find yourself annotating the same texts in different project setups, possibly working locally instead of within the same INCEpTION instance. As a result, you end up with multiple project exports containing annotations for the same texts.

To merge these annotated files into a single project — for example to compare annotations or calculate an inter-annotator agreement — simply copying and pasting the exported files is not always possible. Even if the projects share the same texts, annotation layers, and tagsets, merging them might not be straightforward.

For UIMA CAS XMI or JSON output, INCEpTION does not preserve the original filenames; instead, it names exported annotation files after the annotating user. This script helps by renaming the exported files to match the original input filenames and saving them in a new folder (/annotations_renamed). This allows direct re-import into another INCEpTION project.

The script renames files to the name of the original input file and saves files into new folder (`/annotations_renamed`), so that a user can directly import the annotations into the tool.

*Note*: In Inception when exporting the projects, please choose Exported Backup Archive, not Curated Archive. 


### Usage 


```
$python rename_annotated_inceptfiles.py [-h] [--path PATH]
                                       [--username USERNAME]
                                       [--extension EXTENSION] [--curation]
```

#### Flags: 
```--path``` - Path to the Inception output project. Optionally, the directory will be unziped.  
```--username``` - Inception Username from project1 to extract the annotations from, e.g. "admin".  If curation flag is set True, the user
                        name is per default 'CURATION_USER'.  
```--extension``` - Given extension of files, e.g. "json" or "xmi" in Inception output.    
`--curation` - If set curated files will be renamed. 

#### Example

```$python --path ./dataset/Annotations.zip --username "annotator1" --extension "json"```

The output files can be imported into Inception and will be linked to the user who imported the files. You may want to create a new user first and log in as this user if you want to link the annotations to that username. 

 
