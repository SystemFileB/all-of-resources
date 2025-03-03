@python -m build
@python -m twine upload  --skip-existing dist/*
@flet build windows --arch amd64 x86
@flet build android --arch arm64 x86_64 arm