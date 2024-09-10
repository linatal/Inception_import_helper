# Helper to import annotated files into an existing Inception Annotation Tool Project 
Small skript to rename files from UIMA CAS XMI or UIMA CAS JSON Inception export directory, so that files can be imported back to the Inception UI.

### Introduction
Using Inception annotation tool (https://inception-project.github.io/), sometimes it is handy to import already annotated files into your project. 
For example, if you want to merge two projects with the same annotation layers and tagset. 
For UIMA CAS XMI or JSON output, it is not possible to directly copy paste the files, since the 
original filename is in the parent directory, and the output filename is always the username.

The skript renames files to the name of the original input file and saves files into new folder (`/annotations_renamed`), so that a user can directly import the annotations into the tool.

### Usage 
```
$python rename_annotated_inceptfiles.py [-h] [--path PATH]
                                       [--username USERNAME]
                                       [--extension EXTENSION] [--curation]
```

#### Flags: 
```--path``` - Path to the Inception output project. Optionally, the directory will be unziped.  
```--username``` - Inception Username to extract the annotations from, e.g. "admin".  If curation flag is set True, the user
                        name is per default 'CURATION_USER'.  
```--extension``` - Given extension of files, e.g. "json" or "xmi" in Inception output.    
`--curation` - If set curated files will be renamed. 

#### Example

```$python --path ./dataset/Annotations.zip --username "annotator1" --extension "json"```
The output files can be imported into Inception and will be linked to the user who imported the files. You may want to create a new user first if you want to link the annotations to that user. 

#### Some Remarks
- Works only for Export backup archive, not for curated archive. 