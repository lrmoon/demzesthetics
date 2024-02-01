for package in $(pip freeze | cut -d '=' -f 1); do
    echo "Uninstalling $package"
    pip uninstall -y $package
done