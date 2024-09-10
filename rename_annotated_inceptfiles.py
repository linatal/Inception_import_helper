from pathlib import Path
import argparse
import shutil
import sys
import zipfile
import os


def handle_zipfiles(dirpath):
    if zipfile.is_zipfile(dirpath):
        user_input = input("Given input path is a zipfile. Unzip now (y/n)?")
        if user_input.lower() in ["y", "yes"]:
            with zipfile.ZipFile(dirpath, 'r') as zip_ref:
                unzipped_f = Path(dirpath).stem
                unzipped_dirpath = Path(dirpath).parent / unzipped_f
                zip_ref.extractall(unzipped_dirpath)
            print("Unzipped dir in ", unzipped_dirpath)
            return unzipped_dirpath
    else:
        return dirpath


def rename(path, annot_username, extension):
    # create a new folder for renamed json files
    new_path = path.parent / "annotations_renamed"
    new_path.mkdir(parents=True, exist_ok=True)

    # files
    for p in path.rglob(annot_username + "." + extension):
        # copy files into new dir
        new_basename = p.parent.stem
        new_filename = new_basename + "." + extension
        new_filepath = new_path / new_filename
        shutil.copyfile(p, new_filepath)
    return new_path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", help='Path to the Inception project.')
    parser.add_argument("--username", help="Inception username to extract the annotations from, e.g. 'admin'. "
                                           "If curation flag is set True, the user name is 'CURATION_USER'",
                        required=False)
    parser.add_argument("--extension", help='Add extension of files, e.g. "json" or "xmi"')
    parser.add_argument("--curation", help="If set curated files will be renamed.",
                        action='store_true')
    args = parser.parse_args()
    if not args.path or not args.username:
        parser.print_help()
        sys.exit()

    input_path = args.path
    extension = args.extension
    curation = args.curation

    input_path = handle_zipfiles(input_path)

    if curation:
        annot_path = Path(input_path) / "curation"
        username = "CURATION_USER"
    elif not curation:
        annot_path = Path(input_path) / "annotation"
        try:
            username = args.username
        except:
            print("Please define user name. Abort.")
            sys.exit

    new_path = rename(annot_path, username, extension)
    print(f"Created new directory {Path(input_path)}/annotation_rename in Inception project folder with {len(os.listdir(new_path))} new files.")


if __name__ == "__main__":
    main()
