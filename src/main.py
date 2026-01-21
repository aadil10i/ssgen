import os
import shutil

destination = "./public"
source = "./static"


# ensure copy is started from cleanup
def copy_static_to_public(source, destination):
    if os.path.exists(destination):
        shutil.rmtree(destination)
        print(f"Directory {destination} successfully deleted.")

    os.mkdir(destination)
    copy_recursive(source, destination)


def copy_recursive(source, destination):
    source_content = os.listdir(source)

    for item_name in source_content:
        full_source_path = os.path.join(source, item_name)

        if os.path.isfile(full_source_path):
            print(f"item {full_source_path} is being copied to directory {destination}")
            shutil.copy(full_source_path, destination)

        else:
            new_directory = os.path.join(destination, item_name)
            os.mkdir(new_directory)
            copy_recursive(full_source_path, new_directory)


def main():
    copy_static_to_public(source, destination)


if __name__ == "__main__":
    main()
