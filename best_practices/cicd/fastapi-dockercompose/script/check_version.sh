#!/bin/bash

extract_makefile_value() {
    local key="$1"
    grep -E "^$key\s*:?=" Makefile | awk -F ":?=" '{print $2}' | xargs
}

extract_toml_value() {
    local key="$1"
    grep -E "^$key\s*=" pyproject.toml | awk -F "=" '{print $2}' | xargs | tr -d '"'
}

makefile_name=$(extract_makefile_value "PROJECT_NAME")
makefile_version=$(extract_makefile_value "PROJECT_VERSION")

toml_name=$(extract_toml_value "name")
toml_version=$(extract_toml_value "version")

if [[ "$makefile_name" != "$toml_name" ]]; then
    echo "Project name mismatch: Makefile ($makefile_name) vs pyproject.toml ($toml_name)"
    exit 1
fi

if [[ "$makefile_version" != "$toml_version" ]]; then
    echo "Project version mismatch: Makefile ($makefile_version) vs pyproject.toml ($toml_version)"
    exit 1
fi

echo "Project name and version match."
exit 0
