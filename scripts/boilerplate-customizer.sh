#!/bin/bash

README_FILE="README-TEMPLATE.md"
TEMP_README_FILE="README.md"

get_info() {
    # This script is used to customize the boilerplate code for a new project.
    read -p "Enter the project name: " project_name
    read -p "Enter the project description: " project_description
    read -p "Enter the author name: " author_name
    read -p "Enter the author email: " author_email
    read -p "Choose the database type (mysql, postgres, sqlite, mongodb): " db_type
}

set_info() {
    if [[ ! -e $README_FILE ]]; then
        echo "Error: $README_FILE not found."
        exit 1
    fi

    cp "$README_FILE" "$TEMP_README_FILE"

    echo "Customizing boilerplate code... s/PROJECT_NAME/$project_name/g $TEMP_README_FILE"

    sed -i "" "s/PROJECT_NAME/$project_name/g" "$TEMP_README_FILE"
    sed -i "" "s/PROJECT_DESCRIPTION/$project_description/g" "$TEMP_README_FILE"
    sed -i "" "s/AUTHOR_NAME/$author_name/g" "$TEMP_README_FILE"
    sed -i "" "s/AUTHOR_EMAIL/$author_email/g" "$TEMP_README_FILE"
    sed -i "" "s/DB_TYPE/$db_type/g" "$TEMP_README_FILE"
}

get_info
set_info
echo "Boilerplate code customized successfully."
read -p "Press any key to exit"
